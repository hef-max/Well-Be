from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import User
import jwt, datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data) 

def login(request):
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('pass')

    #     try:
    #         user = User.objects.filter(email=email).first()

    #         if user is None:
    #             message  = AuthenticationFailed("user not found!")
    #             raise message
            
    #         if not user.check_password(password):
    #             message = AuthenticationFailed("Inccorect password!")
    #             raise message

    #         payload = {
    #             "id": user.id,
    #             "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
    #             "iat": datetime.datetime.utcnow()
    #         }

    #         token  = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

    #         response = Response()
    #         response.set_cookie(key='jwt', value=token, httponly=True)
    #         response.data = {
    #             "jwt": token
    #         }

    #         return HttpResponseRedirect('/index/')
            
    #     except:
    #         context = {
    #             "page_title": "Login",
    #             "error": message,
    #         }
    #         return render(request, 'users/index.html', context)
    # else:
    context = {
        "page_title": "Login",
    }
    return render(request, 'users/index.html', context)

def logout(request):
    response = Response()
    response.delete_cookie('jwt')
    context = {
        "message":"logout success"
    }
    return render(request, 'users/index.html', context)
