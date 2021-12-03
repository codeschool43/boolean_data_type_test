try:
    from bool04 import main
except ImportError:
    assert False, "Not found"


def test_main_1():
    expectation = main(0.1)
    assert expectation == False, "Error"

def test_main_2():
    expectation = main(-2.4)
    assert expectation == True, "Error"