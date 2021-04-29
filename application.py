from flask import Flask, render_template, request
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import tweepy
import json
import pandas as pd
import hashtag


application = Flask(__name__)


"""
It displays the Home Pages of the Visualisations.
"""


@application.route('/')
def homepage():
    sentiment_general = 'negative'
    sentiment_vaccination = 'negative'
    sentiment_restriction = 'negative'

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


if __name__ == '__main__':
    application.run()
