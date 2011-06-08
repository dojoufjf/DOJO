/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package dojo8411;


/**
 *
 * @author Akio
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {



    }

    public static String extenso(int num)
    {


        String unidade[] = new String[20];
        unidade[0] = "zero";
        unidade[1] =  "um";
        unidade[2] = "dois";
        unidade[3] = "tres";
        unidade[4] = "quatro";
        unidade[5] = "cinco";
        unidade[6] = "seis";
        unidade[7] = "sete";
        unidade[8] = "oito";
        unidade[9] = "nove";
        unidade[10] = "dez";
        unidade[11] =  "onze";
        unidade[12] = "doze";
        unidade[13] = "treze";
        unidade[14] = "quatorze";
        unidade[15] = "quinze";
        unidade[16] = "dezesseis";
        unidade[17] = "dezessete";
        unidade[18] = "dezoito";
        unidade[19] = "dezenove";
        

        String dezena[] = new String[8];
        dezena[0] = "vinte";
        dezena[1] = "trinta";
        dezena[2] = "quarenta";
        dezena[3] = "cinquenta";
        dezena[4] = "sessenta";
        dezena[5] = "setenta";
        dezena[6] = "oitenta";
        dezena[7] = "noventa";

        String centena[] = new String[9];
        centena[0] = "cento";
        centena[1] = "duzentos";

        if(num == 100)
            return "cem";
        else
        {
            if(num > 100)
            {
                if(num %100 == 0 )
                    return centena[num/100 - 1];
                else
                    return centena[num/100 - 1] + " e " +
            }
        }


        if(num>19 && num%10 == 0)
        {
            return dezena[num/10 - 2];
        }

        if(num>19 && num<100)
            return dezena[num/10 - 2] + " e " + extenso(num%10);
        
        return unidade[num];
    }

}
