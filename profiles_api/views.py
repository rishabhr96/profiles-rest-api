from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """returns a list of APIview features"""
        an_apiview = [
            'uses Http methods as fuction (get, post, patch, put , delete)',
            'is similar to traditionsal Django View',
            'Gives you the most control over your application logic',
            'is mapped manually to URLs',
            'logic'*5,
        ]

        return Response({'message':'Hello', 'an_apiview': an_apiview})

 
