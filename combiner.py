#!/usr/bin/env python3
import sys

current_key = None
sum_ratings = 0
total_rating_count = 0
app_count = 0
current_year = None
current_developer_id = None

for line in sys.stdin:
    developer_id, year, rating, rating_count, _ = line.strip().split("\t")
    composite_key = f"{developer_id},{year}"
    rating = float(rating)
    rating_count = int(rating_count)

    if composite_key == current_key:
        sum_ratings += rating * rating_count
        total_rating_count += rating_count
        app_count += 1
    else:
        if current_key:
            print(f"{current_developer_id}\t{current_year}\t{sum_ratings}\t{total_rating_count}\t{app_count}")
        current_year = year
        current_developer_id = developer_id
        current_key = f"{current_developer_id},{current_year}"
        sum_ratings = rating * rating_count
        total_rating_count = rating_count
        app_count = 1

if current_key:
    print(f"{current_developer_id}\t{current_year}\t{sum_ratings}\t{total_rating_count}\t{app_count}")
