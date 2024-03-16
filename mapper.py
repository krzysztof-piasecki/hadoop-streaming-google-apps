#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        values = line.strip().split('\x01')
        developer_id = values[21]
        released = values[13]
        rating = values[3]
        rating_count = values[4]

        # Sprawdzanie, czy rating i rating_count są dostępne i czy liczba ocen jest >= 1000
        if rating != 'null' and rating_count != 'null' and int(rating_count) >= 1000:
            rating = float(rating)
            rating_count = int(rating_count)
            # Parsowanie daty wydania, aby uzyskać rok
            year = released.split(' ')[-1]  # Biorąc pod uwagę format "Miesiąc Dzień, Rok"
            print(f"\t{developer_id}\t{year}\t{rating}\t{rating_count}\t1")
    except ValueError:
        continue
