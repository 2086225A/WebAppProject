__author__ = 'Naeem'
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kinky_cuts_project.settings')

import django
django.setup()
import datetime

from kinkyCuts.models import Creation, Rating, User

def addcreation(user,imageID,picture):
    c = Creation.objects.get_or_create(user=user,imageID=imageID,picture=picture)
    c[0].save()
    return c
def addrating(user,creation):
    if user != creation.user:
        r = Rating.objects.get_or_create(user=user, imageID=creation)
        creation = Creation.objects.get(imageID=creation)
        creation.likes += 1
        creation.save()
        r[0].save()
        return r


def populate():
    naeem = User.objects.get(username="naeemb123")
    sayyad = User.objects.get(username="sayyad")
    alex = User.objects.get(username="alex")
    nayhall = User.objects.get(username="nayhall")

    #scenario 1
    c1 = addcreation(nayhall, "2", "2.png") #nayhall creates picture
    sayyadlikes = addrating(sayyad, c1[0]) #sayyad likes nayhalls pic

    #scenario 2
    c2 = addcreation(alex, "3", "3.png") #alex creates pic
    #all 3 like users like it
    naeemlikes = addrating(naeem, c2[0])
    nayhall_likes  = addrating(nayhall, c2[0])
    sayyadlikes = addrating(sayyad, c2[0])

    #scenario 3 - creation with no likes
    c3 = addcreation(sayyad, "4", "4.png")

    #scenario 4 - all users like it
    c4 = addcreation(naeem, "1", "1.png")
    sayyadlikes = addrating(sayyad, c4[0])
    nayhall_likes = addrating(nayhall, c4[0])
    alexlikes = addrating(alex, c4[0])
    naeemlikes = addrating(naeem, c4[0]) #testing to see if user can like his own picture

    #scenario5
    c5 = addcreation(sayyad, "5", "baldguy.png")
    naeemlikes = addrating(naeem, c5[0])
    alexlikes = addrating(alex, c5[0])

    #scenario 6
    c6 = addcreation(nayhall, "6", "leif-azzopardi.jpg")
    sayyadlikes = addrating(sayyad, c6[0])

    # Print out what we have added to the user.
    for c in Creation.objects.all():
        for r in Rating.objects.filter(imageID=c):
            print "- {0} - {1}".format(str(c), str(r))


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()