#  Explore US Bikeshare Data — Project README


Author      : Michael Lianeris
Project     : Bikeshare Data Analysis


This script analyses bike-share usage data for three US cities:
  • Chicago         (chicago.csv)
  • New York City   (new_york_city.csv)
  • Washington DC   (washington.csv)

The data covers the first six months of 2017 and was provided by Motivate,
a bike-share system operator. The script is fully interactive: the user selects
a city and optional filters (month, day, or both), then sees descriptive
statistics followed by an option to view the raw data 5 rows at a time.

# STATISTICS COMPUTED

1. Popular Times of Travel
   - Most common month
   - Most common day of the week
   - Most common start hour

2. Popular Stations and Trips
   - Most common start station
   - Most common end station
   - Most common start → end trip combination

3. Trip Duration
   - Total travel time
   - Average travel time

4. User Info
   - Counts of each user type
   - Counts by gender          (Chicago & New York City only)
   - Earliest, most recent,
     and most common birth year (Chicago & New York City only)

# HOW TO RUN

Prerequisites:
  Python 3.x, pandas, numpy  (install via: pip install pandas numpy)

Place the three CSV files in the same directory as bikeshare.py, then run:

  python bikeshare.py

Follow the on-screen prompts. At the end of each analysis session the script
asks whether you want to restart or exit.

# FILE STRUCTURE

  bikeshare.py         — Main Python script   
  readme.txt           — This file            

  chicago.csv          — Chicago data         
  new_york_city.csv    — New York City data   
  washington.csv       — Washington DC data   


