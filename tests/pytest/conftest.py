from example.models import db

from fixtures import *


def pytest_runtest_setup(item):
    integration_marker = item.get_marker("integration")

    if integration_marker is not None:
        db.drop_all_tables(with_all_data=True)
        db.create_tables()
