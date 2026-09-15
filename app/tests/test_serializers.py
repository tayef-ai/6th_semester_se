from app.models import Student
from rest_framework.test import APITestCase
from app.serializers import StudentSerializer

class StudentSerializerTestCase(APITestCase):
    def test_student_serializer_valid_data(self):
        data = {
            'name': "bkon",
            'roll': 12,
            'section': "7D"
        }
        serializer = StudentSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})
