from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, StreamingHttpResponse
from .models import Song
from django.template import loader
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from pytube import YouTube


def get_template_for(request, str, ctx={}):
    template = loader.get_template(str + '.html')
    context = ctx
    ctx['user'] = request.user
    return HttpResponse(template.render(context, request))

def index(request):
    return get_template_for(request, 'index')

@csrf_exempt
def addsong(request):
    url = request.POST['url']
    song = Song.create(url, request.user)
    return redirect('/profile')

def profile(request):
    list = Song.objects.filter(user=request.user).all()
    return get_template_for(request, 'profile', { 'slist' : list });


@csrf_exempt
def signin(request):
    if request.POST.get('username') is not None and request.POST.get('password') is not None:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return get_template_for(request, 'signin', {'error' : 1})
    else:
        return get_template_for(request, 'signin')

@csrf_exempt
def signup(request):

    if request.POST.get('username') is not None:
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('username') + '@users.com', request.POST.get('password'))
        login(request, user)
        return redirect('/')
    else:
        return get_template_for(request, 'signup')