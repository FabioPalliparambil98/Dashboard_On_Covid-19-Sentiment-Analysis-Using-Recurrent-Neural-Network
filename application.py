from flask import Flask, render_template, request
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import tweepy
import json
import pandas as pd
import hashtag


application = Flask(__name__)

df_general_filter = pd.read_csv('https://raw.githubusercontent.com/FabioPalliparambil98/cleaned-covid-dataset/main/general_covid.csv')
df_restriction_filter = pd.read_csv('https://raw.githubusercontent.com/FabioPalliparambil98/cleaned-covid-dataset/main/covid_restriction.csv')
df_vaccination_filter = pd.read_csv('https://raw.githubusercontent.com/FabioPalliparambil98/cleaned-covid-dataset/main/covid_vaccination.csv')


df_general_filter_sentiment = df_general_filter.copy()
df_restriction_filter_sentiment = df_restriction_filter.copy()
df_vaccination_filter_sentiment = df_vaccination_filter.copy()


df_general_filter['sentiment'].replace(0, 'negative', inplace=True)
df_general_filter['sentiment'].replace(1, 'positive', inplace=True)

df_restriction_filter['sentiment'].replace(0, 'negative', inplace=True)
df_restriction_filter['sentiment'].replace(1, 'positive', inplace=True)

df_vaccination_filter['sentiment'].replace(0, 'negative', inplace=True)
df_vaccination_filter['sentiment'].replace(1, 'positive', inplace=True)
"""
It displays the Home Pages of the Visualisations.
"""


@application.route('/')
def homepage():
    sentiment_general = sentiment_data(df_general_filter_sentiment)
    sentiment_vaccination = sentiment_data(df_restriction_filter_sentiment)
    sentiment_restriction = sentiment_data(df_vaccination_filter_sentiment)

    plot_general, plot_restriction, plot_vaccination, line_general, line_restriction,line_vaccination, all_line_scatters,scatter_circles,pie_general = hashtag.create_plot(hashtag.df_general_hash_tag,
                                                                           hashtag.df_restriction_hash_tag,
                                                                           hashtag.df_vaccination_hash_tag)
    plots = {'plot_general': plot_general,
             'plot_restriction': plot_restriction,
             'plot_vaccination': plot_vaccination,
             'line_general': line_general,
             'line_restriction': line_restriction,
             'line_vaccination': line_vaccination,
             'all_line_scatters': all_line_scatters,
             'scatter_circles': scatter_circles,
             'pie_general': pie_general}

    return render_template("index.html",
                           sentiment_general=sentiment_general,
                           sentiment_vaccination=sentiment_vaccination,
                           sentiment_restriction=sentiment_restriction,
                           plots=plots)


def sentiment_data(df):
    df_sentiment = df['sentiment'].value_counts()
    negative = df_sentiment.loc[0]
    positive = df_sentiment.loc[1]
    if negative > positive:
        return "negative"
    else:
        return "positive"


if __name__ == '__main__':
    application.run()
