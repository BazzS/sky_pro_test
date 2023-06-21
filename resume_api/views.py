from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Resume


@api_view(['GET'])
def get_resume(request):
    try:
        resume = Resume.objects.get(user=request.user.id)
        resume_data = {
            'status': resume.status,
            'grade': resume.grade,
            'specialty': resume.specialty,
            'salary': resume.salary,
            'education': resume.education,
            'experience': resume.experience,
            'portfolio': resume.portfolio,
            'title': resume.title,
            'phone': resume.phone,
            'email': resume.email
        }
        return Response(resume_data)
    except Resume.DoesNotExist:
        return Response({'message': 'Resume not found.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update_resume(request):
    resume = Resume.objects.get(user=request.user)
    resume.status = request.data.get('status', resume.status)
    resume.grade = request.data.get('grade', resume.grade)
    resume.specialty = request.data.get('specialty', resume.specialty)
    resume.salary = request.data.get('salary', resume.salary)
    resume.education = request.data.get('education', resume.education)
    resume.experience = request.data.get('experience', resume.experience)
    resume.portfolio = request.data.get('portfolio', resume.portfolio)
    resume.title = request.data.get('title', resume.title)
    resume.phone = request.data.get('phone', resume.phone)
    resume.email = request.data.get('email', resume.email)
    resume.save()
    return Response({'message': 'Resume updated successfully.'})
