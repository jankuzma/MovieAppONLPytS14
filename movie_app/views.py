from django.shortcuts import render, redirect
from django.views import View

from movie_app.forms import AddPersonForm, AddProducderForm
from movie_app.models import Genre, Person, Producer


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
        return render(request, 'list_view.html', {'objects':genres})


class AddPersonView(View):

    def get(self, request):
        form = AddPersonForm()
        return render(request, 'form2.html', {'form':form})

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
        return render(request, 'form2.html', {'form':form})

    def post(self, request):
        form = AddProducderForm(request.POST)
        if form.is_valid():
            Producer.objects.create(
                **form.cleaned_data)
            return redirect('add_producer')
        return render(request, 'form2.html', {'form': form})