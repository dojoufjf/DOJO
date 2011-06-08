import org.junit.Assert;
import org.junit.Test;



public class TesteMiojo {

	@Test
	public void teste_3_3_5()
	{
		Assert.assertEquals(3, Miojo.compara(3,3,5));
	}
	
	@Test
	public void teste_3_5_3()
	{
		Assert.assertEquals(3, Miojo.compara(3, 5, 3));
	}
	
	@Test
	public void teste_4_5_4(){
		Assert.assertEquals(4, Miojo.compara(4, 5, 4));
	}
	
	@Test
	public void test_3_4_7(){
		Assert.assertEquals(7, Miojo.compara(3,4,7));
	}
	@Test
	public void test_3_5_7(){
		Assert.assertEquals(10, Miojo.compara(3,5,7));
	}
	@Test
	public void test_14_15_22(){
		Assert.assertEquals(44, Miojo.compara(14,15,22));
		//Loop Infinito
	}
}
