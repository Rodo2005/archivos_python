#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import csv
import re


def ej1():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de líneas
    de un archivo. Abra el archivo "notas.txt" en modo "lectura",
    lea linea alinea el archivo, y cuente la cantidad de líneas.
    Al finalizar el proceso, imprimir en pantalla la cantidad
    de líneas leaidas.

    Como práctica de funciones, puede realizar la función
    "contar_lineas" que reciba como parámetro el nombre del archivo
    y cumpla el objetivo especificado, retornando la cantidad
    de líneas encontradas.
    '''


def contar_lineas():
    cantidad_lineas = 0
    fi = open('notas.txt', 'r')
    for lineas in ('notas.txt'):
        lineas = fi.readline()
        cantidad_lineas += 1
    print('El texto tiene', cantidad_lineas, 'lineas')
    fi.close()


#if __name__ == '__main__':
    #contar_lineas()



def ej2():
    # Ejercicios con archivos txt
    cantidad_lineas = 0

    '''
    Copy paste!!
    Deberá abrir dos archivo txt, uno para lectura (fi) y otro
    para escritura (fo) (un archivo nuevo).
    El archivo abierto para lectura (fi) debe ser el archivo
    "notas.txt"

    Debe leer "línea por línea" el archivo "nota.txt" y copiar
    "línea a línea" en el archivo para escritura.

    A su vez, mientras va escribiendo "línea a línea" debe
    contar la cantidad de línea que se copiaron e imprimir
    al final del proceso el valor.
    '''
def escribir_archivo():

    cantidad_lineas = 0
    fi = open('notas.txt', 'r')
    for lineas in ('notas.txt'):
        lineas = fi.readline()
        fo = open('notas_copia.txt', 'a')   # Inove: Esta linea sería más "segura" si se ejecuta antes de empezar el bucle
        fo.writelines(lineas)
        cantidad_lineas += 1
    print('El nuevo archivo tiene', cantidad_lineas, 'lineas')
    fo.close()
    fi.close()
    
    # Inove: El ejercicio está perfectamente realizado, acotamos un comentario
    # respecto al "open" del archivo de salida "fo". El archivo se está cerrando cuando se sale del loop
    # pero esta está volviendo a abrir en cada iteración del loop, Python esto lo está manejando por detras
    # pero para evitar un problema en el futuro siempre es conveniente cerrar un archivo antes de volverlo a abrir
    # Se podría cerrar "fo" en cada iteración del loop, o para hacerlo más eficiente, solo abrirlo una vez
    # antes de empezar el loop
    # Es solo una nota de "color" para futuros casos no tener un problema "invisible" relacionado a esto


#if __name__ == '__main__':
    #escribir_archivo()
    

    # fi = open('nota.txt', 'r')
    # fo = open(.......)

    # Recuerde cerrar los archivos al final ;)


def ej3():
    # Ejercicios con archivos CSV
    archivo = 'propiedades.csv'
    '''
    Realice un programa que abra el archivo CSV "propiedades.csv"
    en modo lectura. Recorrar dicho archivo y contar
    la cantidad de departamentos de 2 ambientes y la cantidad
    de departamentos de 3 ambientes disponibles.
    Al finalizar el proceso, imprima en pantalla los resultados.
    '''
'''
    fi = open('propiedades.csv', 'r')

    '''

def propiedades():
    with open('propiedades.csv', 'r') as csvfile:
        data = list(csv.DictReader(csvfile))
        dos_amb = 0
        tres_amb = 0
        dif_amb = 0
        for i in range(len(data)):
            datos = data[i]
            ambientes = datos.get('ambientes')
            if ambientes == '':
                ambientes = 0
                dif_amb += 1
            elif ambientes != '':
                ambientes = int(ambientes)
            if ambientes == 2:
                dos_amb += 1
            elif ambientes == 3:
                tres_amb += 1
            elif ambientes != 2 and ambientes != 3:
                dif_amb += 1
        print('Hay', dos_amb, 'departamentos de dos ambientes\n')
        print('Hay', tres_amb, 'departamentos de tres ambientes\n')
        print('Hay', dif_amb, 'propiedades que no cumplen con la busqueda\n')


#if __name__ == '__main__':
    #propiedades()



 
def ej4():
    # Ejercicios con diccionarios
    inventario = {'manzanas': 6}

    '''
    Realice un programa que pida por consola
    el nombre de una fruta o verdura y luego
    pida la cantidad que hay en stock
    Agregar al diccionario el par:
    <fruta>:<cantidad>
    Esta operacion se debe realizar en un bucle
    hasta ingresar como fruta/verdura la palabra "FIN"

    Al finalizar el bucle anterior, debe generar otro bucle
    en donde se pida ingresar la fruta o verdura que desea
    conocer su estado de stock.
    Deberá imprimir en pantalla la cantidad de esa fruta en
    inventario, y en caso de no exista ese elemento en nuestro
    inventario se debe imprimir en pantalla "Elemento no encuentrado"
    NOTA: Proponemos utilizarel método "get" que devuelve "None" si el
    elemeto no existe en el diccionario.

    Se debe terminar ese segundo bucle cuando se ingrese la palabra FIN
    '''

    # 1) Bucle 1
    # Generar y completar el diccionario con las frutas y cantidades
    # ingresadas por consola hasta ingresar la palabra "FIN"
    #inventarios = {}


    #fi = open('inventario', 'r')

    # 2) Bucle 2
    # Ingresar por consola la fruta que desea conocer en stock
    # Finalizar cuando la fruta ingresada sea igual a "FIN"


def ej5():
    # Ejercicios con archivos CSV
    #inventario = {}

    '''
    Basado en el ejercicio anterior, genere un archivo CSV
    (abrir un archivo CSV como escritura) que posea las siguientes
    columnas:
    1) 'Fruta Verdura'
    2) 'Cantidad'

    Estas dos columnas representan el nombre de las dos "claves"
    del diccionario que utilizaremos para escribir en el archivo CSV

    writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    Deberá realizar un bucle en donde en cada iteracion del bucle
    se le socilitará por consola que ingrese un tipo de fruta o verdura
    y su cantidad, deberá escribir una línea en el archivo CSV (una fila)
    con esa información ingresada.
    El bucle finalizará cuando se ingrese como fruta o verdura
    la palabra "FIN"

    Al finalizar deberá tener un archivo (con el nombre que usted haya
    elegido) con todas las filas completas en las dos columnas especificadas
    con todas las frutas o verduras ingresadas y sus cantidades
    '''
    # Recuerde crear el header correspondiente con "writeheader", el cual
    # se debe especificar al abrir el archivo.

    # Bucle....

    # writer.writerow({'Fruta Verdura': ....., 'Cantidad': ....})

    csvfile = open('inventario2.csv', 'a', newline='')
    cant = 0.0
    header = ['vegetales', 'cantidad']
    writer = csv.DictWriter(csvfile, fieldnames=header)
    #writer.writeheader()
    while True:
        vegetales = input('vegetales: ?\n')
        if vegetales == 'fin':
            break
        else:
            cantidad = float(input('cantidad: ?\n'))
            datos = {'vegetales': vegetales, 'cantidad': cantidad}
            writer.writerow(datos)
        csvfile.flush()
    csvfile.close()

    csvfile = open('inventario2.csv', 'r', newline='')
    data = list(csv.DictReader(csvfile))
    vegetal = input('Que vegetal: ?\n')
    for i in range(len(data)):
        row = data[i]
        vegetales = row.get('vegetales')
        cantidad = row.get('cantidad')
        if vegetales == vegetal:
            print('El stock de', vegetales, 'es de', cantidad, 'kilogramos')
            print('')
            break
        elif vegetales != vegetal:
            print('Ingresaste', vegetal, 'pero No existe en el inventario')
            break
    csvfile.close


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
