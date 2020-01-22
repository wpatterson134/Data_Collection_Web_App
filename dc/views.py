from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .models import Media
from .forms import UserForm
from django.db.models import Q
from django.shortcuts import render
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'dc/login.html')
    else:

        all_media = Media.objects.filter(user=request.user)
        x = all_media.filter(check='Accepted')

        query = request.GET.get("q")
        if query:
            albums = all_media.filter(
                Q(model__icontains=query)
            ).distinct()
            return render(request, 'dc/index.html', {
                'albums': albums,
                'x': x,
            })
        context = {
            'all_media': all_media,
            'x': x
        }
        return render(request, 'dc/index.html', context)


def detail(request, pk):
    if not request.user.is_authenticated:
        return render(request, 'dc/login.html')
    else:
        try:
            all_media = Media.objects.filter(user=request.user)
            media = all_media.get(pk=pk)
            context = {
                'media': media
            }
        except Media.DoesNotExist:
            raise Http404("Media Does not exist")
        return render(request, 'dc/detail.html', context)


class MediaCreate(CreateView):
    model = Media
    fields = ['user', 'model', 'year', 'video']


class MediaUpdate(UpdateView):
    model = Media
    fields = ['user', 'model', 'year', 'video']


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'dc/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_media = Media.objects.filter(user=request.user)
                x = all_media.filter(check='Accepted')
                return render(request, 'dc/index.html', {
                    'all_media': all_media,
                    'x': x,
                })
            else:
                return render(request, 'dc/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'dc/login.html', {'error_message': 'Invalid login'})
    return render(request, 'dc/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_media = Media.objects.filter(user=request.user)
                return render(request, 'dc/index.html', {'all_media': all_media})
    context = {
        "form": form,
    }
    return render(request, 'dc/register.html', context)