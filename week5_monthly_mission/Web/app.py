from flask import Flask, render_template  # jsonify, request,
from eda_plot import EDA

app = Flask(__name__)

# GET /
@app.route('/')
def index() : #{
    eda = EDA('static/data/tracks.csv')

    corr      = eda.plot_corr()

    columns   = ["acousticness", "danceability", "energy", "speechiness", "liveness", "valence"]
    year_plot = []
    year_plot.append(eda.plot_release_by_year())
    year_plot.append(eda.plot_features_by_year(['popularity']))
    year_plot.append(eda.plot_features_by_year(['duration']))
    year_plot.append(eda.plot_features_by_year(columns))

    feature_set  = [['energy', 'loudness'], ['acousticness', 'loudness'], ['acousticness', 'energy'], ['danceability', 'valence'], ['tempo', 'danceability']]
    feature_plot = []
    for f in feature_set : #{
        feature_plot.append(eda.plot_by_two_features(f))
    #}

    feature_plot.append(eda.plot_key_mode())

    return render_template('homepage.html', plot={'corr':corr, 'year_plot':year_plot, 'feature_plot':feature_plot})    
#}


if __name__ == '__main__':
    app.run(debug=True)