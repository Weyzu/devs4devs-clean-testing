from pony.orm import Database
from pony.orm import PrimaryKey
from pony.orm import Required
from pony.orm import db_session
from pony.orm import select

db = Database("sqlite", "example.sqlite", create_db=True)


class Person(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    age = Required(int)


class PersonRepository:

    @db_session
    def create(self, name, age):
        person = Person(name=name, age=age)
        return person

    @db_session
    def get_by_id(self, id_):
        return select(p for p in Person if p.id == id_).first()

    @db_session
    def get_by_name(self, name):
        return list(select(p for p in Person if p.name == name))


db.generate_mapping(create_tables=True)
