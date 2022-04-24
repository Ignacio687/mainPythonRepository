import unittest     
from persona import Persona

class Test_Persona(unittest.TestCase):
    def test_persona(self):
        persona = Persona()
        print(persona)
        persona = Persona()
        print(persona)
        self.assertEqual(persona.__dict__, {"dni":1, "apellido":"Fernandez", "nombre":"Alberto"})

if __name__=="__main__":
    unittest.main()