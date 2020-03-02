from .contacto import Contacto
from .cita import Cita

class Model:
    def __init__(self):
        self.contactos = []
        self.citas = []

    def esta_id(self, id_contacto):
        for c in self.contactos:
            if c.id_contacto == id_contacto:
                return True, c
        return False, 0
    def esta_cita_id(self, id_cita):
        for d in self.citas:
            if d.id_cita == id_cita:
                return True, d
        return False, 0        

    #Contacto methods
    def agregar_contacto(self, id_contacto='', nombre='', tel='', correo='', _dir=''):
        if not self.esta_id(id_contacto)[0]:
            c = Contacto(id_contacto, nombre, tel, correo, _dir)
            self.contactos.append(c)
            return True, c
        return False, c

    def leer_contacto(self, id_contacto):
        e,c = self.esta_id(id_contacto)
        return e, c
    
    def leer_todos_contactos(self):
        lis = []
        for c in self.contactos:
            lis.append(c)
        return lis

    def actualizar_contacto(self, id_contacto, n_nombre, n_tel, n_correo, n_dir):
        e,c = self.esta_id(id_contacto)
        if e:
            if not n_nombre == '':
                c.nombre =  n_nombre
            if not n_tel == '':
                c.tel = n_tel
            if not n_correo == '':
                c.correo = n_correo
            if not n_nombre == '':
                c._dir = n_dir
            return True
        return False
    
    def borrar_contacto(self, id_contacto):
        e,contacto = self.esta_id(id_contacto)
        if e:
            self.contactos.remove(contacto)
            lista_temp = [c for c in self.citas if c.id_contacto == id_contacto]            
            for c in lista_temp:
                    self.citas.remove(c)
            return True, contacto
        return False, contacto

    def encontrar_personas(self, car):
        lis = []
        for c in self.contactos:
            if c.nombre[0].lower() == car.lower():
                lis.append(c)
        return lis

    #Cita methods
    
    def agregar_cita(self, id_cita='', id_contacto='', lugar='', fecha='', hora='', asunto=''):
        e,d = self.esta_id(id_contacto)
        if e:
            if not self.esta_cita_id(id_cita)[0]:
                d = Cita(id_cita, id_contacto, lugar, fecha, hora, asunto)
                self.citas.append(d)
                return True, d
        return False, d
    def leer_cita(self, id_cita):
        e,d = self.esta_cita_id(id_cita)
        return e, d
    def leer_todas_citas(self):
        lis = []
        for c in self.citas:
            lis.append(c)
        return lis
    def actualizar_cita(self, id_cita, id_contacto, lugar, fecha, hora, asunto):
        e,d = self.esta_cita_id(id_cita)
        if e:
            if not id_contacto == '':
                d.id_contacto = id_contacto
            if not lugar == '':
                d.lugar = lugar
            if not fecha == '':
                d.fecha = fecha
            if not hora == '':
                d.hora = hora
            if not asunto == '': 
                d.asunto = asunto
            return True, d
        return False, d
    def eliminar_cita(self, id_cita):
        e,d = self.esta_cita_id(id_cita)
        if e:
            self.citas.remove(d)
            return True
        return False
    def encontrar_fechas(self, date):
        lis = [c for c in self.citas if c.fecha == date]
        """ 
        lis = []
            for d in self.citas:
                if d.fecha == date:
                    lis.append(d)
                    """
        return lis