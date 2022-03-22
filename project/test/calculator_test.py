import src


def test_add():
    calc = src.Calculator()

    assert calc.add(1, 3) == 4
