from lib_math import moyenne

def test_moyenne_pure():
    
    x1_test = -1
    x2_test =  3
    expected_result = 1
    assert expected_result == moyenne(x1_test, x2_test)