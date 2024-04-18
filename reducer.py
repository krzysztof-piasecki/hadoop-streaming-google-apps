#!/usr/bin/env python3

import sys

current_developer_id = None
current_key = None
sum_ratings = 0
total_rating_count = 0
app_count = 0
current_year = None
for line in sys.stdin:
    developer_id, year, sum_ratings_input, total_rating_count_input, app_count_input = line.strip().split("\t")
    composite_key = f"{developer_id},{year}"
    sum_ratings_input = float(sum_ratings_input)
    total_rating_count_input = int(total_rating_count_input)
    app_count_input = int(app_count_input)

    if composite_key == current_key:
        sum_ratings += sum_ratings_input
        total_rating_count += total_rating_count_input
        app_count += app_count_input
    else:
        if current_key:
            print(f"{current_developer_id}\t{current_year}\t{int(sum_ratings)}\t{total_rating_count}\t{app_count}")
        current_developer_id = developer_id
        current_year = year
        current_key = f"{current_developer_id},{current_year}"
        sum_ratings = sum_ratings_input
        total_rating_count = total_rating_count_input
        app_count = app_count_input

if current_key:
    print(f"{current_key}\t{current_year}\t{int(sum_ratings)}\t{total_rating_count}\t{app_count}")
