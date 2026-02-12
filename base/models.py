from django.db import models
import uuid

class About(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    image = models.ImageField(upload_to='about/')
    about_text = models.TextField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    github_link = models.URLField()
    telegram_link = models.URLField()
    instagram_link = models.URLField()


    def __str__(self):
        return self.firstname

class Projects(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=50)
    project_image = models.ImageField(upload_to='projects/',null=True,blank=True)
    project_description = models.TextField(null=True,blank=True)
    project_link = models.URLField(null=True,blank=True)
    project_github_link = models.URLField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField()
    answer = models.CharField(max_length=50,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

