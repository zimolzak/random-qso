from random import choice
from random import randint
from string import ascii_uppercase

ARRL_SECTIONS = []
with open('arrl-sections.csv') as fh:
    for line in fh:
        fields = line.replace('\n', '').split(',')
        ARRL_SECTIONS.append(fields[1])


def random_suffix(p_two_char=1 / 26):
    n_null = round(-26 * p_two_char / (p_two_char - 1))
    uppercase_plus_null = list(ascii_uppercase) + [''] * n_null
    return choice(ascii_uppercase) + choice(ascii_uppercase) + choice(uppercase_plus_null)


class RandomQso:
    def __init__(self, my_call='KI5XYZ', my_name=''):
        self.my_call = my_call
        self.my_name = my_name
        self.call = '%s%s%s' % (
            choice('KG KI W K KA'.split()),
            randint(0, 9),
            random_suffix(p_two_char=1 / 3)
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
        self.rig = 'rig ' + \
                   choice(['is ', '']) + \
                   choice(['IC 7300', 'Kenwood TS 940S', 'TS 890S', 'Yaesu FT 1000',
                           'FT DX 101D', 'FT DX 10', 'Yaesu FT 101'])
        self.wx = 'WX %s%s%s %i deg' % (
            choice(['', 'is ']),
            choice('rainy cloudy clr'.split()),
            choice([' es', '']),
            randint(35, 99)
        )
        skcc_stub = str(randint(1000, 25000)) + choice(['C', 'T', ''])
        self.skcc = 'skcc %s%s%s %s' % (
            choice(['nr ', '']),
            choice(['is ', '']),
            skcc_stub,
            skcc_stub
        )
        r = randint(4, 5)
        s = randint(5, 9)
        t = choice(['n', '9'])
        self.rst = 'UR %s%i%i%s %i%i%s' % (
            choice(['rst ', 'rst is ', '']),
            r, s, t, r, s, t
        )
        self.good_morning = choice([' gm ', ' ga ', ' ge '])

        # ARRL Sweepstakes elements

        self.ser = randint(100, 9999)
        self.pre = choice("Q A B U M S".split())
        self.ck = randint(10, 99)
        self.sec = choice(ARRL_SECTIONS)  # In theory should match the state but whatever

    def intro(self):
        # class method so it can be different each time
        full = self.my_call + ' DE ' + self.call
        return choice(['BK', full])
        pass

    def outro_over(self):
        outro_stub = self.intro()
        if outro_stub == 'BK':
            return ' BK'
        else:
            return ' = ' + outro_stub + choice([' k', ' k', ' kn'])

    def first(self):
        return(
                self.intro() + ' ' +
                self.rst + ' = ' +
                self.name + ' = ' +
                self.qth +
                self.outro_over()
        )

    def second(self):
        return (
                self.intro() +
                self.good_morning + self.my_name + ' nice to meet u = ' +
                self.wx + ' = ' +
                self.rig +
                self.outro_over()
        )

    def third(self):
        return (
                self.intro() +
                ' R R FB ' + self.my_name +
                choice([' = ', ' ']) +
                self.skcc + ' QSL?' +
                self.outro_over()
        )

    def arrl_ss_short(self):
        return "%s %s %s %s %s" % (self.ser, self.pre, self.call, self.ck, self.sec)

    def arrl_ss_long(self):
        return "%s de %s %s" % (self.my_call, self.call, self.arrl_ss_short())

    def __str__(self):
        all_features = [self.intro(), self.rst, self.name, self.qth, self.wx, self.rig, self.skcc]
        return str(all_features)
    # rst === name qth skcc
    # gm name nice to meet u === wx === rig


if __name__ == '__main__':
    qso = RandomQso(my_call='KI5XYZ', my_name='Andy')
    print(qso.first())
    print(qso.second())
    print(qso.third())
    print(qso.arrl_ss_long())
    print(qso.arrl_ss_short())
