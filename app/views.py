from django.shortcuts import render
from .models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
import io
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def singlestudentview(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def allstudentview(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def studentview(request):
    if request.method == 'POST':
        req = request.body
        stream = io.BytesIO(req)
        data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': "Data Inserted Successfully"}
            json_res = JSONRenderer().render(res)
            return HttpResponse(json_res, content_type='application/json')
        error = serializer.errors()
        return HttpResponse(error, content_type='application/json')



