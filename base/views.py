from rest_framework.generics import GenericAPIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema
import requests
import os
from dotenv import load_dotenv
load_dotenv()

class AboutView(GenericAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    http_method_names = ['get']
    @extend_schema(tags=['About'],summary="Profilni malumotlarini olish")
    @method_decorator(ratelimit(key='ip', rate='30/h', method='GET'))
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        custom_data = {
            "status": True,
            "statuscode": status.HTTP_200_OK,
            "message": "Ma'lumotlar muvaffaqiyatli yuklandi",
            "data": serializer.data,
            "timestamp": datetime.now().isoformat()
        }
        return Response(custom_data)

class ProjectsView(GenericAPIView):
    serializer_class = ProjectsSerializer
    queryset = Projects.objects.all()
    http_method_names = ['get']
    @method_decorator(ratelimit(key='ip', rate='30/h', method='GET'))
    @extend_schema(tags=['Projects'],summary="Projectlar malumotlarini olish")
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        custom_data = {
            "status": True,
            "statuscode": status.HTTP_200_OK,
            "message": "Ma'lumotlar muvaffaqiyatli yuklandi",
            "data": serializer.data,
            "timestamp": datetime.now().isoformat()
        }
        return Response(custom_data)


class ContactView(GenericAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    http_method_names = ['post']

    @method_decorator(ratelimit(key='ip', rate='30/h', method='POST'))
    @extend_schema(tags=['SendQuestion'], summary="Savol yuborish")
    def post(self, request, *args, **kwargs):
        recaptcha_token = request.data.get('recaptcha_token')

        if not recaptcha_token:
            return Response({"status": False, "message": "reCAPTCHA token topilmadi"}, status=400)

        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            'secret': os.getenv('CAPTCHA_SECRET'),  # .env da saqlang!
            'response': recaptcha_token
        })
        res = r.json()

        if not res.get('success') or res.get('score') < 0.5:
            return Response({
                "status": False,
                "message": "reCAPTCHA tekshiruvidan o'tolmadingiz (Bot ehtimoli)"
            }, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": True,
            "statuscode": status.HTTP_201_CREATED,
            "message": "Ma'lumotlar muvaffaqiyatli yuborildi, admin javobini kuting",
            "timestamp": datetime.now().isoformat()
        })

class QuestionsListView(GenericAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all().order_by('-id')
    http_method_names = ['get']
    @method_decorator(ratelimit(key='ip', rate='30/h', method='GET'))
    @extend_schema(tags=['QuestionsList'], summary="Oxirgi savollar listini olish")
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()[:20]
        serializer = self.get_serializer(queryset, many=True)

        custom_data = {
            "status": True,
            "statuscode": status.HTTP_200_OK,
            "message": "Oxirgi savollar listi",
            "data": serializer.data,
            "timestamp": datetime.now().isoformat()
        }
        return Response(custom_data)

