import openai
import os
from gtts import gTTS
import playsound
import speech_recognition as sr
import webbrowser
import win32api
import win32con
import time

def ini():
    ruta = r"C:\Users\KOBE\.vscode\Repositorio-Personal\Proyectos Python\AI Alpha\Alpha_v0.0.1.py"
    os.system(f'python "{ruta}"')  # Ejecutar el archivo RunA1.py

def limpiar_terminal():
    # Comando para limpiar la terminal en Windows
    os.system('cls' if os.name == 'nt' else 'clear')

def reproducir_texto(texto):
    output_path = r"C:\Users\KOBE\.vscode\Repositorio-Personal\Proyectos Python\AI Alpha"
    file_path = os.path.join(output_path, "output.mp3")

    tts = gTTS(texto, lang='es', tld='com')  # Crear objeto gTTS con el texto y el idioma
    tts.save(file_path)  # Guardar el archivo mp3 en la ruta especificada

    # Reproducir el archivo mp3 en segundo plano
    playsound.playsound(file_path, True)

    # Eliminar el archivo mp3
    os.remove(file_path)
    ini()

def buscar_en_internet(texto):
    # Abrir el navegador con la búsqueda en Google
    query = texto.replace("busca en internet", "").replace("busca en la web", "")
    query = query.strip()
    url = "https://www.google.com/search?q=" + query
    webbrowser.open(url)
    texto ="estos son los resultados de la búsqueda"
    reproducir_texto(texto)
    ini()

def reproducir_playlist():
    url = "https://www.youtube.com/watch?v=ugZ3DQYYaWQ&list=PLTyd066XHxi1u-rXz80hZqYfuWQurdDpT&pp=gAQBiAQB8AUB"
    webbrowser.open(url)
    texto ="con gusto"
    reproducir_texto(texto)
    ini()

def pausar_reproduccion_multimedia():
    win32api.keybd_event(win32con.VK_MEDIA_PLAY_PAUSE, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
    ini()

openai.api_key = "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"

contador = 0

# Configurar un temporizador de 11 segundos
start_time = time.time()
timeout = 3

while True:
    with sr.Microphone() as source:
        limpiar_terminal()
        print("Escuchando...")
        try:
            # Iniciar la grabación de audio
            audio = sr.Recognizer().listen(source, timeout=timeout)
            texto = sr.Recognizer().recognize_google(audio, language='es-ES')
            print("Texto reconocido:", texto)
        except sr.UnknownValueError:
            continue
        except sr.RequestError as e:
            print("Error al enviar la solicitud al servicio de reconocimiento de voz: {0}".format(e))
            continue  # Continuar con el siguiente ciclo

    prompt = texto

    if prompt == "exit" or prompt == "salir":
        limpiar_terminal()
        break

    elif "busca en internet" in prompt.lower() or "busca en la web" in prompt.lower() or "abre el navegador" in prompt.lower() or "escribe en el navegador" in prompt.lower():
        # Obtener el texto después de la palabra clave
        indice = max(prompt.lower().find("busca en internet"), prompt.lower().find("busca en la web"),
                     prompt.lower().find("abre el navegador"), prompt.lower().find("escribe en el navegador"))
        texto_busqueda = prompt[indice + len("busca en internet") + 1:]
        buscar_en_internet(texto_busqueda)

    elif "reproduce una playlist para un torneo" in prompt.lower() or "reproduce mi playlist" in prompt.lower():
        reproducir_playlist()

    elif "para la música" in prompt.lower() or "pausa" in prompt.lower() or "reanuda" in prompt.lower() or "pausa la música" in prompt.lower() or "play" in prompt.lower():
        pausar_reproduccion_multimedia()

    completion = openai.Completion.create(engine="text-davinci-003",
                                          prompt=prompt,
                                          max_tokens=2048)
    texto = completion.choices[0].text

    # tts
    language = 'es-es'
    print(texto)
    reproducir_texto(texto)
    ini()

exit

