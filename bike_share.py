import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6}
MONTHS_KEY_LIST = list(MONTHS.keys())
MONTHS_VALUE_LIST  = list(MONTHS.values())
DAYS_OF_WEEK = {'sat': 5, 'sun': 6, 'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4}
DAYS_OF_WEEK_KEY_LIST = list(DAYS_OF_WEEK.keys())
DAYS_OF_WEEK_VALUE_LIST  = list(DAYS_OF_WEEK.values())
def get_filters():

       """
       Asks user to specify a city, month, and day to analyze.

       Returns:
              (str) city - name of the city to analyze
              (str) month - name of the month to filter by, or "all" to apply no month filter
              (str) day - name of the day of week to filter by, or "all" to apply no day filter
       """
       while True:

              print('Hello! Let\'s explore some US bikeshare data!')

              # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
              print('Would you like to see data for (Chicago, New York, or Washington) ?')
              city=input().lower()
              if city not in CITY_DATA.keys():
                     print("Sorry, there is no city called '{}' . The program will restart....".format(city.title()))
                     print('-' * 40)
                     continue

              # get which type of filters to filter by  (month, day, both, or Not at all )
              print('Would you like to filter by (month, day, both, or Not at all) ?')
              filter_by = input().lower()
              if filter_by == 'month':
              # get user input for month (Jan, Feb, Mar, Apr, May, Jun)
                     print('Which month (Jan, Feb, Mar, Apr, May, Jun) ?')
                     month = input().lower()
                     if month not in MONTHS.keys():
                            print("Sorry, there is no month called '{}' . The program will restart....".format(month.title()))
                            print('-' * 40)
                            continue
                     day = 'all'

              elif filter_by == 'day':
              # get user input for day of week (Sat, Sun, Mon, Tue, Wed, Thu, or Fri)
                     print('which day (Sat, Sun, Mon, Tue, Wed, Thu, or Fri) ?')
                     day = input().lower()
                     if day not in DAYS_OF_WEEK.keys():
                            print("Sorry, there is no day called '{}' . The program will restart....".format(day.title()))
                            print('-' * 40)
                            continue
                     month = 'all'
              elif filter_by == 'both':
                     print('Which month (Jan, Feb, Mar, Apr, May, Jun) ?')
                     month = input().lower()
                     if month not in MONTHS.keys():
                            print("Sorry, there is no month called '{}' . The program will restart....".format(month.title()))
                            print('-' * 40)
                            continue
                     print('which day (Sat, Sun, Mon, Tue, Wed, Thu, or Fri) ?')
                     day = input().lower()
                     if day not in DAYS_OF_WEEK.keys():
                            print("Sorry, there is no day called '{}' . The program will restart....".format(day.title()))
                            print('-' * 40)
                            continue
              elif filter_by == 'not at all':
                     month = 'all'
                     day = 'all'
              else :
                     print('Sorry, there is no filter called {} . The program will restart....'.format(filter_by.title()))
                     print('-' * 40)
                     continue
              print('Have you chosen these?')
              print('Filter: {}'.format(filter_by))
              print('City: {}'.format(city))
              print('Month: {}'.format(month))
              print('Day: {}'.format(day))
              print("Press 'yes' to start the calculation or 'no' to restart the program.")
              start=input().lower()
              if start == 'yes':
                     break
              else:
                     print('-' * 40)
                     continue
       return city, month, day


def load_data(city, month, day):
       """
       Loads data for the specified city and filters by month and day if applicable.

       Args:
              (str) city - name of the city to analyze
              (str) month - name of the month to filter by, or "all" to apply no month filter
              (str) day - name of the day of week to filter by, or "all" to apply no day filter
       Returns:
               df - Pandas DataFrame containing city data filtered by month and day
       """

       df = pd.read_csv(CITY_DATA[city])
       df['Start Time'] = pd.to_datetime(df['Start Time'])
       df['month'] = df['Start Time'].dt.month
       df['day_of_week'] = df['Start Time'].dt.weekday
       df['hour'] = df['Start Time'].dt.hour
       df['Trip'] =  df['Start Station'] + ' to ' + df['End Station']
       # filter by month if applicable
       if month != 'all':
              # use the index of the months dict to get the corresponding int
              month = MONTHS[month]
              df = df[df['month'] == month]
       if day != 'all':
              # filter by day of week to create the new dataframe
              df = df[df['day_of_week'] == DAYS_OF_WEEK[day]]
       return df


def time_stats(df):

       """Displays statistics on the most times of travel."""

       print('\nCalculating The Most Frequent Times of Travel...\n')
       start_time = time.time()

       # display the most common month
       month = df['month'].value_counts().idxmax()
       print('Most frequent month:', MONTHS_KEY_LIST[MONTHS_VALUE_LIST.index(month)].title())
       month_count = df['month'].value_counts().max()
       print('Count:',month_count)

       # display the most common day of week
       day_of_week = df['day_of_week'].value_counts().idxmax()
       print('Most frequent day of week:', DAYS_OF_WEEK_KEY_LIST[DAYS_OF_WEEK_VALUE_LIST.index(day_of_week)].title())
       day_of_week_count = df['day_of_week'].value_counts().max()
       print('Count:', day_of_week_count)

       # display the most common start hour
       hour = df['hour'].value_counts().idxmax()
       print('Most frequent hour:',hour)
       hour_count = df['hour'].value_counts().max()
       print('Count:', hour_count)

       print("\nThis took %s seconds." % (time.time() - start_time))
       print('-'*40)


def station_stats(df):

       """Displays statistics on the most popular stations and trip."""

       print('\nCalculating The Most Popular Stations and Trip...\n')
       start_time = time.time()

       # display most commonly used start station
       start_station = df['Start Station'].value_counts().idxmax()
       print('Most frequent start station:',start_station)
       start_station_count = df['Start Station'].value_counts().max()
       print('Count',start_station_count)

       # display most commonly used end station

       end_station = df['End Station'].value_counts().idxmax()
       print('Most frequent end station:', end_station)
       end_station_count = df['End Station'].value_counts().max()
       print('Count', end_station_count)

       # display most frequent combination of start station and end station trip
       trib= df['Trip'].value_counts().idxmax()
       print('Most frequent trip:', trib)
       trib_count = df['Trip'].value_counts().max()
       print('Count:', trib_count)

       print("\nThis took %s seconds." % (time.time() - start_time))
       print('-'*40)       
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        #trip_duration_stats(df)
        #user_stats(df,city)
        #display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
       main()

