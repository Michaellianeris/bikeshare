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


# RESOURCES & REFERENCES

The following resources were consulted during development:

1. Pandas Documentation — DataFrame, Series, and datetime accessor methods
   https://pandas.pydata.org/docs/

2. pandas.to_datetime() reference
   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html

3. pandas Time/Date Components (dt accessor: .month, .day_name(), .hour)
   https://pandas.pydata.org/docs/user_guide/timeseries.html#time-date-components

4. pandas Series.mode() — finding the most frequent value
   https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html

5. pandas Series.value_counts() — counting unique values
   https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html

6. Python datetime module documentation
   https://docs.python.org/3/library/datetime.html

7. Python time module (used for performance timing)
   https://docs.python.org/3/library/time.html

8. NumPy Documentation (general reference)
   https://numpy.org/doc/

9. Udacity — Programming for Data Science with Python
   Course materials, quizzes, and project template (bikeshare_2.py)

10. Motivate — original bike-share system data sources
    Chicago:       https://www.divvybikes.com/system-data
    New York City: https://www.citibikenyc.com/system-data
    Washington DC: https://www.capitalbikeshare.com/system-data


# FILE STRUCTURE

  bikeshare.py         — Main Python script   
  readme.txt           — This file            

  chicago.csv          — Chicago data         
  new_york_city.csv    — New York City data   
  washington.csv       — Washington DC data   


