"""
URL configuration for Movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from movie_app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('addGenre/', views.AddGenreView.as_view(), name='add_genre'),
    path('listGenre/', views.GenreListView.as_view(), name='list_genre'),
    path('addPerson/', views.AddPersonView.as_view(), name='add_person'),
    path('addProducer/', views.AddProducerView.as_view(), name='add_producer'),
    path('addMovie/', views.AddMovieView.as_view(), name='add_movie'),
    path('listPerson/', views.PersonListView.as_view(), name='list_person'),

]
