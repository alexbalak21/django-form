from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorsListView.as_view(), name="authors"),
    path('authors/add/', views.AuthorsCreateView.as_view(), name="add_author"),
]
