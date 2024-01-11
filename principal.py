"""
Este módulo se encarga de generar el turno para que el usuario lo imprima
y de genrerar el nuevo turno o salir del sistema
"""

# importamos el modulo numeros con todas las funcionalidades que tiene
from numeros import *

# esta clase de encarga de generar el turno para imprimir
class NumeroDelTurno:

    # almacenamos en una variable el indice que se genera por cada codigo de cada categoria
    generadores_por_categoria = {}

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

    eleccion = input('\nDeseas generar otro turno?, si eliges \033[3m\033[1mN\033[0m saldras del sistema S/N: ').upper()

    while eleccion not in ['N', 'S']:

        print('\nNo has elegido correctamente, intenta de nuevo')

        eleccion = input('\nDeseas generar otro turno?, si eliges \033[3m\033[1mN\033[0m saldras del sistema S/N: ').upper()

    if eleccion == 'S':

        generar_nuevo_turno()

    elif eleccion == 'N':

        print('\nHas salido del sistema, Hasta Pronto!')

        exit()
