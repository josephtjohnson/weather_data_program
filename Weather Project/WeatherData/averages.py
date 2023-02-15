import seaborn as sns
import matplotlib as plt
import time
from buildplot import build_plot

def seven_year_moving_average(city_temp, user_city):

    plot = build_plot(city_temp, user_city)

    city_temp['7-yr MA'] = city_temp.avg_temp.rolling(7).mean()
    city_temp['Global 7-yr MA'] = city_temp.avg_global_temp.rolling(7).mean()

    sns.lineplot( x = 'year',
        y = '7-yr MA',
        data = city_temp,
        label = 'Average Temperature - 7-yr Moving Average')
            
    sns.lineplot( x = 'year',
        y = 'Global 7-yr MA',
        data = city_temp,
        label = 'Average Global Temperature - 7-yr Moving Average')

    plot.show()

def ten_year_moving_average(city_temp, user_city):

    plot = build_plot(city_temp, user_city)

    city_temp['10-yr MA'] = city_temp.avg_temp.rolling(10).mean()
    city_temp['Global 10-yr MA'] = city_temp.avg_global_temp.rolling(10).mean()

    sns.lineplot( x = 'year',
        y = '10-yr MA',
        data = city_temp,
        label = 'Average Temperature - 10-yr Moving Average')
            
    sns.lineplot( x = 'year',
        y = 'Global 10-yr MA',
        data = city_temp,
        label = 'Average Global Temperature - 10-yr Moving Average')

    plot.show()

def fifteen_year_moving_average(city_temp, user_city):

    plot = build_plot(city_temp, user_city)

    city_temp['15-yr MA'] = city_temp.avg_temp.rolling(15).mean()
    city_temp['Global 15-yr MA'] = city_temp.avg_global_temp.rolling(15).mean()

    sns.lineplot( x = 'year',
        y = '15-yr MA',
        data = city_temp,
        label = 'Average Temperature - 15-yr Moving Average')
            
    sns.lineplot( x = 'year',
        y = 'Global 15-yr MA',
        data = city_temp,
        label = 'Average Global Temperature - 15-yr Moving Average')

    plot.show()

def all_moving_averages(city_temp, user_city):

    plot = build_plot(city_temp, user_city)

    city_temp['7-yr MA'] = city_temp.avg_temp.rolling(7).mean()
    city_temp['10-yr MA'] = city_temp.avg_temp.rolling(10).mean()
    city_temp['15-yr MA'] = city_temp.avg_temp.rolling(15).mean()
    city_temp['Global 7-yr MA'] = city_temp.avg_global_temp.rolling(7).mean()
    city_temp['Global 10-yr MA'] = city_temp.avg_global_temp.rolling(10).mean()
    city_temp['Global 15-yr MA'] = city_temp.avg_global_temp.rolling(15).mean()

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

    plot.show()