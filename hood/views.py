from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    # try:
    #     if not request.user.is_authenticated:
    #         return redirect('/accounts/login/')
    #     current_user=request.user
    #     profile =Profile.objects.get(username=current_user)
    # except ObjectDoesNotExist:
    #     return redirect('create-profile')

    return render(request,'index.html')  

def notification(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(neighbourhood=profile.neighbourhood)

    return render(request,'notifications.html',{"notifications":all_notifications})      
