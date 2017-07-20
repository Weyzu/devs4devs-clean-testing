import pytest

from example.controllers import send_user_info_to_nsa


@pytest.fixture()
def requests_mock(mocker):
    return mocker.patch("requests.sessions.Session.send")


@pytest.mark.integration
@pytest.mark.parametrize('person', ['Edward Joseph Snowden'], indirect=True)
def test_send_user_info_to_nsa_makes_call_to_nsa_with_user_info(
    person,
    requests_mock,
):
    send_user_info_to_nsa(person.id)

    assert requests_mock.call_count == 1

    sent_request = requests_mock.call_args[1]['request']

    assert sent_request.method == 'POST'
    assert sent_request.body == (
        b'"{\\"age\\": 20, \\"name\\": \\"Edward Joseph Snowden\\"}"'
    )
