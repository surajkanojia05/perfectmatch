from theapp.models import partner
from django.shortcuts import render
from theapp.forms import addprofileform
from .forms import addprofileform
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home.html')


def membership(request):
    return render(request, 'membership.html')


def contact(request):
    return render(request, 'contactus.html')


def partnersearch(request):
    partners=partner.objects.all()
    return render(request, 'partnersearch.html',{'partners':partners})


def searchbyID(request):
    if request.method=="POST":
        searchfor = request.POST['searchfor']
        partners = partner.objects.filter(partner_id__contains=searchfor) 
        return render(request,"searchbyID.html",
         {'searchfor':searchfor, 'partners':partners}) 
         
    else: return render(request,"searchbyID.html")


def about(request):
    return render(request, 'aboutus.html')


def payment(request):
    return render(request, 'payment.html')


def search(request): 
    if request.method=="POST": 
        searched = request.POST['searched'] 
        partners = partner.objects.filter(tag__contains=searched) 
        return render(request,"search.html",
         {'searched':searched, 'partners':partners}) 
         
    else: return render(request,"search.html")
       
def addprofile(request):
    submitted = False
    if request.method == "POST":
        form = addprofileform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_profile?submitted=True')
    else:
        form = addprofileform
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_profile.html', {'form':form, 'submitted':submitted})
