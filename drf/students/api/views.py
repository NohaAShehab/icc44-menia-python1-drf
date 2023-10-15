


from rest_framework.decorators import  api_view

from rest_framework.response import  Response

# api --> hello world
@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        # print(request.body) # bytes
        print(request.data)  # serialized data
        return Response({"message": "POST REQUEST Recived !"})
    return Response({"message":"Hello World!"})