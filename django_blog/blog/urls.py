from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, profile_view, profile_update_view
from .views import ( BlogPostListView, BlogPostCreateView,
                    BlogPostDeleteView, BlogPostDetailView,
                    BlogPostUpdateView, BlogCommentCreateView,
                    BlogCommentUpdateView, BlogCommentDeleteView
                    , SearchView, PostByTagListView)

urlpatterns = [
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('register/', register_view, name='register'),
    # path('profile/update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile-update/', profile_update_view, name='profile-updates'),
    path('profile/', profile_view, name='profile'),
    path('post/', BlogPostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('post/new/', BlogPostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', BlogPostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', BlogCommentCreateView.as_view(), name='comment-create'),
    # /posts/int:post_id/comments/new/
    path('comment/<int:pk>/update/', BlogCommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', BlogCommentDeleteView.as_view(), name='comment-delete'),
    path('search/', SearchView.as_view(), name='search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='tag-posts') # the url can be /<str:tag_name>/ following the context_object_data name in the taglistview
]