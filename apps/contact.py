import streamlit as st


def app():
    st.markdown("<h1 style='text-align: center; color: Purple;'>Contact</h1>",
                unsafe_allow_html=True)


    st.header("""The Best way to connect with me is via Linkedin or email. However, below you can see other options to connect with me.""")
    st.subheader("""Feel Free to connect with me.""")


    col1, col2 = st.beta_columns([1, 20])

    with col1:
        st.markdown("<img src=\"https://img.icons8.com/android/40/000000/phone.png\"/>",
                unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.markdown("<img src=\"https://img.icons8.com/offices/40/000000/gmail-login.png\"/>",
                unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.markdown("<img src=\"https://img.icons8.com/android/40/000000/linkedin.png\"/>",
                unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.markdown("<img src=\"https://img.icons8.com/metro/40/000000/github.png\"/>",
                unsafe_allow_html=True)

    with col2:
        st.write("+91 9634740565")
        st.text("")
        st.text("")
        st.markdown("<address><a href=\"mailto:devmani96@gmail.com\">devmani96@gmail.com</a></address>",
                unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.markdown("<p><a href=\"https://www.linkedin.com/in/devmanidhiman\">Devmani Dhiman</a></p>",
                unsafe_allow_html=True)
        st.text("")
        st.text("")
        st.markdown("<p><a href=\"https://github.com/devmani-dhiman/\">Github</a></p>",
                unsafe_allow_html=True)
