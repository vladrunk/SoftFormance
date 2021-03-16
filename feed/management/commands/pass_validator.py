from itertools import count

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        start()


def start():
    raw_data, i = [], 1
    while i < 5:
        user_input = [
            int(d) for d in input(f'Enter #{i}: ').split(',')
            if d.isdecimal() and int(d) > 0
        ]
        if len(user_input) != 2:
            print(f'Wrong input #{i}. Try again...')
            continue
        else:
            i += 1
            raw_data.append(user_input)
    for (count_arr, len_arr) in raw_data:
        raw_arr = [[] for _ in range(count_arr)]
        limit = count_arr * len_arr
        cur_arr, num = 0, 1
        while limit:
            raw_arr[cur_arr].append(num)
            if not num % len_arr:
                cur_arr += 1
            num += 1
            limit -= 1
        print(raw_arr)
