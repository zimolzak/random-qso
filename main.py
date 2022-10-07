from random import choice
from random import randint
from string import ascii_uppercase


def random_suffix():
    uppercase_plus_null = list(ascii_uppercase) + ['']
    return choice(ascii_uppercase) + choice(ascii_uppercase) + choice(uppercase_plus_null)


class RandomQso:
    def __init__(self, my_call, my_name):
        self.my_call = my_call
        self.my_name = my_name
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
        self.qth = 'QTH%s %s %s %s %s' % (
            choice([' is', '']),
            city_state[0], city_state[0], city_state[1], city_state[1]
        )
        name_once = choice('John Phil Bob Mary Ali Alex Tom Dennis Lou Leo Larry Ann'.split())
        self.name = '%s %s %s' % (
            choice(['name is', 'name', 'op']),
            name_once,
            name_once
        )
        self.rig = 'rig ' +\
                   choice(['is ', '']) +\
                   choice(['IC 7300', 'Kenwood TS 940S', 'TS 890S', 'Yaesu FT 1000',
                           'FT DX 101D', 'FT DX 10', 'Yaesu FT 101'])
        self.wx = 'WX %s%s%s %i deg' % (
            choice(['', 'is ']),
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
        self.good_morning = choice([' gm ', ' ga ', ' ge '])

    def intro_outro(self):
        # class method so it can be different each time
        full = self.my_call + ' DE ' + self.call
        return choice(['BK', full])
        pass

    def second(self):
        return (
            self.intro_outro() +
            self.good_morning + self.my_name + ' nice to meet u = ' +
            self.wx + ' = ' +
            self.rig + ' = ' +
            self.intro_outro()
        )

    def __str__(self):
        all_features = [self.intro_outro(), self.qth, self.name, self.rig, self.wx, self.skcc, self.rst]
        return str(all_features)
    # rst === name qth skcc
    # gm name nice to meet u === wx === rig


if __name__ == '__main__':
    qso = RandomQso(my_call='KI5XYZ', my_name='Andy')
    print(qso)
    print(qso.second())
