import pytest

def multiplicacion(a, b):
    """Multiplica dos números."""
    return a * b

def test_multiplicacion():
    """Prueba de la función multiplicacion."""
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 5) == 0
    assert multiplicacion(-5, -5) == 25
    assert multiplicacion(100, 200) == 20000
    assert multiplicacion(1.5, 2.5) == 3.75

def test_multiplicacion_fail():
    """Prueba fallida de la función multiplicacion."""
    with pytest.raises(AssertionError):
        assert multiplicacion(2, 2) == 5  # Esto debería fallar
    with pytest.raises(AssertionError):
        assert multiplicacion(1, -1) == 3  # Esto también debería fallar

def test_multiplicacion_edge_cases():
    """Pruebas de casos límite para la función multiplicacion."""
    assert multiplicacion(0, 1) == 0
    assert multiplicacion(1, 0) == 0
    assert multiplicacion(-1, -1) == 1
    assert multiplicacion(1000000, 2000000) == 2000000000000
    assert multiplicacion(1e10, 1e10) == 1e20
    assert multiplicacion(-1e10, -1e10) == 1e20

def test_multiplicacion_large_numbers():
    """Prueba de la función multiplicacion con números grandes."""
    assert multiplicacion(10**18, 10**18) == 10**36
    assert multiplicacion(-10**18, -10**18) == 10**36
    assert multiplicacion(10**18, -10**18) == -10**36
    assert multiplicacion(10**9, 10**9) == 10**18
    assert multiplicacion(-10**9, -10**9) == 10**18