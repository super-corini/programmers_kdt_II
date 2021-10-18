from flask import Flask, render_template, jsonify, request
from plot_graph import *

app = Flask(__name__)


@app.route('/')
def eda():

    # box_graphJSON = draw_boxplot()
    #scatter_graphJSON = draw_scatter()
    bar_graphJSON = bar_plot()
    bar_mean_graphJSON = bar_mean()
    table_graphJSON = table()
    isnull_graphJSON = table_isnull()
    violin_graphJSON = violin_plot()
    treemap_graphJSON = treemap()
    tablesort_graphJSON = TableSort()
    space_graphJSON = axis_plot()
    return render_template('eda.html', plot={'bargraph':bar_graphJSON, 'barmean' : bar_mean_graphJSON,'table':table_graphJSON, 'isnull':isnull_graphJSON, 'violin':violin_graphJSON, 'treemap': treemap_graphJSON, 'tablesort': tablesort_graphJSON, 'space':space_graphJSON})


if __name__ == '__main__':
    app.run(debug=True)