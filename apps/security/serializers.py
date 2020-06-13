from rest_framework import serializers
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'first_name', 'last_name', 'age', 'password']

    def create(self, validated_data):
        user = UserModel.objects.create_user(validated_data['email'], validated_data['first_name'],
                                            validated_data['last_name'], validated_data['age'], validated_data['password'])
        return user


class UserSigninSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required = True)




