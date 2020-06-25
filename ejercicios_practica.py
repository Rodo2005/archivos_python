#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    print("Cuenta caracteres\n")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''
    fi = open('texto.txt', 'r')
    for line in fi:
        print(line, end='')
        linea_caracteres = len(line)
        cantidad_letras = cantidad_letras + linea_caracteres
    print('El total de caracteres es:', cantidad_letras)
    fi.close


def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    transcribir = open('escritura.txt', 'a')
    while True:
        texto = str(input('Ingresar texto!\n'))
        if texto == '':
            break
        elif texto != '':
            cantidad_letras = cantidad_letras + len(texto)
    print('La longitud del texto es de', cantidad_letras, 'caracteres')
    transcribir.close

def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2

    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''
    import csv

    lista_pr = []
    suma_pr = 0.0
    pr = float
    cuantos = int
    promedio = float
    maximo = float
    minimo = float
    precio = float
    i = 0
    propiedades = open('propiedades.csv', 'r')
    data = list(csv.DictReader(propiedades))
    buscar = input('Cuantos ambientes ?\n')
    print('')
    j = 0
    for i in range(len(data)):
        row = data[i]
        amb = row.get('ambientes')
        if buscar == amb:
            mon = row.get('moneda')
            if mon == 'ARS':
                j += 1
                pr = float(row.get('precio'))
                lista_pr.append(pr)
                suma_pr = suma_pr + pr
    promedio = suma_pr / j
    maximo = max(lista_pr)
    minimo = min(lista_pr)
    print('Tenés', j, 'departamentos de', buscar, 'ambientes para elegir\n')
    print('El valor promedio de alquiler es', '$','{0:.2f}'.format(promedio), end='\n')
    print('El alquiler del departamento mas caro cuesta', '$', maximo, end='\n')
    print('El alquiler del departamento mas barato cuesta', '$', minimo, end='\n')
    propiedades.close


        
def ej4():
    print("Ahora sí! buena suerte :)")

    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    '''

import csv
import re
import statistics
import time
import datetime


def estadisticas():
    resultados = open('2019 Ironman.csv', 'r')
    datos = list(csv.DictReader(resultados))
    swin = str
    bike = str
    run = str
    t_max_swin = 0
    t_min_swin = 0
    t_prom_swin = 0
    t_max_bike = 0
    t_min_bike = 0
    t_prom_bike = 0
    t_max_run = 0
    t_min_run = 0
    t_prom_run = 0
    div = ''
    print('Las categorias son "MPRO" "M45-49" "M25-29" "M18-24"')
    print('Si la categoria es MPRO ingrese "1"')
    print('Si la categoria es M45-49 ingrese "2"')
    print('Si la categoria es M25-29 ingrese "3"')
    print('Si la categoria es M18-24 ingrese "4"')
    categoria = input('Sobre que categoria desea obtener la estadistica: ?\n')
    while True:
        if categoria == '1':
            div = 'MPRO'
        elif categoria == '2':
            div = 'M45-49'
        elif categoria == '3':
            div = 'M25-29'
        elif categoria == '4':
            div = 'M18-24'
        elif categoria != 1 and categoria != 2 and categoria != 3 and categoria != 4:
            print('No selecciono ninguna categoria valida!')
            break
        lista_swim = []
        lista_bike = []
        lista_run = []
        longitud = len(datos)
        for i in range(2260):
            row = datos [i] 
            division = row.get('Division')
            
            if division == div:
                swim = row.get('Swim')
                Swim = datetime.datetime.strptime(swim, '%H:%M:%S')
                seg_1_s = int(Swim.strftime('%H')) * 3600
                seg_2_s = int(Swim.strftime('%M')) * 60
                seg_3_s = int(Swim.strftime('%S'))
                segundos_swim = seg_1_s + seg_2_s + seg_3_s
                lista_swim.append(segundos_swim)
                bike = row.get('Bike')
                Bike = datetime.datetime.strptime(bike, '%H:%M:%S')
                seg_1_b = int(Bike.strftime('%H')) * 3600
                seg_2_b = int(Bike.strftime('%M')) * 60
                seg_3_b = int(Bike.strftime('%S'))
                segundos_bike = seg_1_b + seg_2_b + seg_3_b
                lista_bike.append(segundos_bike)
                run = row.get('Run')
                Run = datetime.datetime.strptime(run, '%H:%M:%S')
                seg_1_r = int(Run.strftime('%H')) * 3600
                seg_2_r = int(Run.strftime('%M')) * 60
                seg_3_r = int(Run.strftime('%S'))
                segundos_run = seg_1_r + seg_2_r + seg_3_r
                lista_run.append(segundos_run)    
                
                t_max_swim = max(lista_swim)
                t_min_swim = min(lista_swim)
                t_prom_swim = statistics.mean(lista_swim)
                t_max_bike = max(lista_bike)
                t_min_bike = min(lista_bike)
                t_prom_bike = statistics.mean(lista_bike)
                t_max_run = max(lista_run)
                t_min_run = min(lista_run)
                t_prom_run = statistics.mean(lista_run)

                d, r1 = divmod(t_max_swim, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                max_swim = datetime.time(h, m, s)
                d, r1 = divmod(t_min_swim, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                min_swim = datetime.time(h, m, s)
                d, r1 = divmod(t_prom_swim, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                prom_swim = datetime.time(h, m, s)

                d, r1 = divmod(t_max_bike, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                max_bike = datetime.time(h, m, s)
                d, r1 = divmod(t_min_bike, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                min_bike = datetime.time(h, m, s)
                d, r1 = divmod(t_prom_bike, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                prom_bike = datetime.time(h, m, s)

                d, r1 = divmod(t_max_run, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                max_run = datetime.time(h, m, s)
                d, r1 = divmod(t_min_run, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                min_run = datetime.time(h, m, s)
                d, r1 = divmod(t_prom_run, 86400)
                h, r2 = divmod(r1, 3600)
                m, s = divmod(r2, 60)
                h = int(h)
                m = int(m)
                s = int(s)
                prom_run = datetime.time(h, m, s)
                
                    
            elif i == 2260:
                    break
        print('En la categoria', div)
        print('El tiempo maximo en natacion fue de ', max_swim)
        print('El tiempo minimo en natacion fue de', min_swim)
        print('El tiempo promedio de natacion fue de', prom_swim)
        print('')
        print('El tiempo maximo en ciclismo fue de ', max_bike)
        print('El tiempo minimo en ciclismo fue de', min_bike)
        print('El tiempo promedio de ciclismo fue de', prom_bike)
        print('')
        print('El tiempo maximo corriendo fue de ', max_run)
        print('El tiempo minimo corriendo fue de', min_run)
        print('El tiempo promedio corriendo fue de', prom_run)
        break

    resultados.close()

if __name__ == '__main__':
   estadisticas()
            



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
