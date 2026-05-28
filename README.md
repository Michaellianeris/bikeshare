# 🚲 Explore US Bikeshare Data

A Python command-line application that analyses bike-share usage data for three major US cities: **Chicago**, **New York City**, and **Washington DC**.

Built as part of the **Udacity Programming for Data Science with Python** nanodegree.

---

## 📊 Overview

This interactive script lets you explore bike-share data from the first six months of 2017, provided by [Motivate](https://www.motivateco.com/). Filter by city, month, and day of the week to uncover usage patterns and statistics.

---

## 🏙️ Cities Covered

| City | File |
|------|------|
| Chicago | `chicago.csv` |
| New York City | `new_york_city.csv` |
| Washington DC | `washington.csv` |

---

## 📈 Statistics Computed

### ⏰ Popular Times of Travel
- Most common month
- Most common day of the week
- Most common start hour

### 🚉 Popular Stations & Trips
- Most common start station
- Most common end station
- Most common start → end trip combination

### ⏱️ Trip Duration
- Total travel time
- Average travel time

### 👤 User Info
- Counts by user type (Subscriber / Customer)
- Counts by gender *(Chicago & NYC only)*
- Earliest, most recent, and most common birth year *(Chicago & NYC only)*

---

## ▶️ How to Run

### Prerequisites
Make sure you have Python 3 and the required libraries installed:

```bash
pip install pandas numpy
```

### Run the script
Place the three CSV data files in the same folder as `bikeshare.py`, then:

```bash
python bikeshare.py
```

### Example interaction
```
Hello! Let's explore some US bikeshare data!
----------------------------------------
Which city would you like to explore?
  → chicago / new york city / washington
Your choice: chicago

Would you like to filter the data by month, day, both, or not at all?
  → month / day / both / none
Your choice: month

Which month?
  → january / february / march / april / may / june
Your choice: june

Calculating The Most Frequent Times of Travel...

  Most Common Month      : June
  Most Common Day        : Tuesday
  Most Common Start Hour : 17:00
```

---

## 📁 Project Structure

```
bikeshare/
│
├── bikeshare.py          # Main Python script
├── readme.txt            # Project references
├── README.md             # This file
│
├── chicago.csv           # Chicago data (not included)
├── new_york_city.csv     # New York City data (not included)
└── washington.csv        # Washington DC data (not included)
```

> ⚠️ The CSV data files are not included in this repository. They can be obtained from [Motivate](https://www.motivateco.com/) or through the Udacity course resources.

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [pandas](https://pandas.pydata.org/)
- [NumPy](https://numpy.org/)

---

## 📚 References

- [pandas Documentation](https://pandas.pydata.org/docs/)
- [Python datetime module](https://docs.python.org/3/library/datetime.html)
- [Udacity — Programming for Data Science with Python](https://www.udacity.com/)
- Original data: [Divvy Bikes](https://www.divvybikes.com/system-data) · [Citi Bike NYC](https://www.citibikenyc.com/system-data) · [Capital Bikeshare](https://www.capitalbikeshare.com/system-data)

---

## 👤 Author

**Michael Lianeris**  
[GitHub](https://github.com/Michaellianeris)

---

*Project completed as part of Udacity's Programming for Data Science with Python Nanodegree*
