


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


@api_view(['GET', 'PUT', 'DELETE'])
def student_resource(request, id):
    student = Student.get_sepecific_students(id)
    if student and request.method == 'PUT':
        serialized_student = StudentSerializer(data=request.data, instance=student)
        if serialized_student.is_valid():
            serialized_student.save()
            return Response({'student': serialized_student.data}, status=200)
        return Response({'errors': serialized_student.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif student and request.method == 'DELETE':
        student.delete()
        return Response({"message": "Deleted Successfully! "},
                        status=status.HTTP_204_NO_CONTENT)

    elif student and request.method == 'GET':
        serialized_student = StudentSerializer(student)
        return Response({'data': serialized_student.data}, status=status.HTTP_200_OK)

    else:
        return  Response({"message":"object not found , please reload the page"},
                         status=status.HTTP_205_RESET_CONTENT)

