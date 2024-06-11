# 2. Realizar solicitud POST a /validate
# validate_url = 'http://mini-challenge.foris.ai/validate'
# validate_body = {
#     'number_of_groups': 10,  # Cambiar esto al número real de grupos
#     'answer': 'Tu_respuesta'  # Cambiar esto a tu respuesta real
# }
# validate_response = requests.post(validate_url, json=validate_body, headers=headers)

# if validate_response.status_code == 200:
#     print("Respuesta de validación:")
#     print(validate_response.json())
# else:
#     print("La solicitud POST a /validate no fue exitosa. Código de estado:", validate_response.status_code)