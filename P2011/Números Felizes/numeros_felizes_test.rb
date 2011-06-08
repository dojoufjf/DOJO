require 'test/unit'
require 'set'
class NumerosFelizesTest < Test::Unit::TestCase

  def test_truth
    assert true
  end
  
  def test_um_eh_feliz
    assert_equal 'feliz', NumeroFeliz.new(1).is_feliz
  end
  
  def test_zero_eh_infeliz
    assert_equal 'infeliz', NumeroFeliz.new(0).is_feliz
  end
  
  def test_dez_eh_feliz
    assert_equal 'feliz', NumeroFeliz.new(10).is_feliz
  end
  
  def test_cem_eh_feliz
    assert_equal "feliz", NumeroFeliz.new(100).is_feliz
  end
  
  def test_vinte_eh_infeliz
    assert_equal "infeliz", NumeroFeliz.new(20).is_feliz
  end
  
  def test_nove_eh_infeliz
    assert_equal "infeliz", NumeroFeliz.new(9).is_feliz
  end
  
  def test_sete_eh_feliz
    assert_equal "feliz", NumeroFeliz.new(7).is_feliz
  end
  
  def test_49_eh_feliz
    assert_equal 'feliz', NumeroFeliz.new(49).is_feliz
  end
  
  def test_5_eh_infeliz
    assert_equal "infeliz", NumeroFeliz.new(5).is_feliz
  end
  
  def test_89_eh_infeliz
    assert_equal "infeliz", NumeroFeliz.new(89).is_feliz
  end
end

class NumeroFeliz
  def initialize(n)
    @n = n
  end
  
  def is_feliz
    a = Set.new
    
    while true
      return 'feliz' if @n == 1
      return 'infeliz' if a.include? @n
      a << @n
    
      soma = 0
      @n.to_s.each_char do |caracter|
        soma += (caracter.to_i ** 2)
      end
      
      @n = soma
    end
  end
end