from random import choice
from random import randint
from string import ascii_uppercase

MY_CALL = 'KI5XYZ'


def random_suffix():
    uppercase_plus_null = list(ascii_uppercase) + ['']
    return choice(ascii_uppercase) + choice(ascii_uppercase) + choice(uppercase_plus_null)


class RandomOperator:
    def __init__(self):
        self.call = '%s%s%s' % (
            choice('KG KI W K KA'.split()),
            randint(0, 9),
            random_suffix()
        )
        city_state = choice([['Phoenix', 'AZ'],
                             ['Troy', 'MI'],
                             ['St Paul', 'MN'],
                             ['San Diego', 'CA'],
                             ['Asheville', 'NC'],
                             ['Austin', 'TX'],
                             ['Omaha', 'NE']])
        self.qth = '%s %s %s %s' % (city_state[0], city_state[0], city_state[1], city_state[1])
        self.name = choice('John Phil Bob Mary Ali Alex Tom Dennis Lou Leo Larry Ann'.split())
        self.rig = choice(['IC 7300', 'Kenwood TS 940S', 'TS 890S', 'Yaesu FT 1000',
                           'FT DX 101D', 'FT DX 10', 'Yaesu FT 101'])
        self.wx = '%s%s %i deg' % (
            choice('rainy cloudy clr'.split()),
            choice([' es', '']),
            randint(35, 99)
        )
        self.skcc = 'skcc %s%s%i%s' % (
            choice(['nr ', '']),
            choice(['is ', '']),
            randint(1000, 25000),
            choice(['C', 'T', ''])
        )
        r = randint(4, 5)
        s = randint(5, 9)
        t = choice(['n', '9'])
        self.rst = 'UR %s%i%i%s %i%i%s' % (
            choice(['rst ', 'rst is ', '']),
            r, s, t, r, s, t
        )

    def __str__(self):
        all_features = [self.call, self.qth, self.name, self.rig, self.wx, self.skcc, self.rst]
        return str(all_features)


def intro(operator: RandomOperator):
    full = MY_CALL + ' DE ' + operator.call
    return choice(['BK', full])


if __name__ == '__main__':
    op = RandomOperator()
    print(intro(op))
    print(op)
