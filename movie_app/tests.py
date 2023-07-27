from datetime import datetime

import pytest
from django.test import Client
from django.urls import reverse

from movie_app.forms import SearchPersonForm, AddPersonForm
from movie_app.models import Person, Genre, Producer, Comment


@pytest.mark.django_db
def test_index():
    browser = Client()
    url = reverse('index')
    response = browser.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_genre_list(genres):
    browser = Client()
    url = reverse('list_genre')
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['genres'].count() == len(genres)


@pytest.mark.django_db
def test_person_list(persons):
    browser = Client()
    url = reverse('list_person')
    response = browser.get(url)
    assert response.status_code == 200
    assert list(response.context['persons']) == persons
    assert (isinstance(response.context['form'], SearchPersonForm))


@pytest.mark.django_db
def test_person_search(persons):
    browser = Client()
    url = reverse('list_person')
    data = {
        'first_name': '1',
        'last_name': '1',
        'year': 10
    }
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['persons'].get(**data)


# @pytest.mark.django_db
# def test_producers(producers):
#     browser = Client()
#     url = reverse('list_producer')
#     response = browser.get(url)
#     assert response.status_code == 200
#     assert list(response.context['producers']) == producers


@pytest.mark.django_db
def test_person_delete(persons_delete):
    browser = Client()
    url = reverse('list_person')
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['persons'].count() == 0


# @pytest.mark.django_db
# def test_person_edit(person_edit):
#     browser = Client()
#     url = reverse('detail_person')
#     response = browser.get(url)
#     assert  response.status_code == 200
#     assert response.context['person']


@pytest.mark.django_db
def test_producer_detail_view(producers):
    browser = Client()
    p = producers[0]
    url = reverse('detail_producer', kwargs={'id': p.id})
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['producer'] == p


@pytest.mark.django_db
def test_person_detail_view(persons):
    browser = Client()
    p = persons[0]
    url = reverse('detail_person', kwargs={'id': p.id})
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['person'] == p


@pytest.mark.django_db
def test_genre_detail_view_notlogged(genres):
    browser = Client()
    g = genres[0]
    url = reverse('detail_genre', args=(g.id,))
    response = browser.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_genre_detail_view_logged_no_perms(genres, user):
    browser = Client()
    g = genres[0]
    url = reverse('detail_genre', args=(g.id,))
    browser.force_login(user)
    response = browser.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_genre_detail_view_logged_perms(genres, user_with_genre_perms):
    browser = Client()
    g = genres[0]
    url = reverse('detail_genre', args=(g.id,))
    browser.force_login(user_with_genre_perms)
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['genre'] == g


@pytest.mark.django_db
def test_movie_list_view_notlogged(movies):
    browser = Client()
    url = reverse('list_movie')
    response = browser.get(url)
    assert response.status_code == 200
    assert list(response.context['movies']) == movies


@pytest.mark.django_db
def test_movie_list_view_logged_no_perms(movies, user_with_movie_perms):
    browser = Client()
    url = reverse('list_movie')
    response = browser.get(url)
    assert response.status_code == 200
    assert list(response.context['movies']) == movies


@pytest.mark.django_db
def test_movie_list_view(movies):
    browser = Client()
    url = reverse('list_movie')
    response = browser.get(url)
    assert response.status_code == 200
    assert list(response.context['movies']) == movies


@pytest.mark.django_db
def test_movie_detail_view_notlogged(movie):
    browser = Client()
    url = reverse('detail_movie', args=(movie.id,))
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['movie'] == movie


@pytest.mark.django_db
def test_movie_detail_view_logged_no_perms(movie, user):
    browser = Client()
    url = reverse('detail_movie', args=(movie.id,))
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['movie'] == movie


@pytest.mark.django_db
def test_movie_detail_view_logged_with_perms(movie, user_with_movie_perms):
    browser = Client()
    url = reverse('detail_movie', args=(movie.id,))
    response = browser.get(url)
    assert response.status_code == 200
    assert response.context['movie'] == movie

@pytest.mark.django_db
def test_add_person_get():
    browser = Client()
    url = reverse('add_person')
    response = browser.get(url)
    assert  response.status_code == 200
    assert isinstance(response.context['form'], AddPersonForm)


@pytest.mark.django_db
def test_add_person_post():
    browser = Client()
    url = reverse('add_person')
    data ={
        'first_name': 'a',
        'last_name': 'b',
        'year': 10
    }
    response = browser.post(url, data)
    assert  response.status_code == 302
    assert  response.url.startswith(reverse('add_person'))
    assert  Person.objects.get(**data)

@pytest.mark.django_db
def test_add_genre_get():
    browser = Client()
    url = reverse('add_genre')
    response = browser.get(url)
    assert  response.status_code == 200

@pytest.mark.django_db
def test_add_genre_post():
    browser = Client()
    url = reverse('add_genre')
    data = {
        'name': 'horror'
    }
    response = browser.post(url, data)
    assert  response.status_code == 302
    assert response.url.startswith(reverse('add_genre'))
    assert Genre.objects.get(**data)


@pytest.mark.django_db
def test_add_producer_get():
    browser = Client()
    url = reverse('add_producer')
    response = browser.get(url)
    assert  response.status_code == 200

@pytest.mark.django_db
def test_add_producer_post():
    browser = Client()
    url = reverse('add_producer')
    data = {
        'name': 'Eniu',
        'city': 'Lodz',
        'year': 2200
    }
    response = browser.post(url, data)
    assert  response.status_code == 302
    assert response.url.startswith(reverse('add_producer'))
    assert Producer.objects.get(**data)

@pytest.mark.django_db
def test_add_comment_to_movie_get(movie):
    browser = Client()
    url = reverse('add_comment', args=(movie.id, ))
    response = browser.get(url)
    assert  response.status_code == 302

@pytest.mark.django_db
def test_add_comment_to_movie_post(user, movie):
    browser = Client()
    browser.force_login(user)
    url = reverse('add_comment', args=(movie.id,))
    data = {
        'text': 'testowy tekst'
    }
    response = browser.post(url, data)
    assert  response.status_code == 302
    assert  response.url.startswith(reverse('detail_movie', args=(movie.id, )))
    assert  Comment.objects.get(**data)