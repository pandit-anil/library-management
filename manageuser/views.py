from django.shortcuts import render
from .models import User
from .serializers import UserSeralizer
from rest_framework.response import Response
from rest_framework.views import APIView

class UserApiView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSeralizer(user,many=True)
        return Response({'status':200,'payload':serializer.data})
    
    def post(self, request):
        profile_data = {
        'username':request.data.get('username'),
        'email':request.data.get('email'),
        'phone_number': request.data.get('phone_number'),
        'profile': request.FILES.get('profile'),
        'address': request.data.get('address')
        }
        user = User(**profile_data)
        user.set_password(request.data.get('password'))
        serializer = UserSeralizer(data=user.__dict__)
        if not serializer.is_valid():
            return Response({'status':403,'Error':serializer.errors,'message':'Something gone wrong'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'Your account has been created'})
    

    def put(self, request):
        pass
    def patch(self, request):
        pass
    def delete(self, request):
        pass