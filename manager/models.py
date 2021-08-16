from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin



# Расширяем класс юзер(дополнительные данные, после регистрации)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #Привязываем к модели юзер
    Passport_series = models.CharField(max_length=10, blank=True)
    Passport_number = models.CharField(max_length=40, blank=True)
    Passport_received = models.CharField(max_length=60, blank=True)
    Location = models.CharField(max_length=30, blank=True)
    School_name = models.CharField(max_length=60, blank=True)
    School_class= models.CharField(max_length=10, blank=True)
    Birth_date = models.DateField(null=True, blank=True)
    Phone = models.CharField(max_length=30, blank=True)
    Status = models.CharField(max_length=10, blank=True)
    id_stepik = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.username

#Расширяем класс юзер Данные о родителях
class Parent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязываем к модели юзер
    Name = models.CharField(max_length=60, blank=True)
    Birth_date = models.DateField(null=True, blank=True)
    Location = models.CharField(max_length=30, blank=True)
    Passport_series = models.CharField(max_length=10, blank=True)
    Passport_number = models.CharField(max_length=40, blank=True)
    Passport_received = models.CharField(max_length=60, blank=True)
    Phone = models.CharField(max_length=30, blank=True)



class personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Привязываем к модели юзер
    permission_code = models.IntegerField()
    work =  models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username


class Group(models.Model):
    g_user = models.ManyToManyField(User)
    g_name = models.CharField(max_length=30, blank=True)
    prepod = models.ForeignKey(personal, on_delete=models.CASCADE,null=True)  # Привязываем к модели юзер

    def __str__(self):
        return self.g_name

class novelty(models.Model):
    name = models.CharField(max_length=30, blank=True)
    heading = models.CharField(max_length=30, blank=True)
    body = models.TextField()
    data = models.DateField(null=True, blank=True)
    time =  models.TimeField(null=True, blank=True)
    def __str__(self):
        return self.heading







#Добавляем в админку
admin.site.register(Group)
admin.site.register(Profile)
admin.site.register(Parent)
admin.site.register(personal)
admin.site.register(novelty)
