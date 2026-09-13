from django.test import TestCase
from django.urls import reverse

from main.models import Experience, Lakon


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="organization",
            period_label="2026",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "organization")

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, self.experience.period_label)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")
        self.assertContains(response, "Belum ada pengalaman organisasi.")


class LakoniTest(TestCase):
    def setUp(self):
        self.lakon = Lakon.objects.create(
            title="Main Kalimba",
            category="musik",
            photo="img/lakoni/kalimba.jpg",
        )

    def test_lakoni_url_is_accessible(self):
        response = self.client.get(reverse("main:show_lakoni"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lakoni.html")

    def test_lakoni_data_appears(self):
        response = self.client.get(reverse("main:show_lakoni"))

        self.assertContains(response, self.lakon.title)
        self.assertContains(response, "Musik")

    def test_lakon_without_photo(self):
        Lakon.objects.all().delete()
        Lakon.objects.create(
            title="Menulis Puisi",
            category="tulisan",
        )
        response = self.client.get(reverse("main:show_lakoni"))

        self.assertContains(response, "Menulis Puisi")
        self.assertContains(response, "...")

    def test_empty_lakoni_page(self):
        Lakon.objects.all().delete()
        response = self.client.get(reverse("main:show_lakoni"))

        self.assertContains(response, "Belum ada hal yang dilakoni.")