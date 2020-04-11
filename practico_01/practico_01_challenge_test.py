from hypothesis import given
import hypothesis.strategies as st


def test_asserts_ejercicio_05():
    from ejercicio_05 import multiplicar_reduce
    assert multiplicar_reduce([1, 2, 3, 4]) == 24
    assert multiplicar_reduce([2, 5]) == 10
    assert multiplicar_reduce([]) == 0
    assert multiplicar_reduce([1, 2, 3, 0, 4, 5]) == 0
    assert multiplicar_reduce(range(1, 20)) == 121_645_100_408_832_000


def test_asserts_ejercicio_06():
    from ejercicio_06 import numeros_al_final_filter, numeros_al_final_recursivo
    assert numeros_al_final_filter([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]
    assert numeros_al_final_recursivo([3, "a", 1, "b", 10, "j"]) == ["a", "b", "j", 3, 1, 10]


def test_asserts_ejercicio_09():
    from ejercicio_09 import sumatoria_reduce, sumatoria_gauss

    assert sumatoria_reduce(1) == 1
    assert sumatoria_reduce(100) == 5050

    assert sumatoria_gauss(1) == 1
    assert sumatoria_gauss(100) == 5050


def test_asserts_ejercicio_13():
    from ejercicio_13 import generar_pares_generator_send, generar_pares_delegados
    generador_pares = generar_pares_generator_send()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4
    assert generador_pares.send(10) == 10
    assert next(generador_pares) == 12
    assert next(generador_pares) == 14
    assert next(generador_pares) == 16

    generador_pares = generar_pares_delegados()
    assert next(generador_pares) == 0
    assert next(generador_pares) == 2
    assert next(generador_pares) == 4


def test_asserts_ejercicio_15():
    from ejercicio_15 import calcular_posibilidades_recursiva, calcular_posibilidades

    n = 11
    limite = 10
    lista = list(range(n))

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    assert result == 28671512

    result, elapsed = calcular_posibilidades_recursiva(lista, limite)
    assert result == 28671512

    result, elapsed = calcular_posibilidades(lista, limite + 1)
    assert result == 68588312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 1)
    assert result == 68588312

    result, elapsed = calcular_posibilidades(lista, limite + 2)
    assert result == 108505112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite + 2)
    assert result == 108505112

    result, elapsed = calcular_posibilidades(lista, limite - 1)
    assert result == 8713112

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 1)
    assert result == 8713112

    result, elapsed = calcular_posibilidades(lista, limite - 2)
    assert result == 2060312

    result, elapsed = calcular_posibilidades_recursiva(lista, limite - 2)
    assert result == 2060312
