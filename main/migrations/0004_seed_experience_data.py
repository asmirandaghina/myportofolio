import uuid
from django.db import migrations


def create_experience_data(apps, schema_editor):
    Experience = apps.get_model('main', 'Experience')
    
    data = [
        {
            "title": "Universitas Indonesia",
            "description": "Sistem Informasi, Fakultas Ilmu Komputer",
            "category": "education",
            "period_label": "2025 - hingga kini",
        },
        {
            "title": "MAN 2 Kota Malang",
            "description": "Peminatan Ilmu Pengetahuan Alam",
            "category": "education",
            "period_label": "2022 - 2025",
        },
        {
            "title": "BEM UI 2026",
            "description": "Staf Departemen Aksi dan Propaganda",
            "category": "organization",
            "period_label": "2026",
        },
        {
            "title": "OSIS MAN 2 Kota Malang",
            "description": "Divisi Pengembangan Minat dan Bakat",
            "category": "organization",
            "period_label": "2023 - 2024",
        },
    ]
    
    for item in data:
        Experience.objects.create(id=uuid.uuid4(), **item)


def reverse_seed(apps, schema_editor):
    Experience = apps.get_model('main', 'Experience')
    Experience.objects.filter(
        title__in=[
            "Universitas Indonesia",
            "MAN 2 Kota Malang",
            "BEM UI 2026",
            "OSIS MAN 2 Kota Malang",
        ]
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_experience_period_label'),
    ]

    operations = [
        migrations.RunPython(create_experience_data, reverse_seed),
    ]