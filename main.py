from random import choice
from random import randint

MY_CALL = 'KI5XYZ'


class RandomOperator:
    def __init__(self):
        self.call = 'KG4ABC'
        self.qth = 'Phoenix Phoenix AZ AZ'
        self.name = 'Phil'
        self.rig = 'IC 7300'
        self.wx = 'rainy 65 deg'
        self.skcc = 'skcc %s%s%i%s' % (
            choice(['nr ', '']),
            choice(['is ', '']),
            randint(1000, 25000),
            choice(['C', 'T', ''])
        )

    def __str__(self):
        all_features = [self.call, self.qth, self.name, self.rig, self.wx, self.skcc]
        return str(all_features)


def intro(operator: RandomOperator):
    full = MY_CALL + ' DE ' + operator.call
    return choice(['BK', full])


if __name__ == '__main__':
    op = RandomOperator()
    print(intro(op))
    print(op)
