from django.test import TestCase
from app.models import Student

class StudentModelTest(TestCase):
    def test_create_student(self):
        name = "FKON"
        roll = 1233
        section = '7DM'

        student = Student.objects.create(name=name, roll=roll, section=section)
        self.assertEqual(student.name, name)
        self.assertEqual(student.roll, roll)
        self.assertEqual(student.section, section)