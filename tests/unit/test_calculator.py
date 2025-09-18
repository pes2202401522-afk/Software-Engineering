"""
Unit Tests for Calculator
Students start with 2 passing tests, then add more
"""
import pytest
from src.calculator import add, divide, subtract, multiply, power, square_root

class TestBasicOperations:
    """Test basic arithmetic operations"""
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers"""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
    
    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers"""
        assert subtract(5, 3) == 2
        assert subtract(10, 4) == 6
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers"""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2
    
    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers"""
        assert subtract(-1, -1) == 0
        assert subtract(-5, -3) == -2
    
    def test_add_edge_cases(self):
        """Test add with zero and decimals"""
        assert add(0, 5) == 5
        assert add(2.5, 2.5) == 5.0
    
    def test_subtract_edge_cases(self):
        """Test subtract with zero and decimals"""
        assert subtract(5, 0) == 5
        assert subtract(5.0, 2.0) == 3.0

class TestMultiplyDivide:
    """Test multiplication and division operations"""
    
    def test_multiply_valid_inputs(self):
        """Test multiply with valid numeric inputs."""
        assert multiply(2, 3) == 6
        assert multiply(-5, 4) == -20
        assert multiply(2.5, 2) == 5.0
        assert multiply(0, 100) == 0

    def test_divide_valid_inputs(self):
        """Test divide with valid numeric inputs."""
        assert divide(10, 2) == 5
        assert divide(100, 4) == 25
        assert divide(-10, 2) == -5
        assert divide(9, 3) == 3

class TestMultiplyDivideValidation:
    """Test multiplication and division input validation"""
    
    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")

    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide(10, "2")

    def test_divide_by_zero_error(self):
        """Test that dividing by zero raises a ValueError."""
        with pytest.raises(ValueError, match="Cannot divide"):
            divide(10, 0)

class TestPowerSquareRoot:
    """Test power and square root operations"""

    def test_power_positive_numbers(self):
        """Test power with positive numbers"""
        assert power(2, 3) == 8
        assert power(5, 2) == 25

    def test_power_zero_exponent(self):
        """Test power with zero exponent"""
        assert power(5, 0) == 1
        assert power(10, 0) == 1

    def test_power_negative_base(self):
        """Test power with negative base and positive exponent"""
        assert power(-2, 2) == 4

    def test_power_validation(self):
        """Test power rejects non-numeric inputs"""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power("2", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            power(2, "3")

    def test_power_negative_exponent(self):
        """Test power raises ValueError for negative exponent"""
        with pytest.raises(ValueError, match="Negative exponents are not supported"):
            power(2, -1)

    def test_square_root_positive_numbers(self):
        """Test square root with positive numbers"""
        assert square_root(4) == 2.0
        assert square_root(16) == 4.0

    def test_square_root_zero(self):
        """Test square root of zero"""
        assert square_root(0) == 0.0

    def test_square_root_validation(self):
        """Test square root rejects non-numeric inputs"""
        with pytest.raises(TypeError, match="Argument must be a number"):
            square_root("4")

    def test_square_root_negative_number(self):
        """Test square root raises ValueError for negative number"""
        with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
            square_root(-4)