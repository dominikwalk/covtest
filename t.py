
def print_num(number: int) -> str:
    return str(number)

def add(num1: int, num2: int) -> int:
    return num1 + num1

def test_print_num():
    out = print_num(number=42)
    assert out == "42"
