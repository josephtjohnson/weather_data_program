import pandas as pd

def input_clean_up(user_city):

    if len(user_city) > 1:
        correct_name = ""
        for name in user_city:
            correct_name += name.capitalize()
            correct_name += " "
        return correct_name.strip()
    else:
        return user_city[0]

def all_cities():

    df = pd.read_csv(r'../weather_data.csv')

    cities = set(df['city'])

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

    city_temp = pd.DataFrame(df, columns = ['year', 'city', 'country', 'avg_temp', 'avg_global_temp'])

    city_temp = city_temp[city_temp['city'] == user_city]

    return user_city, city_temp

def louisville_city():

    user_city = "Louisville"

    df = pd.read_csv(r'../weather_data_louisville.csv')

    city_temp = pd.DataFrame(df, columns = ['year', 'city', 'country', 'avg_temp', 'avg_global_temp'])

    return user_city, city_temp
