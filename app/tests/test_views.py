from rest_framework.test import APITestCase, APIClient
from app.models import Student
from django.urls import reverse
from rest_framework import status

class StudentViewTestCase(APITestCase):
    def test_student_create_view(self):
        url = reverse('createstudent')
        data = {
            'name': 'Okon',
            'roll': 162,
            'section': '88DM'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'msg': 'Data Inserted Successfully'})