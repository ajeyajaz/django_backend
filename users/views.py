from .serializers import RegisterSerializer
from django.shortcuts import render
from .tasks import send_welcome_email

from  rest_framework.generics import CreateAPIView
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import  permissions
from  rest_framework import status

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



# register view
def register_page(request):
    return render(request, 'register.html')

class RegisterApiView(CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()

        #send email after 2sec
        send_welcome_email.apply_async(args =[user.username, user.email],countdown=2)


class CookieTokenLoginView(APIView):

    def get(self,request):
        return render(request,'login.html')

    def post(self, request):
        serializer = TokenObtainPairSerializer(data=request.data)

        if serializer.is_valid():
            access = serializer.validated_data['access']
            refresh = serializer.validated_data['refresh']

            response = Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            response.set_cookie('access_token', access, httponly=True, secure=True, samesite='Lax')
            response.set_cookie('refresh_token', refresh, httponly=True, secure=True, samesite='Lax')
            return response

        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)



class PublicAPIView(APIView):

    def get(self,request):
        return Response({'message' : "Hi welcome to the public API endpoint."})


class ProtectedAPIView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        return Response({'message':'Seeing this because your are Authenticated.'})





