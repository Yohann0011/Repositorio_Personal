<<<<<<< HEAD
import os
from pdf2image import convert_from_path
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def pdf_to_png(pdf_file):
    # Convierte el archivo PDF en una lista de imágenes PNG
    images = convert_from_path(pdf_file)

    # Obtiene el nombre del archivo sin la extensión
    filename = os.path.splitext(pdf_file)[0]

    # Guarda cada imagen PNG con el mismo nombre del archivo original
    for i, image in enumerate(images):
        image.save(f"{filename}_{i+1}.png", "PNG")

def main():
    # Abre el cuadro de diálogo para seleccionar los archivos PDF
    Tk().withdraw()
    files = askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])

    # Convierte cada archivo PDF seleccionado a PNG
    for file in files:
        pdf_to_png(file)

    print("Conversión completada.")

if __name__ == "__main__":
    main()
=======
import os
from pdf2image import convert_from_path
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

def pdf_to_png(pdf_file):
    # Convierte el archivo PDF en una lista de imágenes PNG
    images = convert_from_path(pdf_file)

    # Obtiene el nombre del archivo sin la extensión
    filename = os.path.splitext(pdf_file)[0]

    # Guarda cada imagen PNG con el mismo nombre del archivo original
    for i, image in enumerate(images):
        image.save(f"{filename}_{i+1}.png", "PNG")

def main():
    # Abre el cuadro de diálogo para seleccionar los archivos PDF
    Tk().withdraw()
    files = askopenfilenames(filetypes=[("Archivos PDF", "*.pdf")])

    # Convierte cada archivo PDF seleccionado a PNG
    for file in files:
        pdf_to_png(file)

    print("Conversión completada.")

if __name__ == "__main__":
    main()
>>>>>>> 8086880b55efd63f49e0728f2f4fa0b85da2c170
