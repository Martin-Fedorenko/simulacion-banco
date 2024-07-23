import random
import math
import time
from datetime import datetime, timedelta

### C.I. ###

# VARIABLES DE CONTROL
N = 0
H = 0
IPC = 0
VC = 0
M = 0

INS_PETICION = 0 #cantidad instrucciones promedio por peticion
MEM_PETICION = 0 #cantidad memoria promedio por peticion

# VARIABLES DE RESULTADO
CVCS = 0
PRF = 0
PCF = 0
PPR = 0

# VARIABLES DE ESTADO
P = 0

# VARIABLES AUXILIARES
T=0
TF = 24 * 365 * 10 # 10 años de simulación 24 horas al dia
FECHA_INICIAL = datetime(2024, 1, 1)
SPRF = 0 #sumatoria
SPCF = 0 #sumatoria
SPPR = 0 #sumatoria
DDOS_FLAG = False 

HV = 9999999999999

while True:
    try:
        ### VARIABLES DE CONTROL ###
        M = int(input("Cantidad de memoria RAM (M): "))
        N = int(input("Cantidad de nucleos (N): "))
        H = int(input("Cantidad de hilos (H): "))
        VC = int(input("Velocidad clock en Hz, NO en Ghz (VC): "))
        IPC = int(input("Cantidad de instrucciones por ciclo (IPC): "))


        break
    except ValueError:
        print("\nError: Solo se permiten numeros enteros.\n")
        continue

def obtener_PH(): #peticiones por hora
    R = random.uniform(0, 1)
    #ACA VA LA FORMULA DE LA FDP
    PH = 0
    return  PH 

def obtener_hora():
    global T

    return T % 24

def obtener_fecha():
    global T, FECHA_INICIAL

    cant_dias = T // 24
    cant_horas_restantes = obtener_hora()
    fecha_actual = FECHA_INICIAL + timedelta(days=cant_dias, hours=cant_horas_restantes)
    return fecha_actual

def obtener_capacidad_cpu():
    global N, H, IPC, VC, DDOS_FLAG

    if (DDOS_FLAG):
        return N*H*IPC*VC*0.8
    else:
        N*H*IPC*VC

def obtener_capacidad_ram():
    global M, DDOS_FLAG

    if (DDOS_FLAG):
        return M*0.8
    else:
        M

def obtener_max_peticiones_cpu():
    global INS_PETICION
    return obtener_capacidad_cpu*3600/INS_PETICION

def obtener_max_peticiones_ram():
    global MEM_PETICION
    return obtener_capacidad_ram/MEM_PETICION

def resultados():
    global T

    PRF = SPRF / T
    PCF = SPCF / T
    PPR = SPPR / T


    print(f"Cantidad de veces capacidad del servidor superada {CVCS}")
    print(f"Promedio de RAM faltante: {PRF}")
    print(f"Promedio de CPU faltante: {PCF}")
    print(f"Promedio peticiones rechazadas: {PPR}")


def realizar_simulacion():
    global T, P
    while True:

        T=T+1

        ### GENERO, CALCULO O USO TODO LO QUE ENTRA ###

        ph = obtener_PH()

        if obtener_hora() in [18, 19, 20, 21, 22]:
            ph = ph * 3

        # FALTAN LAS OTRAS CONDICIONES

        ### GENERO, CALCULO O USO TODO LO QUE SALE ###

        pcpu = obtener_max_peticiones_cpu
        pram = obtener_max_peticiones_ram

        ### MODIFICO VAR DE ESTADO CON TODO LO QUE SALE Y ENTRA ###

        P = P + ph - min(pcpu, pram)

        ### EFECTUO CONTROL DE MINIMA (OPCIONAL)

        if (P < 0):
            P = 0

        ### EFECTUO CONTROL DE MAXIMA (OPCIONAL)

        if T < TF:
            continue
        else:
            break

    resultados()


def main():
    print("\n\n### Comenzando simulacion ###\n\n")
    realizar_simulacion()
    print("\nFinalizando simulacion...")


if __name__ == "__main__":
    main()