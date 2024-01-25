import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_courses_list(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_filter_id(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/', {'id': courses[5].id},)

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[5].id


@pytest.mark.django_db
def test_filter_name(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/', {'name': courses[5].name},)

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[5].name

@pytest.mark.django_db
def test_course_create(client, course_factory):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', {'id': 1, 'name': 'Python'},)

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_patch_course(client, course_factory):
    courses = course_factory(_quantity=1)

    response = client.patch(f'/api/v1/courses/{courses[0].id}/', {'name': 'New_Name'},)
    response_1 = client.get(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 200
    data = response.json()
    data_1 = response_1.json()
    assert data['name'] == data_1['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=1)

    response = client.delete(f'/api/v1/courses/{courses[0].id}/')
    response_1 = client.get(f'/api/v1/courses/{courses[0].id}/')

    assert response.status_code == 204
    assert response_1.status_code == 404
