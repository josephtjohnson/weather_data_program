import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time

def input_clean_up(user_city):
    if len(user_city) > 1:
        correct_name = ""
        for name in user_city:
            correct_name += name.capitalize()
            correct_name += " "
        return correct_name.strip()
    else:
        return user_city[0]

def moving_average():

    keepGoing = True

    df = pd.read_csv(r'../weather_data.csv')

    cities = set(df['city'])

    print("\nWELCOME TO THE MOVING AVERAGE WEATHER DATA PLOTTING PROGRAM!\n\n/////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
    print("\n\nHello! Would you like to see the list of cities?\n")

    show_cities = str(input().strip().lower())
    accepted_responses = ['yes','no']

    while show_cities not in accepted_responses:
        print("\nHmm, I didn't understand. Please type yes or no\n")
        show_cities = str(input().strip().lower())
        
    if show_cities == 'yes':
        pass
    elif show_cities == 'no':
        keepGoing = False
        print("\nOk! This program will now terminate.")
        time.sleep(3)

    while keepGoing:

        for city in cities:
            print(city)

        print("\nWhich city would you like to investigate?")   
        user_city = input().capitalize().split()

        user_city = input_clean_up(user_city)

        while user_city not in cities:
            print("City must be in the list. Please try again.\n")
            user_city = input().capitalize().split()
            user_city = input_clean_up(user_city)

        print("\nYou have selected {0}".format(user_city))

        city_temp = pd.DataFrame(df, columns = ['year', 'city', 'country', 'avg_temp'])

        city_temp = city_temp[city_temp['city'] == user_city]
        
        print("\nWould you like to see the 7, 10, or 15-yr temp rolling average for your city as compared to global temps?")
        print("Please type '7', '10', '15', or 'all'")
        rolling_average_inputs = ["7", "10", "15" , "all"]
        
        type_selection = input().strip().lower()
        
        while type_selection not in rolling_average_inputs:
            print("\nPlease make a valid selection. '7', '10', '15', or 'all' \n")
            type_selection = input().strip().lower()

        city_temp['7-yr MA'] = city_temp.avg_temp.rolling(7).mean()
        city_temp['10-yr MA'] = city_temp.avg_temp.rolling(10).mean()
        city_temp['15-yr MA'] = city_temp.avg_temp.rolling(15).mean()
        city_temp['Global 7-yr MA'] = city_temp.avg_temp.1.rolling(7).mean()
        city_temp['Global 10-yr MA'] = city_temp.avg_temp.1.rolling(10).mean()
        city_temp['Global 15-yr MA'] = city_temp.avg_temp.1.rolling(15).mean()
        #avg_temp_global = pd.DataFrame(df, columns = ['year', 'country', 'avg_temp.1'])

        #create plot for moving averages here
        plt.figure(figsize = (12,5))
        
        if type_selection == 'all':

            sns.lineplot( x = 'year',
                 y = '7-yr MA',
                 data = city_temp,
                 label = 'Average Temperature - 7-yr Moving Average')

            sns.lineplot( x = 'year',
                 y = '10-yr MA',
                 data = city_temp,
                 label = 'Average Temperature - 10-yr Moving Average')

            sns.lineplot( x = 'year',
                 y = '15-yr MA',
                 data = city_temp,
                 label = 'Average Temperature - 15-yr Moving Average')
            
            sns.lineplot( x = 'year',
                y = 'Global 7-yr MA',
                data = city_temp,
                label = 'Average Global Temperature - 7-yr Moving Average')

            sns.lineplot( x = 'year',
                y = 'Global 10-yr MA',
                data = city_temp,
                label = 'Average Global Temperature - 10-yr Moving Average')

            sns.lineplot( x = 'year',
                y = 'Global 15-yr MA',
                data = city_temp,
                label = 'Average Global Temperature - 15-yr Moving Average')
            
        elif type_selection == '7':
            sns.lineplot( x = 'year',
                y = '7-yr MA',
                data = city_temp,
                label = 'Average Temperature - 7-yr Moving Average')
            
            sns.lineplot( x = 'year',
                y = 'Global 7-yr MA',
                data = city_temp,
                label = 'Average Global Temperature - 7-yr Moving Average')
        
        elif type_selection == '10':
            sns.lineplot( x = 'year',
                y = '10-yr MA',
                data = city_temp,
                label = 'Average Temperature - 10-yr Moving Average')
            
            sns.lineplot( x = 'year',
                y = 'Global 10-yr MA',
                data = city_temp,
                label = 'Average Global Temperature - 10-yr Moving Average')
            
        elif type_selection == '15':
            sns.lineplot( x = 'year',
                y = '15-yr MA',
                data = city_temp,
                label = 'Average Temperature - 15-yr Moving Average')
            
            sns.lineplot( x = 'year',
                y = 'Global 15-yr MA',
                data = city_temp,
                label = 'Average Global Temperature - 15-yr Moving Average')
  
        plt.xlabel('Years')
        length = len(city_temp['year'])
        lab = [city_temp.iloc[0]['year'],
              city_temp.iloc[round(length * 0.1)]['year'],
              city_temp.iloc[round(length * 0.2)]['year'],
              city_temp.iloc[round(length * 0.3)]['year'], 
              city_temp.iloc[round(length * 0.4)]['year'],
              city_temp.iloc[round(length * 0.5)]['year'], 
              city_temp.iloc[round(length * 0.6)]['year'],
              city_temp.iloc[round(length * 0.7)]['year'],
              city_temp.iloc[round(length * 0.8)]['year'],
              city_temp.iloc[round(length * 0.9)]['year'], 
              city_temp.iloc[-1]['year']]

        plt.xticks(lab)
  
        plt.ylabel('Average Temperature')

        plt.title("{} Average Temperatures".format(user_city))

        print("\nPlease be patient while I gather your data...\n")

        plt.show()

        print("Do you want to look at another city?\n")
        onward = str(input().strip().lower())

        while onward not in accepted_responses:
            print("\nPlease type yes or no.\n")
            onward = str(input().strip().lower())

        if onward == 'yes':
            keepGoing = True
        elif onward == 'no':
            keepGoing = False
            print("\nOk! This program will now terminate.")
            time.sleep(3)

moving_average()

