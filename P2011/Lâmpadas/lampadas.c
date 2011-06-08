#include <stdio.h>
#include <stdlib.h>

int *vetorSolucao;

void verificaLampada(int numIdas, int numLampadas){
  int i, j;
   for(i=0; i<numLampadas; i++)
        vetorSolucao[i]=1;
        for (i = 2; i <= numIdas; i++)
        {
            for (j = (i-1); j < numLampadas; j += i)
            {
                if (vetorSolucao[j] == 0)
                    vetorSolucao[j] = 1;
                else
                    vetorSolucao[j] = 0;
            }
        }
}

void solucao(int solucaoGerada[], int solucaoEsperada[]){
   int i;

   for(i=0; i<10; i++)
    if (solucaoGerada[i] != solucaoEsperada[i])

    {
        printf("solucao esperada diferente da gerada...\n");
        return;
    }
    printf("solucao correta!\n");
}

int main()
{
    vetorSolucao = (int*)malloc(10*sizeof(int));
    verificaLampada(1, 10);
    int vetorResposta[10] = {1,1,1,1,1,1,1,1,1,1};
    solucao(vetorSolucao, vetorResposta);

    verificaLampada(2, 10);
    int vetorResposta2[10] = {1,0,1,0,1,0,1,0,1,0};
    solucao(vetorSolucao, vetorResposta2);

    verificaLampada(3, 10);
    int vetorResposta3[10] = {1,0,0,0,1,1,1,0,0,0};
    solucao(vetorSolucao, vetorResposta3);

    verificaLampada(5, 10);
    int vetorResposta4[10] = {1,0,0,1,0,1,1,1,0,1};
    solucao(vetorSolucao, vetorResposta4);

}
