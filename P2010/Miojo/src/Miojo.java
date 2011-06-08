
public class Miojo {

	
	
	
	public static Object compara(int miojo, int ampulheta_1, int ampulheta_2) {
		if (Math.abs(ampulheta_1-ampulheta_2) == miojo)
			return Math.max(ampulheta_1, ampulheta_2);
		if(ampulheta_1==miojo ||ampulheta_2==miojo) return miojo;
		
		int soma = 0;
		int amp1 = ampulheta_1;
		int amp2 = ampulheta_2;
		
		//Solução com erro
		while(Math.abs(amp1-amp2) != miojo){
			if(amp1 == 0) amp1 = ampulheta_1;
			if(amp2 == 0) amp2 = ampulheta_2;
			if(amp1 < amp2){
				soma += amp1;
				amp2 -= amp1;
			}
			else {
				soma += amp2;
				amp1 -= amp2;
			}
		}
		return soma+Math.max(amp1, amp2);
		
		//Solução funciona... qual o erro na refatoração de cima?
	/*	while(true){
			amp1--;
			amp2--;
			soma++;
			if (amp1==0){
				if (amp2 == miojo){
					return soma+miojo;
					
				}else{
					amp1 = ampulheta_1;
				}
			}
			
			if (amp2==0){
				if(amp1==miojo){
					return soma+miojo;
				}else{
					amp2 = ampulheta_2;
				}
			}
			
		}
	
	}*/

}
