import calc as module 

class TestClass:

    def test_function_1(self):
        # Override the Python built-in input method 
        module.input = lambda: '4'
        # Call the function you would like to test (which uses input)
        output = module.choose()  
        assert output == 4

    def test_function_2(self):
        module.input = lambda: '3'
        output = module.choose()  
        assert not output == 4        

    def teardown_method(self, method):
        # This method is being called after each test case, and it will revert input back to original function
        module.input = input

def test_numbers_3_4_add():
    assert module.add(3,4) == 7 

def test_addfalse():
    assert not module.add(4,4) == 2  

def test_numbers_3_4_sub():
    assert module.sub(3,4) == -1 

def test_subfalse():
    assert not module.sub(4,4) == 2  

def test_numbers_3_4_multiply():
    assert module.multiply(3,4) == 12 
      
def test_multiplyfalse():
    assert not module.multiply(4,4) == 2  

def test_numbers_3_4_div():
    assert module.div(3,4) == 0.75    

def test_divfalse():
    assert not module.div(4,4) == 2    

# import mock

# def test_choose():

#     with mock.patch('builtins.input', return_value='3'):
#         assert choose() == 3

#     with mock.patch('builtins.input', return_value='4'):
#         assert choose() == 4    		