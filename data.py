headers = {
    "Content-Type": "application/json"
}

user_body = {
    "firstName": "Andrea", 
    "phone": "+11234567890",
    "address": "123 Elm Street, Hilltop"
}
kits_url = "/api/v1/kits"
kit_body = {
    "name": "Mi kit",
    "productsList": [
        {
            "id": 1,
            "quantity": 2
        },
        {
            "id": 4,
            "quantity": 3
        },
        {
            "id": 44,
            "quantity": 1
        }
    ]
}
