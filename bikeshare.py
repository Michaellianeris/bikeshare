import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS   = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


# ---------------------------------------------------------------------------
# Helper: prompt until the user gives a valid answer
# ---------------------------------------------------------------------------
def _ask(prompt, valid_options):
    """Loop until the user enters one of valid_options (case-insensitive)."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid_options:
            return answer
        print(f"  ⚠  Invalid input. Please choose from: {', '.join(valid_options)}")


# ---------------------------------------------------------------------------
# 1. get_filters
# ---------------------------------------------------------------------------
def get_filters():
    """
    Asks user to specify a city, month, and day to analyse.

    Returns:
        (str) city  – name of the city to analyse
        (str) month – name of the month to filter by, or 'all'
        (str) day   – name of the day of week to filter by, or 'all'
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    print('-' * 40)

    # --- city ---
    city = _ask(
        "Which city would you like to explore?\n"
        "  → chicago / new york city / washington\n"
        "Your choice: ",
        valid_options=list(CITY_DATA.keys())
    )

    # --- filter type ---
    filter_type = _ask(
        "\nWould you like to filter the data by month, day, both, or not at all?\n"
        "  → month / day / both / none\n"
        "Your choice: ",
        valid_options=['month', 'day', 'both', 'none']
    )

    # --- month ---
    if filter_type in ('month', 'both'):
        month = _ask(
            "\nWhich month?\n"
            "  → january / february / march / april / may / june\n"
            "Your choice: ",
            valid_options=MONTHS
        )
    else:
        month = 'all'

    # --- day ---
    if filter_type in ('day', 'both'):
        day = _ask(
            "\nWhich day of the week?\n"
            "  → monday / tuesday / wednesday / thursday / friday / saturday / sunday\n"
            "Your choice: ",
            valid_options=DAYS
        )
    else:
        day = 'all'

    print('-' * 40)
    return city, month, day


# ---------------------------------------------------------------------------
# 2. load_data
# ---------------------------------------------------------------------------
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and/or day.

    Args:
        city  (str) – city name key from CITY_DATA
        month (str) – month name or 'all'
        day   (str) – weekday name or 'all'

    Returns:
        df – filtered Pandas DataFrame
    """
    df = pd.read_csv(CITY_DATA[city])

    # Parse Start Time once
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Derived columns used by multiple stat functions
    df['month']       = df['Start Time'].dt.month          # 1-12
    df['day_of_week'] = df['Start Time'].dt.day_name()     # e.g. 'Monday'
    df['hour']        = df['Start Time'].dt.hour            # 0-23

    # Filter by month
    if month != 'all':
        df = df[df['month'] == MONTHS.index(month) + 1]

    # Filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


# ---------------------------------------------------------------------------
# 3. time_stats
# ---------------------------------------------------------------------------
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Most common month
    common_month_num = df['month'].mode()[0]
    common_month     = MONTHS[common_month_num - 1].title()
    print(f"  Most Common Month      : {common_month}")

    # Most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"  Most Common Day        : {common_day}")

    # Most common start hour
    common_hour = df['hour'].mode()[0]
    print(f"  Most Common Start Hour : {common_hour:02d}:00")

    print(f"\n  [Took {time.time() - start_time:.4f} seconds]")
    print('-' * 40)


# ---------------------------------------------------------------------------
# 4. station_stats
# ---------------------------------------------------------------------------
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Most common start station
    common_start = df['Start Station'].mode()[0]
    print(f"  Most Common Start Station : {common_start}")

    # Most common end station
    common_end = df['End Station'].mode()[0]
    print(f"  Most Common End Station   : {common_end}")

    # Most common trip (start → end combination)
    df['trip'] = df['Start Station'] + '  →  ' + df['End Station']
    common_trip = df['trip'].mode()[0]
    print(f"  Most Common Trip          : {common_trip}")

    print(f"\n  [Took {time.time() - start_time:.4f} seconds]")
    print('-' * 40)


# ---------------------------------------------------------------------------
# 5. trip_duration_stats
# ---------------------------------------------------------------------------
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_seconds = int(df['Trip Duration'].sum())
    mean_seconds  = df['Trip Duration'].mean()

    def fmt(seconds):
        h, rem = divmod(int(seconds), 3600)
        m, s   = divmod(rem, 60)
        return f"{h}h {m}m {s}s"

    print(f"  Total Travel Time   : {fmt(total_seconds)}  ({total_seconds:,} seconds)")
    print(f"  Average Travel Time : {fmt(mean_seconds)}  ({mean_seconds:,.1f} seconds)")

    print(f"\n  [Took {time.time() - start_time:.4f} seconds]")
    print('-' * 40)


# ---------------------------------------------------------------------------
# 6. user_stats
# ---------------------------------------------------------------------------
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts of user types
    print("  User Type Counts:")
    for utype, count in df['User Type'].value_counts().items():
        print(f"    {utype:<15}: {count:,}")

    # Gender (Chicago & NYC only)
    if 'Gender' in df.columns:
        print("\n  Gender Counts:")
        for gender, count in df['Gender'].value_counts().items():
            print(f"    {gender:<15}: {count:,}")
        missing = df['Gender'].isna().sum()
        if missing:
            print(f"    (Not specified  : {missing:,})")
    else:
        print("\n  Gender data not available for this city.")

    # Birth year (Chicago & NYC only)
    if 'Birth Year' in df.columns:
        earliest   = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode()[0])
        print(f"\n  Birth Year Stats:")
        print(f"    Earliest    : {earliest}")
        print(f"    Most Recent : {most_recent}")
        print(f"    Most Common : {most_common}")
    else:
        print("\n  Birth year data not available for this city.")

    print(f"\n  [Took {time.time() - start_time:.4f} seconds]")
    print('-' * 40)


# ---------------------------------------------------------------------------
# 7. display_raw_data
# ---------------------------------------------------------------------------
def display_raw_data(df):
    """Prompts the user and prints 5 rows of raw data at a time."""
    idx = 0
    # Drop helper columns we added internally
    display_df = df.drop(columns=['month', 'day_of_week', 'hour', 'trip'],
                         errors='ignore')
    total = len(display_df)

    while idx < total:
        show = _ask(
            "\nWould you like to see 5 rows of raw data? Enter yes or no.\n"
            "Your choice: ",
            valid_options=['yes', 'no']
        )
        if show != 'yes':
            break
        print(display_df.iloc[idx: idx + 5].to_string())
        idx += 5
        if idx >= total:
            print("\n  (No more raw data to display.)")


# ---------------------------------------------------------------------------
# 8. main
# ---------------------------------------------------------------------------
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print("\n  ⚠  No data found for the selected filters. Please try again.")
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            display_raw_data(df)

        restart = _ask(
            '\nWould you like to restart? Enter yes or no.\n'
            'Your choice: ',
            valid_options=['yes', 'no']
        )
        if restart != 'yes':
            print("\nThank you for exploring US bikeshare data. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
