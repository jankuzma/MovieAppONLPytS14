import pytest
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType

from movie_app.models import Genre, Person, Producer, Movie


@pytest.fixture
def genres():
    return [Genre.objects.create(name = x) for x in range(5)]

@pytest.fixture
def user():
    return User.objects.create(username='testowy')

@pytest.fixture
def user_with_genre_perms(user):
    content_type = ContentType.objects.get(app_label='movie_app',
                                           model='genre')
    permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(permissions)
    return user

@pytest.fixture
def user_with_movie_perms(user):
    content_type = ContentType.objects.get(app_label='movie_app',
                                           model='movie')
    permissions = Permission.objects.filter(content_type=content_type)
    user.user_permissions.set(permissions)
    return user

@pytest.fixture
def persons():
    return [Person.objects.create(first_name=x, last_name=x, year=10) for x in range(5)]

@pytest.fixture
def persons_delete():
    [Person.objects.create(first_name=x, last_name=x, year=10) for x in range(5)]
    [obj.delete() for obj in Person.objects.all()]
    return Person.objects.all()

@pytest.fixture
def person_edit():
    p1 = Person.objects.create(first_name='x', last_name='x', year=10)

    p1.first_name = 'test'
    p1.last_name ='test'
    p1.year = 20
    p1.save()
    return p1

@pytest.fixture
def producers():
    return [Producer.objects.create(name=x, city=x, year=10) for x in range(5)]

@pytest.fixture
def movie(producers, persons):
    producer = producers[0]
    person = persons[0]
    return Movie.objects.create(title='new hope', year=10,
                                director_id=person.id,
                                producer_id=producer.id)

@pytest.fixture
def movies(producers, persons):
    return [Movie.objects.create(title=x, year=10, director_id=1, producer_id=1) for x in range(5)]