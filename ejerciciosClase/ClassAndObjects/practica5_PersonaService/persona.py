class Persona:
    def __init__(self, documento = 1, apellido = 'Torvalds', nombre = 'Linus'):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre

    def __repr__(self):
        return f'Persona: {self.documento} - {self.apellido}, {self.nombre}'

    def input(self):
        self.documento = int(input('Ingrese documento: '))
        self.apellido = input('Ingrese apellido: ')
        self.nombre = input('Ingrese nombre: ')