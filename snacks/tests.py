from django.http import response
from django.test import TestCase
from django.urls import reverse
from snacks.models import Snacks
from django.contrib.auth import get_user_model

class SnacksTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass")
        self.snack = Snacks.objects.create(
            name = 'cookie', purchaser = self.user, description = "yummy")
    
    def test_string_rep(self):
        self.assertEqual(str(self.snack), 'cookie')

    def test_snack_name(self):
        self.assertEqual(f'{self.snack.name}', 'cookie')
    
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        
    def test_home_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")