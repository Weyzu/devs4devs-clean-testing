import pytest


@pytest.mark.integration
def test_person_repository_gets_the_person_by_id(person, person_repository):
    retrieved_person = person_repository.get_by_id(id_=person.id)

    assert retrieved_person.id == person.id
    assert retrieved_person.name == person.name
    assert retrieved_person.age == person.age


@pytest.mark.integration
def test_person_repository_gets_the_person_by_name(person, person_repository):
    retrieved_persons = person_repository.get_by_name(name=person.name)

    assert len((retrieved_persons)) == 1
    assert retrieved_persons[0].id == person.id
    assert retrieved_persons[0].name == person.name
    assert retrieved_persons[0].age == person.age
