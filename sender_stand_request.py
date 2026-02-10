import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                        json=body,
                        headers=data.headers)


def get_new_user_token():
    user_body = data.user_body.copy()  # o como tengas definido tu cuerpo de usuario
    response = post_new_user(user_body)

    # Líneas de depuración - agrégalas temporalmente
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    print("Response headers:", response.headers)

    # Solo intenta parsear JSON si el status code es exitoso
    if response.status_code == 201:
        return response.json()["authToken"]
    else:
        print("Error: No se pudo crear el usuario")
        return None
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                        json=kit_body,
                        headers=headers)
def get_new_user_token():
    user_response = post_new_user(data.user_body)
    if user_response.status_code == 201:
        return user_response.json()["authToken"]
    else:
        print(f"Error creando usuario: {user_response.status_code}")
        return None

def test_create_kit_511_characters_success():
        response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
        print(f"Código de respuesta: {response.status_code}")
        assert response.status_code == 201
