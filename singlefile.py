import snscrape.modules.twitter as sntwitter
import pandas as pd
import streamlit as st
st.title("Tweeter Data Scrapping")
attributes_container = []
option = st.selectbox('Search By',('username', '#HASHTAG', "Keyword"))


if option == "username":
        hash_tag = st.text_input("username")
        since1 = st.date_input("since")
        until1 = st.date_input("until")
        st.write(since1)
        st.write(until1)
        filters = [f'since:{since1}', f'until:{until1}']
        from_filters = []
        from_filters.append(f'from:{hash_tag}')
        filters.append(' OR '.join(from_filters))
        for n, k in enumerate(hash_tag):
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(' '.join(filters)).get_items()):
                if i > 100:
                    break
                attributes_container.append(
                    [tweet.date, tweet.likeCount, tweet.url, tweet.content, tweet.id, tweet.user.username,
                     tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.media])
        # Using TwitterSearchScraper to scrape data and append tweets to list
        tweets_df1 = pd.DataFrame(attributes_container,
                                  columns=["date", "like_count", "url", "tweet_content", "id", "user", "reply_count",
                                           "retweet_count", "language", "source"])
        st.write(tweets_df1.astype(str))


elif option == "#HASHTAG":
        hash_tag1 = st.text_input("HASHTAG")
        hash_tag = "#"+ hash_tag1
        st.write(hash_tag)
        since1 = st.date_input("since")
        until1 = st.date_input("until")
        st.write(since1)
        st.write(until1)
        filters = [f'since:{since1}', f'until:{until1}']
        from_filters = []
        from_filters.append(hash_tag)
        filters.append(' OR '.join(from_filters))
        for n, k in enumerate(hash_tag):
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(' '.join(filters)).get_items()):
                if i > 100:
                    break
                attributes_container.append(
                    [tweet.date, tweet.likeCount, tweet.url, tweet.content, tweet.id, tweet.user.username,
                     tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.media])
        # Using TwitterSearchScraper to scrape data and append tweets to list
        tweets_df1 = pd.DataFrame(attributes_container,
                                  columns=["date", "like_count", "url", "tweet_content", "id", "user", "reply_count",
                                           "retweet_count", "language", "source"])
        st.write(tweets_df1.astype(str))

elif option == "Keyword":
        hash_tag = st.text_input("Keyword")
        since1 = st.date_input("since")
        until1 = st.date_input("until")
        st.write(since1)
        st.write(until1)
        filters = [f'since:{since1}', f'until:{until1}']
        from_filters = []
        from_filters.append(hash_tag)
        filters.append(' OR '.join(from_filters))
        for n, k in enumerate(hash_tag):
            for i, tweet in enumerate(sntwitter.TwitterSearchScraper(' '.join(filters)).get_items()):
                if i > 100:
                    break
                attributes_container.append(
                    [tweet.date, tweet.likeCount, tweet.url, tweet.content, tweet.id, tweet.user.username,
                     tweet.replyCount, tweet.retweetCount, tweet.lang, tweet.media])
        # Using TwitterSearchScraper to scrape data and append tweets to list
        tweets_df1 = pd.DataFrame(attributes_container,
                                  columns=["date", "like_count", "url", "tweet_content", "id", "user", "reply_count",
                                           "retweet_count", "language", "source"])
        st.write(tweets_df1.astype(str))

#from io import BytesIO
#from pyxlsb import open_workbook as open_xlsb
df = tweets_df1
json1 = df.to_json()
csv = df.to_csv()
#df_xlsx = to_excel(df)
#df_csv = to_csv(df)
#df_json = to_excel(df)
#st.download_button(label='📥 Download Current Result as xlsx',
#                                data=df_xlsx ,
#                                file_name= 'train.xlsx')
st.download_button(label='📥 csv',
                                    data=csv,
                                    file_name= 'train.csv')
st.download_button(label='📥 json',
                                    data=json1,
                                    file_name= 'train.json')



button1 = st.button("Upload to Mongo")

if button1:
    from pymongo import MongoClient
    import json
    from datetime import datetime
    # call fun1 from file2.py
    data = tweets_df1
    client = MongoClient("mongodb://localhost:27017")
    print("Connection Successful")
    mydb = client["TWEET"]
    import json
    # records = json.loads(tweets_df1.to_json(orient='records'))
    data = json.loads(data.to_json(orient='records'))
    from datetime import datetime
    Date = datetime.now().strftime('%d-%m-%Y')
    dict1 = {"Scraped Word": hash_tag, "Scraped Date": Date, "Data": data}
    mydb.mycol.insert_many([dict1])
