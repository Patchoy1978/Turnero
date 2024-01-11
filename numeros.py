"""
Este código se encarga de generar la categoria y los números
para el turnero, en primera instancia esta diseñado para una farmacia, se 
podra implementar en algo más si se desea

"""
# importamos librerias que necesitamos
import os
import platform

# creamos la clase para limpiar la pantalla
class LimpiarPantalla:

    #creamos el constructor
    def __init__(self):

        # en una variable almacenamos el SO en el que se esta trabajando
        sistema_operativo = platform.system()

        # realizamos la validacion de que SO es y realizamos la limpieza de la pantalla
        if sistema_operativo == 'Windows':

            os.system('cls')

        else:

            os.system('clear')

# en esta funcion creamos los numeros del turno
def numeros_turno(categoria):

    # inicamos una variable en cero
    i = 000

    # creamos el bucle para que me genere el codigo del turno 
    while True:

        # usamos el yield  para nuestro generador
        yield f'{categoria[:3]}{i:03d}'

        # vamos incrementando la variable
        i += 1

        # creamos un condicional para mantener el turnero solo hasta 100
        if i > 100:

            i = 000

# en esta funcion obtenemos el turno para cada categoria
def obtener_numero_turno(categoria):

    # almacenamos el generador en una variable
    generador = numeros_turno(categoria)

    # retornamos el generador
    return next(generador)

# en esta clase definimos el mensaje de bienvenida para el menu
def menu_ppal(funcion):

    """
    esta función es un decorador

    """

    # definimos la funcion interna que es el mensaje decorador
    def interior():

        print(f'\n\033[3m\033[1mBienvenido\033[0m\033[0m\n\nElige una opción del siguiente \033[1mMenú\033[0m\n')
        return funcion()

    return interior

# en esta clase definimos el mensaje para el turno generado
def mostrar_informacion_turno(funcion):

    """
    esta función es un decorador
    
    """

    # este es el mensaje del turno 
    def interna(self, *args, **kwargs):

        print(f'\033[1m{'Farmacias Python'.center(40)}\033[0m\n\033[1m{'Bienvenido'.center(40)}\033[0m\n{'Su truno es:'.center(40)}\n')
        resultado = funcion(self, *args, **kwargs)
        print(f'\033[1m{'Pronto será Atendido!'.center(42)}\033[0m\n\033[1m')
        return resultado

    return interna

# ponemos el decorador a la categoria
@menu_ppal
# esta función se encarga de mostrar las categorias al usuario
def categorias():

    # se almacena en una variabke la lista de las categorias
    usuario = ['Farmacia', 'Cosmeticos', 'Perfumeria']

    # creamos el bucle para la elección del usuario
    while True:

        # con el bucle imprimimos el menú para el usuario
        for i,r in enumerate(usuario, start=1):

            print (f'{i} = {r}')
            
        # manejamos la elección dentro de un try - except
        try:

            opcion = input('\nElige una opcion: ')

            # llamamos la clase de limpiar pantalla
            LimpiarPantalla()

            # eñ condicional para las opciones
            if opcion == '1':

                eleccion = 'Farmacia'
                
            elif opcion == '2':

                eleccion = 'Cosmeticos'

            elif opcion == '3':

                eleccion = 'Perfumeria'

            return eleccion

        except:

            print('\nHas elegido un número inválido, intenta de nuevo\n')
            
            continue

# for s in range(105):

#     print(next(t))
