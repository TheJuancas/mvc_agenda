from model.model import Model
from view.view import View

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    #Contacto controllers
    def agregar_contacto(self, id_contacto, nombre, tel, correo, _dir):
        e,c = self.model.agregar_contacto( id_contacto, nombre, tel, correo, _dir)
        if e:
            self.view.agregar_contacto(c)
        else:
            self.view.contacto_ya_existe(c)
    def leer_contacto(self, id_contacto):
        e,c = self.model.leer_contacto(id_contacto)
        if e:
            self.view.mostrar_contacto(c)
        else:
            self.view.contacto_no_existe(id_contacto)
    def leer_todos_contactos(self):
        c = self.model.leer_todos_contactos()
        self.view.mostrar_contactos(c)
    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e = self.model.actualizar_contacto(id_contacto, n_nombre, n_tel, n_correo, n_dir)
        if e:
            self.view.actualizar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)
    def borrar_contacto(self, id_contacto):
        e, c = self.model.borrar_contacto(id_contacto)
        if e:
            self.view.borrar_contacto(id_contacto)
        else:
            self.view.contacto_no_existe(id_contacto)
    def encontrar_personas(self, letra):
        c = self.model.encontrar_personas(letra)
        self.view.mostrar_contactos(c)
    #Cita controllers
    def agregar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, c = self.model.agregar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.agregar_cita(c)
        else:
            if e == 0:
                self.view.contacto_no_existe(id_contacto)
            else:
                self.view.cita_ya_existe(id_cita)

    def leer_cita(self,id_cita):
        e,d = self.model.leer_cita(id_cita)
        if e:
            self.view.mostrar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def leer_citas(self):
        lis = self.model.leer_todas_citas()
        self.view.mostrar_citas(lis)
    
    def actualizar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e, d = self.model.actualizar_cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
        if e:
            self.view.actualizar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)
    def eliminar_cita(self, id_cita):
        e,d = self.model.eliminar_cita(id_cita)
        if e:
            self.view.borrar_cita(id_cita)
        else:
            self.view.cita_no_existe(id_cita)

    def encontrar_fechas(self, date):
        lis = self.model.encontrar_fechas(date)
        self.view.mostrar_citas(lis)
    #General controllers
    def insertar_contactos(self):
        self.agregar_contacto('1','Juan Perez', '4625954655','juan@gmail.com', 'Paseo Vergel 1')
        self.agregar_contacto('2','Jaime Perez', '4626006682','jaime@gmail.com', 'Paseo Vergel 2')
        self.agregar_contacto('3','Alejando Perez','4628008080','alex@gmail.com','Circuito Comedia')
    def insertar_citas(self):
        self.agregar_cita('1','1', 'DICIS', '20-02-20', '16:00', 'Comer chilaquiles')
        self.agregar_cita('2','2', 'DICIS', '20-02-20', '16:00', 'Comer tortas')
        self.agregar_cita('3','1', 'DICIS', '20-02-22', '16:00', 'Comer tacos')
    def start(self):
        #Dispay welcome message
        self.view.start()
        #Inser data in model
        self.insertar_contactos()
        self.insertar_citas()
        #Show all contacts in DB
        """
        self.leer_todos_contactos()
        self.encontrar_personas('j')
        self.leer_citas()
        self.encontrar_fechas('20-02-20') 
        """
        self.menu()
    def menu(self):
        self.view.menu()
        o = input('Selecciona una opcion (1-10): ')
        while not o=='10':
            if o == '1':
                idc = input('Ingresa id del contacto: ')
                n = input('Ingresa el nombre: ')
                tel = input('Ingresa el telefono: ')
                cor = input('Ingrese el correo: ')
                dire = input('Ingrese la direccion: ')
                self.agregar_contacto(idc, n, tel, cor, dire)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '2':
                idc = input('Ingrese id del contacto: ')
                self.leer_contacto(idc)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '3':
                idc = input('Ingresa id del contacto: ')
                n = input('Ingresa el nombre: ')
                tel = input('Ingresa el telefono: ')
                cor = input('Ingrese el correo: ')
                dire = input('Ingrese la direccion: ')
                self.actualizar_contacto(idc, n, tel, cor, dire)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '4':
                idc = input('Ingresa id del contacto: ')
                self.borrar_contacto(idc)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '5':
                idci = input('Ingresa id de la cita: ')
                idc = input('Ingresa id del contacto: ')
                lu = input('Ingresa el lugar: ')
                fe = input('Ingrese la fecha: ')
                ho = input('Ingrese la hora: ')
                asu = input('Ingresa el asunto: ')
                self.agregar_cita(idci,idc,lu,fe,ho,asu)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '6':
                idci = input('Ingresa id de la cita: ')
                self.leer_cita(idci)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '7':
                idci = input('Ingresa id de la cita: ')
                idc = input('Ingresa id del contacto: ')
                lu = input('Ingresa el lugar: ')
                fe = input('Ingrese la fecha: ')
                ho = input('Ingrese la hora: ')
                asu = input('Ingresa el asunto: ')
                self.actualizar_cita(idci,idc,lu,fe,ho,asu)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '8':
                idci = input('Ingresa id de la cita: ')
                self.eliminar_cita(idci)
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            elif o == '9':
                self.leer_todos_contactos()
                self.leer_citas()
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
                pass
            else:
                self.view.opcion_invalida()
                self.view.menu()
                o = input('Selecciona una opcion (1-10): ')
        