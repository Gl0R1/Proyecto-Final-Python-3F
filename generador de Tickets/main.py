import pickle, sys, os, random

#creo la variable archivo_tickets donde se guardarán los datos de los tickets utilizando pickle. 
#tickets.pkl para guardar datos en un archivo y recuperarlos más tarde
archivo_tickets = 'tickets.pkl'

#limpiador de pantlla para win y linux
def limpiarPantalla():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')
        
#funcion para mostrar el menu de inicio
def mostrarMenu():
    print("\n================================================")
    print("   Hola!  Bienvenido al sistema de Tickets ")
    print("================================================")
    print("1 - Generar un Nuevo Ticket")
    print("2 - Leer Un ticket")
    print("3 - Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

#creo la funcion para generar un nuevo ticket y creo un diccionario para almacenar los datos 
#ingresado, uso la funcion random para reibir un numero aleatorio luego guardo el ticket y lo imprimo x pantalla
def altaTicket():
    limpiarPantalla()
    print("\nIngrese los datos para Generar un Nuevo Ticket")
    nombre = input("Nombre: ")
    sector = input("Sector: ")
    asunto = input("Asunto: ")
    mensaje = input("Mensaje: ")

    ticket_numero = random.randrange(1000, 9999)
    ticket = {
        'numero': ticket_numero,
        'nombre': nombre,
        'sector': sector,
        'asunto': asunto,
        'mensaje': mensaje
    }

    guardarTicket(ticket)
    limpiarPantalla()
    print("\n================================================")
    print("        Se generó el siguiente Ticket ")
    print("================================================")
    print(f"Su nombre: {nombre}    N° Ticket: {ticket_numero}")
    print(f"Sector: {sector}")
    print(f"Asunto: {asunto}")
    print(f"Mensaje: {mensaje}")
    print("\n      Recordar su número de ticket")
    
    
#creo las funciones para cargar y guardar un ticket
def guardarTicket(ticket):
    tickets = cargarTicket()
    tickets.append(ticket)
    with open(archivo_tickets, "wb") as f:
        pickle.dump(tickets, f)
        
        

def cargarTicket():
    if os.path.isfile(archivo_tickets):
        with open(archivo_tickets, "rb") as f:
            tickets = pickle.load(f)
    else:
        tickets = []
    return tickets


#creo la funcion para leer un ticket
def leerTicket():
    try:
        numero_ticket = int(input("Ingrese el número de ticket: "))
    except ValueError:
        print("Ingrese un número de ticket válido.")
        return

    tickets = cargarTicket()

    for ticket in tickets:
        limpiarPantalla()
        if ticket['numero'] == numero_ticket:
            print("\n=================================================")
            print("            Ticket Encontrado ")
            print("=================================================")
            print(f"Nombre: {ticket['nombre']}        N° Ticket: {ticket['numero']}")
            print(f"Sector: {ticket['sector']}")
            print(f"Asunto: {ticket['asunto']}")
            print(f"Mensaje: {ticket['mensaje']}\n")
            break
    else:
        print(f"No se encontró un ticket con el número: {numero_ticket}")
        
        
#creo la funcion para salir del programa
def confirmarSalida():
    confirmacion = input("¿Está seguro que desea salir? (s/n): ")
    if confirmacion.lower() == 's':
        print("Saliendo del programa.")
        sys.exit()
    else:
        print("Regresando al menú principal.")
        
        
        
        
#creo la funcion principal 
def main():
    while True:
        opcion = mostrarMenu()
        if opcion == '1':
            while True:
                altaTicket()
                continuar = input("\n¿Desea Generar un nuevo ticket? (s/n): ")
                if continuar.lower() != 's':
                    break
        elif opcion == '2':
            while True:
                leerTicket()
                continuar = input("¿Desea leer otro ticket? (s/n): ")
                if continuar.lower() != 's':
                    break
        elif opcion == '3':
            confirmarSalida()
        else:
            print("Opción no válida. Por favor, intente nuevamente.")


main()