try:
    from bool02 import main
except ImportError:
    assert False, "Not found"


def test_main_1():
    expectation = main(3)
    assert expectation == False, "Error"

def test_main_2():
    expectation = main(7)
    assert expectation == True, "Error"