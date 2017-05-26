"""
**************************************************************************

 DataQuantity.py

**************************************************************************
 Description:

 Represents a data quantity in bits.

**************************************************************************
 Author: Rob Lyon
 Email : robert.lyon@manchester.ac.uk
 web   : www.scienceguyrob.com

**************************************************************************
 License:

 Code made available under the GPLv3 (GNU General Public License), that
 allows you to copy, modify and redistribute the code as you see fit
 (http://www.gnu.org/copyleft/gpl.html). Though a mention to the
 original author using the citation above in derivative works, would be
 very much appreciated.

**************************************************************************
"""

from DataConversions import *


# ******************************
#
# CLASS DEFINITION
#
# ******************************


class DataQuantity(object):
    """
    The data quantity object. Represents a quantity
    of information in bits.
    """

    # ******************************
    #
    # Constructor.
    #
    # ******************************

    def __init__(self, bits=0):
        """
        Default constructor for the base class.

        Parameters
        ----------
        @param bits: the number of bits being represented
                     by the data quantity.

        Examples
        --------
        >>> dq = DataQuantity(1)
        >>> print dq
        >>> 1 bit
        """

        if type(bits) == int or type(bits) == float:
            if bits <= 0:
                self.bits = 0
            else:
                self.bits = bits
        else:
            self.bits = 0

    # ******************************

    def __str__(self):
        """
        Overridden string method, outputs a string
        representation of this class.

        Returns
        ----------
        @return a string describing this object in terms of bits.

        Examples
        --------
        >>> dq = DataQuantity(1)
        >>> print dq
        >>> 1 bit
        """

        if self.bits <= 0:
            return '0 bits'
        elif self.bits == 1:
            return '1 bit'
        else:
            return str(self.bits) + ' bits'

    # ******************************

    def get(self, units='bits'):
        """
        Gets a textual description of the data quantity,
        according to the user specified units.

        Parameters
        ----------
        @param units: the units used to describe the bit value.

        Returns
        ----------
        @return a string describing the number of bits in this data quantity, according to the
                desired units.

        Examples
        --------
        >>> dq = DataQuantity(100)
        >>> print dq
        >>> 100 bit
        >>> print dq.get('kbit')
        >>> 0.1 kbit
        """
        if type(units) == str:
            if isByteUnitValid(units):
                if units == 'B':
                    return str(convertBitToByte(self.bits, 'B')) + ' B'
                elif units == 'kB':
                    return str(convertBitToByte(self.bits, 'kB')) + ' kB'
                elif units == 'MB':
                    return str(convertBitToByte(self.bits, 'MB')) + ' MB'
                elif units == 'GB':
                    return str(convertBitToByte(self.bits, 'GB')) + ' GB'
                elif units == 'TB':
                    return str(convertBitToByte(self.bits, 'TB')) + ' TB'
                elif units == 'PB':
                    return str(convertBitToByte(self.bits, 'PB')) + ' PB'
                else:
                    return str(self.bits) + " bits"

            elif isBitUnitValid(units):
                if units == 'bit':
                    return str(convertFromBit(self.bits, 'bit')) + ' bit'
                elif units == 'kbit':
                    return str(convertFromBit(self.bits, 'kbit')) + ' kbit'
                elif units == 'Mbit':
                    return str(convertFromBit(self.bits, 'Mbit')) + ' Mbit'
                elif units == 'Gbit':
                    return str(convertFromBit(self.bits, 'Gbit')) + ' Gbit'
                elif units == 'Tbit':
                    return str(convertFromBit(self.bits, 'Tbit')) + ' Tbit'
                elif units == 'Pbit':
                    return str(convertFromBit(self.bits, 'Pbit')) + ' Pbit'
                else:
                    return str(self.bits) + " bits"
        else:
            return str(self.bits) + " bits"

    # ******************************

    def getRate(self, seconds=1.0, units='bits'):
        """
        Gets a text description of the data quantity,
        according to the user specified units.

        Parameters
        ----------
        @param seconds: the time over which to compute the data
                        rate in seconds.
        @param units the units to use to describe the data

        Returns
        ----------
        @return a string describing the number of bits in this data
                quantity, as a data rate.

        Examples
        --------
        >>> dq = DataQuantity(1000)
        >>> print dq
        >>> 1000 bit
        >>> print dq.getRate(2,'kbit') # 1000 bits over 2 seconds
        >>> 500 bit/s
        """

        if seconds <= 0:
            return 'Number of seconds invalid.'

        if type(units) == str:
            if isByteUnitValid(units):
                if units == 'B':
                    return str(convertBitToByte(self.bits, 'B') / float(seconds)) + ' B/s'
                elif units == 'kB':
                    return str(convertBitToByte(self.bits, 'kB') / float(seconds)) + ' kB/s'
                elif units == 'MB':
                    return str(convertBitToByte(self.bits, 'MB') / float(seconds)) + ' MB/s'
                elif units == 'GB':
                    return str(convertBitToByte(self.bits, 'GB') / float(seconds)) + ' GB/s'
                elif units == 'TB':
                    return str(convertBitToByte(self.bits, 'TB') / float(seconds)) + ' TB/s'
                elif units == 'PB':
                    return str(convertBitToByte(self.bits, 'PB') / float(seconds)) + ' PB/s'
                else:
                    return str(self.bits) + " bits"

            elif isBitUnitValid(units):
                if units == 'bit':
                    return str(convertFromBit(self.bits, 'bit') / float(seconds)) + ' bit/s'
                elif units == 'kbit':
                    return str(convertFromBit(self.bits, 'kbit') / float(seconds)) + ' kbit/s'
                elif units == 'Mbit':
                    return str(convertFromBit(self.bits, 'Mbit') / float(seconds)) + ' Mbit/s'
                elif units == 'Gbit':
                    return str(convertFromBit(self.bits, 'Gbit') / float(seconds)) + ' Gbit/s'
                elif units == 'Tbit':
                    return str(convertFromBit(self.bits, 'Tbit') / float(seconds)) + ' Tbit/s'
                elif units == 'Pbit':
                    return str(convertFromBit(self.bits, 'Pbit') / float(seconds)) + ' Pbit/s'
                else:
                    return str(self.bits) + " bits"
        else:
            return str(self.bits) + " bits"

    # ******************************

    def __add__(self, otherdq):
        """
        Adds a data quantity to this object.

        Parameters
        ----------
        @param otherdq: the data quantity to add to this object.

        Returns
        ----------
        @return a data quantity representing the sum of this object
                and the otherdq object.

        Examples
        --------
        >>> dq1 = DataQuantity(1)
        >>> dq2 = DataQuantity(1)
        >>> print dq1 + dq2
        >>> 2 bits
        """
        if type(otherdq) == DataQuantity:
            bit_sum = self.bits + otherdq.bits
            return DataQuantity(bit_sum)
        elif type(otherdq) == int or type(otherdq) == float:
            bit_sum = self.bits + otherdq
            return DataQuantity(bit_sum)
        else:
            return self

    __radd__ = __add__

    # ******************************

    def __sub__(self, otherdq):
        """
        Subtracts a data quantity from this object.

        Parameters
        ----------
        @param otherdq: the data quantity to subtract from this object.

        Returns
        ----------
        @return a data quantity representing the sum of this object
                subtracted from the otherdq object.

        Examples
        --------
        >>> dq1 = DataQuantity(1)
        >>> print 1 - dq1
        >>> 0 bits
        """
        if type(otherdq) == DataQuantity:
            bit_sub = self.bits - otherdq.bits
            return DataQuantity(bit_sub)
        elif type(otherdq) == int or type(otherdq) == float:
            bit_sub = self.bits - otherdq
            return DataQuantity(bit_sub)
        else:
            return self

    __rsub__ = __sub__

    # ******************************

    def __mul__(self, otherdq):
        """
        Multiples a data quantity with this object.

        Parameters
        ----------
        @param otherdq: the data quantity to multiply.

        Returns
        ----------
        @return a data quantity representing the mulitplcation of this object
                and the otherdq object.

        Examples
        --------
        >>> dq1 = DataQuantity(2)
        >>> dq2 = DataQuantity(2)
        >>> print dq1 * dq2
        >>> 4 bits
        """
        if type(otherdq) == DataQuantity:
            bit_mul = self.bits * otherdq.bits
            return DataQuantity(bit_mul)
        elif type(otherdq) == int or type(otherdq) == float:
            bit_mul = self.bits * otherdq
            return DataQuantity(bit_mul)
        else:
            return self

    __rmul__ = __mul__

    # ******************************

    def __div__(self, otherdq):
        """
        Divides a data quantity with this object.

        Parameters
        ----------
        @param otherdq: the data quantity to divide.

        Returns
        ----------
        @return a data quantity representing the division of this object
                and the otherdq object.

        Examples
        --------
        >>> dq1 = DataQuantity(10)
        >>> dq2 = DataQuantity(4)
        >>> print dq1 / dq2
        >>> 2.5 bits
        """
        if type(otherdq) == DataQuantity:
            if otherdq.bits > 0:
                bit_mul = float(self.bits) / float(otherdq.bits)
                return DataQuantity(bit_mul)
            else:
                return None
        elif type(otherdq) == int or type(otherdq) == float:
            if otherdq > 0:
                bit_mul = float(self.bits) / float(otherdq)
                return DataQuantity(bit_mul)
            else:
                return None
        else:
            return self

    def __floordiv__(self, otherdq):
        """
        Divides a data quantity with this object.
        This is the floor division implementation, which rounds down.

        Parameters
        ----------
        @param otherdq: the data quantity to divide.

        Returns
        ----------
        @return a data quantity representing the division of this object
                and the otherdq object.

        Examples
        --------
        >>> dq1 = DataQuantity(10)
        >>> dq2 = DataQuantity(4)
        >>> print dq1 // dq2
        >>> 2.0 bits
        """
        if type(otherdq) == DataQuantity:
            bit_mul = self.bits // otherdq.bits
            return DataQuantity(bit_mul)
        elif type(otherdq) == int or type(otherdq) == float:
            bit_mul = self.bits // otherdq
            return DataQuantity(bit_mul)
        else:
            return self

    __rdiv__ = __div__
    __rfloordiv__ = __floordiv__

    # ****************************************************************************************************



