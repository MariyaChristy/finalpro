from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from MovieApp.models import Profile
from .forms import ProfileEditForm
# Create your views here.
def  profile(request):
    profile=Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})


def edit_profile(request, id):
    profile = get_object_or_404(Profile, id=id)
    form = ProfileEditForm(request.POST or None, request.FILES or None, instance=profile)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile is updated')
            return redirect('/')

    return render(request, "edit_profile.html", {'form': form, 'profile': profile})
