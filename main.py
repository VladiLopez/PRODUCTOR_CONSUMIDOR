#Actividad 2 - Programa 1 - Simular procesamiento por lotes
#Alumnos: López Reynoso Javier Vladimir
#         López Ríos Ian Daniel

import os
import time
from proceso import Proceso

lista_lotes = []
lotes = []
procesos = []
listaAux = []
id_usados = []
proc_terminados = []      
                                
contador_global = 0
contador_procesos = 0

def funcionOperacion(operador):
    proceso.numero1 = int(input("Ingresa el numero 1: "))   
    proceso.numero2 = int(input("Ingresa el numero 2: "))
    proceso.cadena_operacion = '{}{}{}'.format(proceso.numero1, operador, proceso.numero2)

    procesos.append(proceso.cadena_operacion)

# lotes = [ ['Juan', '6+3', 10, 1], [''Ramon','4-7',15,2], [...]]

cantidad = int(input("Ingrese la cantidad de procesos a realizar: "))

while(contador_procesos < cantidad):

    proceso = Proceso()

    #-------------Inputs-------------
    print('\n---------Proceso {}---------'.format(contador_procesos + 1))

    proceso.programador = input("Ingresa el nombre del programador: ")
    procesos.append(proceso.programador)

    #?Validacion de la operacion
    while True:
        proceso.operacion = input("Ingrese la operacion a realizar (+, -, *, /, %): ")  
        
        if proceso.operacion == "+":
            funcionOperacion('+')
            proceso.resultado_operacion = proceso.numero1 + proceso.numero2
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "-":
            funcionOperacion('-')
            proceso.resultado_operacion = proceso.numero1 - proceso.numero2
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "*":
            funcionOperacion('*')
            proceso.resultado_operacion = proceso.numero1 * proceso.numero2
            procesos.append(proceso.resultado_operacion)
            break

        elif proceso.operacion == "/":
            proceso.numero1 = int(input("Ingresa el numero 1: "))   
            proceso.numero2 = int(input("Ingresa el numero 2: "))
            
            #?Validacion para que no se divida entre 0
            if proceso.numero2 > 0:              
                proceso.cadena_operacion = '{}/{}'.format(proceso.numero1, proceso.numero2)
                proceso.resultado_operacion = proceso.numero1 / proceso.numero2
                procesos.append(proceso.cadena_operacion)
                procesos.append(proceso.resultado_operacion)
                break
            else:
                proceso.numero2 = int(input("El numero tiene que ser mayor a 0, vuelve a ingresarlo:"))
                proceso.cadena_operacion = '{}/{}'.format(proceso.numero1, proceso.numero2)
                proceso.resultado_operacion = proceso.numero1 / proceso.numero2
                procesos.append(proceso.cadena_operacion)
                procesos.append(proceso.resultado_operacion)
                break

        elif proceso.operacion == "%":
            proceso.numero1 = int(input("Ingresa el numero 1: "))
            proceso.numero2 = int(input("Ingresa el numero 2: "))
            
            #?Validacion para que no se divida entre 0
            if proceso.numero2 > 0:              
                proceso.cadena_operacion = '{}%{}'.format(proceso.numero1, proceso.numero2)
                proceso.resultado_operacion = proceso.numero1 / proceso.numero2
                procesos.append(proceso.cadena_operacion)
                procesos.append(proceso.resultado_operacion)
                break
            else:
                proceso.numero2 = int(input("El numero tiene que ser mayor a 0, vuelve a ingresarlo:"))
                proceso.cadena_operacion = '{}%{}'.format(proceso.numero1, proceso.numero2)
                proceso.resultado_operacion = proceso.numero1 / proceso.numero2
                procesos.append(proceso.cadena_operacion)
                procesos.append(proceso.resultado_operacion)
                break
        else:
            print("Operacion invalida, ingresala de nuevo\n") 

    #?Validacion del TME
    while True:
        proceso.tiempo_maximo = int(input("Ingresa el Tiempo Maximo Estimado del proceso: ")) 
        if proceso.tiempo_maximo > 0:
            procesos.append(proceso.tiempo_maximo)
            break
        else:
            print("El tiempo debe ser mayor a 0, ingresalo de nuevo")

    #?Validacion Id
    while True:
        proceso.id_programa = int(input("Ingrese el ID: ")) 
        if proceso.id_programa in id_usados:
            print("El id ingresado ya ha sido utilizado, ingrese uno nuevo")
        else:
            id_usados.append(proceso.id_programa)
            procesos.append(proceso.id_programa)
            break

    lotes.append(procesos) # Se agrega el proceso a la lista 'lotes' 
    procesos = [] # Se vacía la lista de procesos para empezar uno nuevo

    contador_procesos += 1

# Se segmentan los lotes (4 procesos por lote)
if len(lotes) % 4 == 0:
    indexI = 0
    indexF = 4

    for proc in range(len(lotes) // 4):
        lista_lotes.append(lotes[indexI:indexF])
        indexI += 4
        indexF += 4

if len(lotes) % 4 != 0:     # En caso de que el numero de procesos no sea divisible entre 4
    indexI = 0
    indexF = 4

    if len(lotes) < 4:
        lista_lotes.append(lotes[indexI:len(lotes)]) #En caso de que sean menos de 4 procesos, el lote se conforma por ese numero
    else:    
        for proc in range(len(lotes) // 4):
            lista_lotes.append(lotes[indexI:indexF])
            indexI += 4
            indexF += 4

        indexF -= 4
        for proc in range(len(lotes) % 4):
            listaAux.append(lotes[indexF+proc])

        lista_lotes.append(listaAux)

longitudLista = len(lista_lotes)
os.system("pause")

#Impresion de datos
    
for i in range(len(lista_lotes)):   #Longitud de lista_lotes (cuantos lotes hay?)

    contador_procesos_lotes = 0
    
    while contador_procesos_lotes < len(lista_lotes[i]):    #Mientras haya procesos dentro del lote
        
        for j in range(len(lista_lotes[i])):    #Longitud de los lotes (Cuantos procesos hay en el lote?)

            tiempoRestante = lista_lotes[i][j][3]   

            while tiempoRestante >= 0:          

                os.system("cls")        

                print('----Cantidad de lotes pendientes---')
                print(len(lista_lotes)-(i+1))

                print('---------Lote en Ejecucion---------')
                for k in range(len(lista_lotes[i])):    #Recorrer los procesos del lote    
                    print(' Nombre: {} TME: {}'.format(lista_lotes[i][k][0], lista_lotes[i][k][3]), end=' |') 

                print('\n-------Proceso en Ejecucion--------')
                print("Nombre: {} \nOperacion: {} \nTME: {} \nId: {} \nTiempo trascurrido: {} \nTiempo restante: {}".format(lista_lotes[i][j][0], 
                lista_lotes[i][j][1], lista_lotes[i][j][3], lista_lotes[i][j][4], contador_global, tiempoRestante))
                
                print('--------Procesos Terminados--------') 
                if len(proc_terminados) > 0:
                    for proc in range(len(proc_terminados)):                    
                        print("Id: {} Operacion: {} Resultado {:.2f}".format(proc_terminados[proc][0],proc_terminados[proc][1],
                        proc_terminados[proc][2])) 

                if tiempoRestante == 0:             
                    listaAux = []           
                    listaAux.extend([lista_lotes[i][j][4],lista_lotes[i][j][1],lista_lotes[i][j][2]])   #Se agregan los datos a listaAux
                    proc_terminados.append(listaAux)
                    print("Id: {} Operacion: {} Resultado {:.2f}".format(lista_lotes[i][j][4],lista_lotes[i][j][1],lista_lotes[i][j][2]))

                tiempoRestante -= 1
                contador_global += 1
                time.sleep(1)
                
            contador_procesos_lotes += 1