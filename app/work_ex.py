import streamlit as st

def app():
    st.markdown("<h1 style='text-align: center; color: Purple;'>Work Experience</h1>", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .big-font {
        font-size:40px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Infosys</p>', unsafe_allow_html=True)
    st.subheader("Employee")
    st.markdown("<h3 style='color: purple;'>Sep 2019 - Present</h3>", unsafe_allow_html=True)
    st.write("1. Worked as MS Full stack .Net developer.")
    st.write("2. Automated the process of killing a redundant task thus saving resources.")
    st.write("3. Create database schema for the requied task and set up data pipelines.")
    st.write("4. Automated the process of invoice processing using OCR techniques.")
    

    st.markdown('<p class="big-font">The D-zone</p>', unsafe_allow_html=True)
    st.subheader("UX Research Intern")
    st.markdown("<h3 style='color: purple;'>Jan 2019 - Sep 2019</h3>", unsafe_allow_html=True)
    st.write("1. Conducted Research and Polls to know the user Behaviour.")
    st.write("2. Collaborated with other UX/UI to create a basic structure of the application.")
    st.write("3. Collaborated with developers and other stakeholders to gain new insights")
    st.write("4. Organised Brain stroming session with stakeholders to create a better User Experience")
    st.write("5. Done secondary research and also took some content creation task.")


    st.markdown('<p class="big-font">Internshala Student Partner 9.0</p>', unsafe_allow_html=True)
    st.subheader("Intern")
    st.markdown("<h3 style='color: purple;'>March 2018 - May 2018</h3>", unsafe_allow_html=True)
    st.write("1. Represented Intershala in my College.")
    st.write("2. Gained Leadership, Communication and marketing skills.")
    st.write("3. Learned how to approach/talk to people.")


    st.markdown('<p class="big-font">SNA Power Engineering Pvt. Ltd.</p>', unsafe_allow_html=True)
    st.subheader("Hardware Developer Intern")
    st.markdown("<h3 style='color: purple;'>Sep 2017 - Dec 2017</h3>", unsafe_allow_html=True)
    st.write("1. Done research on the working of a Li-ion battery.")
    st.write("2. Worked with the team to create a Battery Management System.")
    st.write("3. Build the prototye with the help of Arduino Micro Controller.")

    st.markdown('<p class="big-font">Infowiz</p>', unsafe_allow_html=True)
    st.subheader("Intern/Trainee")
    st.markdown("<h3 style='color: purple;'>Jun 2017 - July 2017</h3>", unsafe_allow_html=True)
    st.write("1. Built Hardware using 8051 Microcontroller and Arduino.")
    st.write("2. Created a Pick n Place robot using Arduino and Embedded C programing language")