
from rest_framework.response import  Response
from rest_framework import status
from rest_framework.decorators import  api_view

from students.models import Student

from students.api.modelserializers import StudentModelSerializer

@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        students = Student.get_all_students()
        serialized_students = StudentModelSerializer(students, many=True)
        return Response({"data":serialized_students.data}, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serialized_student = StudentModelSerializer(data = request.data)
        if serialized_student.is_valid():
            serialized_student.save()
            return Response({"data":serialized_student.data}, status=status.HTTP_201_CREATED)
        return Response({"error":serialized_student.errors}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"message":"Method Not Allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
