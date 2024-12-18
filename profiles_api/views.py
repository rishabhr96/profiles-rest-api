from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """returns a list of APIview features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put , delete)',
            " Is similar to a traditional Django View",
            "Gives you the most control over your application logic",
        ]
 
        return Response({'message':'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

    
    def put(self, request, pk=None): #pk =  primary key
        """Handles updating an object"""
        return Response({'method':'PUT'})


    def patch(self, request, pk=None):#pk =  primary key
        """Handles a partial update of an object"""
        return Response({'method':'PATCH'})


    def delete(self, request, pk=None):#pk =  primary key
        """Deletes an object"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """return a hello message"""

        a_viewset= [
            'Uses actions(list, create, retrieve, update, partial_updates)',
            'automatically maps to URLs using Routers',
            'Provides more funtionality with less code',
        ]

        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f'hello {name} ok'
            return Response ({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handles updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """handles removing an object"""
        return Response({'http_method':"DELETE"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating profiles"""
    serializer_class= serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all() 
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handles creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    




 
