import pytest

from example.models import PersonRepository


@pytest.fixture
def person_repository():
    return PersonRepository()


@pytest.fixture(params=["Andrew", "James Grossweiner"])
def person(request, person_repository):
    return person_repository.create(request.param, 20)
