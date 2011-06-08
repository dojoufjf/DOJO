import java.lang.reflect.Array;

import junit.framework.TestCase;

import org.junit.Assert;
import org.junit.Test;

public class TesteVovoVitoria extends TestCase {



	@Test
	public void testa_dois_depositos_iguais() {
		Assert.assertArrayEquals(new int[]{0,0},
				VovoVitoria.depositos(2, new int[]{3,8}, new int[]{3,8}));
	}
	
	@Test
	public void testaDoisDepositosDiferentes() {
		Assert.assertArrayEquals(new int[]{1,2}, 
				VovoVitoria.depositos(2, new int[]{3,8}, new int[]{2,7}));
	}
	
	@Test
	public void testa3DepositosDiferentes() {
		Assert.assertArrayEquals(new int[]{-5,0,0}, 
				VovoVitoria.depositos(3, new int[]{20,10,10}, new int[]{25,5,10}));
	}
	
	@Test
	public void testa4DepositosDiferentes() {
		Assert.assertArrayEquals(new int[]{-5,7,-13,3}, 
				VovoVitoria.depositos(4, new int[]{0,12,0,17}, new int[]{5,0,20,1}));
	}
	@Test
	public void testa1DepositoDiferente() {
		Assert.assertArrayEquals(new int[]{16}, 
				VovoVitoria.depositos(1, new int[]{17}, new int[]{1}));
	}
}