from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from kinkyCuts.models import User, Creation, Rating, UserProfile
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from kinkyCuts.forms import UserProfileForm, ImageUploadForm
from django.shortcuts import redirect

@csrf_exempt
def index(request):
    if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		if form.is_valid():
			username = request.user.get_username()
			user = User.objects.get(username=username)
			allCreations = Creation.objects.all()
			imageid = len(allCreations) + 1
			pic = form.cleaned_data['image']
			newC = Creation.objects.create(user=user, imageID=imageid, picture=pic)
			newC.save();

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

    context_dict = {'pictures':pictures, 'ratings':users_ratingList}
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
    #create userprofile object for any user that does not currently have one
    userprofiles = UserProfile.objects.all()
    b = "false"
    for profile in userprofiles:
        if request.user == profile.user:
            b = "true"
    if b == "false":
        user = request.user
        profile1 = UserProfile.objects.create(user=user, profilepic="default.png")
        profile1.save()


    if request.method == 'POST':
        user_profile_form = UserProfileForm(data=request.POST, instance=request.user.userprofile)
        if user_profile_form.is_valid():
            if request.user.is_authenticated():
                user_profile = UserProfile.objects.get(user_id=request.user.id)
                if 'profilepic' in request.FILES:
                    user_profile.profilepic = request.FILES['profilepic']
                user_profile.save()

                return redirect('/kinkycuts/myaccount/')


    user_profile_form = UserProfileForm(instance=request.user.userprofile)
    #show users information
    user = request.user
    profile = UserProfile.objects.get(user=user)
    context_dict['user_name'] = user.username
    context_dict['user_email'] = user.email
    context_dict['userprofile'] = profile
    context_dict['profile_form'] = user_profile_form

    return render(request, 'kinkycuts/myaccount.html', context_dict)

def editProfile(request):
    context_dict = {}
    if request.method == 'POST':
        user_profile_form = UserProfileForm(data=request.POST, instance=request.user.userprofile)
        if user_profile_form.is_valid():
            if request.user.is_authenticated():
                user_profile = UserProfile.objects.get(user_id=request.user.id)
                if 'profilepic' in request.FILES:
                    user_profile.profilepic = request.FILES['profilepic']
                user_profile.save()

                return redirect('/kinkycuts/myaccount/')
    else:
        user_profile_form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'kinkyCuts/edit_profile.html', {'profile_form': user_profile_form})
