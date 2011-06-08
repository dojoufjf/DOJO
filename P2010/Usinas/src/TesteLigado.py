# To change this template, choose Tools | Templates
# and open the template in the editor.

import unittest

class Ligacao():
    def testa(self,estacoes,ligacoes,pares):
        alcancados = Array()
        for i in range(1,estacoes):
           # visitados[i] = 0
            alcancados[i] = 0

        alguem_foi_alcancado = 1
        estacao_atual = 1
        for i in range(1,estacoes):
            for j in range(1,ligacoes):
                if(pares[j][0]==i):
                    alcancados[pares[j][1]]=1
                if(pares[j][1]==i):
                    alcancados[pares[j][0]]=1
        for i in range(1,estacoes):
            if(alcancados[i]==0):
                return 'falha'

        return 'normal'

        #while (alguem_foi_alcancado == 1):
#        #for(j= 0 ; j < estacoes; j++)
#            for (i = 0; i < ligacoes; i++):
#                if (pares[i][0] == estacao_atual):
#                    if(alcancados[pares[i][1]]==0):
#                        alcancados[pares[i][1]]=1
#                        estacao_atual=pares[i][1]
#                if (pares[i][1] == estacao_atual):
#                    if(alcancados[pares[i][0]]==0):
#                        alcancados[pares[i][0]]=1
#                        estacao_atual=pares[i][0]




#            alguem_foi_alcancado = 0
#            for (i = 0; i < ligacoes; i++):
#                if (pares[i][0] == estacao_atual):
#                    #pares[i][1] se liga com estacao_atual
#                    if (alcancado[pares[i][1]] == 0):
#                        alcancado[pares[i][1]] = 1
#                if (pares[i][1] == estacao_atual):
      

   




class TesteLigadoTestCase(unittest.TestCase):
    #def setUp(self):
    #    self.foo = TesteLigado()
    #

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

#    def test_testeLigado(self):
#        #assert x != y;
#        #self.assertEqual(x, y, "Msg");
#        self.fail("TODO: Write test")
#
    def test_trese_tresl(self):
        self.assertEqual("normal", Ligacao().testa(3,3,[[1,2],[2,3],[1,3]]))

    def test_trese_duasl(self):
        self.assertEqual('normal', Ligacao().testa(3,2,[[1,2],[2,3]]))
    
    def test_quatroe_trel_falha(self):
        self.assertEqual('falha', Ligacao().testa(4,3,[[1,2],[2,3],[3,1]]))

    def test_quatroe_tresl_normal(self):
        self.assertEqual('normal', Ligacao().testa(4,3,[[1,2],[1,3],[2,4]]))


if __name__ == '__main__':
    unittest.main()

