import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator
from app.calc import InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
    
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
    
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(3, self.calc.substract(5, 2))
        self.assertEqual(-2, self.calc.substract(3, 5))
        self.assertEqual(4.5, self.calc.substract(10, 5.5))

    def test_substract_method_fails_with_invalid_types(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
    
    @patch('app.util.validate_permissions', return_value=False)
    def test_multiply_raises_when_no_permissions(self, mock_validate):
        # Intentamos multiplicar con permisos denegados
        self.assertRaises(
            InvalidPermissions,
            self.calc.multiply,
            2, 4
            )
        mock_validate.assert_called_once_with("2 * 4", "user1")

    # Se agrega pruebas unitarias para las nuevas funcionalidades.

    def test_power_returns_correct_result(self):
        self.assertEqual(27, self.calc.power(3, 3))
        self.assertEqual(1, self.calc.power(3, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))
    
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 3)
        self.assertRaises(TypeError, self.calc.power, 2, "3")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        
    def test_sqrt_returns_correct_result(self):
        self.assertEqual(4, self.calc.sqrt(16))
        self.assertEqual(0, self.calc.sqrt(0))
    
    def test_sqrt_fails_on_negative_number(self):
        self.assertRaises(ValueError, self.calc.sqrt, -1)
        self.assertRaises(TypeError,  self.calc.sqrt, None)
    
    def test_log10_returns_correct_result(self):
        self.assertEqual(3, self.calc.log10(1000))
        self.assertEqual(0, self.calc.log10(1))

    def test_log10_fails_on_non_positive(self):
        self.assertRaises(ValueError, self.calc.log10, 0)
        self.assertRaises(ValueError, self.calc.log10, -10)
        self.assertRaises(TypeError,  self.calc.log10, None)

    def test_is_even_static_method(self):
        self.assertTrue(Calculator.is_even(4))
        self.assertFalse(Calculator.is_even(5))

    def test_is_even_raises_type_error_on_non_int(self):
        self.assertRaises(TypeError, Calculator.is_even, 2.0)
        self.assertRaises(TypeError, Calculator.is_even, "2")
        self.assertRaises(TypeError, Calculator.is_even, None)
if __name__ == "__main__":  # pragma: no cover
    unittest.main()
