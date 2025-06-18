from  django.contrib.auth import  get_user_model
from .models import TelegramUser
from  django.contrib.auth.password_validation import validate_password
from  rest_framework import  serializers


User = get_user_model()

def validate_user_password(value):
    validate_password(value)
    return value


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True ,validators=[validate_user_password])

    class Meta:
        model = User
        fields =  ['username','email','password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get('username'),
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return user


class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'
        read_only_fields = ['date_joined']












