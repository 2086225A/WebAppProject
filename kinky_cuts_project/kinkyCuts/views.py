from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from kinkyCuts.models import User, Creation, Rating
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        username = request.POST['name']
        user = User.objects.get(username=username)
        data = request.POST['imageData']
        allCreations = Creation.objects.all()
        imageid = len(allCreations) + 1
        newC = Creation.objects.create(user=user, imageID=imageid, picture="1.png")
        newC.save()

    context_dict = {}
    if request.user.is_authenticated():
        context_dict['username'] = request.user.get_username()

    return render(request, 'kinkyCuts/index.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'kinkyCuts/about.html', context_dict)

@csrf_exempt
def explore(request):
    if request.method == 'POST':
        like = request.POST["like"]
        imageid = request.POST["imageID"]
        creation = Creation.objects.get(imageID = imageid)
        if like == "true":
            creation.likes += 1
            creation.save()
            rating = Rating.objects.get_or_create(user=request.user, imageID=creation)
            rating[0].save()
        else:
            creation.likes -= 1
            creation.save()
            rating = Rating.objects.get(user=request.user, imageID=creation)
            rating.delete()

    #get all pictures that the user has liked in a list
    allratings = Rating.objects.all()
    users_ratingList = []
    for rating in allratings:
        if rating.user.username == request.user.username:
            users_ratingList += [rating.imageID]

    #all picture objects in a list
    pictures = Creation.objects.all()

    # picturesDictionary which has picture object as key, and boolean which identifies whether user has liked/not liked a specific picture
    picturesDict = {}
    for pic in pictures:
        boolean = "false"
        try:
            if pic.user != request.user:
                for creation in users_ratingList:
                    if creation == pic:
                        boolean = "true"
                picturesDict[pic] = boolean
        except:
            picturesDict[pic] = "null"


    context_dict = {'pictures':picturesDict, 'ratings':users_ratingList}
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
