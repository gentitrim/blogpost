from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostView.as_view(),name="post"),
    path('create_post/', views.CreatePostView.as_view(),name="new_post"),
    path('edit_post/<pk>/edit/', views.ModifyPostView.as_view(),name="edit_post"),
    path('post_detail/<pk>/detail/', views.PostDetailView.as_view(),name="post_details"),
    path('delete_post/<pk>/delete/', views.DeletePostView.as_view(),name="delete_post"),
    
    path('post_coment/<pk>/coment/', views.ComentPostView.as_view(),name="post_coment"),
]