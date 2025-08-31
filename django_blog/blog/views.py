from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, ProfileUpdateForm, ProfileForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Profile, Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView
                                  )

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user) # Create empty Profile for the new user
            return redirect('login')
        # else:
        #     print("Form errors:", form.errors)
        #     # Render the form again with errors
        #     return render(request, 'blog/register.html', {'form': form})
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
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'blog/profile.html', {'user': request.user, 'profile': profile})


# List all posts (accessible to everyone)
class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    # can also use 
    # queryset = Post.objects.order_by('-published_date')
    # Using get_queryset to add logic to the queryset selection 
    def get_queryset(self):
        return super().get_queryset().filter() # For now, this has no filter, I can add filters later (e.g., filter published posts)

# View a single post (accessible to everyone)
class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add comments to the context, ordered by creation date (newest first)
        # can also be
        # comments = self.get_object().comments.all().order_by('-created_at')
        # but not
        # comments = self.get_object.comments.all().order_by('-created_at')
        comments = self.object.comments.all().order_by('-created_at')
        print(f"Comments for post {self.object.title}: {comments}")
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        return context


        return 
# only logged in users
        # comments = self.get_object().comments.all().order_by('-created_at')
class BlogPostCreateView(CreateView, LoginRequiredMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'
    success_url = reverse_lazy('post-list')

    # Automatically set the author to the current user
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
# only logged in users can have access
class BlogPostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html' #reuse same form as post
    success_url = reverse_lazy('post-list')

    # Automatically set the author to the current user (optional)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Test if the current user is the author
    def test_func(self):
        post = self.get_object() # Get the post being updated
        return self.request.user == post.author # True if user is author, else 403 Forbidden
    
# only authenticated users can delete
class BlogPostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_confirm_delete.html' # delete confirmation template
    success_url = reverse_lazy('post-list')

    # test if the current user is the author
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# class BlogCommentsListView(ListView):
#     model = Comment
#     # template_name = 
#     # success_url =

class BlogCommentCreateView(CreateView, LoginRequiredMixin):
    model = Comment
    template_name = 'blog/post_detail.html'
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])  # Set post from URL pk
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})  # Redirect to post detail



class BlogCommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_form.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.post.pk})
    
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author

class BlogCommentDeleteView(DeleteView, LoginRequiredMixin):
    model = Comment
    template_name =  'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk} )
    
    def test_func(self):
        comment = self.get.object()
        return self.request.user == comment.author

class SearchView(ListView):
    model = Post
    template_name = 'blog/search_results/html'
    context_object_name = 'posts'
    ordering = '-published_date'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            # filter post where title, content, or tags match query (case-insensitive)
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct() # distinct avoid duplicate posts
        return Post.objects.all() # returns all posts if no query
        #returns filtered posts orr all posts if query is empty

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '') # Pass query to template for display
        print(f"Search query? {context['query']}, Results: {context['posts'].count()}") # Debug print
        return context
    
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/tag_posts.html'
    context_object_name = 'posts'
    ordering = ['-published_date'] #can be in a list bracket

    def get_queryset(self):
        tag_name = self.kwargs['tag_name'] # get tagname from url
        return Post.objects.filter(tags__name=tag_name) # filters posts by exact tag name
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['tag_name'] #pass tag to template
        return context