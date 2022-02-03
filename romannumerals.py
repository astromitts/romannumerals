class RomanNumeral(object):
    ROMAN_NUMERALS_BASE_TEN_MAP = [
        ['I', 'V'],
        ['X', 'L'],
        ['C', 'D'],
        ['M', 'V']
    ]

    def __init__(self, number):
        if number <= 5000:
            self.number = number
            self.numeral = '?'
            self.set_numeral()
        else:
            raise ValueError("I can't do numbers higher than 5000 :(")

    def get_numeral(self, base_ten, integer):
        """ Finds the roman numeral for a single given integer, for the given base 10 value.

            Parameters:
            base_ten (Int) - whether the number is in the 1, 10, 100, or 1000 position of the original number
            integer (Int) - the actual value of the number (1 through 9)

            Returns: Str
        """
        numeral_set = self.ROMAN_NUMERALS_BASE_TEN_MAP[base_ten]
        if integer in [1, 2, 3]:
            return ''.join([numeral_set[0] for i in range(0, integer)])
        elif integer == 4:
            return '{}{}'.format(numeral_set[0], numeral_set[1])
        elif integer == 5:
            return numeral_set[1]
        elif integer in [6, 7, 8]:
            remainder = integer - 5
            remainder_as_numeral = ''.join([numeral_set[0] for i in range(0, remainder)])
            return '{}{}'.format(numeral_set[1], remainder_as_numeral)
        elif integer == 9:
            next_set = self.ROMAN_NUMERALS_BASE_TEN_MAP[base_ten + 1]
            return '{}{}'.format(numeral_set[0], next_set[0])

    def set_numeral(self):
        """ Converts a given number into its equivalent Roman Numeral.

            Parameters:
            number (Int) - the number to convert

            Returns: Str
        """

        int_as_str = str(self.number)
        base_ten = len(int_as_str) - 1

        numerals = []

        for i in int_as_str:
            if i != '0':
                numerals.append(self.get_numeral(base_ten, int(i)))
            base_ten -= 1

        self.numeral = ''.join(numerals)


class RomanNumeralXCalculator(object):
    """ Class for generating count of occurrances of "X" for Roman Numerals in given range."""

    def __init__(self, range_min, range_max, debug=False):
        """ Sets initial values to use for calculations and then runs them.
            Parameters:
            min (Int) - the number at which to start the range (inclusive)
            max (Int) - the number at which to end the range (inclusive)
            debug (Bool) - set to true if you want to verify the generated numerals and their "X" counts

            Returns: Int
        """
        self.range_min = range_min
        self.range_max = range_max
        self.debug = debug
        self.x_count = 0
        self.count_x_for_range()

    def count_x_for_range(self):
        """ Calculate the number of times the character 'X' appears for all Roman Numerals in given range.

        """
        numerals = [RomanNumeral(numeral) for numeral in range(self.range_min, self.range_max + 1)]
        x_count = 0
        for numeral in numerals:
            x_in_numeral = len([i for i in numeral.numeral if i == 'X'])
            if self.debug:
                print('numeral: {} (x: {})'.format(numeral, x_in_numeral))
            x_count += x_in_numeral
        self.x_count = x_count


numerals = RomanNumeralXCalculator(1, 2660)
print(numerals.x_count)
