from app.calculate import calcular_hipotenusa

def test_calcular_hipotenusa():
    assert calcular_hipotenusa(-8, -6) ==  10.0

def test_calcular_hipotenusa_caso1():
    assert calcular_hipotenusa(3, 4) == 5.0

def test_calcular_hipotenusa_caso2():
    assert calcular_hipotenusa(8, 15) == 17.0
