#pip install necesarios

"""
========================================================================
-------------------------| IMPORTACIONES |------------------------------
========================================================================
"""

"""
========================================================================
-----------------------| VARIABLES GLOBALES |---------------------------
========================================================================
"""


"""
========================================================================
---------------------------| FUNCIONES |--------------------------------
========================================================================
"""

"""
========================================================================
-----------------------------| LÓGICA |---------------------------------
========================================================================
"""


import requests

# url = 'http://mini-challenge.foris.ai/login'
# data = {
#     'username': 'foris_challenge',
#     'password': 'ForisChallenge'
# }

# response = requests.post(url, json=data)

# print(response.status_code)
# print(response.json())

"""
========================================================================
"""

# # URL del endpoint /challenge
# challenge_url = 'http://mini-challenge.foris.ai/challenge'

# # Token de acceso obtenido después del inicio de sesión
# access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjUyMzc5OCwianRpIjoiOTQ4MTkxZGEtNzk4MC00ZTQwLTg0NzctNmU2NTE3YmE3YTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZvcmlzX2NoYWxsZW5nZSIsIm5iZiI6MTcxNjUyMzc5OCwiY3NyZiI6IjE2ZmEzODZkLWVlYjQtNDNkNy04ZGI5LWM0NzY3NTc1YmM0NSIsImV4cCI6MTcxNjUyNzM5OH0.zljnLCSDmjyTIdJ4Lj2TFSwgV6lkXmEBqMbV3dT14pE'

# # Encabezado de autorización con el token de acceso
# headers = {
#     'Authorization': f'Bearer {access_token}'
# }

# # Realizar solicitud GET a /challenge con el token de acceso
# response = requests.get(challenge_url, headers=headers)

# # Verificar el código de estado de la respuesta
# if response.status_code == 200:
#     # Imprimir la respuesta 
#     print(response.content)
# else:
#     print("La solicitud no fue exitosa. Código de estado:", response.status_code)

"""
========================================================================
"""

# Token de acceso obtenido después del inicio de sesión
access_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcxNjUyMzc5OCwianRpIjoiOTQ4MTkxZGEtNzk4MC00ZTQwLTg0NzctNmU2NTE3YmE3YTJkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6ImZvcmlzX2NoYWxsZW5nZSIsIm5iZiI6MTcxNjUyMzc5OCwiY3NyZiI6IjE2ZmEzODZkLWVlYjQtNDNkNy04ZGI5LWM0NzY3NTc1YmM0NSIsImV4cCI6MTcxNjUyNzM5OH0.zljnLCSDmjyTIdJ4Lj2TFSwgV6lkXmEBqMbV3dT14pE'

# Encabezado de autorización con el token de acceso
headers = {
    'Authorization': f'Bearer {access_token}'
}

# 1. Realizar solicitud GET a /dumps/{dump_type}
dump_type = 'mysql'  # Cambiar esto según el tipo de volcado que necesites
dumps_url = f'http://mini-challenge.foris.ai/dumps/{dump_type}'
dumps_response = requests.get(dumps_url, headers=headers)

if dumps_response.status_code == 200:
    print(f"Contenido del volcado {dump_type}:")
    print(dumps_response.text)
else:
    print("La solicitud GET a /dumps/{dump_type} no fue exitosa. Código de estado:", dumps_response.status_code)

"""
========================================================================
"""

# # 2. Realizar solicitud POST a /validate
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