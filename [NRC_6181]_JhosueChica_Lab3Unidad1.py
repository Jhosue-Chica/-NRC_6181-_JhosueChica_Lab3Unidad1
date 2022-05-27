from ast import IfExp
from datetime import datetime
from http import client
from pydoc import cli

# DEFINIR UNA CLASE CLIENTE (METODO __init__)
class Cliente():
    def __init__(self, nombre, telefono, estado):
        self.nombre=str(nombre)
        self.telefono=str(telefono)
        self.estado=int(estado)
    
    def RegistrarCuenta(self, nombre, telefono):
        nombre = str(input("Ingrese el nombre del cliente: "))
        telefono = str(input("Ingrese el telefono del cliente: "))
        self.usuario1=nombre+str(telefono[2:])
        self.clave1= nombre+telefono[:4]
        print("Sr/Sra. ",cliente1.nombre," su usuario y contraseña son ",self.usuario1," y ",self.clave1)

    def IniciarSesion(self, usuarioIniciar):
        self.usuarioIniciar=str(input("Ingrese un usuario: "))
        while(usuarioIniciar==self.usuario1):
            print("Valor incorrecto. ")
            usuarioIniciar = int(input("Ingrese el usuario del cliente: "))
        
    def RegistrarTienda(self, tienda):
        self.nombreTienda = str(input("Ingrese el nombre de la tienda: "))
        self.telefonoTienda = str(input("Ingrese el telefono de la tienda: "))
        self.gerente = str(input("Ingrese el gerente de la tienda: "))
        self.estadoTienda = int(input("Ingrese el estado de la tienda: "))
        self.fechaRegistro=datetime.today().strftime('%A, %B %d, %Y')
        self.horaRegistro=datetime.today().strftime('%H-%M:%S')
        if self.nombreTienda == tienda:
            print("Se ha registrado la tienda ",tienda," en la fecha ",self.fechaRegistro," y hora",self.horaRegistro)
        else:
            print("no se ha registrado")

    def HistoriaVisitasTienda(self,tienda, fechaRegistro, horaRegistro):
        print("Historial de Visitas en tienda: ")
        print("Tienda: ",tienda)
        print("Fecha: ",fechaRegistro)
        print("Hora: ",horaRegistro)

    def MostrarEstado(self, nombre, telefono, estado):
        ''' i. Normal: el cliente es normal (es decir, sin COVID-19).
            ii. Caso: El cliente es un caso de COVID-19 positivo.
            iii. Cercano: el cliente es un contacto cercano de un caso.
        '''
        print("Nombre: ",nombre,", Telefono: ",telefono,", Estado: ",estado)
        if estado==1:
            print("Estado i. Normal")
        elif estado==2:
            print("Estado ii. Caso")
        elif estado==3:
            print("Estado iii. Cercano")

# DEFINIR UNA CLASE TIENDA
class Tienda():
    
    def __init__(self, nombreTienda, telefonoTienda, gerente, estadoTienda):
        self.nombre=nombreTienda
        self.telefono=telefonoTienda
        self.gerente=gerente
        self.estadoTienda=estadoTienda


# DEFINIR UNA CLASE ADMIN
class Admin():
    def mostrarDatosCliente():
        print("funcionEstado")

    def mostrarEstadoTienda(self, nombreTienda, telefonoTienda, estadoTienda):
        ''' i. Normal: el cliente es normal (es decir, sin COVID-19).
            ii. Caso: El cliente es un caso de COVID-19 positivo.
        '''
        print("Nombre de tienda: ",nombreTienda,", Telefono: ",telefonoTienda,", Estdo: ",estadoTienda)
        if estadoTienda==1:
            print("Estado i. Normal")
        elif estadoTienda==2:
            print("Estado ii. Caso")

    def cambiarEstadoCliente(self, nombre, estado):
        self.cambioEstado =input("Actualizar estado del cliente ",nombre,": si o no")
        if self.cambioEstado == "si":
            self.estado=2
            print("Se cambio el estado a caso")
        else:
            print("No se realizo un cambio")

    def cambiarEstadoTienda(self, nombreTienda, estado, estadoTienda):
        self.cambioEstado =input("Actualizar estado del cliente ",nombreTienda,": si o no")
        if self.cambioEstado == "si":
            self.estadoTienda=2
            self.estado=3
            print("Se cambio el estado de la tienda a Caso y el del cliente a Cercano")
        else:
            print("No se realizo un cambio")

while(True):
    cliente1=Cliente("nombre","telefono","estado")
    tienda1=Tienda("nombre","telefono","gerente","estado")
    listaCliente=list()
    print("\n||             MENU DE OPCIONES           ||")
    print("1. Ingrese un Nuevo Cliente")
    print("2. Iniciar sesión en el sistema")
    print("3. Salir")
    opcion= int(input("\nIngrese la opcion que desea realizar: "))
    if (opcion==1):
        cliente1.RegistrarCuenta(cliente1.nombre,cliente1.telefono)
        listaCliente.append(str(cliente1.usuario1))
        print(listaCliente)
    elif (opcion==2):
        cliente1.IniciarSesion(cliente1.usuario1)
        while(True):
            print("\n||                MENU DE OPCIONES              ||")
            print("1. Registrarse en una tienda")
            print("2. Ver el historial de las tiendas que visitó")
            print("3. Ver su estado")
            print("4. Salir de Sesion")
            opcion= int(input("\nIngrese la opcion que desea realizar: "))
            if (opcion==1):
                cliente1.RegistrarTienda(tienda1.nombre)
            elif (opcion==2):
                cliente1.HistoriaVisitasTienda(cliente1.nombreTienda, cliente1.fechaRegistro, cliente1.horaRegistro)
            elif (opcion==3):
                cliente1.MostrarEstado(cliente1.nombre, cliente1.telefono, cliente1.estado)
            elif (opcion==4):
                print("\n Volviendo al menu principal...")
            else:
                print("\n Opcion no valida")
            if(opcion==4):
                break
    elif (opcion==3):
        print("\n Gracias por visitarnos :)")
    else:
        print("\n Opcion no valida")
    if(opcion==3):
        break


