from rest_framework import serializers

from profiles_api import models


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name= serializers.CharField(max_length=10)
    

class UserProfileSerializer(serializers.ModelSerializer):
    """ it Serializes a user profile objects"""

    class Meta:
        model= models.UserProfile
        fields= ['id','email','name','password']
        extra_kwargs = {
            'password' : {
                'write_only': True
            }
        }


    def create(self, validated_data):
        """creates and returns new user"""
        user= models.UserProfile.objects.create_user(
            email= validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']


        )

        return user