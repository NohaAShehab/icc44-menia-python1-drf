


from rest_framework.decorators import  api_view
from rest_framework.response import  Response
from students.api.serializers import StudentSerializer
from rest_framework import status

from students.models import Student

# api --> hello world
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        # print(request.body) # bytes
        print(request.data)  # serialized data
        return Response({"message": "POST REQUEST Recived !"})
    return Response({"message":"Hello World!"})


# @api_view(['GET', 'POST'])
# ## create , get all students
# def index(request):
#     if request.method == 'POST':
#         student = Student.objects.create(name=request.data['name'],
#                 email=request.data['email'],grade=request.data['grade'],
#                                          image=request.data['image'])
#         student.save()
#         return Response({'student': StudentSerializer(student).data})
#
#     elif request.method == 'GET':
#         # 1- get all objects
#         students= Student.get_all_students()
#         serialized_students= []
#         for std in students:
#             print(StudentSerializer(std).data)
#             serialized_students.append(StudentSerializer(std).data)
#
#         return Response({'students':serialized_students})

# ask serializer to create object ?
@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        # student = Student.objects.create(name=request.data['name'],
        # email=request.data['email'],grade=request.data['grade'],image=request.data['image'])
        # student.save()
        serialized_student =StudentSerializer(data=request.data)
        if serialized_student.is_valid():
            serialized_student.save()
            return Response({'student': serialized_student.data}, status=201)
        return Response({'errors': serialized_student.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # 1- get all objects
        students= Student.get_all_students()
        serialized_students= StudentSerializer(students, many=True)

        return Response({'students':serialized_students.data})