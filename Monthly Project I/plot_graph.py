import pandas as pd
import numpy as np
import json
import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import json
import os
import pycountry_convert as pc
import chart_studio.plotly as py
from plotly.subplots import make_subplots

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA = pd.read_csv(os.path.join(THIS_FOLDER, 'static/data/train.csv'))
df_cabin_group = pd.read_csv(os.path.join(THIS_FOLDER, 'static/data/eda.csv'))
titanic_0 = DATA[DATA['Survived'] == 0]
titanic_1 = DATA[DATA['Survived'] == 1]
# Feature의 select 조건(filtering)을 만들어 주는 부분
pc1 = DATA['Pclass'] == 1
pc2 = DATA['Pclass'] == 2
pc3 = DATA['Pclass'] ==3
e_s = DATA['Embarked'] =='S'
e_c = DATA['Embarked'] == 'C'
e_q = DATA['Embarked'] == 'Q'

# 두가지 조건를 동시에 충족하는 데이터를 필터링하여 새로운 변수에 저장
df_1_s = DATA[pc1 & e_s]
df_1_c = DATA[pc1 & e_c]
df_1_q = DATA[pc1 & e_q]

df_2_s = DATA[pc2 & e_s]
df_2_c = DATA[pc2 & e_c]
df_2_q = DATA[pc2 & e_q]

df_3_s = DATA[pc3 & e_s]
df_3_c = DATA[pc3 & e_c]
df_3_q = DATA[pc3 & e_q]
cabin_pc1 = DATA[pc1]['Cabin'].unique()
cabin_pc2 = DATA[pc2]['Cabin'].unique()
cabin_pc3 = DATA[pc3]['Cabin'].unique()
titanic_pc1_sort=DATA[pc1].sort_values('Fare', ascending=False)
titanic_pc1_sort_ascending = DATA[pc1].sort_values('Ticket', ascending=True)

cabin_pc1 = np.delete(cabin_pc1, 6) # nan값 제외
pc1_A = []
for i in range(len(cabin_pc1)):
    if cabin_pc1[i][0] == 'A':
        pc1_A.append(cabin_pc1[i])

        
        
pc1_B = []
for i in range(len(cabin_pc1)):
    if cabin_pc1[i][0] == 'B':
        pc1_B.append(cabin_pc1[i])
        
pc1_C =[]
for i in range(len(cabin_pc1)):
    if cabin_pc1[i][0] == 'C':
        pc1_C.append(cabin_pc1[i])

pc1_D = []
for i in range(len(cabin_pc1)):
    if cabin_pc1[i][0] == 'D':
        pc1_D.append(cabin_pc1[i])

pc1_E =[]
for i in range(len(cabin_pc1)):
    if cabin_pc1[i][0] == 'E':
        pc1_E.append(cabin_pc1[i])

def table():
    

    fig = make_subplots(
        rows=1, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        specs=[[{"type": "table"}]]
    )
    fig.add_trace(
        go.Table(
            header=dict(
                values=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
                'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
                font=dict(size=10),
                align="left"
                ),
            cells=dict(
                values=[DATA[k].tolist() for k in DATA.columns],
                align = "left")
                ),
            row=1, col=1
        )

    fig.update_layout(
        height=800,
        showlegend=False,
        title_text="Titanic Dataset",
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def table_isnull():
    

    fig = make_subplots(
        rows=1, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.03,
        specs=[[{"type": "table"}]]
    )
    fig.add_trace(
        go.Table(
            header=dict(
                values=['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
                'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
                font=dict(size=10),
                align="left"
                ),
            cells=dict(
                values=[DATA[k].isnull().sum() for k in DATA.columns],
                align = "left")
                ),
            row=1, col=1
        )

    fig.update_layout(
        height=230,
        showlegend=False,
        title_text="Null Count",
    )
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON



def bar_plot():

    fig = go.Figure()

    #Add Traces

    fig.add_trace(go.Bar(name='Die', x=['Female', 'Male'], y=[len(titanic_0[titanic_0['Sex'] =='female']), len(titanic_0[titanic_0['Sex'] =='male'])], visible=False))
    fig.add_trace(go.Bar(name='Live', x=['Female', 'Male'], y=[len(titanic_1[titanic_1['Sex'] =='female']), len(titanic_1[titanic_1['Sex'] =='male'])], visible=False))
    fig.add_trace(go.Bar(name='Die', x=['1','2','3'], y=[len(titanic_0[titanic_0['Pclass'] ==1]), len(titanic_0[titanic_0['Pclass'] ==2]), len(titanic_0[titanic_0['Pclass'] ==3])]))
    fig.add_trace(go.Bar(name='Live', x=['1','2','3'], y=[len(titanic_1[titanic_1['Pclass'] ==1]), len(titanic_1[titanic_1['Pclass'] ==2]), len(titanic_1[titanic_1['Pclass'] ==3])]))  
    fig.add_trace(go.Bar(name='Die', x=['S','C','Q'], y=[len(titanic_0[titanic_0['Embarked'] =='S']), len(titanic_0[titanic_0['Embarked'] =='C']), len(titanic_0[titanic_0['Embarked'] =='Q'])], visible=False))  
    fig.add_trace(go.Bar(name='Live', x=['S','C','Q'], y=[len(titanic_1[titanic_1['Embarked'] =='S']), len(titanic_1[titanic_1['Embarked'] =='C']), len(titanic_1[titanic_1['Embarked'] =='Q'])], visible=False))  




    fig.data[0].marker.line.color = "black"
    fig.data[1].marker.line.color = "black"
    fig.data[2].marker.line.color = "black"
    fig.data[3].marker.line.color = "black"
    fig.data[4].marker.line.color = "black"
    fig.data[5].marker.line.color = "black"

    # Add Buttons
    fig.update_layout(
        updatemenus=[
            dict(
                active=1,
                buttons=list([ 
                    
                        dict(label='Sex',
                            method='update',
                            args=[{'visible': [True, True,False, False, False, False]},
                                {'title': '<b>Barplot for Sex<b>'}]),
                
                        dict(label='Pclass',
                            method='update',
                            args=[{'visible': [False, False,True, True, False, False]},
                                {'title': '<b>Barplot for Pclass<b>'}]),
                    
                        dict(label='Embarked',
                            method='update',
                            args=[{'visible': [False, False,False, False, True, True]},
                                {'title': '<b>Barplot for Embarked<b>'}]),                
                            ]),
                )
                ])
    fig.update_layout(title=f"<b>Barplot for Pclass<b>")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def bar_mean():
        
    fig = go.Figure()

    # Add Traces

    fig.add_trace(go.Bar(x=['Female', 'Male'], y=[DATA.groupby(DATA['Sex']).mean()['Survived'][0], DATA.groupby(DATA['Sex']).mean()['Survived'][1]], visible=False ))
    fig.add_trace(go.Bar(x=['1','2','3'], y=[DATA.groupby(DATA['Pclass']).mean()['Survived'].iloc[0], DATA.groupby(DATA['Pclass']).mean()['Survived'].iloc[1], DATA.groupby(DATA['Pclass']).mean()['Survived'].iloc[2]]))  
    fig.add_trace(go.Bar(x=['S','C','Q'], y=[DATA.groupby(DATA['Embarked']).mean()['Survived'][2], DATA.groupby(DATA['Embarked']).mean()['Survived'][0], DATA.groupby(DATA['Embarked']).mean()['Survived'][1]], visible=False))

    fig.data[0].marker.line.color = "black"
    fig.data[1].marker.line.color = "black"
    fig.data[2].marker.line.color = "black"
    # Add Buttons

    fig.update_layout(
        updatemenus=[
            dict(
                active=1,
                buttons=list([ 
                    
                        dict(label='Sex',
                            method='update',
                            args=[{'visible': [True, False,False]},
                                {'title': '<b>Barplot for Sex (Mean) <b>'}]),
                    
                        dict(label='Pclass',
                            method='update',
                            args=[{'visible': [False, True, False]},
                                {'title': '<b>Barplot for Pclass (Mean)<b>'}]),
                    
                        dict(label='Embarked',
                            method='update',
                            args=[{'visible': [False, False, True]},
                                {'title': '<b>Barplot for Embarked (Mean)<b>'}]),
                    
                
                    ]),
                    )
                ])
    fig.update_layout(title=f"<b>Barplot for Pclass (Mean)<b>")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON


def violin_plot():
    fig = go.Figure()

    fig.add_trace(go.Violin(x= DATA['Embarked'][pc1 & e_s],
                        y=DATA['Fare'][DATA['Pclass']==1],
                        name='Pclass = 1',
                        legendgroup = 'Pclass = 1',
                        scalegroup = 'Pclass = 1',
                            box_visible=True,
                            meanline_visible=True))
    fig.add_trace(go.Violin(x= df_2_s['Embarked'],
                            y=DATA['Fare'][DATA['Pclass']==2],
                            name='Pclass = 2',
                        legendgroup = 'Pclass = 2',
                        scalegroup = 'Pclass = 2',
                            box_visible=True,
                            meanline_visible=True))
    fig.add_trace(go.Violin(x= df_3_s['Embarked'],
                            y=DATA['Fare'][DATA['Pclass']==3],
                            name='Pclass = 3',
                        legendgroup = 'Pclass = 3',
                        scalegroup = 'Pclass = 3',
                            box_visible=True,
                            meanline_visible=True))



    fig.add_trace(go.Violin(x= df_1_c['Embarked'],
                        y=DATA['Fare'][DATA['Pclass']==1],
                        name='Pclass = 1',
                        legendgroup = 'Pclass = 1',
                        scalegroup = 'Pclass = 1',
                            box_visible=True,
                            meanline_visible=True))
    fig.add_trace(go.Violin(x= df_2_c['Embarked'],
                            y=DATA['Fare'][DATA['Pclass']==2],
                            name='Pclass = 2',
                        legendgroup = 'Pclass = 2',
                        scalegroup = 'Pclass = 2',
                            box_visible=True,
                            meanline_visible=True))
    fig.add_trace(go.Violin(x= df_3_c['Embarked'],
                            y=DATA['Fare'][DATA['Pclass']==3],
                            name='Pclass = 3',
                        legendgroup = 'Pclass = 3',
                        scalegroup = 'Pclass = 3',
                            box_visible=True,
                            meanline_visible=True))


    fig.add_trace(go.Violin(x= df_1_q['Embarked'],
                        y=DATA['Fare'][DATA['Pclass']==1],
                        name='Pclass = 1',
                        legendgroup = 'Pclass = 1',
                        scalegroup = 'Pclass = 1',
                            box_visible=True,
                            meanline_visible=True))
    fig.add_trace(go.Violin(x= df_2_q['Embarked'],
                            y=DATA['Fare'][DATA['Pclass']==2],
                            name='Pclass = 2',
                        legendgroup = 'Pclass = 2',
                        scalegroup = 'Pclass = 2',
                            box_visible=True,
                            meanline_visible=True))
    fig.add_trace(go.Violin(x= df_3_q['Embarked'],
                            y=DATA['Fare'][DATA['Pclass']==3],
                            name='Pclass = 3',
                        legendgroup = 'Pclass = 3',
                        scalegroup = 'Pclass = 3',
                            box_visible=True,
                            meanline_visible=True))
    fig.update_layout(
    updatemenus=[
        dict(
            active=1,
            buttons=list([ 
                    
                    dict(label='Embarked = S',
                        method='update',
                        args=[{'visible': [True, True,True, False, False, False, False, False, False]},
                            {'title': '<b>Violinplot for (Embarked = S) and Fare<b>'}]),
                
                    dict(label='Embarked = C',
                        method='update',
                        args=[{'visible': [False, False,False, True, True, True, False, False, False]},
                            {'title': '<b>Violinplot for (Embarked = C) and Fare<b>'},
                             ]),
                    
                    dict(label='Embarked = Q',
                        method='update',
                        args=[{'visible': [False, False,False, False, False, False, True, True, True]},
                            {'title': '<b>Violinplot for (Embarked = Q) and Fare<b>'}]),                
                ]),
            )
        ])
    fig.update_traces(box_visible=True, meanline_visible=True)
    fig.update_layout(title="<b>ViolinPlot for Embarked, Pclass and Fare<b>",violinmode='group')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def treemap():
    fig = px.treemap(
    names = ["Total","Pclass = 1", pc1_A, pc1_B, pc1_C, pc1_D, pc1_E, "Pclass = 2", cabin_pc2, "Pclass = 3", cabin_pc3],
    parents = ["", "Total", "Pclass = 1", "Pclass = 1", "Pclass = 1","Pclass = 1","Pclass = 1","Total", "Pclass = 2", "Total", "Pclass = 3"],
    )
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def TableSort():

    fig = go.Figure()

    fig.add_trace(go.Table(
        header=dict(values=['Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[titanic_pc1_sort.Survived, titanic_pc1_sort.Pclass, titanic_pc1_sort.Sex, titanic_pc1_sort.Age, titanic_pc1_sort.SibSp, titanic_pc1_sort.Parch, titanic_pc1_sort.Ticket, titanic_pc1_sort.Fare, titanic_pc1_sort.Cabin, titanic_pc1_sort.Embarked],
               fill_color='lavender',
               align='left'))
    )

    fig.add_trace(go.Table(
        header=dict(values=['Survived', 'Pclass', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'],
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[titanic_pc1_sort_ascending.Survived, titanic_pc1_sort_ascending.Pclass, titanic_pc1_sort_ascending.Sex, titanic_pc1_sort_ascending.Age, titanic_pc1_sort_ascending.SibSp, titanic_pc1_sort_ascending.Parch, titanic_pc1_sort_ascending.Ticket, titanic_pc1_sort_ascending.Fare, titanic_pc1_sort_ascending.Cabin, titanic_pc1_sort_ascending.Embarked],
               fill_color='lavender',
               align='left'))
    )

    fig.update_layout(
    updatemenus=[
        dict(
            active=1,
            buttons=list([ 
                    
                    dict(label='Descending',
                        method='update',
                        args=[{'visible': [True, False]},
                            {'title': '<b>Table for Fare (Sort = Descending)<b>'}]),
                
                    dict(label='Ascending',
                        method='update',
                        args=[{'visible': [False, True]},
                            {'title': '<b>Table for Fare (Sort = Ascending)<b>'},
                             ]),
           
                ]),
            )
        ])
    fig.update_layout(title=f"<b>Table for Sort<b>")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def axis_plot():
    
    fig = go.Figure()

    # Add Traces

    fig.add_trace(go.Bar(x=['1','2','3','4'], y=[df_cabin_group.groupby(df_cabin_group['group']).mean()['Survived'].iloc[0], 
                                             df_cabin_group.groupby(df_cabin_group['group']).mean()['Survived'].iloc[1],
                                             df_cabin_group.groupby(df_cabin_group['group']).mean()['Survived'].iloc[2],
                                             df_cabin_group.groupby(df_cabin_group['group']).mean()['Survived'].iloc[3]] ))
    fig.add_trace(go.Bar(x=['0','1','2','3','4','5','6'], y=[df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[0], 
                                                         df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[1], 
                                                         df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[2],
                                                         df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[3],
                                                         df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[4],
                                                         df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[5],
                                                         df_cabin_group.groupby(df_cabin_group['Cabin']).mean()['Survived'].iloc[6]
                                                        ]))  


    fig.data[0].marker.line.color = "black"
    fig.data[1].marker.line.color = "black"

    # Add Buttons


    fig.update_layout(
    updatemenus=[
        dict(
            active=1,
            buttons=list([ 
                    
                    dict(label='X-coordinates',
                        method='update',
                        args=[{'visible': [True, False]},
                            {'title': '<b>Survival rate for X - coordinates<b>'}]),
                    
                    dict(label='Y-coordinates',
                        method='update',
                        args=[{'visible': [False, True]},
                            {'title': '<b>Survival rate for Y - coordinates<b>'}]),

                    
                
                ]),
            

        )])
    fig.update_layout(title=f"<b>Plot for Space coordinates<b>")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON




