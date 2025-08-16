from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileUpdateForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) # Create empty Profile for the new user
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        return render(request, 'blog/register.html', {'form': form})
    
# using class based view sample
# class RegisterView(CreateView):
#     form_class = CustomUserCreationForm  # Use your custom form
#     template_name = 'registration/register.html'  # Template for the form
#     success_url = reverse_lazy('login')  # Redirect to login after success

#     def form_valid(self, form):
#         # Optional: Add custom logic here, e.g., send welcome email
#         return super().form_valid(form)

# user profile view

# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     # get or create user profile if one doesn't exist
#     form_class = ProfileUpdateForm
#     template_name = 'blog/profile_update.html'
#     success_url= reverse_lazy('profile')

#     def get_object(self):
#         return self.request.user
    
#     def form_valid(self, form):
#         print("Form is valid, saving user:", self.request.user.username)
#         return super().form_valid(form)
    
#     def form_invalid(self, form):
#         print("Form errors:", form.errors)
#         return super().form_invalid(form)
    
# function based profile update
@login_required
def profile_update_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            print("Saving user:", request.user.username)  # Debugging
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            print("Form errors:", user_form.errors)  # Debugging
    else:
        user_form = ProfileUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
    return render(request, 'blog/profile_update.html', {'user_form': user_form, 'profile_form': profile_form})

    
# blog/views.py (add this for a basic profile view)
@login_required
def profile_view(request):
    return render(request, 'blog/profile.html', {'user': request.user})
