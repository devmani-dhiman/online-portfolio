import streamlit as st


def app():
    st.markdown("<h1 style='text-align: center; color: Purple;'>Home</h1>", unsafe_allow_html=True)

    st.markdown("<h2><b>Hello! Thank You for taking the time to view my Portfolio. This webapp was built using Streamlit, a Python Library</b></h2>", unsafe_allow_html=True)

    st.text("")

    st.markdown("<h2> <b>Feel Free to drop your feedback about this portfolio. You can find the necessary details in the contact section of web app.</b></h2>", unsafe_allow_html=True)

    st.text("")

    st.markdown("<h2><b>Have a great Day</b></h2>", unsafe_allow_html=True)

    st.text("")
    st.subheader("Thank you")

    st.write("P.S: - This is still under development. Apologies for the inconvienence")