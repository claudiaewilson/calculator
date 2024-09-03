from calculator import operations

def test_add():
    assert operations.add(2, 3) == 5, 'incorrect'
    assert operations.add(-1, 1) == 0, 'incorrect'

def test_subtract():
    assert operations.subtract(5, 3) == 2, 'incorrect'
    assert operations.subtract(2, 5) == -3, 'incorrect'

def test_multiply():
    assert operations.multiply(2, 3) == 6, 'incorrect'
    assert operations.multiply(-1, 5) == -5, 'incorrect'

def test_divide():
    assert operations.divide(6, 3) == 2, 'incorrect'
    assert operations.divide(1, 0) == ValueError, 'incorrect'

def test_sqrt():
    assert operations.sqrt(9) == 3, 'incorrect'
    assert operations.sqrt(-1) == ValueError, 'incorrect'