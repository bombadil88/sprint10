import sender_stand_request
import data

def get_kit_body(name):
    data.kit_body["name"] = name
    return data.kit_body

def positive_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == name

def negative_assert(name):
    kit_body = get_kit_body(name)
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


def test_1_letter():
    positive_assert('имя')

def test_2_letter():
    negative_assert('123123123123123123')

def test_3_letter():
    negative_assert(123)