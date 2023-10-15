


from rest_framework.decorators import  api_view
from rest_framework.response import  Response
from students.api.serializers import StudentSerializer

from students.models import Student

# api --> hello world
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        # print(request.body) # bytes
        print(request.data)  # serialized data
        return Response({"message": "POST REQUEST Recived !"})
    return Response({"message":"Hello World!"})


@api_view(['GET', 'POST'])
## create , get all students
def index(request):
    if request.method == 'POST':
        pass

    elif request.method == 'GET':
        # 1- get all objects
        students= Student.get_all_students()
        serialized_students= []
        for std in students:
            print(StudentSerializer(std).data)
            serialized_students.append(StudentSerializer(std).data)

        return Response({'students':serialized_students})