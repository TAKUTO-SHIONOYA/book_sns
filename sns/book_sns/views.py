from django.shortcuts import render
from django.http import HttpResponse
#from .forms import LoginForm
from .models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import forms
from .forms import UserCreateForm
# Create your views here.
class loginView(LoginView):
    form_class = forms.LoginForm
    template_name = "book_sns/login.html"

class logoutView(LoginRequiredMixin, LogoutView):
    template_name = "book_sns/logout.html"

class TopView(TemplateView):
    template_name = "book_sns/top.html"



def userpage(request):

    if request.user.is_authenticated:
        username = str(request.user)

        #request.session['name'] = request.POST['name']
        context = {'username': username}

        return render(request, 'book_sns/userpage.html',context)
    else:
        return render(request, 'book_sns/top.html')


"""def top(request):

    return render(request, 'book_sns/top.html')
def create(request):
    if (request.method == 'POST'):
        obj = User()
        user = CreateForm(request.POST, instance=obj)
        user.save()
        return redirect(to='/book_sns')
    params = {
        'form': CreateForm()
    }
    return render(request, 'book_sns/user_create.html',params)"""

"""def login(request):
    params = {
    'form': LoginForm()

    }
    if (request.method == 'POST'):
        if mail_address == mail:
            if password == pass:
                return render(request, 'book_sns/userpage<user_id>')
            else:
                message = "passwordが間違っています"
                return render (request,message)
        else:
            message = "mailaddressが間違っています"
            return render(request,message)
    return(request,)"""

def create(request):
    params = {
    'title': 'create',
    'form': UserCreateForm(),

    }

    if (request.method == 'POST'):
        name = request.POST['name']
        mail = request.POST['mail']
        password = request.POST[password]
        user = User(name=name,mail=mail,password=password)
        User.save()
        return redirect(to='/top')
    return render(request, 'book_sns/user_create.html', params)
