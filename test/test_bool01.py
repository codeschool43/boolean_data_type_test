try:
    from bool01 import main
except ImportError:
    assert False, "Not found"


def test_main_1():
    expectation = main(5,5)
    assert expectation == True, "Error"

def test_main_2():
    expectation = main(2,5)
    assert expectation == False, "Error"