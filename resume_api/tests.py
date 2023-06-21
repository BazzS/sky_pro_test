from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status

from resume_api.models import Resume

from django.conf import settings


class ResumeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_get_resume(self):
        # Создаем тестовое резюме
        resume_data = {
            'status': 'Active',
            'grade': 'A',
            'specialty': 'Backend Developer',
            'salary': 5000,
            'education': 'Bachelor of Computer Science',
            'experience': '5 years',
            'portfolio': 'https://portfolio.example.com',
            'title': 'Resume Title',
            'phone': '123456789',
            'email': 'test@example.com',
        }
        Resume.objects.create(user=self.user, **resume_data)

        # Отправляем GET запрос на эндпоинт /resume
        response = self.client.get('/resume')

        # Проверяем статус код и ожидаемые данные
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, resume_data)

    def test_update_resume(self):
        # Создаем тестовое резюме
        resume_data = {
            'status': 'Active',
            'grade': 'A',
            'specialty': 'Backend Developer',
            'salary': 5000,
            'education': 'Bachelor of Computer Science',
            'experience': '5 years',
            'portfolio': 'https://portfolio.example.com',
            'title': 'Resume Title',
            'phone': '123456789',
            'email': 'test@example.com',
        }
        resume = Resume.objects.create(user=self.user, **resume_data)

        # Подготавливаем данные для обновления резюме
        updated_resume_data = {
            'status': 'Updated',
            'grade': 'B',
            'specialty': 'Frontend Developer',
            'salary': 6000,
            'education': 'Master of Computer Science',
            'experience': '7 years',
            'portfolio': 'https://new-portfolio.example.com',
            'title': 'Updated Resume Title',
            'phone': '987654321',
            'email': 'updated@example.com',
        }

        # Отправляем PATCH-запрос для обновления резюме
        response = self.client.patch('/resume/update', data=updated_resume_data)

        # Проверяем, что запрос выполнен успешно (код статуса 200)
        self.assertEqual(response.status_code, 200)

        # Обновляем резюме из базы данных
        resume.refresh_from_db()

        # Проверяем, что данные резюме были обновлены
        self.assertEqual(resume.status, 'Updated')
        self.assertEqual(resume.grade, 'B')
        self.assertEqual(resume.specialty, 'Frontend Developer')
        self.assertEqual(resume.salary, 6000)
        self.assertEqual(resume.education, 'Master of Computer Science')
        self.assertEqual(resume.experience, '7 years')
        self.assertEqual(resume.portfolio, 'https://new-portfolio.example.com')
        self.assertEqual(resume.title, 'Updated Resume Title')
        self.assertEqual(resume.phone, '987654321')
        self.assertEqual(resume.email, 'updated@example.com')

