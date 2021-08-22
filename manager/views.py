from django.conf import settings
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import * #RegistrForm, LoginForm, settingg
from django.core.mail import send_mail
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User

from .functional import _get_grpoup
from .models import *
from .functional import *
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime as DT
from django.contrib.auth.models import Permission,User
from django.contrib.contenttypes.models import ContentType
from datetime import date, datetime


def permist(request,id):
    data={}
    content_type = ContentType.objects.get_for_model(Profile)
    permission = Permission.objects.get_or_create(codename='can_admins',
                                                  name='panel_admins',
                                                  content_type=content_type)


    prava = Permission.objects.get(codename='panel_admins')
    us = User.objects.get(pk=id)
    us.user_permissions.remove
    us.user_permissions.add(prava)
    us.save()


def index(request):
    #permission = Permission.objects.get_or_create(codename='set_administrator')
    data = {}
    data.update(init_news(request))

    return render(request, 'manager/home/index.html', data)


def statistic(request):
    data={}
    data.update(init_news(request))
    return render(request, 'manager/statistic.html', data)



def reg(request):
    return render(request, 'manager/home/reg.html', {"name": "name", "msg": "msg"})


def user_login(request):
    data = {}

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return render(request, 'manager/index.html', {"name": user, "msg": "msg"}) #Не срабатывает изменение url
                    return redirect('index') #Работает )
                    #data['res'] = 'Authenticated successfully'
                else:
                    data['activ'] = 'Ваша учетная запись не активна, обратитесь к администратору'
            else:
                data['res'] = 'Неверный логин, или пароль'
    else:
        form = LoginForm()
    return render(request, 'manager/home/login.html', {'form': form, "data":data})




# Функция регистрации
def registr(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"

            #return render(request, 'manager/login.html', {"msg":"Регистрация прошла успешно, авторизируйтесь"})
            return redirect('login')
            # Рендаринг страницы
            #return render(request, 'manager/reg.html', data)
        else:
            data['form'] = form

            data['res'] = form.errors.as_data()
            print(form.errors.as_data())
            # Рендаринг страницы
            return render(request, 'manager/home/reg.html', data)

    else: # Иначе
        # Создаём форму
        form = RegistrForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
        return render(request, 'manager/home/reg.html', data)


#Выход из системы
def logout_view(request):
    data = {}
    data['res'] = "Вышли"
    logout(request)
    return render(request, 'manager/home/logout.html', data)


#Пример отправки письма (удалить)
def mail(request):
    data = {}
    print("mails")
    print(send_mail(
        'Subject here',
        'Here is the message.',
        'quantorium_tomsk@mail.ru',
        ['kirillkalita2@gmail.com'],
        fail_silently=True,#(True Страница загрузится даже если произошла ошибка) (false не загрузится)
    ))
    return render(request, 'manager/home/index.html', data)


def setting(request):
    try:
        #Преобразование даты в строку, что бы отобразилось при загрузке
        test = request.user.profile.Birth_date.__str__()
        print(type(test))
        data = {
            'email': request.user.email,
            'Passport_series': request.user.profile.Passport_series,
            'Passport_number': request.user.profile.Passport_number,
            'Passport_received': request.user.profile.Passport_received,
            'Location': request.user.profile.Location,
            'School_name': request.user.profile.School_name,
            'School_class': request.user.profile.School_class,
            'Birth_date':  test,
            'Phone': request.user.profile.Phone,
        }
        print(request.user.profile.Birth_date)
        form = setting_p(data)
    except Profile.DoesNotExist:
        # Если нету профиля, не заполняем
        form = setting_p()
        data = {}

    data['form'] = form

    if request.method == 'POST':
        form = setting_p(request.POST)
        if form.is_valid():
            #form = setting_p(request.POST)
            dataform = form.cleaned_data
            print("valid")
            try:
                # pro = Profile.objects.get(user__username=data['name'])
                # Ищем сопостовление по id из данных сеанса
                pro = Profile.objects.get(user_id=request.user.id)
            except Profile.DoesNotExist:
                # Если нету профиля, заместо обшики создаем новый профиль
                pro = Profile(user_id=request.user.id)
                pro.save()

            #ищем пользователя что бы заменить емаил
            u = User.objects.get(pk=request.user.id)
            u.email = dataform['email']
            u.save()

            pro.Passport_series = dataform['Passport_series']
            pro.Passport_number = dataform['Passport_number']
            pro.Passport_received = dataform['Passport_received']
            pro.Location = dataform['Location']
            pro.School_name = dataform['School_name']
            pro.School_class = dataform['School_class']
            pro.Birth_date = dataform['Birth_date']
            pro.Phone = dataform['Phone']

            print("Save")
            print(pro.Birth_date)
            pro.save()
            data['form'] = form
        else:
            print("inValid")
            data['form'] = form

    data['name'] = request.user.username

    data.update(init_news(request))

    return render(request, 'manager/home/setting.html', data)




def myprofile(request,name):
    data={}
    data.update(init_news(request))
    data['user'] = User.objects.get(username=name)
    data['age'] = calculate_age(data['user'].profile.Birth_date)

    return render(request, 'manager/home/myprofile.html', data)


def new_post(request,post):
    data = {}
    data.update(init_news(request))
    data['new_post'] = novelty.objects.get(pk=post)


    return render(request, 'manager/news/new_post.html', data)




def profile(request,profileid):
    content_type = ContentType.objects.get_for_model(Profile)

    #Создать права
    #Permission.objects.create(codename='adminenter',
                                           #name='Enter Admin',
                                           #content_type=content_type)
    """
        us = User.objects.get(pk=10)
        permission = Permission.objects.get(codename='can_publish')
        us.user_permissions.add(permission)
        us.email="krut@oschen.kz"
        us.save()
    """

    data = {}

    data.update(init_news(request))

    if (request.GET.get('newadmin', None)):
        data['new'] = 'kirill'


    # data['profile_id'] = profileid
    data['user'] = User.objects.get(pk=profileid)

    return render(request, 'manager/home/profile.html', data)





def news(request):
    data={}
    data.update(init_news(request))
    data['new'] = novelty.objects.all().order_by('-data').order_by('-time')
    return render(request, 'manager/news/news.html', data)



def edit_news(request,id_post):
    data={}
    data['redactory'] = True
    data.update(init_news(request))
    all_news = novelty.objects.all()
    print(all_news)
    data['all_news'] = all_news

    # -----------------------------------------------------------------------
    edit=novelty.objects.get(id=id_post)
    dataform={
                'zagolovok':edit.heading,
                'body': edit.body
             }
    form = add_new_post(dataform)
    if request.method == 'POST':  # Если передается форма (нажали добавить)
        form = add_new_post(request.POST)  # Заполняем форму значениям которые получили
        if form.is_valid():  # Проверяем валидность
            dataform = form.cleaned_data  # получаем чистые данные
            edit.heading = dataform['zagolovok']
            edit.body = dataform['body']
            edit.data = date.today()
            print(datetime.now().time())
            edit.time = datetime.now().time()
            edit.save()
    data['post_data'] = edit.data
    data['post_time'] = edit.time
    data['form'] = form
    return render(request, 'manager/news/add_news.html', data)






def profile_group(request,id_profile):
    data={}
    data.update(init_news(request))
    gr = Group.objects.get(id=id_profile)
    if not gr.course == None:
        data['zaivki'] = claim.objects.filter(course=Course.objects.get(id=gr.course.id))

    data['cours'] = Course.objects.all()

    #data['zaivki'] = claim.objects.filter(course=Course.objects.get(id=Group.course.id))
    if request.method=="POST":
        print("test")

        try:
            data['zaivki'] = claim.objects.filter(course=Course.objects.get(id=request.POST['item_id']))
            gr = Group.objects.get(id=id_profile)
            gr.course = Course.objects.get(id=request.POST['item_id'])
        except Course.DoesNotExist:
            data['error'] = "Выберите курс"
            print("sdf")
        gr.save()
        return redirect('group')

    data['group'] = gr
    return render(request, 'manager/group/profile_group.html', data)






def create_group(request):
    data={}
    data.update(init_news(request))
    """  # получение курсов для конкретоного пользователя 
    /*  Шаблон
     {% for courses in course %}
                      <a href="#"> {{ courses.g_name }} </a>   <br>

                    {% endfor %}
      */              
    
    try:
        user = User.objects.get(id=12).course_set.all()
        data['course'] = user
    except User.DoesNotExist:
        data['error'] = "None"
   
    prep= Course.objects.get(g_name="3D моделирование")
    data['error'] = prep.prepod.user.username
 """
    objectlist = Course.objects.all()
    data['list'] = objectlist
    group = Group.objects.all() # Выбираем все группы для списка
    data['Group'] = group #Передаем их в шаблон
    form = add_group() #Создаем форму

    if request.GET.get('delete'): #Если нажали удалить (существует такой параметр в GET)
        delet = Group.objects.get(id=request.GET['id']) #Ищем по ид
        delet.delete() #Удаляем запись
        return redirect('group') #Обновляем страницу (Выходим из функции)

    if request.GET.get('redactory'): #Если нажали на редактировать (имя из списка нажали)
        data['knopka_red'] = True #Устанавливаем скрытому полю значение
        poisk= Group.objects.get(id=request.GET.get('id'))#Ищем запись с указанным ид
        dataform = {'Name': poisk.g_name} #Передаем в форму
        form = add_group(dataform) #Создаем форму и заполняем найденым значением


    prep = personal.objects.all()
    data['pred'] = prep

    data['form'] = form #Создаем пустую форму (первый вход)
    if request.method == 'POST': #Если передается форма (нажали добавить)
        form = add_group(request.POST) #Заполняем форму значениям которые получили
        if form.is_valid(): # Проверяем валидность
             dataform = form.cleaned_data # получаем чистые данные
             try:
                if request.GET.get('redactory'):#Если была нажата кнопка редактировать (заранее)
                    red = Group.objects.get(id=request.GET['id']) #ищем ид который так же передавался
                    red.g_name = dataform['Name'] #новое значение
                    red.save() # сохраняем

                    return redirect('group') #Обновляем страницу(редерект туда же)
                #Если не была нажата кнопка редактировать, значит пытаемся добавить
                new=Group.objects.get(g_name=dataform['Name'])
                data['error'] = 'Уже есть такой курс' #Если нашелся такой же курс
             except Group.DoesNotExist:#Если не нашелся создаем
                new=Group.objects.create(g_name=dataform['Name'])
                new.save()#Сохраняем

    return render(request, 'manager/group/create_group.html', data)


def delete_news(request,id_post):
    post=novelty.objects.get(id=id_post)
    post.delete()
    print("delete")
    return redirect('add_news')


def add_news(request):
    data = {}
    data.update(init_news(request))
  #-----------------------------------------------------------------------

    form = add_new_post()

    if request.method == 'POST':
        form = add_new_post(request.POST)
        if form.is_valid():
             dataform = form.cleaned_data

             try:
                new=novelty.objects.get(heading =dataform['zagolovok'])
                print("exces")
                data['error'] = 'Такая новость уже есть'
             except novelty.DoesNotExist:
                new=novelty.objects.create(
                    name=request.user.first_name+" "+request.user.last_name,
                    heading=dataform['zagolovok'],
                    body=dataform['body'],
                    data=date.today(),
                    time = datetime.now().time()
                )
                new.save()

        else:
            print("Error")


    data['form'] = form

    all_news = novelty.objects.all()

    data['all_news'] = all_news


    return render(request, 'manager/news/add_news.html', data)


def course(request):
    data={}
    data.update(init_news(request))
    data['posts'] = Course.objects.filter(type_cours='2')
    return render(request, 'manager/course/course.html', data)





def course_qvant(request):
    data={}
    data.update(init_news(request))

    return render(request, 'manager/qvant/qvant.html', data)



def info_qvant(request,id):
    data={}
    data.update(init_news(request))
    qv = Course.objects.get(id=id)

    if request.method == 'POST':
        count = claim.objects.all().filter(user=request.user.id, type_cours='1')  # Смотрим количество заявок от данного пользователя
        qvant_ =claim.objects.all().filter(user=request.user.id, type_cours='1')
        print(count)
        if qvant_ == 1:
            data['error'] = "Уже есть заявка"
        else:
            if (count.count() < 1):  # Если количество записей больше двух (или изменено в настройках)
                zaivka = claim.objects.create()
                zaivka.user = User.objects.get(id=request.user.id)
                zaivka.data = datetime.now().date()
                zaivka.course = Course.objects.get(id=id)
                zaivka.type_cours = '1'
                zaivka.status = 1
                zaivka.save()
            else:
                data['max'] = "Больше нельзя"
        # print(qv.body)
    data['qv'] = qv
    data['user'] = request.user


    return render(request, 'manager/qvant/info_qvant.html', data)



def info_course(request,id):
    data={}
    data.update(init_news(request))
    qv= Course.objects.get(id=id)

    if request.method=='POST':
            count=claim.objects.all().filter(user=request.user.id,type_cours='2') #Смотрим количество заявок от данного пользователя
            cours_doubl = claim.objects.all().filter(user=request.user.id,course=id) #Смотрим, что бы такой (с таким же курсом) заявки не было
            print(cours_doubl.count())
            if (cours_doubl.count()==1):#Если уже есть заявка
                data['doubl'] = "Уже отправлена"
            else: #Иначе проверяем and (cours_doubl.count() < 1
                if (count.count() < settings.COUNT_ZAIVOK): # Если количество записей больше двух (или изменено в настройках)
                    zaivka = claim.objects.create()
                    zaivka.user=User.objects.get(id=request.user.id)
                    zaivka.data = datetime.now().date()
                    zaivka.course=Course.objects.get(id=id)
                    zaivka.status=1
                    zaivka.type_cours='2'
                    zaivka.save()
                else:
                     data['max'] = "Больше нельзя"

    #print(qv.body)
    data['qv'] = qv
    data['user'] = request.user

    return render(request, 'manager/course/info_cours.html', data)






def edit_course(request,id):
    data={}
    form = add_cours()
    data['form'] = form

    if request.method == "POST":
        form = add_cours(request.POST)
        if form.is_valid():
            dataform = form.cleaned_data

            try:
                cour = Course.objects.get(name=dataform['name'])
                print("exces")
                data['error'] = 'Такой курс уже есть'
            except Course.DoesNotExist:
                cour = Course.objects.create(name=dataform['name'])
                cour.type_cours = '2'  # Указываем что это не квант а курс
                cour.save()

    data.update(init_news(request))
    data['courses'] = Course.objects.all()
    return render(request, 'manager/course/add_course.html', data)





def delete_course(request,id_profile):
    post = Course.objects.get(id=id_profile)
    post.delete()
    print("delete")
    return redirect('add_course')







def add_course(request):
    data={}
    form = add_cours()
    data['form'] = form

    if request.method == "POST":
        form = add_cours(request.POST)
        if form.is_valid():
            dataform = form.cleaned_data

            try:
                cour=Course.objects.get(name = dataform['name'])
                print("exces")
                data['error'] = 'Такой курс уже есть'
            except Course.DoesNotExist:
                cour = Course.objects.create(name=dataform['name'])
                cour.type_cours='2'#Указываем что это не квант а курс
                cour.save()

    data.update(init_news(request))
    data['courses'] = Course.objects.all()
    return render(request, 'manager/course/add_course.html', data)








def bid(request):
    data={}
    data.update(init_news(request))
    data['zaivki'] = claim.objects.filter(user_id=request.user.id)
    if data['zaivki'].count() ==0:
        data['error'] = 1
    if request.GET.get('id'):
        try:
            za=claim.objects.get(id=request.GET['id'])
            za.delete()
        except claim.DoesNotExist:
            print("error")


    return render(request, 'manager/zaivki/zaivki.html', data)



def group(request):
    data = {}
    data.update(init_news(request))
    data['group'] = _get_grpoup()


    return render(request, 'manager/group/group.html', data)






def raspisanie(request):
    data = {}
    data.update(init_news(request))
    data['form'] = time_table()
    data['group'] = _get_grpoup()

    return render(request, 'manager/group/raspisanie.html', data)







#Api -----------------------------------------------
def api_login(request):
    name = request.GET['name']
    #obj = User.objects.get(pk=id)
    otv = "NONE"
    try:
        obj = User.objects.get(username=name)
        #otv = obj.username
        otv = "<div class='red'>Занято</div>"
    except User.DoesNotExist:
        otv = "<div class='green'>Свободно</div>"


    response = HttpResponse(otv, content_type="text/plain")
    return response;






#admins -------------------------------------------------------------------------------
@permission_required('manager.adminenter',login_url='login')
def admin_user(request):
    #print(request.user.is_authenticated)
    data= {}
    data['prava'] = request.user.has_perm('manager.adminenter')
    data['new'] = novelty.objects.all().order_by('-pk')[:settings.NEWS_COLUMN]
    data['longing'] =request.user.is_authenticated


    try:
        print(request.user.profile.Status)
        #if (int(request.user.profile.Status) >= 3):
        #    acess = 1
        #    print("ENTER")


    except Profile.DoesNotExist:
        print("No")

    data.update(init_news(request))
    data['users'] = User.objects.all()


    return render(request, 'manager/admins.html', data)

