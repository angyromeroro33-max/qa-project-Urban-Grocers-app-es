import sender_stand_request

# Crear usuario y obtener authToken
def test_create_user():
    auth_token = sender_stand_request.get_new_user_token()
    print(f"AuthToken obtenido: {auth_token}")

    # Verificar que el token no esté vacío
    assert auth_token != ""
    print("✅ Usuario creado exitosamente!")


# Ejecutar la prueba
if __name__ == "__master__":
    test_create_user()