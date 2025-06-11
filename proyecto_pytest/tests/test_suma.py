import pytest

def suma(a, b):
    """Suma dos números."""
    return a + b

def test_suma():
    """Prueba de la función suma."""
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(-5, -5) == -10
    assert suma(100, 200) == 300
    assert suma(1.5, 2.5) == 4.0

def test_suma_fail():
    """Prueba fallida de la función suma."""
    with pytest.raises(AssertionError):
        assert suma(2, 2) == 5  # Esto debería fallar
    with pytest.raises(AssertionError):
        assert suma(1, -1) == 3  # Esto también debería fallar

def test_suma_edge_cases():
    """Pruebas de casos límite para la función suma."""
    assert suma(0, 1) == 1
    assert suma(1, 0) == 1
    assert suma(-1, -1) == -2
    assert suma(1000000, 2000000) == 3000000
    assert suma(1e10, 1e10) == 2e10
    assert suma(-1e10, -1e10) == -2e10

def test_suma_large_numbers():
    """Prueba de la función suma con números grandes."""
    assert suma(10**18, 10**18) == 2 * 10**18
    assert suma(-10**18, -10**18) == -2 * 10**18
    assert suma(10**18, -10**18) == 0
    assert suma(10**9, 10**9) == 2 * 10**9
    assert suma(-10**9, -10**9) == -2 * 10**9