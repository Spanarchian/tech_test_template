from .xfile import funcx


def test_funcx():
    act = funcx()
    exp = 1
    assert act == exp, f"ERROR: Expected {exp} but had {act} returned!"
