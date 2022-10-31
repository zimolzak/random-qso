from main import RandomQso

NUMBER_OF_RANDOM_EXCHANGES = 10

if __name__ == '__main__':
    for i in range(NUMBER_OF_RANDOM_EXCHANGES):
        qso = RandomQso(my_call='KI5PED')
        print(qso.arrl_ss(), ' =')
