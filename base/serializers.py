from rest_framework import serializers
from .models import About, Projects, Contact


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About

        fields = ['firstname','lastname','image','about_text','phone_number','email','github_link','telegram_link','instagram_link']


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['project_name','project_image','project_description','project_link','project_github_link','created_at']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name','email','message']