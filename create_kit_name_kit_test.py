import sender_stand_request
import data

def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    auth_token = sender_stand_request.get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 201

def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")
def test_create_kit_1_letter_in_name_get_success_response():
       pass

def test_create_kit_511_letter_in_name_get_success_response():
       pass
def test_create_kit_512_characters_error():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    }