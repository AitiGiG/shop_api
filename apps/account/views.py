from http import HTTPStatus

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

                send_confirmation_email(user.email, user.activation_code)
            except:
                return Response(
                    {
                        'message': 'Че то не то, на почте нет ниче',
                        'data': serializer.data
                    }, status=HTTPStatus.CREATED
                )
            return Response(serializer.data, status=HTTPStatus.CREATED)

# class ActivationView(APIView):
#     def get(self, request):
#         code = request.query_params.get('u')
#         user = get_object_or_404(User, activation_code=code)
#         user.is_active = True
#         user.activation_code = ''
#         user.save()
#         return Response('Активирован', status=HTTPStatus.OK)

class ActivationView(APIView):
    def post(self, request):
        activation_code = request.data.get('activation_code')
        if not activation_code:
            return Response({
                'error': 'Нужен код активации'
            }, status=HTTPStatus.BAD_REQUEST)
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        try:
            send_confirmation_email(user.email, user.activation_code)
            return Response({
                'message': 'Пользователь активирован'}, status=HTTPStatus.OK
            )
        except Exception as e:
            return Response(
                {'error': f'Ошибка при отправке подтверждения по электронной почте: {e}'},
                            status=HTTPStatus.INTERNAL_SERVER_ERROR
            )
#
# class ActivationView(APIView):
#     def get(self, request):
#         code = request.query_params.get('u')
#         user = get_object_or_404(User, activation_code=code)
#         user.is_active = True
#         user.activation_code = ''
#         user.save()
#         return Response('Успешено активирован', 200)

# активация аккаунта через пост запрос
# принимаем активационный код и сверяем с нашими данными
# если юзер есть то активируем | 404
