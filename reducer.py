#!/usr/bin/env python3

import sys

current_key = None
sum_ratings = 0
total_rating_count = 0
app_count = 0

for line in sys.stdin:
    composite_key, sum_ratings_input, total_rating_count_input, app_count_input = line.strip().split("\t")
    sum_ratings_input = float(sum_ratings_input)
    total_rating_count_input = int(total_rating_count_input)
    app_count_input = int(app_count_input)

    if composite_key == current_key:
        sum_ratings += sum_ratings_input
        total_rating_count += total_rating_count_input
        app_count += app_count_input
    else:
        if current_key:
            print(f"{current_key}\t{sum_ratings}\t{total_rating_count}\t{app_count}")
        current_key = composite_key
        sum_ratings = sum_ratings_input
        total_rating_count = total_rating_count_input
        app_count = app_count_input

if current_key:
    print(f"{current_key}\t{sum_ratings}\t{total_rating_count}\t{app_count}")
