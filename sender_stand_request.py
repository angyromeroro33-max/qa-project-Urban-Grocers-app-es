import requests
import configuration
import data


def post_new_user(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=body
    )


def post_new_client_kit(kit_body, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
        json=kit_body,
        headers=headers
    )