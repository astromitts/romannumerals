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
