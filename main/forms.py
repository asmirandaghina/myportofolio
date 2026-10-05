from django.forms import ModelForm, TextInput, Select, ClearableFileInput
from main.models import Lakon
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


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

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Nama kegiatan tidak boleh hanya berisi tag HTML.")
        return title