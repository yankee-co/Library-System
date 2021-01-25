from django.test import TestCase

from personal.utils import factorial


class FactorialTestCase(TestCase):
    """
    - check negative integer number -
    - check zero -
    - check 1 -
    - check positive case (natural number) -
    - check float -
    - check non-number -
    - check large natural number -
    """

    # def setUp(self) -> None:
    #     print("SETUP TEST")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print("SETUP CLASS")
    #
    # def tearDown(self) -> None:
    #     print("TEAR TEST")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("TEAR CLASS")

    def test_positive_case(self):
        """Test positive case for Factorial"""
        init_value: int = 6
        result_to_compare: int = 720

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)

    def test_negative_case(self):
        """Test negative case for Factorial"""
        init_value: int = -6
        result_to_compare = 'Wrong data given to function'

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)

    def test_zero_case(self):
        """Test zero case for Factorial"""
        init_value: int = 0
        result_to_compare: int = 1

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)

    def test_one_case(self):
        """Test 1 case for Factorial"""
        init_value: int = 1
        result_to_compare: int = 1

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)

    def test_large_int_number_case(self):
        """Test large int number case for Factorial"""
        init_value: int = 100
        result_to_compare: int = (93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000)

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)

    def test_non_number_case(self):
        """Test non number case for Factorial"""
        init_value = 'LOL'
        result_to_compare = 'Wrong data given to function'

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)

    def test_decimal_case(self):
        """Test decimal case for Factorial"""
        init_value: int = 3.14
        result_to_compare: int = 'Wrong data given to function'

        fact_result = factorial(init_value)

        self.assertEqual(fact_result, result_to_compare)
