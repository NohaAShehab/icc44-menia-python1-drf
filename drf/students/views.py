from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
from students.models import Student

def hello(request):
    return JsonResponse({"data":"Hello World!", "message":"GET Request"})

@csrf_exempt
def acceptdata(request):
    if request.method == "POST":
        print(request.POST)
        # get data from request
        print(request.body)
        request_data = json.loads(request.body)
        return  JsonResponse({"message":"POST Request Received!", 'data':request_data})

    return JsonResponse({"data": "Accepted Data", "message": "GET Request"})


#### create api for students

### serialize data manually
@csrf_exempt
def students_index(request):
    if request.method=='POST':
        request_data = json.loads(request.body)
        student= Student()
        student.name =request_data['name']
        student.email =request_data['email']
        student.save()
        return  JsonResponse({"data": {"id":student.id, 'name':student.name}}, status=201)

    students = Student.get_all_students()
    serialized_students = []
    for std in students:
        serialized_students.append({"id":std.id, 'name':std.name})
    return JsonResponse({"data":serialized_students})

