import unittest     
from persona import Persona
from unittest.mock import patch

class PersonaTestCase(unittest.TestCase):
    def test_persona(self):
        persona = Persona()
        self.assertEqual(persona.__dict__, {"dni":1, "apellido":"Fernandez", "nombre":"Alberto"})

    @patch('bultins.input', side_effects = [3, 'Fernandez', 'Alberto'])
    def test_input(self):
        persona = Persona()
        persona.input()
        self.assertEqual(persona.__dict__, {'dni': 3, 'apellido': 'Fernandez', 'nombre': 'Alberto'})


if __name__=="__main__":
    unittest.main()