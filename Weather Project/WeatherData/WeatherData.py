import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
from helper import all_cities
from helper import louisville_city
from averages import seven_year_moving_average
from averages import ten_year_moving_average
from averages import fifteen_year_moving_average
from averages import all_moving_averages


def moving_average():

    print("\nWELCOME TO THE MOVING AVERAGE WEATHER DATA PLOTTING PROGRAM!\n\n/////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

    keepGoing = True
    while keepGoing:

        print("\n\nHello! Would you like to see the list of cities, or weather for Louisville, KY only?")
        print("Please type 'all cities', 'Louisville', or 'no'. ")

        show_cities = str(input().strip().lower())
        accepted_responses = ['all cities','louisville', 'no']

        while show_cities not in accepted_responses:
            print("\nHmm, I didn't understand. Please type 'all cities', 'Louisville', or 'no'\n")
            show_cities = str(input().strip().lower())
        
        if show_cities == 'no':
            keepGoing = False
            print("\nOk! This program will now terminate.")
            time.sleep(2)
            break
        else:
            print("\nYou have selected {}".format(show_cities.capitalize()))


        if show_cities == 'all cities':

            city_selection = all_cities()
            user_city = city_selection[0]
            city_temp = city_selection[1]

        if show_cities == 'louisville':

            city_selection = louisville_city()
            user_city = city_selection[0]
            city_temp = city_selection[1]


        print("\nWould you like to see the 7, 10, or 15-yr temp rolling average for your city as compared to global temps?")
        print("\nPlease type '7', '10', '15', or 'all'")
        rolling_average_inputs = ["7", "10", "15" , "all"]
        
        type_selection = input().strip().lower()
        
        while type_selection not in rolling_average_inputs:
            print("\nPlease make a valid selection. '7', '10', '15', or 'all' \n")
            type_selection = input().strip().lower()

        #create plot for moving averages here
        
        if type_selection == 'all':

            all_moving_averages(city_temp, user_city)
            
        elif type_selection == '7':

            seven_year_moving_average(city_temp, user_city)
        
        elif type_selection == '10':

            ten_year_moving_average(city_temp, user_city)
            
        elif type_selection == '15':

            fifteen_year_moving_average(city_temp, user_city)

        print("Do you want to look at another city?\n")
        onward = str(input().strip().lower())

        while onward not in ['yes','no']:
            print("\nPlease type yes or no.\n")
            onward = str(input().strip().lower())

        if onward == 'yes':
            keepGoing = True
        elif onward == 'no':
            keepGoing = False
            print("\nOk! This program will now terminate.")
            time.sleep(2)

moving_average()
