import json
from collections import OrderedDict

import requests

from example.models import PersonRepository


class NSAService:

    def __init__(self):
        self._session = requests.Session()

    def send(self, data):
        unprepared_request = requests.Request(
            headers={
                'Content-Type': 'application/json',
            },
            auth=None,
            method='POST',
            url='https://httpbin.org/post',
            json=data,
        )
        prepared_request = self._session.prepare_request(unprepared_request)

        with self._session as session:
            result = session.send(request=prepared_request)

        result.raise_for_status()

        return result


def send_user_info_to_nsa(user_id):
    nsa_service = NSAService()
    person = PersonRepository().get_by_id(user_id)
    user_info = OrderedDict([('age', person.age), ('name', person.name)])
    return nsa_service.send(data=json.dumps(user_info))
