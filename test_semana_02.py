'''

@file   test_semana_02.py
@autor  Luciano E. Rielo
@date   09-May-2025
@brief  Testing for semana_02.py's methods
@note   This file is part of the MIA_PSI_Rielo package.
@note   Copyright (C) 2025 Luciano E. Rielo

'''

import unittest
from semana_02 import invertir_lista, collatz, contar_definiciones, cantidad_de_claves_letra, propagar

class TestSemana02(unittest.TestCase):
    def test_invertir_lista(self):
        self.assertEqual(invertir_lista([1,2,3,4,5]), [5,4,3,2,1])
        self.assertEqual(invertir_lista([]), [])
        self.assertEqual(invertir_lista([1]), [1])
        self.assertEqual(invertir_lista([0]),[0])
        self.assertEqual(invertir_lista([1,5,10]), [10,5,1])

    def test_def_collatz(self):
        self.assertEqual(collatz(1), 0)
        self.assertEqual(collatz(2), 1)
        self.assertEqual(collatz(3), 7)
        self.assertEqual(collatz(4), 2)
        self.assertEqual(collatz(5), 5)
        self.assertEqual(collatz(6), 8)
        self.assertEqual(collatz(10), 6)

    def test_contar_definiciones(self):
        self.assertEqual(contar_definiciones(
            {'a':[1,2,3], 'b':[1,2,3,4,5]}), {'a':3, 'b':5})
        self.assertEqual(contar_definiciones(
            {'a':[0,0,0], 'b':[1,1,1]}), {'a':3, 'b':3})
        self.assertEqual(contar_definiciones(
            {'a':['a','b','c'], 'b':['str', 'test', 'contar']}), {'a':3, 'b':3})

    def test_cantidad_de_claves_letra(self):
        self.assertEqual(
            cantidad_de_claves_letra({'Test':1},'T'),1)
        self.assertNotEqual(
            cantidad_de_claves_letra({'Test':1},'t'),1)
        self.assertEqual(
            cantidad_de_claves_letra({'Test 1':1,'Test 2':1,'test':1},'T'),2)

    def test_propagar(self):
        self.assertEqual(
            propagar([0,0,0,0,0,0,0]), [0,0,0,0,0,0,0])
        self.assertEqual(
            propagar([-1,-1,-1,-1,-1]), [-1,-1,-1,-1,-1])
        self.assertEqual(
            propagar([1,1,1,1,1]), [1,1,1,1,1])
        self.assertEqual(
            propagar([1,0,0,0,0,0,0]), [1,1,1,1,1,1,1])
        self.assertEqual(
            propagar([0,0,0,1,0,0,0]), [1,1,1,1,1,1,1])
        self.assertEqual(
            propagar([0,0,0,-1,0,0,1]), [0,0,0,-1,1,1,1])
        self.assertEqual(
            propagar([1,0,0,-1,0,0,0]), [1,1,1,-1,0,0,0])
        self.assertEqual(
            propagar([0,0,-1,0,0,1,0,0,-1,0,0]), [0,0,-1,1,1,1,1,1,-1,0,0])
        self.assertEqual(
            propagar([0]), [0])
        self.assertEqual(
            propagar([1]), [1])
        self.assertEqual(
            propagar([-1]), [-1])

if __name__ == "__main__":
    unittest.main()