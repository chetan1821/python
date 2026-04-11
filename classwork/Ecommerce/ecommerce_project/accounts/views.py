from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.views.decorators.http import require_http_methods
from django.db import transaction
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm, UserUpdateForm, CustomPasswordChangeForm
from .models import UserProfile


def register(request):
    """
    User registration view.
    Handles both GET (display form) and POST (process registration) requests.
    """
    if request.user.is_authenticated:
        return redirect('products:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # Create user
                    user = form.save()
                    
                    # Create user profile
                    UserProfile.objects.create(user=user)
                    
                    messages.success(request, 'Registration successful! Please log in.')
                    return redirect('accounts:login')
            except Exception as e:
                messages.error(request, f'Registration failed: {str(e)}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = UserRegistrationForm()
    
    context = {
        'form': form,
        'page_title': 'Register',
    }
    return render(request, 'accounts/register.html', context)


def login_view(request):
    """
    User login view.
    Authenticates user credentials and creates session.
    """
    if request.user.is_authenticated:
        return redirect('products:home')
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            remember_me = form.cleaned_data.get('remember_me')
            
            # Try to authenticate with username first, then email
            user = authenticate(request, username=username, password=password)
            
            if user is None:
                # Try with email
                from django.contrib.auth.models import User
                try:
                    user = User.objects.get(email=username)
                    user = authenticate(request, username=user.username, password=password)
                except User.DoesNotExist:
                    user = None
            
            if user is not None:
                login(request, user)
                
                # Set session expiry based on "remember me"
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)  # Browser close
                
                messages.success(request, f'Welcome back, {user.first_name or user.username}!')
                
                # Redirect to next page or home
                next_url = request.GET.get('next', 'products:home')
                return redirect(next_url)
            else:
                messages.error(request, 'Invalid username/email or password.')
    else:
        form = UserLoginForm()
    
    context = {
        'form': form,
        'page_title': 'Login',
    }
    return render(request, 'accounts/login.html', context)


@login_required(login_url='accounts:login')
def logout_view(request):
    """
    User logout view.
    Clears session and redirects to home.
    """
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('products:home')


@login_required(login_url='accounts:login')
def profile_view(request):
    """
    User profile view.
    Displays user information and allows editing.
    """
    try:
        user_profile = request.user.profile
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'page_title': 'My Profile',
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='accounts:login')
def change_password(request):
    """
    Change password view.
    Allows authenticated users to change their password.
    """
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # This is important to refresh the user's session
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully!')
            return redirect('accounts:profile')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{error}')
    else:
        form = CustomPasswordChangeForm(request.user)
    
    context = {
        'form': form,
        'page_title': 'Change Password',
    }
    return render(request, 'accounts/change_password.html', context)


def page_not_found(request, exception):
    """Handle 404 errors."""
    return render(request, '404.html', status=404)


def server_error(request):
    """Handle 500 errors."""
    return render(request, '500.html', status=500)
