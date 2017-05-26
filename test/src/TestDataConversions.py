"""
**************************************************************************

 TestDataConversions.py

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

import os
import unittest

from main.src.DataConversions import *

# ******************************
#
# CLASS DEFINITION
#
# ******************************


class TestDataConversions(unittest.TestCase):
    """
    Defines the tests for notebook functions individually.
    """

    # ******************************
    #
    # TESTS
    #
    # ******************************

    def test_bits_to_bytes(self):
        """
        Tests the method that converts bits to bytes.

        def bitsToBytes(bits):

        The tests are based on the following assumed
        correct conversion values (computed manually).

        Tests:

        |---------------------------------------
        | Test number |    Bits   |    Bytes   |
        |---------------------------------------
        |     1.      |     0     |      0     |
        |     2.      |     1     |    0.125   |
        |     3.      |     2     |     0.25   |
        |     4.      |    10     |     1.25   |
        |     5.      |    100    |     12.5   |
        |     6.      |   1,000   |     125    |
        |     7.      | 1,000,000 |    125000  |
        |---------------------------------------

        """
        self.assertEqual(bitsToBytes('a'), None)
        self.assertEqual(bitsToBytes('1'), None)
        self.assertEqual(bitsToBytes(0), 0)
        self.assertEqual(bitsToBytes(1), 0.125)
        self.assertEqual(bitsToBytes(2), 0.25)
        self.assertEqual(bitsToBytes(10), 1.25)
        self.assertEqual(bitsToBytes(100), 12.5)
        self.assertEqual(bitsToBytes(1000), 125)
        self.assertEqual(bitsToBytes(1000000), 125000)

    # ******************************

    def test_bytes_to_bits(self):
        """
        Tests the method that converts bytes to bits.

        def bytesToBits(bytes):

        The tests are based on the following assumed
        correct conversion values (computed manually).

        Tests:

        |---------------------------------------
        | Test number |    Bits   |    Bytes   |
        |---------------------------------------
        |     1.      |     0     |      0     |
        |     2.      |     1     |    0.125   |
        |     3.      |     2     |     0.25   |
        |     4.      |    10     |     1.25   |
        |     5.      |    100    |     12.5   |
        |     6.      |   1,000   |     125    |
        |     7.      | 1,000,000 |    125000  |
        |---------------------------------------

        """
        self.assertEqual(bytesToBits('a'), None)
        self.assertEqual(bytesToBits('1'), None)
        self.assertEqual(bytesToBits(0), 0)
        self.assertEqual(bytesToBits(0.125), 1)
        self.assertEqual(bytesToBits(0.25), 2)
        self.assertEqual(bytesToBits(1.25), 10)
        self.assertEqual(bytesToBits(12.5), 100)
        self.assertEqual(bytesToBits(125), 1000)
        self.assertEqual(bytesToBits(125000), 1000000)

    # ******************************

    def test_is_Bit_Data_Format_Valid(self):
        """
        Test the dunction that determines if a user
        supplied bit data format is valid.

        def isBitDataFormatValid(format):

        The valid formats should include:

        bit     - a single bit of information.
        kbit    - kilobit, 10^3 = 1000 bits.
        Mbit    - megabit, 10^6  bits.
        Gbit    - gigabit, 10^9  bits.
        Tbit    - terabit, 10^12 bits.
        Pbit    - petabit, 10^15 bits.
        """

        self.assertEqual(isBitUnitValid('a'), False)
        self.assertEqual(isBitUnitValid(0.0), False)
        self.assertEqual(isBitUnitValid(0), False)
        self.assertEqual(isBitUnitValid('kbits'), False)

        self.assertEqual(isBitUnitValid('bit'), True)
        self.assertEqual(isBitUnitValid('kbit'), True)
        self.assertEqual(isBitUnitValid('Mbit'), True)
        self.assertEqual(isBitUnitValid('Gbit'), True)
        self.assertEqual(isBitUnitValid('Tbit'), True)
        self.assertEqual(isBitUnitValid('Pbit'), True)

    # ******************************

    def test_is_Byte_Data_Format_Valid(self):
        """
        Test the dunction that determines if a user
        supplied byte data format is valid.

        def isByteDataFormatValid(format):

        The valid formats should include:

        B       - 8 bits of information.
        kB      - kilobyte, 10^3 bytes (or 8 x 10^3 bits).
        MB      - megabyte, 10^6  bytes (or 8 x 10^6 bits).
        Gb      - gigabyte, 10^9  bytes (or 8 x 10^9 bits).
        TP      - terabyte, 10^12 bytes (or 8 x 10^12 bits).
        PB      - petabyte, 10^15 bytes (or 8 x 10^15 bits).
        """

        self.assertEqual(isByteUnitValid('a'), False)
        self.assertEqual(isByteUnitValid(0.0), False)
        self.assertEqual(isByteUnitValid(0), False)
        self.assertEqual(isByteUnitValid('kbits'), False)

        self.assertEqual(isByteUnitValid('B'), True)
        self.assertEqual(isByteUnitValid('kB'), True)
        self.assertEqual(isByteUnitValid('MB'), True)
        self.assertEqual(isByteUnitValid('GB'), True)
        self.assertEqual(isByteUnitValid('TB'), True)
        self.assertEqual(isByteUnitValid('PB'), True)

    # ******************************

    def test_convert_from_bit_format(self):
        """
        Tests the function that converts a bits value to the
        user specified format.

        def convertFromBitFormat(bits,format='None')

        The supported formats inlcude:

        bit     - a single bit of information.
        kbit    - kilobit, 10^3 = 1000 bits.
        Mbit    - megabit, 10^6  bits.
        Gbit    - gigabit, 10^9  bits.
        Tbit    - terabit, 10^12 bits.
        Pbit    - petabit, 10^15 bits.

        """
        self.assertEqual(convertFromBit('a', 'a'), None)
        self.assertEqual(convertFromBit('1', '1'), None)
        self.assertEqual(convertFromBit('1', '1'), None)
        self.assertEqual(convertFromBit(0, '1'), None)
        self.assertEqual(convertFromBit(0, 'bit'), 0)
        self.assertEqual(convertFromBit(1, 'bit'), 1)
        self.assertEqual(convertFromBit(100, 'bit'), 100)

        # Now test some conversions...
        # Covert 10^15 bits to Pbit etc ...
        self.assertEqual(convertFromBit(pow(10, 15), 'Pbit'), 1.0)
        self.assertEqual(convertFromBit(pow(10, 15), 'Tbit'), pow(10, 3))
        self.assertEqual(convertFromBit(pow(10, 15), 'Gbit'), pow(10, 6))
        self.assertEqual(convertFromBit(pow(10, 15), 'Mbit'), pow(10, 9))
        self.assertEqual(convertFromBit(pow(10, 15), 'kbit'), pow(10, 12))
        self.assertEqual(convertFromBit(pow(10, 15), 'bit'), pow(10, 15))

        # Covert 1 bit to Pbit etc ...
        self.assertEqual(convertFromBit(1, 'Pbit'), pow(10, -15))
        self.assertEqual(convertFromBit(1, 'Tbit'), pow(10, -12))
        self.assertEqual(convertFromBit(1, 'Gbit'), pow(10, -9))
        self.assertEqual(convertFromBit(1, 'Mbit'), pow(10, -6))
        self.assertEqual(convertFromBit(1, 'kbit'), pow(10, -3))
        self.assertEqual(convertFromBit(1, 'bit'), 1)

    # ******************************

    def test_convert_to_bit_format(self):
        """
        Tests the function that converts a bits value to the
        user specified format.

        def convertToBitFormat(nonbits,format='None')

        The supported formats inlcude:

        bit     - a single bit of information.
        kbit    - kilobit, 10^3 = 1000 bits.
        Mbit    - megabit, 10^6  bits.
        Gbit    - gigabit, 10^9  bits.
        Tbit    - terabit, 10^12 bits.
        Pbit    - petabit, 10^15 bits.

        """
        self.assertEqual(convertToBit('a', 'a'), None)
        self.assertEqual(convertToBit('1', '1'), None)
        self.assertEqual(convertToBit('1', '1'), None)
        self.assertEqual(convertToBit(0, '1'), None)
        self.assertEqual(convertToBit(0, 'bit'), 0)
        self.assertEqual(convertToBit(1, 'bit'), 1)
        self.assertEqual(convertToBit(100, 'bit'), 100)

        # Now test some conversions... start with 1 bit values to 1 bit.
        self.assertEqual(convertToBit(pow(10, -15), 'Pbit'), 1.0)
        self.assertEqual(convertToBit(pow(10, -12), 'Tbit'), 1.0)
        self.assertEqual(convertToBit(pow(10, -9), 'Gbit'), 1.0)
        self.assertEqual(convertToBit(pow(10, -6), 'Mbit'), 1.0)
        self.assertEqual(convertToBit(pow(10, -3), 'kbit'), 1.0)
        self.assertEqual(convertToBit(pow(10, 1), 'bit'), pow(10, 1))

        # Now convert from larger values to the expected number of bits.
        self.assertEqual(convertToBit(1, 'Pbit'), pow(10, 15))
        self.assertEqual(convertToBit(1, 'Tbit'), pow(10, 12))
        self.assertEqual(convertToBit(1, 'Gbit'), pow(10, 9))
        self.assertEqual(convertToBit(1, 'Mbit'), pow(10, 6))
        self.assertEqual(convertToBit(1, 'kbit'), pow(10, 3))
        self.assertEqual(convertToBit(1, 'bit'), 1)

    # ******************************

    def test_convert_to_byte_format(self):
        """
        Tests the function that converts a bits value to the
        user specified byte format.

        def convertToByteFormat(nonbits,format='None')

        The suported formats inlcude:

        bit     - a single bit of information.
        kbit    - kilobit, 10^3 = 1000 bits.
        Mbit    - megabit, 10^6  bits.
        Gbit    - gigabit, 10^9  bits.
        Tbit    - terabit, 10^12 bits.
        Pbit    - petabit, 10^15 bits.

        """
        self.assertEqual(convertBitToByte('a', 'a'), None)
        self.assertEqual(convertBitToByte('1', '1'), None)
        self.assertEqual(convertBitToByte('1', '1'), None)
        self.assertEqual(convertBitToByte(0, '1'), None)
        self.assertEqual(convertBitToByte(0, 'B'), 0)
        self.assertEqual(convertBitToByte(1, 'B'), 0.125)

        # Now test some conversions... start with 1 bit values to 1 bit.
        self.assertEqual(convertBitToByte(1, 'PB'), 1.25 * pow(10, -16))
        self.assertEqual(convertBitToByte(1, 'TB'), 1.25 * pow(10, -13))
        self.assertEqual(convertBitToByte(1, 'GB'), 1.25 * pow(10, -10))
        self.assertEqual(convertBitToByte(1, 'MB'), 1.25 * pow(10, -7))
        self.assertEqual(convertBitToByte(1, 'kB'), 1.25 * pow(10, -4))
        self.assertEqual(convertBitToByte(1, 'B'), 1.25 * pow(10, -1))

        # Now convert from larger values to the expected number of bits.
        self.assertEqual(convertBitToByte(1000, 'PB'), 1.25 * pow(10, -13))
        self.assertEqual(convertBitToByte(1000, 'TB'), 1.25 * pow(10, -10))
        self.assertEqual(convertBitToByte(1000, 'GB'), 1.25 * pow(10, -7))
        self.assertEqual(convertBitToByte(1000, 'MB'), 1.25 * pow(10, -4))
        self.assertEqual(convertBitToByte(1000, 'kB'), 1.25 * pow(10, -1))
        self.assertEqual(convertBitToByte(1000, 'B'), 1.25 * pow(10, 2))

    # ******************************

    def test_convert_from_byte_format(self):
        """
        Tests the function that converts a byte value to the
        user specified bit format.

        def convertFromByteFormat(bits,format='None')

        The supported formats inlcude:

        bit     - a single bit of information.
        kbit    - kilobit, 10^3 = 1000 bits.
        Mbit    - megabit, 10^6  bits.
        Gbit    - gigabit, 10^9  bits.
        Tbit    - terabit, 10^12 bits.
        Pbit    - petabit, 10^15 bits.

        """
        self.assertEqual(convertByteToBit('a', 'a'), None)
        self.assertEqual(convertByteToBit('1', '1'), None)
        self.assertEqual(convertByteToBit('1', '1'), None)
        self.assertEqual(convertByteToBit(0, '1'), None)
        self.assertEqual(convertByteToBit(0, 'B'), 0)
        self.assertEqual(convertByteToBit(1, 'B'), 8)

        # Now test some conversions...
        # Covert 10^15 bits to Pbit etc ...
        self.assertEqual(convertByteToBit(1, 'PB'), 8 * pow(10, 15))
        self.assertEqual(convertByteToBit(1, 'TB'), 8 * pow(10, 12))
        self.assertEqual(convertByteToBit(1, 'GB'), 8 * pow(10, 9))
        self.assertEqual(convertByteToBit(1, 'MB'), 8 * pow(10, 6))
        self.assertEqual(convertByteToBit(1, 'kB'), 8 * pow(10, 3))
        self.assertEqual(convertByteToBit(1, 'B'), 8)

        # Covert 1 bit to Pbit etc ...
        self.assertEqual(convertByteToBit(10, 'PB'), 8 * pow(10, 16))
        self.assertEqual(convertByteToBit(10, 'TB'), 8 * pow(10, 13))
        self.assertEqual(convertByteToBit(10, 'GB'), 8 * pow(10, 10))
        self.assertEqual(convertByteToBit(10, 'MB'), 8 * pow(10, 7))
        self.assertEqual(convertByteToBit(10, 'kB'), 8 * pow(10, 4))
        self.assertEqual(convertByteToBit(10, 'B'), 8 * pow(10, 1))

    def test_exploratory(self):
        """
        Some simple exploratory tests, design to ensure everything works.
        Output compared with wolfram alpha output.

        """

        # 1000 bits to GB (should be 1.25*10^-7 GB (gigabytes))
        self.assertEqual(convertBitToByte(1000, 'GB'), 1.25 * pow(10, -7))


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