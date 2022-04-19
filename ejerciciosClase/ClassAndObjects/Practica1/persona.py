class Persona:
    def __init__(self, dni=1, apellido="Fernandez", nombre="Alberto"):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
    def __repr__(self):
        return f"Persona:{self.dni},{self.apellido},{self.nombre}"

persona = Persona()
print(persona)