import csv
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UserProfile
from .forms import UserProfileForm

def list_profiles(request):
    profiles = UserProfile.objects.all()
    return render(request, 'list.html', {'profiles': profiles})

def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_profiles')
    else:
        form = UserProfileForm()
    
    return render(request, 'create.html', {'form': form})

def view_profile(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    return render(request, 'view_profile.html', {'profile': profile})

def update_profile(request, pk):
    
    profile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('list_profiles')
    else:
        form = UserProfileForm(instance=profile)
    
    return render(request, 'create.html', {'form': form, 'edit_mode': True})

def delete_profile(request, pk):
    
    profile = UserProfile.objects.get(pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('list_profiles')
    
    return render(request, 'delete_confirm.html', {'profile': profile})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="user_profiles.csv"'

    writer = csv.writer(response)
    
    writer.writerow(['Username', 'Age', 'Public Status'])

    profiles = UserProfile.objects.all()
    for profile in profiles:
        status = 'Public' if profile.is_public else 'Private'
        writer.writerow([profile.username, profile.age, status])

    return response
