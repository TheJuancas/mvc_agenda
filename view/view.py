class View:
    #Metodos contacto
    def mostrar_contacto(self,contacto):
        print('******* Datos del contacto *******')
        print('Nombre: ',contacto.nombre)
        print('Telefono: ', contacto.tel)
        print('Correo: ', contacto.correo)
        print('Direccion: ', contacto.dir)
        print('**********************************')

    def mostrar_contactos(self, contactos):
        print('************ Contactos ************')
        for c in contactos:
            print(c.nombre,c.tel,c.correo,c.dir)
        print('***********************************')

    def agregar_contacto(self, contacto):
        print('El contacto',contacto.nombre,'se a agregado a la base de datos.')        

    def borrar_contacto(self, contacto):
        print('El contacto',contacto.nombre,'se a borrado a la base de datos.')
    
    def actualizar_contacto(self, id_contacto):
        print('El contacto',id_contacto,'se ma modificado correctamente.')

    def contacto_ya_existe(self, contacto):
        print('El contacto', contacto.id_contacto,'YA EXISTE EN LA BASE DE DATOS.')

    def contacto_no_existe(self, id_contacto):
        print('El contacto',id_contacto,'NO EXISTE EN LA BASE DE DATOS.')
    
    
    #Metodos de Cita
    def mostrar_cita(self, cita):
        print('******** Datos de la cita ********')
        print('Contacto: ',cita.id_contacto)
        print('Lugar: ', cita.lugar)
        print('Fecha: ', cita.fecha)
        print('Hora: ', cita.hora)
        print('Asunto: ', cita.asunto)
        print('**********************************')
    def mostrar_citas(self, citas):
        print('************** Citas **************')
        for c in citas:
            print(c.id_contacto,c.lugar,c.fecha,c.hora,c.asunto)
        print('***********************************')
    def agregar_cita(self, cita):
        print('La cita',cita.id_cita,'se a agregado a la base de datos.')        

    def borrar_cita(self, id_cita):
        print('La cita',id_cita,'se a borrado a la base de datos.')
    
    def actualizar_cita(self, id_cita):
        print('La cita',id_cita,'se ma modificado correctamente.')

    def cita_ya_existe(self, cita):
        print('La cita',cita.id_cita,'YA EXISTE EN LA BASE DE DATOS.')

    def cita_no_existe(self, id_cita):
        print('La cita',id_cita,'NO EXISTE EN LA BASE DE DATOS.')

    #Metodos Generales
    def start(self):
        print('Esto es un ejemplo sencillo de MVC.')
    
    def end(self):
        print('Hasta la vista!')
    def menu(self):
        print('1. Agregar contacto')
        print('2. Leer contacto')
        print('3. Actualizar contacto')
        print('4. Borrar contacto')
        print('5. Agregar cita')
        print('6. Leer cita')
        print('7. Actualizar cita')
        print('8. Borrar Cita')
        print('9. Leer base de datos')
        print('10. Salir')
    def opcion_invalida(self):
        print('Seleccionaste una opcion invalida.')