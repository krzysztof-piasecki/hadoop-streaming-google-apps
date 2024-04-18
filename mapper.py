#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        values = line.strip().split('\u0001')
        developer_id = values[21]
        released = values[13]
        rating = values[3]
        rating_count = values[4]

        if rating != 'null' and rating_count != 'null' and int(rating_count) >= 1000:
            rating = float(rating)
            rating_count = int(rating_count)
            year = released.split(' ')[-1]
            if year.isdigit():
                print(f"{developer_id}\t{year}\t{rating}\t{rating_count}\t1")
    except ValueError:
        continue
