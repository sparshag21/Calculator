from calc.py import test_numbers_3_4_add
from calc.py import test_numbers_3_4_sub
from calc.py import test_numbers_3_4_multiply
from calc.py import test_numbers_3_4_div

def test_numbers_3_4_add():
    assert add(3,4) == 7 

def test_numbers_3_4_sub():
    assert sub(3,4) == -1 

def test_numbers_3_4_multiply():
    assert multiply(3,4) == 12   

def test_numbers_3_4_div():
    assert div(3,4) == 0.75           