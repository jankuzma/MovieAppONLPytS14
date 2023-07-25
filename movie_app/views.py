import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from movie_app.forms import AddPersonForm, AddProducderForm, AddMovieForm, AddMovieModelForm, SearchPersonForm
from movie_app.models import Genre, Person, Producer, Movie


class IndexView(View):

    def get(self, request):


        return render(request, 'base.html')


# Create your views here.

class AddGenreView(View):

    def get(self, request):
        return render(request, 'form.html')

    def post(self, request):
        name = request.POST.get('name')
        Genre.objects.create(name=name)
        return redirect('add_genre')


class GenreListView(View):

    def get(self, request):
        genres = Genre.objects.all()
        return render(request, 'list_view.html', {'objects': genres})

class GenreAPIListView(View):

    def get(self, request):
        name = request.GET.get('name', '')
        genres = Genre.objects.filter(name__icontains=name)
        d= []
        for g in genres:
            d.append({'id':g.id, 'name':g.name})
        # d = [{'id':g.id, 'name':g.name} for g in genres]
        return JsonResponse(d, safe=False)

class AddPersonView(View):

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'form2.html', {'form': form})

    def post(self, request):
        form = AddPersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(
                **form.cleaned_data)
            return redirect('add_person')
        return render(request, 'form2.html', {'form': form})


class AddProducerView(View):

    def get(self, request):
        form = AddProducderForm()
        return render(request, 'form2.html', {'form': form})

    def post(self, request):
        form = AddProducderForm(request.POST)
        if form.is_valid():
            Producer.objects.create(
                **form.cleaned_data)
            return redirect('add_producer')
        return render(request, 'form2.html', {'form': form})


class AddMovieView(View):

    def get(self, request):
        form = AddMovieModelForm()
        return render(request, 'form2.html', {'form': form})

    def post(self, request):
        form = AddMovieModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_movie')
        return render(request, 'form2.html', {'form': form})


class PersonListView(View):
    def get(self, request):
        persons = Person.objects.all()
        form = SearchPersonForm(request.GET)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name', '')
            last_name = form.cleaned_data.get('last_name', '')
            year = form.cleaned_data.get('year')
            persons = persons.filter(first_name__icontains=first_name, last_name__icontains=last_name)
            if year is not None:
                persons = persons.filter(year=year)
        return render(request, 'person_list.html', {'persons': persons, 'form':form})
