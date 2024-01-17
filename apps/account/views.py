from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from .send_email import send_confirmation_email
from django.shortcuts import get_object_or_404

User = get_user_model()

class RegistrationView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(
                    user.email,
                    user.activation_code
                )
            except:
                return Response({'message':'Зарегались, но на почту код не отправился', 'data':serializer.data}, 201)
        return Response(serializer.data, 201)

class ActivationView(APIView):
    def get(self, request):
        code = request.query_params.get('u')
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return Response('Успешено активирован', 200)

# активация аккаунта через пост запрос
# принимаем активационный код и сверяем с нашими данными
# если юзер есть то активируем | 404