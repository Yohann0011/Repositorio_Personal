<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from Capa2 import Capacidades, ciclos

#Dimensiones de la ventana
alto = 280
ancho = 520
# Restringir valores máximos
Npu_max = 182
It_max = 2000

vueltas = ciclos()

# Número de puestos en uso
Npu = 3
#Inventario Total
It = 600
#Cantidad de personas por puesto 
Mper = "Mixto"

# Funciones para obtener los valores seleccionados
def obtener_valores():
    from Capa2 import corto, medio, largo, Baja, Media, Alta
    if periodo_de_simulacion_var.get() == "Corto":
        cantdias = corto()
    elif periodo_de_simulacion_var.get() == "Mediano":
        cantdias = medio()
    else: 
        cantdias = largo()

    if tasa_de_ventas_var.get() == "Baja":
        tasa = Baja()
    elif tasa_de_ventas_var.get() == "Media":
        tasa = Media()
    else: 
        tasa = Alta()

    global periodo
    periodo = cantdias
    Tasa = tasa
    promediosCA = Capacidades(periodo, Tasa, Npu, It, Mper)
    
    promedio_QgT, promedio_RaT, promedio_QraT, promedio_CpT, promedio_PvT, promedio_MuaT, Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT = promediosCA
    
    resultado_label.config(text=f" Periodo de Simulación: \t\t{periodo} días\n\n Iteraciones de Simulación: \t\t{vueltas} ciclos\n\n Cantidad de residuos generados: \t{promedio_QgT} U.\n\n Cantidad de residuos aprovechados: \t{promedio_RaT} U.\n\n Porcentaje aprovechamiento: \t\t{promedio_QraT} %\n\n Costo del proceso por producto: \t{promedio_CpT} $\n\n Precio de venta promedio: \t\t{promedio_PvT} $\n\n Beneficio económico de ventas: \t{promedio_MuaT} %", justify="left")
    print(Npu)
    mostrar_graficas(Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT)

# Función para mostrar las gráficas
def mostrar_graficas(Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT):
    # Limpiar la figura anterior si existe
    plt.close()
    
    # Crear una figura de Matplotlib con una subtrama
    fig, axs = plt.subplots(3, 2, figsize=(13, 9))
    
    ciclos = [i + 1 for i in range(vueltas)] 

    # Crear gráficas para los valores de los arrays en cada subtrama
    axs[0, 0].plot(ciclos, Ca_valoresT, color="#0B5345" ,linestyle="-." ,label='Ca')
    axs[0, 0].set_title('Capacidad Ambiental')
    axs[0, 0].set_ylabel('Unidades')

    axs[0, 1].plot(ciclos, Qra_valoresT, color="#16A085" ,linestyle="--" ,label='Qra')
    axs[0, 1].set_title('Residuos aprovechados')
    axs[0, 1].set_ylabel('Porcentaje (%)')

    axs[1, 0].plot(ciclos, Co_valoresT,color="#154360",linestyle="-.", label='Co')
    axs[1, 0].set_title('Capacidad Organizativa')
    axs[1, 0].set_ylabel('%')

    axs[1, 1].plot(ciclos, Mua_valoresT, color="#2980B9" ,linestyle="--" , label='Mua')
    axs[1, 1].set_title('Beneficio')
    axs[1, 1].set_ylabel('Pesos')

    axs[2, 0].plot(ciclos, Cop_valoresT, color="#4A235A" ,linestyle="-." , label='Cop')
    axs[2, 0].set_title('Capaciadad Operativa')
    axs[2, 0].set_ylabel('Pesos')

    axs[2, 1].plot(ciclos, Sg_valoresT, color="#8E44AD" ,linestyle="--" , label='Sg')
    axs[2, 1].set_title('Costo Proceso')
    axs[2, 1].set_ylabel('Pesos')

    # Configurar etiquetas y leyendas
    for ax in axs.flat:
        ax.autoscale()
        ax.set_xlabel('Ciclos')
        ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)

    # Configurar la posición de la ventana de Matplotlib
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')  # Maximizar la ventana
    mng.window.wm_geometry("+0+0")  # Establecer la posición en la esquina superior izquierda

    # Ajustar el diseño de las subtramas
    plt.tight_layout()
    # Mostrar las gráficas
    plt.show()

# Función para redimensionar la ventana
def redimensionar_ventana():
    ventana_principal.geometry("520x630")
    ventana_principal.resizable(False, False)  # Hacer que la ventana sea de tamaño fijo
    obtener_valores()

def validar_entero_positivo(text):
    return text.isdigit() and int(text) >= 0


# Función para abrir la nueva ventana
def abrir_nueva_ventana():
    from Capa2 import Npu, It, Mper
    nueva_ventana = tk.Toplevel(ventana_principal)
    nueva_ventana.title("CONFIGURACIÓN")
    nueva_ventana.geometry("400x400")
    nueva_ventana.resizable(False, False)

    # Función para actualizar los valores en Capa2
    def actualizar_valores():
        try:
            # Obtener los valores ingresados
            nuevo_Npu = int(cuadro_puestos.get())
            nuevo_It = int(cuadro_inventario.get())
            nuevo_Mper = combo_max_personas_var.get()

            # Validar los valores ingresados
            if nuevo_Npu < 0:
                messagebox.showerror("Error", "El número de puestos en uso no puede ser un valor negativo.")
            elif nuevo_Npu > Npu_max:
                messagebox.showerror("Error", f"El número de puestos en uso no puede ser mayor que {Npu_max}.")
            elif nuevo_It < 0:
                messagebox.showerror("Error", "El inventario total no puede ser un valor negativo.")
            elif nuevo_It > It_max:
                messagebox.showerror("Error", f"El inventario total no puede ser mayor que {It_max}.")
            else:
                # Actualizar los valores en Capa2
                Npu = nuevo_Npu
                It = nuevo_It
                Mper = nuevo_Mper

                regresar_a_ventana_principal()
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos (números enteros) para Número de puestos en uso e Inventario total.")
    # Función para regresar a la ventana principal
    def regresar_a_ventana_principal():
        nueva_ventana.destroy()
        ventana_principal.deiconify()  # Mostrar la ventana principal cuando se cierra la ventana secundaria
    
    # Estilo de texto
    estilo_texto = ('Arial', 18)

     # Cuadro de texto editable para puestos en uso
    cuadro_puestos = tk.Entry(nueva_ventana, font=estilo_texto, validate="key")
    cuadro_puestos.insert(0, str(Npu))
    cuadro_puestos.place(relx=0.1, rely=0.2)
    cuadro_puestos['validatecommand'] = (cuadro_puestos.register(validar_entero_positivo), '%P')

    # Cuadro de texto editable para inventario total
    cuadro_inventario = tk.Entry(nueva_ventana, font=estilo_texto, validate="key")
    cuadro_inventario.insert(0, str(It))
    cuadro_inventario.place(relx=0.1, rely=0.4)
    cuadro_inventario['validatecommand'] = (cuadro_inventario.register(validar_entero_positivo), '%P')

    # Label para "Número de puestos en uso"
    label_puestos = tk.Label(nueva_ventana, text="Número de puestos en uso", font=estilo_texto)
    label_puestos.place(relx=0.1, rely=0.1)

    # Cuadro de texto editable para puestos en uso
    cuadro_puestos = tk.Entry(nueva_ventana, font=estilo_texto)
    cuadro_puestos.insert(0, str(Npu))
    cuadro_puestos.place(relx=0.1, rely=0.2)

    # Label para "Inventario total"
    label_inventario = tk.Label(nueva_ventana, text="Inventario total", font=estilo_texto)
    label_inventario.place(relx=0.1, rely=0.3)

    # Cuadro de texto editable para inventario total
    cuadro_inventario = tk.Entry(nueva_ventana, font=estilo_texto)
    cuadro_inventario.insert(0, str(It))
    cuadro_inventario.place(relx=0.1, rely=0.4)

    # Label para "Máximo de personas"
    label_max_personas = tk.Label(nueva_ventana, text="Máximo de personas", font=estilo_texto)
    label_max_personas.place(relx=0.1, rely=0.5)

    # Combobox con las opciones "Mixto", "Pocas", "Muchas"
    opcPerson = ["Mixto", "Pocas", "Muchas"]
    combo_max_personas_var = tk.StringVar(value=opcPerson[0])
    combo_max_personas = ttk.Combobox(nueva_ventana, values=opcPerson, textvariable=combo_max_personas_var, font=estilo_texto)
    combo_max_personas.configure(state="readonly")
    combo_max_personas.place(relx=0.1, rely=0.6)

    # Botón para actualizar
    boton_actualizar = tk.Button(nueva_ventana, text="Actualizar", font=estilo_texto, command=actualizar_valores)
    boton_actualizar.place(relx=0.3, rely=0.75)

    ventana_principal.withdraw()  # Ocultar la ventana principal
    nueva_ventana.mainloop()

# Función para centrar una ventana en la mitad de la pantalla
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() - ancho_ventana) // 2
    y = (ventana.winfo_screenheight() - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("SICAPLAM")
ventana_principal.geometry("400x250")
ventana_principal.resizable(False, False) 

# Opciones por defecto para Tasa de Ventas y Periodo de Simulación
tasa_de_ventas_opciones = ["Baja", "Media", "Alta"]
periodo_de_simulacion_opciones = ["Corto", "Mediano", "Largo"]

tasa_de_ventas_label = tk.Label(ventana_principal, text="Tasa de Ventas")
tasa_de_ventas_label.pack(pady=10)  # Agregar margen superior
tasa_de_ventas_label.configure(font=("Arial", 20))  # Modificar el tamaño de la fuente
tasa_de_ventas_var = tk.StringVar(value=tasa_de_ventas_opciones[0])  # Establecer la opción por defecto
tasa_de_ventas_selector = ttk.Combobox(ventana_principal, textvariable=tasa_de_ventas_var, values=tasa_de_ventas_opciones)
tasa_de_ventas_selector.configure(font=("Arial", 15), width=(15))
tasa_de_ventas_selector.configure(state="readonly")  # Combobox como solo lectura (deshabilitar la opción de escribir)

tasa_de_ventas_selector.pack()
tasa_de_ventas_selector.set(tasa_de_ventas_opciones[0])  # Establecer la opción por defecto

# Etiqueta y caja de selección para las opciones de Periodo de Simulación
periodo_de_simulacion_label = tk.Label(ventana_principal, text="Periodo de Simulación")
periodo_de_simulacion_label.configure(font=("Arial", 20))
periodo_de_simulacion_label.pack(pady=10)  # Agregar margen superior
periodo_de_simulacion_var = tk.StringVar(value=periodo_de_simulacion_opciones[0])  # Establecer la opción por defecto
periodo_de_simulacion_selector = ttk.Combobox(ventana_principal, textvariable=periodo_de_simulacion_var,
                                                values=periodo_de_simulacion_opciones)
periodo_de_simulacion_selector.configure(font=("Arial", 15), width=(15))
periodo_de_simulacion_selector.configure(state="readonly")
periodo_de_simulacion_selector.pack()
periodo_de_simulacion_selector.set(periodo_de_simulacion_opciones[0])  # Establecer la opción por defecto

# Botón para obtener los valores seleccionados
obtener_valores_button = tk.Button(ventana_principal, text="Ejecutar Simulación", command=redimensionar_ventana)
obtener_valores_button.pack(pady=15)  # Agregar margen superior

# Etiqueta para mostrar el resultado con margen horizontal
resultado_label = tk.Label(ventana_principal, text="", wraplength=540, padx=8, font=("Arial", 16))
resultado_label.pack()

# Botón con un icono de engranaje para abrir la nueva ventana
boton_abrir_nueva_ventana = tk.Button(ventana_principal, text="⚙️", command=abrir_nueva_ventana)
boton_abrir_nueva_ventana.place(relx=0.9, rely=0.05)

# Centrar la ventana principal en la mitad de la pantalla
centrar_ventana(ventana_principal)

=======
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from Capa2 import Capacidades, ciclos

#Dimensiones de la ventana
alto = 280
ancho = 520
# Restringir valores máximos
Npu_max = 182
It_max = 2000

vueltas = ciclos()

# Número de puestos en uso
Npu = 3
#Inventario Total
It = 600
#Cantidad de personas por puesto 
Mper = "Mixto"

# Funciones para obtener los valores seleccionados
def obtener_valores():
    from Capa2 import corto, medio, largo, Baja, Media, Alta
    if periodo_de_simulacion_var.get() == "Corto":
        cantdias = corto()
    elif periodo_de_simulacion_var.get() == "Mediano":
        cantdias = medio()
    else: 
        cantdias = largo()

    if tasa_de_ventas_var.get() == "Baja":
        tasa = Baja()
    elif tasa_de_ventas_var.get() == "Media":
        tasa = Media()
    else: 
        tasa = Alta()

    global periodo
    periodo = cantdias
    Tasa = tasa
    promediosCA = Capacidades(periodo, Tasa, Npu, It, Mper)
    
    promedio_QgT, promedio_RaT, promedio_QraT, promedio_CpT, promedio_PvT, promedio_MuaT, Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT = promediosCA
    
    resultado_label.config(text=f" Periodo de Simulación: \t\t{periodo} días\n\n Iteraciones de Simulación: \t\t{vueltas} ciclos\n\n Cantidad de residuos generados: \t{promedio_QgT} U.\n\n Cantidad de residuos aprovechados: \t{promedio_RaT} U.\n\n Porcentaje aprovechamiento: \t\t{promedio_QraT} %\n\n Costo del proceso por producto: \t{promedio_CpT} $\n\n Precio de venta promedio: \t\t{promedio_PvT} $\n\n Beneficio económico de ventas: \t{promedio_MuaT} %", justify="left")
    print(Npu)
    mostrar_graficas(Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT)

# Función para mostrar las gráficas
def mostrar_graficas(Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT):
    # Limpiar la figura anterior si existe
    plt.close()
    
    # Crear una figura de Matplotlib con una subtrama
    fig, axs = plt.subplots(3, 2, figsize=(13, 9))
    
    ciclos = [i + 1 for i in range(vueltas)] 

    # Crear gráficas para los valores de los arrays en cada subtrama
    axs[0, 0].plot(ciclos, Ca_valoresT, color="#0B5345" ,linestyle="-." ,label='Ca')
    axs[0, 0].set_title('Capacidad Ambiental')
    axs[0, 0].set_ylabel('Unidades')

    axs[0, 1].plot(ciclos, Qra_valoresT, color="#16A085" ,linestyle="--" ,label='Qra')
    axs[0, 1].set_title('Residuos aprovechados')
    axs[0, 1].set_ylabel('Porcentaje (%)')

    axs[1, 0].plot(ciclos, Co_valoresT,color="#154360",linestyle="-.", label='Co')
    axs[1, 0].set_title('Capacidad Organizativa')
    axs[1, 0].set_ylabel('%')

    axs[1, 1].plot(ciclos, Mua_valoresT, color="#2980B9" ,linestyle="--" , label='Mua')
    axs[1, 1].set_title('Beneficio')
    axs[1, 1].set_ylabel('Pesos')

    axs[2, 0].plot(ciclos, Cop_valoresT, color="#4A235A" ,linestyle="-." , label='Cop')
    axs[2, 0].set_title('Capaciadad Operativa')
    axs[2, 0].set_ylabel('Pesos')

    axs[2, 1].plot(ciclos, Sg_valoresT, color="#8E44AD" ,linestyle="--" , label='Sg')
    axs[2, 1].set_title('Costo Proceso')
    axs[2, 1].set_ylabel('Pesos')

    # Configurar etiquetas y leyendas
    for ax in axs.flat:
        ax.autoscale()
        ax.set_xlabel('Ciclos')
        ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)

    # Configurar la posición de la ventana de Matplotlib
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')  # Maximizar la ventana
    mng.window.wm_geometry("+0+0")  # Establecer la posición en la esquina superior izquierda

    # Ajustar el diseño de las subtramas
    plt.tight_layout()
    # Mostrar las gráficas
    plt.show()

# Función para redimensionar la ventana
def redimensionar_ventana():
    ventana_principal.geometry("520x630")
    ventana_principal.resizable(False, False)  # Hacer que la ventana sea de tamaño fijo
    obtener_valores()

def validar_entero_positivo(text):
    return text.isdigit() and int(text) >= 0


# Función para abrir la nueva ventana
def abrir_nueva_ventana():
    from Capa2 import Npu, It, Mper
    nueva_ventana = tk.Toplevel(ventana_principal)
    nueva_ventana.title("CONFIGURACIÓN")
    nueva_ventana.geometry("400x400")
    nueva_ventana.resizable(False, False)

    # Función para actualizar los valores en Capa2
    def actualizar_valores():
        try:
            # Obtener los valores ingresados
            nuevo_Npu = int(cuadro_puestos.get())
            nuevo_It = int(cuadro_inventario.get())
            nuevo_Mper = combo_max_personas_var.get()

            # Validar los valores ingresados
            if nuevo_Npu < 0:
                messagebox.showerror("Error", "El número de puestos en uso no puede ser un valor negativo.")
            elif nuevo_Npu > Npu_max:
                messagebox.showerror("Error", f"El número de puestos en uso no puede ser mayor que {Npu_max}.")
            elif nuevo_It < 0:
                messagebox.showerror("Error", "El inventario total no puede ser un valor negativo.")
            elif nuevo_It > It_max:
                messagebox.showerror("Error", f"El inventario total no puede ser mayor que {It_max}.")
            else:
                # Actualizar los valores en Capa2
                Npu = nuevo_Npu
                It = nuevo_It
                Mper = nuevo_Mper

                regresar_a_ventana_principal()
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores válidos (números enteros) para Número de puestos en uso e Inventario total.")
    # Función para regresar a la ventana principal
    def regresar_a_ventana_principal():
        nueva_ventana.destroy()
        ventana_principal.deiconify()  # Mostrar la ventana principal cuando se cierra la ventana secundaria
    
    # Estilo de texto
    estilo_texto = ('Arial', 18)

     # Cuadro de texto editable para puestos en uso
    cuadro_puestos = tk.Entry(nueva_ventana, font=estilo_texto, validate="key")
    cuadro_puestos.insert(0, str(Npu))
    cuadro_puestos.place(relx=0.1, rely=0.2)
    cuadro_puestos['validatecommand'] = (cuadro_puestos.register(validar_entero_positivo), '%P')

    # Cuadro de texto editable para inventario total
    cuadro_inventario = tk.Entry(nueva_ventana, font=estilo_texto, validate="key")
    cuadro_inventario.insert(0, str(It))
    cuadro_inventario.place(relx=0.1, rely=0.4)
    cuadro_inventario['validatecommand'] = (cuadro_inventario.register(validar_entero_positivo), '%P')

    # Label para "Número de puestos en uso"
    label_puestos = tk.Label(nueva_ventana, text="Número de puestos en uso", font=estilo_texto)
    label_puestos.place(relx=0.1, rely=0.1)

    # Cuadro de texto editable para puestos en uso
    cuadro_puestos = tk.Entry(nueva_ventana, font=estilo_texto)
    cuadro_puestos.insert(0, str(Npu))
    cuadro_puestos.place(relx=0.1, rely=0.2)

    # Label para "Inventario total"
    label_inventario = tk.Label(nueva_ventana, text="Inventario total", font=estilo_texto)
    label_inventario.place(relx=0.1, rely=0.3)

    # Cuadro de texto editable para inventario total
    cuadro_inventario = tk.Entry(nueva_ventana, font=estilo_texto)
    cuadro_inventario.insert(0, str(It))
    cuadro_inventario.place(relx=0.1, rely=0.4)

    # Label para "Máximo de personas"
    label_max_personas = tk.Label(nueva_ventana, text="Máximo de personas", font=estilo_texto)
    label_max_personas.place(relx=0.1, rely=0.5)

    # Combobox con las opciones "Mixto", "Pocas", "Muchas"
    opcPerson = ["Mixto", "Pocas", "Muchas"]
    combo_max_personas_var = tk.StringVar(value=opcPerson[0])
    combo_max_personas = ttk.Combobox(nueva_ventana, values=opcPerson, textvariable=combo_max_personas_var, font=estilo_texto)
    combo_max_personas.configure(state="readonly")
    combo_max_personas.place(relx=0.1, rely=0.6)

    # Botón para actualizar
    boton_actualizar = tk.Button(nueva_ventana, text="Actualizar", font=estilo_texto, command=actualizar_valores)
    boton_actualizar.place(relx=0.3, rely=0.75)

    ventana_principal.withdraw()  # Ocultar la ventana principal
    nueva_ventana.mainloop()

# Función para centrar una ventana en la mitad de la pantalla
def centrar_ventana(ventana):
    ventana.update_idletasks()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()
    x = (ventana.winfo_screenwidth() - ancho_ventana) // 2
    y = (ventana.winfo_screenheight() - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("SICAPLAM")
ventana_principal.geometry("400x250")
ventana_principal.resizable(False, False) 

# Opciones por defecto para Tasa de Ventas y Periodo de Simulación
tasa_de_ventas_opciones = ["Baja", "Media", "Alta"]
periodo_de_simulacion_opciones = ["Corto", "Mediano", "Largo"]

tasa_de_ventas_label = tk.Label(ventana_principal, text="Tasa de Ventas")
tasa_de_ventas_label.pack(pady=10)  # Agregar margen superior
tasa_de_ventas_label.configure(font=("Arial", 20))  # Modificar el tamaño de la fuente
tasa_de_ventas_var = tk.StringVar(value=tasa_de_ventas_opciones[0])  # Establecer la opción por defecto
tasa_de_ventas_selector = ttk.Combobox(ventana_principal, textvariable=tasa_de_ventas_var, values=tasa_de_ventas_opciones)
tasa_de_ventas_selector.configure(font=("Arial", 15), width=(15))
tasa_de_ventas_selector.configure(state="readonly")  # Combobox como solo lectura (deshabilitar la opción de escribir)

tasa_de_ventas_selector.pack()
tasa_de_ventas_selector.set(tasa_de_ventas_opciones[0])  # Establecer la opción por defecto

# Etiqueta y caja de selección para las opciones de Periodo de Simulación
periodo_de_simulacion_label = tk.Label(ventana_principal, text="Periodo de Simulación")
periodo_de_simulacion_label.configure(font=("Arial", 20))
periodo_de_simulacion_label.pack(pady=10)  # Agregar margen superior
periodo_de_simulacion_var = tk.StringVar(value=periodo_de_simulacion_opciones[0])  # Establecer la opción por defecto
periodo_de_simulacion_selector = ttk.Combobox(ventana_principal, textvariable=periodo_de_simulacion_var,
                                                values=periodo_de_simulacion_opciones)
periodo_de_simulacion_selector.configure(font=("Arial", 15), width=(15))
periodo_de_simulacion_selector.configure(state="readonly")
periodo_de_simulacion_selector.pack()
periodo_de_simulacion_selector.set(periodo_de_simulacion_opciones[0])  # Establecer la opción por defecto

# Botón para obtener los valores seleccionados
obtener_valores_button = tk.Button(ventana_principal, text="Ejecutar Simulación", command=redimensionar_ventana)
obtener_valores_button.pack(pady=15)  # Agregar margen superior

# Etiqueta para mostrar el resultado con margen horizontal
resultado_label = tk.Label(ventana_principal, text="", wraplength=540, padx=8, font=("Arial", 16))
resultado_label.pack()

# Botón con un icono de engranaje para abrir la nueva ventana
boton_abrir_nueva_ventana = tk.Button(ventana_principal, text="⚙️", command=abrir_nueva_ventana)
boton_abrir_nueva_ventana.place(relx=0.9, rely=0.05)

# Centrar la ventana principal en la mitad de la pantalla
centrar_ventana(ventana_principal)

>>>>>>> 8086880b55efd63f49e0728f2f4fa0b85da2c170
ventana_principal.mainloop()