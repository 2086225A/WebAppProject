from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from kinkyCuts.models import User, Creation, Rating
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'kinkyCuts/index.html', context_dict)


def about(request):
    context_dict = {}
    return render(request, 'kinkyCuts/about.html', context_dict)


def explore(request):
    pictures = Creation.objects.all()
    context_dict = {'pictures': pictures}
    return render(request, 'kinkyCuts/explore.html', context_dict)


@login_required
def mypictures(request):
    current_user = request.user.username
    all_pictures = Creation.objects.all()
    current_users_pictures = []  # contains current users pictures
    likes_for_pictures = {}
    all_ratings = Rating.objects.all()

    # updates current users pictures
    #updates all people who liked each picture of current user
    for picture in all_pictures:
        users_likes = []
        if picture.user.username == current_user:
            current_users_pictures += [picture]

    context_dict = {'pictures': current_users_pictures}
    return render(request, 'kinkyCuts/mypictures.html', context_dict)


def myaccount(request):
    context_dict = {}
    return render(request, 'kinkyCuts/myaccount.html', context_dict)


def helpage(request):
    context_dict = {}
    return render(request, 'kinkyCuts/help.html', context_dict)


def sign(request):
    context_dict = {}
    return render(request, 'kinkyCuts/sign.html', context_dict)


def canvas(request):
    context_dict = {}
    return render(request, 'kinkyCuts/canvas.html', context_dict)
