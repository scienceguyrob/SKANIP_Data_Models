"""
**************************************************************************

 TestDataQuantity.py

**************************************************************************
 Description:

 Tests the data class used to represent data quantities.

**************************************************************************
 Author: Rob Lyon
 Email : robert.lyon@manchester.ac.uk
 web   : www.scienceguyrob.com

**************************************************************************
 Required Command Line Arguments:

 N/A

**************************************************************************
 Optional Command Line Arguments:

 N/A

**************************************************************************
 License:

 Code made available under the GPLv3 (GNU General Public License), that
 allows you to copy, modify and redistribute the code as you see fit
 (http://www.gnu.org/copyleft/gpl.html). Though a mention to the
 original author using the citation above in derivative works, would be
 very much appreciated.

**************************************************************************
"""

import unittest
from main.src.DataQuantity import DataQuantity

# ******************************
#
# CLASS DEFINITION
#
# ******************************


class TestDataQuantity(unittest.TestCase):
    """
    Defines the tests for notebook functions individually.
    """

    # ******************************
    #
    # TESTS
    #
    # ******************************

    def test_add(self):
        """
        Tests the method that adds data quantities.


        """

        # *************************************************
        # Addition of quantities
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq2 = DataQuantity(-1)
        dq3 = dq1 + dq2
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq2 = DataQuantity(0)
        dq3 = dq1+dq2
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(0)
        dq3 = dq1 + dq2
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(1)
        dq3 = dq1 + dq2
        self.assertEqual(2, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq2 = DataQuantity(1000)
        dq3 = dq1 + dq2
        self.assertEqual(2000, dq3.bits)

        # *************************************************
        # Addition of quantities with ints
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 + -1
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 + 0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 + 0
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 + 1
        self.assertEqual(2, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = dq1 + 1000
        self.assertEqual(2000, dq3.bits)

        # *************************************************
        # Addition of quantities with ints reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = -1 + dq1
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0 + dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0 + dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1 + dq1
        self.assertEqual(2, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = 1000 + dq1
        self.assertEqual(2000, dq3.bits)

        # *************************************************
        # Addition of quantities with floats
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 + -1.0
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 + 0.0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 + 0.0
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 + 1.0
        self.assertEqual(2, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = dq1 + 1000.0
        self.assertEqual(2000, dq3.bits)

        # *************************************************
        # Addition of quantities with floats reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = -1.0 + dq1
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0.0 + dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0.0 + dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1.0 + dq1
        self.assertEqual(2, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = 1000.0 + dq1
        self.assertEqual(2000, dq3.bits)

    # ******************************

    def test_subtract(self):
        """
        Tests the method that subtracts data quantities.


        """

        # *************************************************
        # Subtraction of quantities
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq2 = DataQuantity(-1)
        dq3 = dq1 - dq2
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq2 = DataQuantity(0)
        dq3 = dq1 - dq2
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(0)
        dq3 = dq1 - dq2
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(1)
        dq3 = dq1 - dq2
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq2 = DataQuantity(500)
        dq3 = dq1 - dq2
        self.assertEqual(500, dq3.bits)

        # *************************************************
        # Subtraction of quantities with ints
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 - (-1)
        self.assertEqual(1, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 - 0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 - 0
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 - 1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = dq1 - 500
        self.assertEqual(500, dq3.bits)

        # *************************************************
        # Subtraction of quantities with ints reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = (-1) - dq1
        self.assertEqual(1, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0 - dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0 - dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1 - dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = 500 - dq1
        self.assertEqual(500, dq3.bits)

        # *************************************************
        # Subtraction of quantities with floats
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 - (-1.0)
        self.assertEqual(1, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 - 0.0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 - 0.0
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 - 1.0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = dq1 - 500.0
        self.assertEqual(500, dq3.bits)

        # *************************************************
        # Subtraction of quantities with floats reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = (-1.0) - dq1
        self.assertEqual(1, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0.0 - dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0.0 - dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1.0 - dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1000)
        dq3 = 500.0 - dq1
        self.assertEqual(500, dq3.bits)

    # ******************************

    def test_multiply(self):
        """
        Tests the method that multiplies data quantities.


        """

        # *************************************************
        # Multiplication of quantities
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq2 = DataQuantity(-1)
        dq3 = dq1 * dq2
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq2 = DataQuantity(0)
        dq3 = dq1 * dq2
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(0)
        dq3 = dq1 * dq2
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(1)
        dq3 = dq1 * dq2
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq2 = DataQuantity(4)
        dq3 = dq1 * dq2
        self.assertEqual(40, dq3.bits)

        # *************************************************
        # Multiplication of quantities with ints
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 * (-1)
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 * 0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 * 0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 * 1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = dq1 * 4
        self.assertEqual(40, dq3.bits)

        # *************************************************
        # Multiplication of quantities with ints reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = (-1) * dq1
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0 * dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0 * dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1 * dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = 4 * dq1
        self.assertEqual(40, dq3.bits)

        # *************************************************
        # Multiplication of quantities with floats
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 * (-1.0)
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 * 0.0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 * 0.0
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 * 1.0
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = dq1 * 4.0
        self.assertEqual(40, dq3.bits)

        # *************************************************
        # Multiplication of quantities with floats reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = (-1.0) * dq1
        self.assertEqual(0, dq3.bits)

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0.0 * dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0.0 * dq1
        self.assertEqual(0, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1.0 * dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = 4.0 * dq1
        self.assertEqual(40, dq3.bits)

    # ******************************

    def test_divide(self):
        """
        Tests the method that divides data quantities.


        """

        # *************************************************
        # Division of quantities
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq2 = DataQuantity(-1)
        dq3 = dq1 / dq2
        self.assertEqual(None, dq3) # Divide by zero effectively.

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq2 = DataQuantity(0)
        dq3 = dq1 / dq2
        self.assertEqual(None, dq3) # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(0)
        dq3 = dq1 / dq2
        self.assertEqual(None, dq3) # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq2 = DataQuantity(1)
        dq3 = dq1 / dq2
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq2 = DataQuantity(4)
        dq3 = dq1 / dq2
        self.assertEqual(2.5, dq3.bits)

        # *************************************************
        # Division of quantities with ints
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 / (-1)
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 / 0
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 / 0
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 / 1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = dq1 / 4
        self.assertEqual(2.5, dq3.bits)

        # *************************************************
        # Division of quantities with ints reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = (-1) / dq1
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0 / dq1
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0 / dq1
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1 / dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = 4 / dq1
        self.assertEqual(2.5, dq3.bits)

        # *************************************************
        # Division of quantities with floats
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = dq1 / (-1.0)
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = dq1 / 0.0
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 / 0.0
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = dq1 / 1.0
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = dq1 / 4.0
        self.assertEqual(2.5, dq3.bits)

        # *************************************************
        # Division of quantities with floats reversed
        # *************************************************

        # Extreme conditions
        dq1 = DataQuantity(-1)
        dq3 = (-1.0) / dq1
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Extreme conditions
        dq1 = DataQuantity(0)
        dq3 = 0.0 / dq1
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 0.0 / dq1
        self.assertEqual(None, dq3)  # Divide by zero effectively.

        # Normal conditions
        dq1 = DataQuantity(1)
        dq3 = 1.0 / dq1
        self.assertEqual(1, dq3.bits)

        # Normal conditions
        dq1 = DataQuantity(10)
        dq3 = 4.0 / dq1
        self.assertEqual(2.5, dq3.bits)

    # ******************************

    # ****************************************************************************************************

    # ******************************
    #
    # Test Setup & Teardown
    #
    # ******************************

    # preparing to test
    def setUp(self):
        """ Setting up for the test """

    # ****************************************************************************************************

    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""

    # ****************************************************************************************************

    if __name__ == "__main__":
        unittest.main(argv=['ignored', '-v'], exit=False)