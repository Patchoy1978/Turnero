"""
Este módulo se encarga de generar el turno para que el usuario lo imprima
y de genrerar el nuevo turno o salir del sistema
"""

# importamos el modulo numeros con todas las funcionalidades que tiene
from numeros_1 import *
from datetime import datetime

# esta clase de encarga de generar el turno para imprimir
class NumeroDelTurno:

    # almacenamos en una variable el indice que se genera por cada codigo de cada categoria
    generadores_por_categoria = {}

    turnos_del_dia = [] # almacenamos una lista en una variable que contiene los turnos generados en el dia

    categorias_dia = []# almacenamos una lista en una variable que contiene las categorias generadas en el dia

    # creamos el constructor 
    def __init__(self, categorias_usuario):
        
        self.categorias_usuario = categorias_usuario

        # realizamos un condicional para verificar si el numero del turno esta y seguir con el siguiente
        if categorias_usuario not in NumeroDelTurno.generadores_por_categoria:

            NumeroDelTurno.generadores_por_categoria[categorias_usuario] = numeros_turno(categorias_usuario)

        self.numeros_usuario = NumeroDelTurno.generadores_por_categoria[categorias_usuario]

    # implementamos el decorador par el turno
    @mostrar_informacion_turno

    # creamos el turno 
    def generar_turno(self):

        # creamos el condicional para crear el formato del turno
        if self.categorias_usuario == 'Farmacia':

            iniciales = 'F - '

        elif self.categorias_usuario == 'Cosmeticos':

            iniciales = 'C - '

        elif self.categorias_usuario == 'Perfumeria':

            iniciales = 'P - '

        # almacenamos el número del turno en una variable
        turno = next(self.numeros_usuario)

        # extraemos el digito del turno 
        extraer_numero = ''.join(i for i in turno if i.isdigit())

        # generamos el turno completp
        turno = f'\033[3m\033[1m{iniciales} {extraer_numero}\033[0m\n'

        # centramos el turno
        turno = turno.center(52)

        NumeroDelTurno.turnos_del_dia.append(extraer_numero) # llenamos la lista anterior con el numero que saldra en el turno

        NumeroDelTurno.categorias_dia.append(iniciales) # llenamos la lista anterior con la categoria que saldra en el turno

        # imprimimos el turno
        print(turno)
    
# generamos el nuevo turno
def generar_nuevo_turno():

    # traemos la categoria que el usuario elige
    categoria_elegida = categorias()

    # almacenamos el turno por categoria
    turno_final = NumeroDelTurno(categoria_elegida)

    # tenemos el nuevo turno
    turno_final.generar_turno()

# traemos la categoria que el usuario elige
categoria_elegida = categorias()

# almacenamos el número del turno por categoria
turnero = obtener_numero_turno(categoria_elegida)

# almacenamos el turno por categoria
turno_final = NumeroDelTurno(categoria_elegida)

# tenemos el turno
turno_final.generar_turno()

# con el bucle mantenemos al usuario en una elección de turno
while True:

    eleccion = input('\nDeseas generar otro turno? S/N: ').upper() # guardamos la respuesta del usuario en una variable

    LimpiarPantalla() # llamamos  la clase de limpiar la pantalla

    # verificamos la respusta del usuario
    while eleccion not in ['N', 'S']:

        print('\nNo has elegido correctamente, intenta de nuevo')

        eleccion = input('\nDeseas generar otro turno? S/N: ').upper()

        LimpiarPantalla()

    # condicionamos la respuesta del usuario
    if eleccion == 'S':

        generar_nuevo_turno()

    elif eleccion == 'N':

        eleccion1 = input('\nDeseas ver la estadistica del dia? S/N: ').upper()

        while eleccion1 not in ['N', 'S']:

            print('\nNo has elegido correctamente, intenta de nuevo')

            eleccion1 = input('\nDeseas ver la estadistica del dia? S/N: ').upper()

        if eleccion1 == 'S':

            print('Los resultados del dia ', datetime.now().strftime('%A, %d de %B de %Y'),'son:')

            # Crear un diccionario para contar las categorías
            contador_categorias = {}
                    
            # en este bucle almacenamos cada recorrido en dos variables de las dos listas inidas con el zip
            for categoria, turno in zip(NumeroDelTurno.categorias_dia, NumeroDelTurno.turnos_del_dia):

                resultado = f'{categoria}{turno}' # guardamos cada recorrido en una variable

                contador_categorias[categoria] = contador_categorias.get(categoria, 0) + 1 # incrementamos en el indice cuando la categoria ya existe por defecto estan en 0

            # en este bucle almacenamos cada recorrido en dos variables los valores del diccionario
            for categoria, cantidad in contador_categorias.items():

                # condicionamos los resultados del bucle
                if 'F - ' in categoria:

                    print('Farmacia : ', cantidad)

                elif 'C - ' in categoria:

                    print('Cosmeticos : ', cantidad)

                elif 'P - ' in categoria:

                    print('Perfumeria : ', cantidad)

        elif eleccion1 == 'N':

            eleccion2 = input('\nDeseas salir del sistema? S/N: ').upper() # la opcion para salir del sistema

            # validamos la respuesta del usuario
            while eleccion2 not in ['N', 'S']:

                print('\nNo has elegido correctamente, intenta de nuevo') # informamos al usuario

                eleccion2 = input('\nDeseas salir del sistema? S/N: ').upper() # la opcion para salir del sistema

            if eleccion2 == 'S':

                print('\nHas salido del sistema, Hasta Pronto!') # informamos al usuario

                exit() # para salir del sistema
