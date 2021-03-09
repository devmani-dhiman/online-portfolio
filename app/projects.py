import streamlit as st

def app():
    st.markdown("<h1 style='text-align: center; color: Purple;'>Projects</h1>",
            unsafe_allow_html=True)

    selected = st.selectbox(label="Select one option", options=[
                        'Data Science', 'Python Development', 'Streamlit'])


    if selected == 'Data Science':

        st.write(f'You have selected to view {selected} projects')
        st.write(
            "Link to Github repository: - https://github.com/devmani-dhiman/projects.git")
        st.markdown("<h2 style='text-align: center;'>Property Price Prediction</h2>",
                unsafe_allow_html=True)

        st.subheader("""This projects predicts the Price of a property based on the following criteria such as
                1. Area (in Square Feet)
                2. Location
                3. BHK
                4. Number of Bathrooms
        """)
        st.write("""
        The program accepts these 4 inputs from the user and based on the model developed it predicts the price of the property.
        This app is tested via Postman software (Postman is used to test the "GET", "POST", and other HTTPS request.)
        The backend was developed with Flask which is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. 
        """)
        st.write("""
        The backend fetches the location data and calculate the price according to the user input.
        Fetching the location was done using "GET" request and prediction was done using "POST" request. 
        """)

        st.markdown("<h2 style='text-align: center;'>Spam Classifier</h2>",
                    unsafe_allow_html=True)

        st.subheader(
            """Spam classifier predicts whether the received message is spam or not.""")
        st.write("""
        The first step is to remove stopwords from input message.
        Stopwords are the words in any language which does not add much meaning to a sentence. Some of the most common, short function words, such as the, is, at, which, and on.
        Next step is to convert the words into vectors in order to make them machine readable.
        Finally, these vectors are classified as Spam or Not Spam (Ham) by the model built using SVM Alogrithm.
        """)

    elif selected == 'Python Development':
        st.write(f'You have selected to view {selected} projects')
        st.write(
            "Link to Github repository: - https://github.com/devmani-dhiman/projects.git")
        st.markdown("<h2 style='text-align: center;'>Web Scraping using Python</h2>",
                    unsafe_allow_html=True)

        st.write("""Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.
        """)
        st.write("""
        The scraper here is used to scrape jobs from the career page of Facebook India, and these jobs were uploaded to a MySQL database. The Library used were
                
                1. Requests
                2. html2text
                3. Beautiful Soup
                4. MySQL.Connector
        """)
        st.write("""
        The data that was scraped includes: -

                1. Total Jobs available
                2. Job Title 
                3. Job Description.
                4. Location.
                5. Responsibilities and Qualification. 
        """)

        st.markdown("<h2 style='text-align: center;'>Creating a WordCloud</h2>",
                unsafe_allow_html=True)

        st.write("""
        A Word cloud is a novelty visual representation of text data, 
        typically used to depict keyword metadata on websites, or to visualize free form text.
        Tags are usually single words, and the importance of each tag is shown with font size or color.
        """)

        st.write("""
        The library used were: - 

                1. Numpy 
                2. Wikipedia
                3. PIL.image
                4. Wordcloud
                5. Matplotlib
        """)

        st.write("""
        The word cloud here uses wikipedia text to visualize the text in a shape of a cloud.
        For more information about this refer to the link mentioned above.
        """)

    else:
        st.write(f'You have selected to view {selected} projects')
        st.write(
            "Link to Github repository: - https://github.com/devmani-dhiman/projects.git")
        st.markdown("<h2 style='text-align: center;'>Crypto Currency Tracker App</h2>",
                unsafe_allow_html=True)

        st.subheader("A tracker to track Multiple Crypto currencies")
        st.write("""
        The tracker scrapes the data from "https://coinmarketcap.com/ website and displays the top 100 crypto currencies.
        The app fetches data in real time and thus could take time to load for the first time. You can check out the app by
        clicking on the link given below.
        
        """)
        st.write("""
        Link to app : https://cryptotrackerstreamlit.herokuapp.com/
        """)

        st.write("""
        You can select multiple currencies from Crypto currency selector given in the navigation slider to
        compare and see volatility in the price and volume with the flexibility of selecting the time duration from
        "1 Hr", "24 Hrs", "7 days".
        """)

        st.markdown("<h2 style='text-align: center;'>Online Portfolio</h2>",
                    unsafe_allow_html=True)

        st.subheader(
            """A web app used to display your skill and achievement online.""")
        st.write("""This Web/Online Portfolio is created using streamlit""")
        st.text("")
        st.text("")
        st.text("")

    st.text(" P.S: - More projects will be added.")
