from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """returns a list of APIview features"""
        an_apiview = [
            'uses Http methods as fuction (get, post, patch, put , delete)',
            'is similar to traditionsal Django View',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',
            'logic '*5 ,
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer._validated_data.get('name')
            message = f'hello {name}'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

    
    def put(self, requrest, pk=None):
        """Handles updating an object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method':'DELETE'})


 
