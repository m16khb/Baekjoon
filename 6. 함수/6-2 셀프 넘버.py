def self_number_printer():
    number = set(range(1, 10001))
    none_self_number = set()

    for i in range(1, 10001):
        clone = i
        my_sum = 0
        while clone != 0:
            my_sum += clone % 10
            clone = int(clone / 10)
        none_self_number.add(i + my_sum)

    self_number = number - none_self_number

    for i in sorted(self_number):
        print(i)


self_number_printer()
