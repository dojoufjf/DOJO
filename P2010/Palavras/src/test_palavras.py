# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest
import math

dicionario = {'a':1,'b':2, 'c':3, 'd':4}

def parImpar(string):

    acumulador = 0
    for letra in string[:]:
        acumulador += dicionario[letra]
    if ((acumulador % 2) == 0):
        return "par"
    return "impar"

def primo(string):
    acumulador = 0
    for letra in string[:]:
        acumulador += dicionario[letra]

    for i in range(2, math.sqrt(acumulador)+1):
        if (acumulador % i == 0):
            return "nao-primo"
    return "primo"

    #if (acumulador == 2):
     #   return "primo"
    #return "nao-primo"


class  Test_palavrasTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = Test_palavras()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

   

    def test_palavra_par(self):
        self.assertEqual("par",parImpar("b"))

    def test_palavra_impar(self):
        self.assertEqual("impar", parImpar("a"))

    def test_nova_palavra_impar(self):
        self.assertEqual("impar", parImpar("c"))
    def test_d_palavra_par(self):
        self.assertEqual("par",parImpar("d"))
    def test_duas_letras_par(self):
        self.assertEqual("par",parImpar("aa"))

    def test_varias_letras_impar(self):
        self.assertEqual("impar",parImpar("bbbbbbbbbbba"))

    def test_letra_prima(self):
        self.assertEqual("primo", primo("b"))

    def test_letras_primas(self):
        self.assertEqual("primo", primo("abbb"))

    def test_letras_nao_primas(self):
        self.assertEqual("nao-primo",primo("abba"))

if __name__ == '__main__':
    unittest.main()

