
public class VovoVitoria {

	/*public static Object depositos(int num_depositos, int deposito1, int deposito2) {
		return deposito1-deposito2;
		
	}*/
	
	public static int[] depositos(int num_depositos, int[] deposito1, int[] deposito2) {
		int resultado[] = new int[num_depositos];
		
		
		resultado[0] = deposito1[0] - deposito2[0];
		for(int i = 1; i < num_depositos; i++) {
			resultado[i] = resultado[i-1] + deposito1[i] - deposito2[i];
		}
		
		return resultado;
	}

}
