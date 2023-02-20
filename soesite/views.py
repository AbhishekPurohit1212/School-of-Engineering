from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse,HttpResponseRedirect
from soesite.models import subject
from soesite.models import resource
from django.contrib.auth.models import User
from soesite.models import review
from django.contrib import messages
# Create your views here.
def disphomepage(request):
    happyusers= review.objects.all().count();
    nbooks= resource.objects.filter(resource_type= 'Book').count();
    nvideos= resource.objects.filter(resource_type='video').count();
    dic={'happyusers': happyusers,
         'nbooks': nbooks,
         'nvideos': nvideos}
    rend = render(request,'soesite/homepage.html',dic)
    return rend

def disresources(request):
    if('islogin' in request.session):
        year1= subject.objects.filter(year_id=1)
        year2= subject.objects.filter(year_id=2)
        year3= subject.objects.filter(year_id=3)
        year4= subject.objects.filter(year_id=4)
        subs= {'year1': year1,
               'year2': year2,
               'year3': year3,
               'year4': year4}
        rend = render(request, 'soesite/resources.html', subs)
        return rend
    else:
        messages.info(request, 'Login to use resources!')
        return HttpResponseRedirect('http://localhost:8000/loginandregister/loginpage/')

def dissubject(request, subject_id):
    if('islogin' in request.session):
        sub= subject.objects.get(subject_id= int(subject_id))
        books=sub.resource_set.filter(resource_type= "Book")
        videos= sub.resource_set.filter(resource_type= "video")
        notes= sub.resource_set.filter(resource_type= "Notes")
        subdic= {'sub': sub,
                 'books': books,
                 'videos': videos,
                 'notes': notes}
        rend= render(request, 'soesite/subject.html', subdic)
        return rend
    else:
        messages.info(request, 'Login to use resources!')
        return HttpResponseRedirect('http://localhost:8000/loginandregister/loginpage/')

def createreview(request, subject_id):
    if(request.method=='POST'):
        sub= subject.objects.get(subject_id= int(subject_id))
        user= User.objects.get(username= request.session['user_name'])
        text=request.POST['reviewtext']
        newrev= review.objects.create(user_id=user, subject_id=sub, suggestion=text)
        newrev.save()
        messages.info(request, "Review submitted successfully. Thanks for your feedback")
        return HttpResponseRedirect('http://localhost:8000/soesite/resources/'+str(subject_id)+'/#query-box')
    else:
        return HttpResponse("bahg")

