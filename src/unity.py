import unittest
from service.registrar_cadastro import registrar_cadastro
from config import config

class TestRegistroCadastro(unittest.TestCase):
    def test_registrar_cadastro(self):
        print("Testando service.registrar_cadastro...")
        self.assertEqual(
            registrar_cadastro({
                                "nome": "teste",
                                "email": "teste",
                                "senha": "teste"
                               }, config), 
                               {
                               "status": 200,
                               "dados":{
                                   "nome": "teste",
                                   "email": "teste",
                                   "senha": "teste"
                               }
                               })

if __name__ == '__main__':
    unittest.main()