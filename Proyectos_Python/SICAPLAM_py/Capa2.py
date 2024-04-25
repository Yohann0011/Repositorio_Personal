<<<<<<< HEAD
import random
import numpy as np

#Declarar Variables
Ca = 0
Co = 0
Cop = 0
promedio_Ca = 0
promedio_Co = 0
promedio_Cop = 0
promedio_Qg = 0
promedio_Ra = 0
promedio_Qra = 0
promedio_Cp = 0
promedio_Pv = 0
promedio_Mua = 0
promedio_Sg = 0
# Crear listas para almacenar los valores
# por dias
Ca_valores = []
Co_valores = []
Cop_valores = []
Qg_valores = []
Ra_valores = []
Qra_valores = []
Cp_valores = []
Pv_valores = []
Mua_valores = []
Sg_valores = []

Ven_Valores = []
Sven_Valores = []
Inv_Valores = []

#por ciclo
Ca_valoresT = []
Co_valoresT = []
Cop_valoresT = []
Qg_valoresT = []
Ra_valoresT = []
Qra_valoresT = []
Cp_valoresT = []
Pv_valoresT = []
Mua_valoresT = []
Sg_valoresT = []

Ven_ValoresT = []
Sven_ValoresT = []
Inv_ValoresT = []

#ejecutar los ciclos de 30 a 60
vueltas = random.randint(30,60)
#Canidad de Días
num_dias = 0
# Número de puestos en uso
Npu = 3
#Inventario Total
It = 600
#Cantidad de personas por puesto 
Mper = "Mixto"

def limpiar_valores():
    # Eliminar los datos de las listas
    Ca_valores.clear()
    Co_valores.clear()
    Cop_valores.clear()

    Qg_valores.clear()
    Ra_valores.clear()
    Cp_valores.clear()
    Pv_valores.clear()
    Mua_valores.clear()
    Sg_valores.clear()
    Ven_Valores.clear()
    Sven_Valores.clear()
    Inv_Valores.clear()

    Ca_valoresT.clear()
    Co_valoresT.clear()
    Cop_valoresT.clear()
    Qg_valoresT.clear()
    Ra_valoresT.clear()
    Qra_valoresT.clear()
    Cp_valoresT.clear()
    Pv_valoresT.clear()
    Mua_valoresT.clear()
    Sg_valoresT.clear()
    Ven_ValoresT.clear()
    Inv_ValoresT.clear()

#Número de días a simular
def corto():
    num_dias = random.randint(90,179)
    return num_dias
def medio():
    num_dias = random.randint(180,269)
    return num_dias
def largo():
    num_dias = random.randint(270,365)
    return num_dias
#Número de ciclos a simular
def ciclos():
    return vueltas
#Tasa Comprometida
def Baja():
    Tasa = 1
    return Tasa
def Media():
    Tasa = 2
    return Tasa
def Alta():
    Tasa = 3
    return Tasa

def Capacidades(num_dias,Tasa,Npu,It,Mper):
    limpiar_valores()

    #---------------------------------- CAPACIDADES AMBIENTALES ----------------------------------#
    Io = 0 # Inventario Inicial
    If = 0 #Inventario Final
    Ncom = 0 # Número de compras
    vueltas = ciclos()
    contVuel = 0

    if Mper == "Mixto":
        Nmper = random.randint(25,70)
    elif Mper == "Pocas":
        Nmper = random.randint(0,25)
    else:    
        Nmper = random.randint(50,100)
    for _ in range(vueltas):
        contD = 0
        contVuel =+ 1

        Sumvp = [] # Suma Ventas Día

        for _ in range(num_dias):
            contD += 1 # Contador de Días
            Fa = random.randint(0,100) / 100 #Factor de Abastecimiento = Aleatorio despues del dia 1 
            
            #******************************************************************************************
            #****************************** PROCESO DE ABASTECIMIENTO *********************************
            #******************************************************************************************

            if contD == 1: #Abastecimiento Total
                Io = It 
            else:
                Io = If

            #******************************************************************************************
            #****************************** PROCESO DE COMPRA Y VENTA *********************************
            #******************************************************************************************
            if Tasa == 1:
                Pi = random.randint(0, Nmper) # Número de personas que ingresan a la plaza
            elif Tasa == 2:
                Pi = random.randint(Nmper,Nmper*3)
            else:
                Pi = random.randint(Nmper*2, Nmper*4)

            if Pi == 0:
                Nc = 0
                Pnc = 0 
            else: # Número de personas que no compran
                if Tasa == 1: 
                    Pnc = random.triangular(0,Pi,(Pi*0.9))
                elif Tasa == 2:
                    Pnc = random.triangular(0,Pi,(Pi*0.5))
                else:
                    Pnc = random.triangular(0,Pi,(Pi*0.1))
            
            Nc = int(Pi - Pnc) # Número de compradores

            if Nc == 0:
                Ncom = 0
            else:
                for _ in range(Nc): #Por si un cliente compra más de un producto
                    # Aplicación de Distribución normal
                    if Tasa == 1:
                        mu = (Nc + 2)  # Valor medio
                        sigma = 6  # Desviación estándar
                    elif Tasa == 2:
                        mu = (Nc + 7) 
                        sigma = 17 
                    else:
                        mu = (Nc + 12) 
                        sigma = 6                     

                    # Generar un valor aleatorio con distribución normal
                    while True:
                        Ncom = int(random.normalvariate(mu, sigma))
                        if Ncom >= Nc: # Verificar que el numero de compras sea >= a los compradores
                            break 
        
            Vd = Ncom # Ventas Día = Número de compras

            If = Io - Vd # Inventario Final = Inventario Inicial - Ventas Día
            
            if If <= 0:
                If = 0
                Io = 0
                Nc = 0
            
            Sumvp.append(Vd)
            Svp = sum(Sumvp) # Sumatoria Ventas

            Lvp = [] # Lista para almacenar las ventas de productos

            for _ in range(Vd):
                Pp = random.randint(500, 2000) #Precio Productos valor minimo y maximo
                Lvp.append(Pp)# Costos Ganancia
            
            if Vd == 0:
                Pvd = 0
            else:
                Pvd = sum(Lvp) / Vd #Promedio de venta diaria = sumatoria de la venta de los productos / numero de ventas en el día

            #******************************************************************************************
            #****************************** PROCESO DE ABASTECIMIENTO *********************************
            #******************************************************************************************
            
            if If == 0 and Vd == 0:
                 Fa = 0
            if If < It and Io < (It*0.7) and Fa >= 0.7:
                if Tasa == 2:
                    Io += random.randint(0, It*0.15)
                elif Tasa == 3:
                    Io += random.randint(0, It*0.25)
            if If < It and Io < (It*0.5) and Fa >= 0.5:
                if Tasa == 1:
                    Io += random.randint(0, It*0.2)
                elif Tasa == 2:
                    Io += random.randint(0, It*0.3)
                else:
                    Io += random.randint(0, It*0.5)
     

            if Fa == 0:
                Dd = 0
            else:
                Dd = Pvd / Fa #Demanda Diaria = (Promedio Ventas Diarias) / (Frecuencia de Abastecimiento)

            Cll = (Dd + Io) - If # Cantidad de producto que llega = (Demanda Diaria + Inventario Inicial) - Inventario Final

            if Io == 0:
                Pm = 0
            else:
                Pm = ((Io - If) /Io) * 100 # Porcentaje de Merma = ((Inventario Inicial - Inventario Final) / Inventario Inicial) x 100

            Ma = (Cll * Pm) / 100 # Porcentaje de merma de alistamiento  

            Pns = (Io - Vd)/100 #porcentaje de productos que no se vendieron

            Pr = Vd * (random.normalvariate(0.3, 0.25) + random.normalvariate(0.2, 0.2)) / 100 # Porcentaje de residuos  = Ventas * (Pérdida de Producto + Parte no comestible al vender)

            Qg = int((Npu * Vd) * (Ma + Pns + Pr)) # Cantidad de los residuos generados
            
            if Qg <= 0:
                Qg = 0
                Qra = 0
                Ra = 0
            else:
                Ra = int(Qg * random.randint(0,60))/100 # Cantidad de residuos aprovechados
                if Ra < 0:
                    Ra = (Ra *-1)
                else:
                    Ra = int(Qg * random.randint(0,70))/100

                Qra = int((Ra * 100) / Qg) # Porcentaje de residuos aprovechados Día
            
            if Tasa == 1:
                Cp = Qra * random.randint(1100, 1300) # Costo del proceso
            elif Tasa == 2:
                Cp = Qra * random.randint(1000, 1200) # Costo del proceso
            else:
                Cp = Qra * random.randint(900, 1100) # Costo del proceso

            Pv = Qra * Pvd # Precio de venta

            Mua = (Pv - Cp) / 100 # Margen de utilidad ambiental Día

            Ca = ((Qra*0.4)+(Mua*0.3))

            # Agregar los valores a las listas y promediarlos
            Ca_valores.append(Ca)
            Qg_valores.append(Qg)
            Ra_valores.append(Ra)
            Cp_valores.append(Cp)
            Pv_valores.append(Pv)
            Mua_valores.append(Mua)
        
            Ven_Valores.append(Vd)
            Sven_Valores.append(Svp)
            Inv_Valores.append(If)

            #--------------------------------- CAPACIDADES ORGANIZATIVAS ----------------------------------#

            # Calculo áreas de plaza de mercado de soacha 
            Ag = (123.93 * 72.50) #Área General
            Ae = (63.17 * 6.00) #Área a eliminar
            Apt = (Ag - Ae) # Área parcial de la plaza 
            
            # Secciones de la plaza
            Sm1 = (36.17 * 6.00)
            Sm2 = (24.54 * 38.26)
            Sm3 = (30.27 * 16.29)
            Sm4 = (11.04 * 18.29)
            Smt = (Sm1 + Sm2 + Sm3 + Sm4)

            # Sección Parqueaderos

            Sp1 = (70.50 * 29.96)
            Sp2 = (9.45 * 54.97)
            Spt = (Sp1 + Sp2)

            # Sección área común

            Sc1 = (19.13 * 72.50)
            Sc2 = Apt - (Smt + Spt + Sc1)

            Dp = (Spt / Apt) * 100 # Disponibilidad de parqueadero = (Área del Parqueadero / Área Total de la Plaza) * 100
            Vv = (Dd * num_dias) # Volumen de Ventas = (Volumen Promedio por Producto) * (Número Promedio de Productos Vendidos por Día) * (Número de Días)
            Zd = (Apt + Vv) # Zona de descargue = Tamaño plaza + Volumen ventas
            SerPu = random.randint(30000, 50000) # Rango de precio por día
            Sg = (Cp + SerPu) # Servicios Generales
            Ng = 8
            Hrs = 24
            Trg = ((random.randint(30000, 50000)*Ng)/(Hrs/2)) # Salario Mensual / Número de Horas Mensuales
            Sv = (Ng * Trg * Hrs) # Servicios de Vigilancia = (Número de Guardias de Seguridad) x (Tarifa por Hora de un Guardia) x (Número de Horas de Servicio)
            Co = ((Dp + Zd + Sg + Sv + Apt)/100) #Recursos Finales

            # Agregar los valores a las listas y promediarlos
            Sg_valores.append(Sg)
            Co_valores.append(Co)

            #--------------------------------- CAPACIDADES OPERACIONALES ----------------------------------#

            Cop=((Ca*0.2)+(Co*0.1)+(Vd*0.4)+(If*0.3))
            Cop_valores.append(Cop)

        promedio_Ca = np.mean(Ca_valores)
        promedio_Co = np.mean(Co_valores)
        promedio_Cop = np.mean(Cop_valores)
        promedio_Qg = np.mean(Qg_valores)
        promedio_Ra = np.mean(Ra_valores)  
        promedio_Cp = np.mean(Cp_valores)
        promedio_Pv = np.mean(Pv_valores)            
        promedio_Mua = np.mean(Mua_valores)
        promedio_Sg = np.mean(Sg_valores)

        promedio_Ven = np.mean(Ven_Valores)
        promedio_Sven = np.mean(Sven_Valores)
        promedio_Inv = np.mean(Inv_Valores)

        Ca_valoresT.append(promedio_Ca)
        Co_valoresT.append(promedio_Co)
        Cop_valoresT.append(promedio_Cop)
        Qg_valoresT.append(promedio_Qg)
        Ra_valoresT.append(promedio_Ra)
        Qra_valoresT.append(promedio_Ra*100/promedio_Qg) # Porcentaje de residuos aprovechados Total
        Cp_valoresT.append(promedio_Cp)
        Pv_valoresT.append(promedio_Pv)
        Mua_valoresT.append(promedio_Mua)
        Sg_valoresT.append(promedio_Sg)

        Ven_ValoresT.append(promedio_Ven)
        Sven_ValoresT.append(promedio_Sven)
        Inv_ValoresT.append(promedio_Inv)

    # Obtener solo los dígitos antes del punto decimal
    promedio_QgT = str((np.mean(Qg_valoresT))).split(".")[0]
    promedio_RaT = str(np.mean(Ra_valoresT)).split(".")[0]
    promedio_QraT = str(np.mean(Qra_valoresT)).split(".")[0]
    promedio_CpT = str(np.mean(Cp_valoresT)).split(".")[0]
    promedio_PvT = str(np.mean(Pv_valoresT)).split(".")[0]
    promedio_MuaT = str(np.mean(int(np.mean(Pv_valoresT) - np.mean(Cp_valoresT)) / 100)).split(".")[0]

    return promedio_QgT, promedio_RaT, promedio_QraT, promedio_CpT, promedio_PvT, promedio_MuaT, Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT
=======
import random
import numpy as np

#Declarar Variables
Ca = 0
Co = 0
Cop = 0
promedio_Ca = 0
promedio_Co = 0
promedio_Cop = 0
promedio_Qg = 0
promedio_Ra = 0
promedio_Qra = 0
promedio_Cp = 0
promedio_Pv = 0
promedio_Mua = 0
promedio_Sg = 0
# Crear listas para almacenar los valores
# por dias
Ca_valores = []
Co_valores = []
Cop_valores = []
Qg_valores = []
Ra_valores = []
Qra_valores = []
Cp_valores = []
Pv_valores = []
Mua_valores = []
Sg_valores = []

Ven_Valores = []
Sven_Valores = []
Inv_Valores = []

#por ciclo
Ca_valoresT = []
Co_valoresT = []
Cop_valoresT = []
Qg_valoresT = []
Ra_valoresT = []
Qra_valoresT = []
Cp_valoresT = []
Pv_valoresT = []
Mua_valoresT = []
Sg_valoresT = []

Ven_ValoresT = []
Sven_ValoresT = []
Inv_ValoresT = []

#ejecutar los ciclos de 30 a 60
vueltas = random.randint(30,60)
#Canidad de Días
num_dias = 0
# Número de puestos en uso
Npu = 3
#Inventario Total
It = 600
#Cantidad de personas por puesto 
Mper = "Mixto"

def limpiar_valores():
    # Eliminar los datos de las listas
    Ca_valores.clear()
    Co_valores.clear()
    Cop_valores.clear()

    Qg_valores.clear()
    Ra_valores.clear()
    Cp_valores.clear()
    Pv_valores.clear()
    Mua_valores.clear()
    Sg_valores.clear()
    Ven_Valores.clear()
    Sven_Valores.clear()
    Inv_Valores.clear()

    Ca_valoresT.clear()
    Co_valoresT.clear()
    Cop_valoresT.clear()
    Qg_valoresT.clear()
    Ra_valoresT.clear()
    Qra_valoresT.clear()
    Cp_valoresT.clear()
    Pv_valoresT.clear()
    Mua_valoresT.clear()
    Sg_valoresT.clear()
    Ven_ValoresT.clear()
    Inv_ValoresT.clear()

#Número de días a simular
def corto():
    num_dias = random.randint(90,179)
    return num_dias
def medio():
    num_dias = random.randint(180,269)
    return num_dias
def largo():
    num_dias = random.randint(270,365)
    return num_dias
#Número de ciclos a simular
def ciclos():
    return vueltas
#Tasa Comprometida
def Baja():
    Tasa = 1
    return Tasa
def Media():
    Tasa = 2
    return Tasa
def Alta():
    Tasa = 3
    return Tasa

def Capacidades(num_dias,Tasa,Npu,It,Mper):
    limpiar_valores()

    #---------------------------------- CAPACIDADES AMBIENTALES ----------------------------------#
    Io = 0 # Inventario Inicial
    If = 0 #Inventario Final
    Ncom = 0 # Número de compras
    vueltas = ciclos()
    contVuel = 0

    if Mper == "Mixto":
        Nmper = random.randint(25,70)
    elif Mper == "Pocas":
        Nmper = random.randint(0,25)
    else:    
        Nmper = random.randint(50,100)
    for _ in range(vueltas):
        contD = 0
        contVuel =+ 1

        Sumvp = [] # Suma Ventas Día

        for _ in range(num_dias):
            contD += 1 # Contador de Días
            Fa = random.randint(0,100) / 100 #Factor de Abastecimiento = Aleatorio despues del dia 1 
            
            #******************************************************************************************
            #****************************** PROCESO DE ABASTECIMIENTO *********************************
            #******************************************************************************************

            if contD == 1: #Abastecimiento Total
                Io = It 
            else:
                Io = If

            #******************************************************************************************
            #****************************** PROCESO DE COMPRA Y VENTA *********************************
            #******************************************************************************************
            if Tasa == 1:
                Pi = random.randint(0, Nmper) # Número de personas que ingresan a la plaza
            elif Tasa == 2:
                Pi = random.randint(Nmper,Nmper*3)
            else:
                Pi = random.randint(Nmper*2, Nmper*4)

            if Pi == 0:
                Nc = 0
                Pnc = 0 
            else: # Número de personas que no compran
                if Tasa == 1: 
                    Pnc = random.triangular(0,Pi,(Pi*0.9))
                elif Tasa == 2:
                    Pnc = random.triangular(0,Pi,(Pi*0.5))
                else:
                    Pnc = random.triangular(0,Pi,(Pi*0.1))
            
            Nc = int(Pi - Pnc) # Número de compradores

            if Nc == 0:
                Ncom = 0
            else:
                for _ in range(Nc): #Por si un cliente compra más de un producto
                    # Aplicación de Distribución normal
                    if Tasa == 1:
                        mu = (Nc + 2)  # Valor medio
                        sigma = 6  # Desviación estándar
                    elif Tasa == 2:
                        mu = (Nc + 7) 
                        sigma = 17 
                    else:
                        mu = (Nc + 12) 
                        sigma = 6                     

                    # Generar un valor aleatorio con distribución normal
                    while True:
                        Ncom = int(random.normalvariate(mu, sigma))
                        if Ncom >= Nc: # Verificar que el numero de compras sea >= a los compradores
                            break 
        
            Vd = Ncom # Ventas Día = Número de compras

            If = Io - Vd # Inventario Final = Inventario Inicial - Ventas Día
            
            if If <= 0:
                If = 0
                Io = 0
                Nc = 0
            
            Sumvp.append(Vd)
            Svp = sum(Sumvp) # Sumatoria Ventas

            Lvp = [] # Lista para almacenar las ventas de productos

            for _ in range(Vd):
                Pp = random.randint(500, 2000) #Precio Productos valor minimo y maximo
                Lvp.append(Pp)# Costos Ganancia
            
            if Vd == 0:
                Pvd = 0
            else:
                Pvd = sum(Lvp) / Vd #Promedio de venta diaria = sumatoria de la venta de los productos / numero de ventas en el día

            #******************************************************************************************
            #****************************** PROCESO DE ABASTECIMIENTO *********************************
            #******************************************************************************************
            
            if If == 0 and Vd == 0:
                 Fa = 0
            if If < It and Io < (It*0.7) and Fa >= 0.7:
                if Tasa == 2:
                    Io += random.randint(0, It*0.15)
                elif Tasa == 3:
                    Io += random.randint(0, It*0.25)
            if If < It and Io < (It*0.5) and Fa >= 0.5:
                if Tasa == 1:
                    Io += random.randint(0, It*0.2)
                elif Tasa == 2:
                    Io += random.randint(0, It*0.3)
                else:
                    Io += random.randint(0, It*0.5)
     

            if Fa == 0:
                Dd = 0
            else:
                Dd = Pvd / Fa #Demanda Diaria = (Promedio Ventas Diarias) / (Frecuencia de Abastecimiento)

            Cll = (Dd + Io) - If # Cantidad de producto que llega = (Demanda Diaria + Inventario Inicial) - Inventario Final

            if Io == 0:
                Pm = 0
            else:
                Pm = ((Io - If) /Io) * 100 # Porcentaje de Merma = ((Inventario Inicial - Inventario Final) / Inventario Inicial) x 100

            Ma = (Cll * Pm) / 100 # Porcentaje de merma de alistamiento  

            Pns = (Io - Vd)/100 #porcentaje de productos que no se vendieron

            Pr = Vd * (random.normalvariate(0.3, 0.25) + random.normalvariate(0.2, 0.2)) / 100 # Porcentaje de residuos  = Ventas * (Pérdida de Producto + Parte no comestible al vender)

            Qg = int((Npu * Vd) * (Ma + Pns + Pr)) # Cantidad de los residuos generados
            
            if Qg <= 0:
                Qg = 0
                Qra = 0
                Ra = 0
            else:
                Ra = int(Qg * random.randint(0,60))/100 # Cantidad de residuos aprovechados
                if Ra < 0:
                    Ra = (Ra *-1)
                else:
                    Ra = int(Qg * random.randint(0,70))/100

                Qra = int((Ra * 100) / Qg) # Porcentaje de residuos aprovechados Día
            
            if Tasa == 1:
                Cp = Qra * random.randint(1100, 1300) # Costo del proceso
            elif Tasa == 2:
                Cp = Qra * random.randint(1000, 1200) # Costo del proceso
            else:
                Cp = Qra * random.randint(900, 1100) # Costo del proceso

            Pv = Qra * Pvd # Precio de venta

            Mua = (Pv - Cp) / 100 # Margen de utilidad ambiental Día

            Ca = ((Qra*0.4)+(Mua*0.3))

            # Agregar los valores a las listas y promediarlos
            Ca_valores.append(Ca)
            Qg_valores.append(Qg)
            Ra_valores.append(Ra)
            Cp_valores.append(Cp)
            Pv_valores.append(Pv)
            Mua_valores.append(Mua)
        
            Ven_Valores.append(Vd)
            Sven_Valores.append(Svp)
            Inv_Valores.append(If)

            #--------------------------------- CAPACIDADES ORGANIZATIVAS ----------------------------------#

            # Calculo áreas de plaza de mercado de soacha 
            Ag = (123.93 * 72.50) #Área General
            Ae = (63.17 * 6.00) #Área a eliminar
            Apt = (Ag - Ae) # Área parcial de la plaza 
            
            # Secciones de la plaza
            Sm1 = (36.17 * 6.00)
            Sm2 = (24.54 * 38.26)
            Sm3 = (30.27 * 16.29)
            Sm4 = (11.04 * 18.29)
            Smt = (Sm1 + Sm2 + Sm3 + Sm4)

            # Sección Parqueaderos

            Sp1 = (70.50 * 29.96)
            Sp2 = (9.45 * 54.97)
            Spt = (Sp1 + Sp2)

            # Sección área común

            Sc1 = (19.13 * 72.50)
            Sc2 = Apt - (Smt + Spt + Sc1)

            Dp = (Spt / Apt) * 100 # Disponibilidad de parqueadero = (Área del Parqueadero / Área Total de la Plaza) * 100
            Vv = (Dd * num_dias) # Volumen de Ventas = (Volumen Promedio por Producto) * (Número Promedio de Productos Vendidos por Día) * (Número de Días)
            Zd = (Apt + Vv) # Zona de descargue = Tamaño plaza + Volumen ventas
            SerPu = random.randint(30000, 50000) # Rango de precio por día
            Sg = (Cp + SerPu) # Servicios Generales
            Ng = 8
            Hrs = 24
            Trg = ((random.randint(30000, 50000)*Ng)/(Hrs/2)) # Salario Mensual / Número de Horas Mensuales
            Sv = (Ng * Trg * Hrs) # Servicios de Vigilancia = (Número de Guardias de Seguridad) x (Tarifa por Hora de un Guardia) x (Número de Horas de Servicio)
            Co = ((Dp + Zd + Sg + Sv + Apt)/100) #Recursos Finales

            # Agregar los valores a las listas y promediarlos
            Sg_valores.append(Sg)
            Co_valores.append(Co)

            #--------------------------------- CAPACIDADES OPERACIONALES ----------------------------------#

            Cop=((Ca*0.2)+(Co*0.1)+(Vd*0.4)+(If*0.3))
            Cop_valores.append(Cop)

        promedio_Ca = np.mean(Ca_valores)
        promedio_Co = np.mean(Co_valores)
        promedio_Cop = np.mean(Cop_valores)
        promedio_Qg = np.mean(Qg_valores)
        promedio_Ra = np.mean(Ra_valores)  
        promedio_Cp = np.mean(Cp_valores)
        promedio_Pv = np.mean(Pv_valores)            
        promedio_Mua = np.mean(Mua_valores)
        promedio_Sg = np.mean(Sg_valores)

        promedio_Ven = np.mean(Ven_Valores)
        promedio_Sven = np.mean(Sven_Valores)
        promedio_Inv = np.mean(Inv_Valores)

        Ca_valoresT.append(promedio_Ca)
        Co_valoresT.append(promedio_Co)
        Cop_valoresT.append(promedio_Cop)
        Qg_valoresT.append(promedio_Qg)
        Ra_valoresT.append(promedio_Ra)
        Qra_valoresT.append(promedio_Ra*100/promedio_Qg) # Porcentaje de residuos aprovechados Total
        Cp_valoresT.append(promedio_Cp)
        Pv_valoresT.append(promedio_Pv)
        Mua_valoresT.append(promedio_Mua)
        Sg_valoresT.append(promedio_Sg)

        Ven_ValoresT.append(promedio_Ven)
        Sven_ValoresT.append(promedio_Sven)
        Inv_ValoresT.append(promedio_Inv)

    # Obtener solo los dígitos antes del punto decimal
    promedio_QgT = str((np.mean(Qg_valoresT))).split(".")[0]
    promedio_RaT = str(np.mean(Ra_valoresT)).split(".")[0]
    promedio_QraT = str(np.mean(Qra_valoresT)).split(".")[0]
    promedio_CpT = str(np.mean(Cp_valoresT)).split(".")[0]
    promedio_PvT = str(np.mean(Pv_valoresT)).split(".")[0]
    promedio_MuaT = str(np.mean(int(np.mean(Pv_valoresT) - np.mean(Cp_valoresT)) / 100)).split(".")[0]

    return promedio_QgT, promedio_RaT, promedio_QraT, promedio_CpT, promedio_PvT, promedio_MuaT, Ca_valoresT, Qra_valoresT, Co_valoresT, Mua_valoresT, Cop_valoresT, Sg_valoresT
>>>>>>> 8086880b55efd63f49e0728f2f4fa0b85da2c170
