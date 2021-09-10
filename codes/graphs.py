# import the relevant packages
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

# import the dataframe
sg_tweets_sent_topics_df = pd.read_csv('/home/cakx1508/mysite/sg_tweets_visualization_2021.csv')


# create chart 1 - to show the number of tweets overtime
fig1 = px.bar(x = sg_tweets_sent_topics_df['month'].unique(),
              y = sg_tweets_sent_topics_df.groupby('month')['id'].agg('count'),
               labels = {
                   'x': 'Month',
                   'y': 'Number of tweets'
              },
             color = sg_tweets_sent_topics_df.groupby('month')['id'].agg('count'),
             color_continuous_scale = px.colors.sequential.Viridis_r,
             text = sg_tweets_sent_topics_df.groupby('month')['id'].agg('count'),
             title = 'Number of monthly tweets in Singapore'
              )

fig1.update_layout(title = dict(x=0.5),
                   xaxis = dict(tickmode = 'array',
                                tickvals = [1, 2, 3, 4, 5, 6, 7],
                                ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']),
                   height = 600)

fig1.update_traces(texttemplate = '%{text:.2s}')


# create chart 2 - to show the top hashtags trending on Twitter in SG
# convert the hashtags from an object to a list
sg_tweets_sent_topics_df['hashtags'] = sg_tweets_sent_topics_df['hashtags'].apply(eval)

# create a function to reduce the dimensions of the hashtags column from 2 to 1
def convert_to_one_dimensional(series):
    return pd.Series([x for _list in series for x in _list])

# implement the function
hashtags_count = convert_to_one_dimensional(sg_tweets_sent_topics_df['hashtags'])

# create a chart to show trending hashtags
fig2 = px.bar(hashtags_count,
              x = hashtags_count.value_counts().head(20).values,
              y = hashtags_count.value_counts().head(20).index,
              labels = {
                  'x': 'Number of tweets',
                  'y': 'Hashtags'
              },
              color = hashtags_count.value_counts().head(20).values,
              color_continuous_scale = px.colors.sequential.Viridis_r,
              text = hashtags_count.value_counts().head(20).values,
              title = 'Top hashtags trending on Twitter in Singapore',
              orientation = 'h'
             )

fig2.update_layout(title = dict(x=0.5), height=600)

fig2.update_yaxes(autorange='reversed')

fig2.update_traces(texttemplate = '%{text:.2s}')


# create chart 3 - to show the distribution of monthly tweets in Singapore with sentiment labels
# create two dataframes - one for positive and the other for negative sentiments
positive_sent_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['lstm_label']=='positive']
negative_sent_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['lstm_label']=='negative']

# create the chart for positive sentiments
trace1 = go.Bar(    
    x = positive_sent_df['month'].unique(),
    y = positive_sent_df.groupby('month')['lstm_label'].agg('count'),
    marker_color = px.colors.qualitative.Bold[2],
    text = positive_sent_df.groupby('month')['lstm_label'].agg('count'),
    textposition = 'outside',
    name = 'Positive sentiment'
)

# create chart for negative sentiments
trace2 = go.Bar(   
    x = negative_sent_df['month'].unique(),
    y = negative_sent_df.groupby('month')['lstm_label'].agg('count'),
    marker_color = px.colors.qualitative.G10[3],
    text = negative_sent_df.groupby('month')['lstm_label'].agg('count'),
    textposition = 'outside',
    name = 'Negative sentiment'
)

# combining both charts into one
data = [trace1, trace2]
layout = go.Layout(barmode='group', title='Distribution of monthly tweets in Singapore with sentiment labels') 
fig3 = go.Figure(data=data, layout=layout)
fig3.update_layout(
    title = dict(x=0.5),
    xaxis_title = 'Month',
    yaxis_title = 'Number of tweets',
    xaxis = dict(tickmode = 'array',
                 tickvals = [1, 2, 3, 4, 5, 6, 7],
                 ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']),
    height = 600,
    margin = dict(l=20, r=20, t=60, b=20)
)

fig3.update_traces(texttemplate="%{text:.2s}")


# create chart 4 - to show the distribution of dominant topics for tweets in Singapore
# create a chart to show the dominant topics
fig4 = px.bar(x = sg_tweets_sent_topics_df['dominant_topic'].unique().sort(),
              y = sg_tweets_sent_topics_df.groupby('dominant_topic')['id'].agg('count'),
               labels = {
                   'x': 'Dominant Topics',
                   'y': 'Number of tweets'
              },
             color = sg_tweets_sent_topics_df.groupby('dominant_topic')['id'].agg('count'),
             color_continuous_scale = px.colors.sequential.Viridis_r,
             text = sg_tweets_sent_topics_df.groupby('dominant_topic')['id'].agg('count'),
             title = 'Distribution of dominant topics for tweets in Singapore'
              )

fig4.update_layout(title = dict(x=0.5),
                   xaxis = dict(tickmode = 'array',
                                tickvals = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                                ticktext = ['Topic 1: Latest online trends and COVID-19 in SG', 
                                            'Topic 2: Military coup in Myanmar', 'Topic 3: Updates on COVID-19 in SG', 
                                            'Topic 4: Occasions and events in SG', 'Topic 5: Recreational activities in SG',
                                            'Topic 6: Online trends/rants', 'Topic 7: Political affairs in USA']),
                   height = 750)

fig4.update_traces(texttemplate = '%{text:.2s}')


# create chart 5 - to show the distribution of monthly tweets in Singapore with dominant topics
# create dataframes for each topic
topic1_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==0.0]
topic2_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==1.0]
topic3_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==2.0]
topic4_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==3.0]
topic5_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==4.0]
topic6_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==5.0]
topic7_df = sg_tweets_sent_topics_df[sg_tweets_sent_topics_df['dominant_topic']==6.0]

# create the chart for topic 1
trace3 = go.Bar(    
    x = topic1_df['month'].unique(),
    y = topic1_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Prism[0],
    text = topic1_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 1'
)

# create the chart for topic 2
trace4 = go.Bar(    
    x = topic2_df['month'].unique(),
    y = topic2_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Prism[1],
    text = topic2_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 2'
)

# create the chart for topic 3
trace5 = go.Bar(    
    x = topic3_df['month'].unique(),
    y = topic3_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Prism[2],
    text = topic3_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 3'
)

# create the chart for topic 4
trace6 = go.Bar(    
    x = topic4_df['month'].unique(),
    y = topic4_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Prism[3],
    text = topic4_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 4'
)

# create the chart for topic 5
trace7 = go.Bar(    
    x = topic5_df['month'].unique(),
    y = topic5_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Prism[4],
    text = topic5_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 5'
)

# create the chart for topic 6
trace8 = go.Bar(    
    x = topic6_df['month'].unique(),
    y = topic6_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Set3[6],
    text = topic6_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 6'
)

# create the chart for topic 7
trace9 = go.Bar(    
    x = topic7_df['month'].unique(),
    y = topic7_df.groupby('month')['dominant_topic'].agg('count'),
    marker_color = px.colors.qualitative.Set3[1],
    text = topic7_df.groupby('month')['dominant_topic'].agg('count'),
    textposition = 'outside',
    name = 'Topic 7'
)

# combining both charts into one
data2 = [trace3, trace4, trace5, trace6, trace7, trace8, trace9]
layout = go.Layout(barmode='group', title='Distribution of monthly tweets in Singapore with dominant topics') 
fig5 = go.Figure(data=data2, layout=layout)
fig5.update_layout(
    title = dict(x=0.5),
    xaxis_title = 'Month',
    yaxis_title = 'Number of tweets',
    xaxis = dict(tickmode = 'array',
                 tickvals = [1, 2, 3, 4, 5, 6, 7],
                 ticktext = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']),
    height = 600,
    margin = dict(l=20, r=20, t=60, b=20)
)

fig5.update_traces(texttemplate="%{text:.2s}")


# create chart 6 - to show the distribution of sentiment per dominant topic for tweets in Singapore
# create the chart for topics with positive sentiment per topic
trace10 = go.Bar(    
    x = positive_sent_df['dominant_topic'].unique().sort(),
    y = positive_sent_df.groupby('dominant_topic')['lstm_label'].agg('count'),
    marker_color = px.colors.qualitative.Bold[2],
    text = positive_sent_df.groupby('dominant_topic')['lstm_label'].agg('count'),
    textposition = 'outside',
    name = 'Positive sentiment'
)

# create chart for negative sentiment per topic
trace11 = go.Bar(   
    x = negative_sent_df['dominant_topic'].unique().sort(),
    y = negative_sent_df.groupby('dominant_topic')['lstm_label'].agg('count'),
    marker_color = px.colors.qualitative.G10[3],
    text = negative_sent_df.groupby('dominant_topic')['lstm_label'].agg('count'),
    textposition = 'outside',
    name = 'Negative sentiment'
)

# combining both charts into one
data3 = [trace10, trace11]
layout = go.Layout(barmode='group', title='Distribution of sentiment per topic for tweets in Singapore') 
fig6 = go.Figure(data=data3, layout=layout)
fig6.update_layout(
    title = dict(x=0.5),
    xaxis_title = 'Dominant Topics',
    yaxis_title = 'Number of tweets',
    xaxis = dict(tickmode = 'array',
                 tickvals = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0],
                 ticktext = ['Topic 1: Latest online trends and COVID-19 in SG', 'Topic 2: Military coup in Myanmar', 
                             'Topic 3: Updates on COVID-19 in SG', 'Topic 4: Occasions and events in SG', 
                             'Topic 5: Recreational activities in SG', 'Topic 6: Online trends/rants', 
                             'Topic 7: Political affairs in USA']),
    height = 700,
    margin = dict(l=20, r=20, t=60, b=20)
)

fig6.update_traces(texttemplate="%{text:.2s}")


# create layout
# set up Dash
# app = dash.Dash(__name__)
app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.Div(
            children=[
                html.H1(
                    children='Life in the "New Normal"', style={'textAlign':'center'}, className='header-title' 
                ), 
                html.H2(
                    children='Analysing tweets in Singapore from 1 January 2021 to 31 July 2021',
                    className='header-description', style={'textAlign':'center'},
                ),
            ],
            className='header',style={'backgroundColor':'#F5F5F5'},
        ),
        
        html.Div(
            children=[
                html.Div(
                children = dcc.Graph(
                    id = 'numbar',
                    figure = fig1,
                    #config={"displayModeBar": False},
                ),
                style={'width':'50%', 'display':'inline-block'},
            ),
                html.Div(
                children = dcc.Graph(
                    id = 'hashbar',
                    figure = fig2,
                    #config={"displayModeBar": False},
                ),
                style={'width':'50%', 'display':'inline-block'},
            ),
                html.Div(
                children = dcc.Graph(
                    id = 'sentbar',
                    figure = fig3,
                    #config={"displayModeBar": False},
                ),
                style={'width': '50%', 'display': 'inline-block'},
            ),
                html.Div(
                children = dcc.Graph(
                    id = 'topicmonthbar',
                    figure = fig5,
                    #config={"displayModeBar": False},
                ),
                style={'width':'50%', 'display':'inline-block'},
            ),
                html.Div(
                children = dcc.Graph(
                    id = 'topicbar',
                    figure = fig4,
                    #config={"displayModeBar": False},
                ),
                style={'width':'50%', 'display':'inline-block'},
            ),
                html.Div(
                children = dcc.Graph(
                    id = 'topicsentbar',
                    figure = fig6,
                    #config={"displayModeBar": False},
                ),
                style={'width':'50%', 'display':'inline-block'},
            ),
        ],
        className = 'double-graph',
        ), 

    ]
)


# for launching on terminal 
if __name__ == '__main__':
    app.run_server(debug=True)