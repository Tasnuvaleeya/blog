from django.urls import path
from .views import PostListView, PostDetailView, AboutView, SamplePostView, ContactView


urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/about/', AboutView.as_view(), name='post-about'),
    path('post/sample_post/', SamplePostView.as_view(), name='sample-post'),
    path('post/contact/', ContactView.as_view(), name='contact-view'),
]
