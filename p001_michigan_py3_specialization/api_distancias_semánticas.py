# 1. Entorno
## 1.1. Cargar libreiras
# import requests
import json
from openai import OpenAI

## 1.2. Llaves
with open("../../00. Recursos/keys/k01_general_pupuse.txt", "r") as file:
    openai_key = file.read()


# 2. Prueba de conexión
client = OpenAI(api_key=openai_key)

pregunta = "¿Para que sirven las tuplas en py?"

respuesta = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "developer",
            "content": "Eres jugalar medieval que habla rimando y siempre con chistes",
        },
        {"role": "user", "content": pregunta},
    ],
)


respuesta_txt = respuesta.choices[0].message
type(respuesta_txt)

str(respuesta_txt).split("\\n")[0]


# response = client.embeddings.create(input=[], model="text-embedding-3-small")
