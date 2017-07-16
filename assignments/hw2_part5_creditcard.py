'''
Homework Assignment 2:
Part 5: 
'''


class CreditCard:

    def __init__(self, card_number):
        self.card_number = card_number
        self.card_type = "INVALID"
        self.valid = False

        self.determine_card_type()

# Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):

        digits = self.card_number

        if digits[:4] == "6011":
            self.card_type = "DISCOVER"
        elif int(digits[0]) == 4:
            self.card_type = "VISA"
        elif int(digits[0]) == 5 and (int(digits[1]) > 0 or int(digits[1]) < 6):
            self.card_type = "MASTERCARD"
        elif int(digits[0]) == 3 and (int(digits[1]) == 4 or int(digits[1]) == 7):
            self.card_type = "AMEX"

        if self.card_type in ("INVALID"):
            self.valid = False
            return self.card_type

           # check if length is valid. if not then return
        if not self.check_length():
            self.card_type = "INVALID"
            return self.card_type
        # check if passes luhn algo.
        if not self.validate():
            self.card_type = "INVALID"
            return self.card_type

        return self.card_type

        # Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        num_digits = len(self.card_number)
        if self.card_type in ("VISA", "MASTERCARD", "DISCOVER"):
            self.valid = num_digits == 16
            return self.valid

        if self.card_type == "AMEX":
            self.valid = num_digits == 15
            return self.valid

        return self.valid

# Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        self.valid = luhn_checksum(self.card_number) == 0
        return self.valid


def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10

# do not modify assert statements


cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"


cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')
assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"
