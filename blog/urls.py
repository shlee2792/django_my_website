from django.urls import path, include
from . import views

urlpatterns = [
    path('category/<str:slug>/', views.PostListByCategory.as_view()),
    path('create/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.PostListByTag.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('<int:pk>/update/', views.PostUpdate.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]

