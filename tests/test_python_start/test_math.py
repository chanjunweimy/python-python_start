from python_start.math import inc
from hypothesis import given, example
import hypothesis.strategies as st

def test_inc():
    assert inc(1) == 2

@given(st.integers())
@example(0)
def test_inc_withhypothesis(x):
    assert inc(x) == x + 1
    