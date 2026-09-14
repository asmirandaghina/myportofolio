import uuid
from django.db import migrations


def create_lakon_data(apps, schema_editor):
    Lakon = apps.get_model('main', 'Lakon')

    data = [
        {"title": "Membuat Origami", "category": "seni", "photo": "img/origami.png"},
        {"title": "Merangkai Kembang", "category": "seni", "photo": "img/rangkaiBunga.png"},
        {"title": "Memanggang makanan manis", "category": "dapur", "photo": "img/baking.png"},
    ]

    for item in data:
        Lakon.objects.create(id=uuid.uuid4(), **item)


def reverse_seed(apps, schema_editor):
    Lakon = apps.get_model('main', 'Lakon')
    Lakon.objects.filter(
        title__in=[
            "Membuat Origami",
            "Merangkai Kembang",
            "Memanggang makanan manis",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_lakon_caption'),
    ]

    operations = [
        migrations.RunPython(create_lakon_data, reverse_seed),
    ]