from dash import Dash, html, Input, Output, dcc, dependencies, dash_table as dt
import snscrape.modules.twitter as sntwitter
import pandas as pd


app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Dropdown(['username', '#HASHTAG', 'Keyword'], id='demo-dropdown'),
        dcc.Input(id='my-input', value='Key_word', type='text'),
        #dcc.Slider(0, 20, 5, value=7, id='my-slider'),
        html.Br()
    ]),
    html.Br(),
    html.Div(id='my-output'),
    html.Div([
        dt.DataTable(id='data_table2')
    ], id='table2'),
    html.Div([
        html.Button(id='submit-button2', children='FUNDAMENTAL')
    ])
])


def ttscp(from_filters):
    attributes_container = []
    # since1 = st.date_input("since")
    # until1 = st.date_input("until")
    # filters = [f'since:{since1}', f'until:{until1}']
    filters = ['since:2023-01-05', 'until:2023-07-06']
    filters.append(' OR '.join(from_filters))
    tweet1 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(' '.join(filters)).get_items()):
        if i > 10:
            break
        attributes_container.append(
            [tweet.date, tweet.likeCount, tweet.url, tweet.content, tweet.id, tweet.user.username,
             tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.media])
        tweet1.append(tweet)
    # Using sntwitter.TwitterSearchScraper to scrape data and append tweets to list
    tweets_df1 = pd.DataFrame(attributes_container,
                              columns=["date", "like_count", "url", "tweet_content", "id", "user", "reply_count",
                                       "retweet_count", "language", "source"])
    return tweets_df1

@app.callback(
    [
        Output(component_id='data_table2', component_property='data'),
        Output(component_id='table2', component_property='columns'),

    ],
    [Input(component_id='submit-button2', component_property='option')],
    [dependencies.State(component_id='my-input', component_property='value')]
)
    #html.Div(dash_table.DataTable(id='my-output'))
    #output_df = pd.read_csv(r'C:\Users\kisho\churn1.csv')
    #@app.callback(Output('out-table', 'data'), Input('demo-dropdown', 'option'), Input('my-input', 'value'))
def scpp(option, value):
        option = "username"
        hash_tag = value
        from_filters = []
        from_filters.append(f'from:{hash_tag}')
        df = ttscp(from_filters)
        print(df)
        #st.write(df.astype(str))
 #       dt_col_param = []
 #       for col in output_df.columns:
 #           dt_col_param.append({"name": str(col), "id": str(col)})
 #       data = output_df.to_dict('records')
 #       df = dash_table.DataTable(column = dt_col_param, data = data.to_dict('records'))
 #       return df
        #data = output_df.to_dict(orient='records')
        #data = dash_table.DataTable(output_df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
        #return data
        dfa = df[(df['S'] == value)]
        data = dfa.to_dict('records')
        columns = [{'name': i, 'id': i, } for i in (dfa.columns)]
        return data, columns

if __name__ == '__main__':
    app.run_server(debug=True)
