import random

#pessoas = {'anna':'anna.claudia@gmail.com','werneck':'rafaelwerneck25@gmail.com','fernando':'oi','luiz':'oi2','rafael ribeiro':'oi3','claudson':'oi4','julia':'oi_perdi_a_conta'}

pessoas ={'anna':'anna.claudia@gmail.com','werneck':'rafaelwerneck25@gmail.com','fernando':'oi'}

sorteados = []
azarados = pessoas.keys()[:]

def sorteio():
   presenteador = ''
   presenteado = ''
   
   possiveisPresenteadores = pessoas.keys()[:]
   possiveisPresenteados = pessoas.keys()[:]
   for presenteador in pessoas.keys():
      possiveisPresenteadores.remove(presenteador)
      presenteado = random.choice(possiveisPresenteados)
      
      if(len(possiveisPresenteados) != 1):
         while ((presenteador == presenteado) or (presenteado in sorteados)):
            presenteado = random.choice(pessoas.keys())
      else:
         if(presenteador == possiveisPresenteados[0]):
            print 'fuuuuuuuu'
            return 1
      possiveisPresenteados.remove(presenteado)   
            
      
      sorteados.append(presenteado)
      print presenteador + ' -> '+ presenteado + '\n'
   return 0
       



while(sorteio()):
   pass





