from random import choice

MY_CALL = 'KI5XYZ'


class RandomOperator:
    def __init__(self):
        self.call = 'KG4ABC'
        self.qth = 'Phoenix'
        self.name = 'Phil'


def intro(operator: RandomOperator):
    full = MY_CALL + ' DE ' + operator.call
    return choice(['BK', full])


if __name__ == '__main__':
    op = RandomOperator()
    print(intro(op))
