from django.utils.html import strip_tags
from rest_framework import serializers

from main.models import Experience, Lakon


class StarredModelSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())


class LakonSerializer(StarredModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True,
    )

    class Meta:
        model = Lakon
        fields = [
            "id", "title", "category", "category_display", "photo",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Nama kegiatan tidak boleh kosong.")
        return value

    def validate_photo(self, value):
        return strip_tags(value).strip()


class ExperienceSerializer(StarredModelSerializer):
    category_display = serializers.CharField(
        source="get_category_display", read_only=True,
    )

    class Meta:
        model = Experience
        fields = [
            "id", "title", "description", "category", "category_display",
            "thumbnail", "period_label",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Judul tidak boleh kosong.")
        return value

    def validate_description(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Deskripsi tidak boleh kosong.")
        return value

    def validate_period_label(self, value):
        return strip_tags(value).strip()