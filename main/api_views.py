from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import (
    api_view, authentication_classes, permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from main.models import Lakon
from main.permissions import IsPortfolioOwnerOrEditorOrReadOnly
from main.serializers import LakonSerializer


@api_view(["GET", "HEAD", "POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def lakon_list(request):
    if request.method in ("GET", "HEAD"):
        lakons = Lakon.objects.prefetch_related("starred_by").order_by("title", "id")
        title = request.query_params.get("title", "").strip()
        if title:
            lakons = lakons.filter(title__icontains=title)
        serializer = LakonSerializer(
            lakons, many=True, context={"request": request},
        )
        return Response(serializer.data)

    serializer = LakonSerializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "HEAD", "PUT", "PATCH", "DELETE"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsPortfolioOwnerOrEditorOrReadOnly])
def lakon_detail(request, lakon_id):
    lakon = get_object_or_404(
        Lakon.objects.prefetch_related("starred_by"), pk=lakon_id,
    )

    if request.method in ("GET", "HEAD"):
        serializer = LakonSerializer(lakon, context={"request": request})
        return Response(serializer.data)

    if request.method == "DELETE":
        lakon.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = LakonSerializer(
        lakon, data=request.data, partial=request.method == "PATCH",
        context={"request": request},
    )
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def lakon_star(request, lakon_id):
    lakon = get_object_or_404(Lakon, pk=lakon_id)

    if lakon.starred_by.filter(pk=request.user.pk).exists():
        lakon.starred_by.remove(request.user)
    else:
        lakon.starred_by.add(request.user)

    serializer = LakonSerializer(lakon, context={"request": request})
    return Response(serializer.data)