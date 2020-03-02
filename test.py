from model.contacto import Contacto
from model.cita import Cita
from model.model import Model
from view.view import View
from controller.controller import Controller
"""
contactos = []
c1 = Contacto(1,'Juan Perez', '4625954655','juan@gmail.com', 'Paseo Vergel 1')
c2 = Contacto(2,'Jaime Perez', '4626006682','jaime@gmail.com', 'Paseo Vergel 2')
d = Cita(1, 1, 'DICIS', '20-02-20', '16:00', 'Comer')

contactos.append(c1)
contactos.append(c2)

guess = input('Dame un nombre: ')
for c in contactos:
    if c.nombre.lower== guess.lower:
        print('Ya se encuentra en los contactos.')
        break
else:
    print('No se encuentra en los contactos.')
    """
"""
m = Model()
m.agregar_contacto(1,'Juan Perez', '4625954655','juan@gmail.com', 'Paseo Vergel 1')
m.agregar_contacto(2,'Jaime Perez', '4626006682','jaime@gmail.com', 'Paseo Vergel 2')
m.agregar_cita(1,1, 'DICIS', '20-02-20', '16:00', 'Comer chilaquiles')
m.agregar_cita(2,2, 'DICIS', '20-02-20', '16:00', 'Comer tortas')
m.agregar_cita(3,1, 'DICIS', '20-02-22', '16:00', 'Comer tacos')
v = View()
s = m.leer_todos_contactos()
v.mostrar_contactos(s)
c = m.leer_contacto(1)
v.mostrar_contacto(c)

f, c = m.borrar_contacto(1)
if f:
    v.borrar_contacto(c)
else:
    v.contacto_no_existe(1)
s = m.leer_todos_contactos()
v.mostrar_contactos(s) 
"""
cont = Controller()
cont.start()