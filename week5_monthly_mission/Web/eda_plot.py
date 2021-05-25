import pandas as pd
import numpy as np
import os
import json
import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
from plotly.subplots import make_subplots

class EDA() : #{
    def __init__(self, data_path) : #{
        dir_path        = os.path.dirname(os.path.abspath(__file__))
        self.spotify_df = pd.read_csv(os.path.join(dir_path, data_path))

        ## Organize dataset : Modify [''] to nan in artists and format of release_date
        self.df                 = self.spotify_df.copy()
        self.df.artists         = self.df.artists.replace("['']", np.nan)
        self.df['release_date'] = pd.to_datetime(self.df['release_date'])
        self.df['year']         = self.df['release_date'].dt.year
        self.df['duration']     = self.df['duration_ms']/60000

        ## Duration average over year
        self.df_columns = ['popularity', 'duration_ms', 'explicit', 'danceability', 'energy', 'key', 'loudness', 'mode', 
              'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'time_signature']

    #}

    def plot_corr(self) : #{
        ## Correlation
        fig = ff.create_annotated_heatmap(np.array(round(self.spotify_df[self.df_columns].corr(),4)), 
                                  x=self.df_columns, y=self.df_columns, colorscale = 'RdBu', reversescale=True )
        fig.update_layout(title=f"<b>Correlation</b>")

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    #}

    def plot_release_by_year(self) : #{
        year_group = self.df[self.df['year'] >= 1920].groupby('year').count()['popularity']
        year_keys  = year_group.index
        values     = list(year_group)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=year_keys, y=values, 
                            name='release_count', marker_color='#166ADC')) #'rgba(152, 0, 0, .8)'))

        fig.update_layout(title='<b>연도별 발매 수</b>',
                        xaxis_title='Year',
                        yaxis_title='Number of Release')      

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    #}

    def plot_features_by_year(self, features) : #{
        year_group = self.df[self.df['year'] >= 1920].groupby('year').mean()
        keys       = year_group.index
       
        # columns = ["acousticness","danceability","energy","speechiness","liveness","valence"]

        fig = go.Figure()
        for col in features : #{
            fig.add_trace(go.Scatter(x=keys, y=list(year_group[col]), name=col, mode='lines+markers'))
        #}

        if len(features) == 1 : #{
            fig.update_layout(title=f'<b>{col.capitalize()} by years</b>',
                        xaxis_title='Year',
                        yaxis_title=col.capitalize())            
        #}
        else : #{
            fig.update_layout(title='<b>연도별 음원 특징</b>',
                        xaxis_title='Year',
                        yaxis_title='Characteristics')
        #}

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON
    #}    


    def plot_by_two_features(self, columns) : #{
        fig = px.scatter(self.df, x=columns[0], y=columns[1], color='popularity') #, size='popularity')
        fig.update_layout(title=f'<b>{columns[0].capitalize()} vs. {columns[1].capitalize()}</b>',
                        xaxis_title=columns[0].capitalize(),
                        yaxis_title=columns[1].capitalize())   

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return graphJSON             
    #}

    def plot_key_mode(self) : #{

        df_keys_mode = self.df.copy()
        key_keys = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
        for idx, k in enumerate(key_keys) : #{
            df_keys_mode['key'] = df_keys_mode['key'].replace([idx], k)
        #}

        mode_keys = ["Minor", "Major"]
        for idx, k in enumerate(mode_keys) : #{
            df_keys_mode['mode'] = df_keys_mode['mode'].replace([idx], k)
        #}

        fig = make_subplots(rows=1, cols=2,
                            horizontal_spacing= 0.15,
                            subplot_titles=('<b>Major Mode의 Key 분포</b>','<b>Minor Mode의 Key 분포</b>'))

        fig.add_trace(go.Bar(x=key_keys, y=df_keys_mode[df_keys_mode['mode']=='Minor'].groupby('key').count()['popularity'],
                        name="Minor"), row=1, col=1)
        fig.add_trace(go.Bar(x=key_keys, y=df_keys_mode[df_keys_mode['mode']=='Major'].groupby('key').count()['popularity'],
                        name="Minor"), row=1, col=2)

        fig.update_layout(title='<b>Mode와 Key에 따른 분포</b>', showlegend=True)

        fig.update_xaxes(title_text="Key", row=1, col=1)
        fig.update_xaxes(title_text="Key", row=1, col=2)
        fig.update_yaxes(title_text="Count", row=1, col=1)
        fig.update_yaxes(title_text="Count", row=1, col=2)

        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)  
        return graphJSON          
    #}
#}