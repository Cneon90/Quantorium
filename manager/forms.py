# Подключаем компонент для работы с формой
from django import forms
# Подключаем компонент UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключаем модель User
from django.contrib.auth.models import User
from .models import *


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



# Создаём класс формы
class RegistrForm(UserCreationForm):
    # Добавляем новое поле Email

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин','oninput':'test()','id':'login-name'}))#forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите E-mail'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Повторите пароль'}))

   # email = forms.EmailField(max_length=254, help_text='This field is required')


    # Создаём класс Meta
    class Meta:
        # Свойство модели User
        model = User
        # Свойство назначения полей
        fields = ('username', 'email', 'password1', 'password2',)


class setting_p(forms.Form):
    #username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите логин','oninput':'test()','id':'login-name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Введите E-mail'}))
    Passport_series = forms.CharField(label='Серия паспорта', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите серию паспорта'}))
    Passport_number = forms.CharField(label='Номер паспотра', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите номер паспотра'}))
    Passport_received = forms.CharField(label='Когда и кем выдан', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите когда и кем выдан'}))
    Location = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Город'}))
    School_name = forms.CharField(label='Номер школы', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Номер школы'}))
    School_class = forms.CharField(label='Класс', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Класс'}))
    Birth_date = forms.DateField(label='День рождения', widget=forms.DateInput(attrs={'type':'date', }))
    Phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Телефонl'}))

class add_group(forms.Form):
    Name = forms.CharField(label='Название группы', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название группы'}))


class add_new_post(forms.Form):
    zagolovok = forms.CharField(label='Заголовок', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Заголовок'}))
    body = forms.CharField(label='Текст ', widget=forms.Textarea)


class add_cours(forms.Form):
    name = forms.CharField(label='Название курса', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Название курса'}))

class group_edit(forms.Form):
    name = forms.CharField(label='Название курса', widget=forms.Select())

class time_table(forms.Form):
    #Name = forms.CharField(label='Название группы', widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название группы'}))
    day  = forms.DateField(label='День занятия', widget=forms.DateInput(attrs={'type':'date', }))
    time = forms.TimeField(label='День занятия', widget=forms.TimeInput(attrs={'type':'time', }))
