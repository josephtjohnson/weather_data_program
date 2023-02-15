import matplotlib.pyplot as plt

def build_plot(city_temp, user_city):

    plot = plt

    plot.figure(figsize = (12,5))

    plot.xlabel('Years')
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

    plot.xticks(lab)
  
    plot.ylabel('Average Temperature (C)')

    plot.title("{} Average Temperatures vs Global Average Temperatures".format(user_city))

    print("\nPlease be patient while I gather your data...\n")

    return plot
