from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Review


class ReviewAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.list_url = reverse("api_reviews")

    def test_list_returns_200(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, 200)

    def test_create_review(self):
        payload = {"author_name": "Unit Test", "rating": 4, "comment": "Nice."}
        resp = self.client.post(self.list_url, payload, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.first().author_name, "Unit Test")


class ReviewHTMLTests(TestCase):
    def test_html_view_returns_200(self):
        url = reverse("review_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
