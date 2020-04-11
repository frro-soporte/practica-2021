from hypothesis import given
import hypothesis.strategies as st


# Ejercicio 1

from ejercicio_01 import maximo_basico, maximo_libreria, maximo_ternario


@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(allow_nan=False, allow_infinity=False))
def test_ejercicio_01_commutative(x, y):
    assert maximo_basico(x, y) == maximo_basico(y, x)
    assert maximo_libreria(x, y) == maximo_libreria(y, x)
    assert maximo_ternario(x, y) == maximo_ternario(y, x)


@given(st.floats(allow_nan=False, allow_infinity=False), st.floats(allow_nan=False, allow_infinity=False))
def test_ejercicio_01_idempotent(x, y):
    assert maximo_basico(maximo_basico(x, y), maximo_basico(y, x)) == maximo_basico(y, x)
    assert maximo_libreria(maximo_libreria(x, y), maximo_libreria(y, x)) == maximo_libreria(y, x)
    assert maximo_ternario(maximo_ternario(x, y), maximo_ternario(y, x)) == maximo_ternario(y, x)


@given(st.floats(allow_nan=False, allow_infinity=False, max_value=0, exclude_max=True),
       st.floats(allow_nan=False, allow_infinity=False, min_value=0, exclude_min=True))
def test_ejercicio_01_positives_negatives(x, y):
    assert maximo_basico(x, y) == y
    assert maximo_libreria(x, y) == y
    assert maximo_ternario(x, y) == y


@given(st.floats(allow_nan=False, allow_infinity=False, max_value=0, exclude_max=True), st.just(0))
def test_ejercicio_01_negatives(x, y):
    assert maximo_basico(x, y) == y
    assert maximo_libreria(x, y) == y
    assert maximo_ternario(x, y) == y


@given(st.floats(allow_nan=False, allow_infinity=False, min_value=0, exclude_min=True), st.just(0))
def test_ejercicio_01_positives(x, y):
    assert maximo_basico(x, y) == x
    assert maximo_libreria(x, y) == x
    assert maximo_ternario(x, y) == x
