""" pip install necesarios """
# pip install watchdog
# pip install keyboard
# pip install pandas
# pip install numpy
# pip install reportlab
# pip install sqlalchemy


"""
========================================================================
-------------------------| IMPORTACIONES |------------------------------
========================================================================
"""
#DOCUMENTO

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import keyboard
import os
import shutil
from datetime import datetime
import pandas as pd
import numpy as np
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph

#BASE DE DATOS
from sqlalchemy import create_engine

#EMAIL
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
"""
========================================================================
-----------------------| VARIABLES GLOBALES |---------------------------
========================================================================
"""

# Ruta de la carpeta compartida
rutaC = r"C:\Temp\Datos"
aPlan = rutaC+r"\Archivos_Planos"
infor = rutaC+r"\Informes"
otros = rutaC+r"\otros"

obs = Observer()
evento = FileSystemEventHandler()
fecha_actual = datetime.now().strftime("%Y%m%d")

"""
========================================================================
---------------------------| FUNCIONES |--------------------------------
========================================================================
"""

# --- Función moni 'Monitorear' ---
# Dentro de esta función se implementa un observador de de eventos 'obs'
# también se implementa el uso de un atajo para detener el observador 
# la combinación de teclas es: 'Ctrl + Alt + S'

def moni():
    folder()

    evento.on_created = e_Crear
    evento.on_deleted = e_Eliminar
    evento.on_modified = e_Modificar

    obs.schedule(evento, rutaC, recursive=True)
    obs.start()
    print (f"Inicio del monitoreo de la carpeta compartida")
    try:
        while True:
            if keyboard.is_pressed('ctrl+alt+s'):
                print('Fin el monitoreo de la carpeta compartida')
                break

    except KeyboardInterrupt:
        pass

    finally:
        obs.stop()
        obs.join()

# --- Función folder 'carpeta' ---
# Esta funcion crear los directorios dentro de la ruta principal
# para dar una organización a los archivos ingresados

def folder():
    for carpeta in [infor, aPlan, otros]:
        if not os.path.exists(carpeta):
            os.makedirs(carpeta)

# --- Funciones de evento 'e' ---
# En este apartado se llaman las acciones a realizar cuando hay una
# + creacion
# + mofidicacion
# + eliminacion 
# de algún elemento dentro de la ruta general y así mismo de los sub elemetos
# el evento es traido de la funcion moni

def e_Eliminar(evento):
    print(f"Archivo eliminado: {evento.src_path}")

def e_Modificar(evento):
    print(f"Archivo modificado: {evento.src_path}")
    #verificar(os.path.basename(evento.src_path))

def e_Crear(evento):
    print(f"Archivo creado: {evento.src_path}")
    verificar(evento.src_path)
    #print(os.path.basename(evento.src_path))

# --- Función verificar 'Discriminación' ---
# Esta función verifica el nombre de archivo y su extensión
# para así mover o no el archivo ingresado, permitiendo clasificar
# los archivos al momento de ser creados o modificados

def verificar(archivo):
    if (os.path.basename(archivo).startswith("Información")
        and os.path.basename(archivo)[11:19].isdigit()):
        if(os.path.basename(archivo).endswith(".pdf")):
            try:
                shutil.move(archivo, infor)
                print("archivo movido")
            except shutil.Error as e:
                print(f"...")

        elif (os.path.basename(archivo).endswith(".txt")):
            try:
                shutil.move(archivo, aPlan)
                print("archivo movido")
            except shutil.Error as e:
                print(f"...")

        elif (os.path.basename(archivo).endswith(".xlsx")):
               arch_P(archivo) 
    else:
        try:
            shutil.move(archivo, otros)
        except shutil.Error as e:
            print(f"Documento de excel añadido {archivo}")

# --- Función arch_P 'Archivo Plano' ---
# Esta funcion trae el documento de excel filtrado anteriormente
# y genera un nuevo archivo plano separado por tabulaciones en caso
# de querer separarlo por comas es cambiar el sep='\t' por sep=','

def arch_P(archivo):
    print(f'Iniciando la conversión a texto plano')
    #print(os.path.exists(archivo))
    try:
        excel = pd.read_excel(archivo, engine='openpyxl')
        
        col_R = ['Identificación', 'Nombre', 'Cantidad']
        datos = excel[col_R]
        
        a = os.path.basename(archivo).replace('.xlsx', '.txt')
        txt = os.path.join(aPlan,a)

        datos.to_csv(txt, index=False, sep='\t')
        
        print(f'Se ha curado el archivo {archivo}. Se ha creado el archivo plano {txt} con los datos curados.')
        
        anDa(txt)

    except Exception as e:
        print(f'Error al leer el archivo {archivo}: {e}')

# --- Función anDa 'Analisis de Datos' ---
# En este apartado se genera la función de analisis de los datos,
# tambien se genera un documento pdf con una tabla del analisis realizado

def anDa(archivo):
    print(f'Iniciando la creacioón del informe')

    excel = pd.read_csv(archivo, sep='\t')

    tRegis = len(excel)

    cant_N = excel['Nombre'].nunique()

    cant_T = excel['Cantidad'].sum()
    cant_M = excel['Cantidad'].mean()
    cant_Medi = excel['Cantidad'].median()
    cant_Mo = excel['Cantidad'].mode()[0]

    rango = np.ptp(excel['Cantidad'])
    vari = np.var(excel['Cantidad'])
    desvi = np.std(excel['Cantidad'])
    coe = (desvi / cant_Medi) * 100


    a = archivo.replace('.txt', '_informe.pdf')
    pdf = os.path.join(infor,a)

    doc = SimpleDocTemplate(pdf, pagesize=letter)

    texto = (f"<center><b>Informe de estadísticas del archivo {os.path.basename(archivo)}</b></center><br/><br/>"
    """ Teniendo en cuanta los datos contenidos dentro del archivo se realiza un análisis estadístico básico general 
    de la información contenida dentro del archivo, se tiene en cuenta la totalidad de los datos teniendo en cuenta 
    las tres columnas requeridas para el ejercicio, sin más preambulo se presenta la siguiente tabla:<br/><br/>"""
    )
    estilo = ParagraphStyle(name="Estilo")
    parrafo = Paragraph(texto, estilo)

    datos = [
        ['Registros Totales', tRegis],
        ['Cantidad de Nombres', cant_N],
        ['Analisis de Cantidad', ''],
        ['Sumatoria total: ', cant_T],
        ['Media: ', cant_M],
        ['Mediana: ', cant_Medi],
        ['Moda: ', cant_Mo],
        ['Rango: ', rango],
        ['Varianza: ', vari],
        ['Desviación Estándar: ', desvi],
        ['Coeficiente de Variación (%)', coe]
    ]
    tabla = Table(datos)
    tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))


    elementos = [parrafo,tabla]
    doc.build(elementos)
    print(f'proceso completado, se inicia el envio del informe estadístico')
    enviarCorreo('yohann0010@gmail.com', f"envio de informe sobre {os.path.basename(archivo)}",pdf)
    #enviarCorreo(destinatario, asunto, mensaje)

    print("Conectando a la base de datos")
    url = 'mysql://root@localhost:8081/sgi_test'
    try:
        engine = create_engine(url)

        with engine.connect() as con:
            # Insertar los datos en la base de datos
            for index, row in excel.iterrows():
                fila = {'Identificación': row['Id'], 'Nombre': row['Nombre'], 'Cantidad': row['Cantidad']}
                try:
                    con.execute("INSERT INTO datos (Id, Name, Quantity) VALUES (:Identificación, :Nombre, :Cantidad)", fila)
                    print("datos subidos satisfactoriamente")
                except Exception as e:
                    print(f'Error al insertar fila {fila}: {e}')

        print(f'Se han agregado los datos a la base de datos.')

    except Exception as e:
        print(f'Error al conectar a la base de datos: {str(e)}')

# --- Función enviarcorreo 'Envia el Correo'
# Se requiere de tres parametros, sin embargo los tres parametros son 
# modificables desde el final de la función anDA, el valor del correo
# del remitente si se encuentra en esta función 

def enviarCorreo(destinatario, asunto, mensaje):
    print(os.path.basename(mensaje))
     # Configuración del servidor SMTP de Gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587  # Puerto de conexión TLS

    # Tu dirección de correo electrónico de Gmail y contraseña
    remitente = 'yohann0011@gmail.com'
    contraseña = 'atqn hfex kncf icgc'

    msg = MIMEMultipart()
    msg['From'] = remitente
    msg['To'] = destinatario
    msg['Subject'] = asunto

    try:
        with open(mensaje, 'rb') as f:
            adjunto = MIMEBase('application', 'octet-stream')
            adjunto.set_payload(f.read())
            encoders.encode_base64(adjunto)
            adjunto.add_header('Content-Disposition', 'attachment', filename=f"{os.path.basename(mensaje)}")
            msg.attach(adjunto)
    except Exception as e:
        print(f'Error al adjuntar el archivo PDF al correo electrónico: {e}')

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(remitente, contraseña)
        server.sendmail(remitente, destinatario, msg.as_string())
        print('Correo electrónico enviado con éxito')
    except Exception as e:
        print(f'Error al enviar el correo electrónico: {e}')
    finally:
        server.quit()


"""
========================================================================
----------------------------| ARRANQUE |--------------------------------
========================================================================
"""
moni()
