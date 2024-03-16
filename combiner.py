#!/usr/bin/env python3

import sys

current_key = None
sum_ratings = 0
total_rating_count = 0
app_count = 0

for line in sys.stdin:
    key, year, rating, rating_count, _ = line.strip().split("\t")
    composite_key = f"{key},{year}"
    rating_count = int(rating_count)

    if composite_key == current_key:
        # Zamiast zliczać wystąpienia, sumujemy rating_count z różnych aplikacji
        sum_ratings += float(rating) * rating_count
        total_rating_count += rating_count
        app_count += 1
    else:
        if current_key:
            print(f"{current_key}\t{sum_ratings}\t{total_rating_count}\t{app_count}")
        current_key = composite_key
        sum_ratings = float(rating) * rating_count
        total_rating_count = rating_count
        app_count = 1

if current_key:
    print(f"{current_key}\t{sum_ratings}\t{total_rating_count}\t{app_count}")
