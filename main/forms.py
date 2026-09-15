from django.forms import ModelForm, TextInput, Select, ClearableFileInput
from main.models import Lakon


class LakonForm(ModelForm):
    class Meta:
        model = Lakon
        fields = [
            "title",
            "category",
            "photo",
        ]
        labels = {
            "title": "Nama Kegiatan",
            "category": "Kategori",
            "photo": "Path Foto (opsional)",
        }
        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Main Kalimba",
                    "maxlength": 100,
                }
            ),
            "category": Select(),
            "photo": TextInput(
                attrs={
                    "placeholder": "img/lakoni/kalimba.jpg",
                }
            ),
        }