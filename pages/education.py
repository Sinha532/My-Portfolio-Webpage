import streamlit as st

def education():
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>Education </h1>",unsafe_allow_html=True)
    left1,center1,right1=st.columns(3)
    with left1:
        st.subheader("BTech - Computer Science and Engineering")
        st.write("University College of Engineering JNTK, Narasaraopet")
        st.write("CGPA: 7.62")
    with center1:
        st.subheader("Intermediate - MPC")
        st.write("Sri Chaitanya Junior College, Rajamahendravaram")
        st.write("CGPA: 9.25")
    with right1:
        st.subheader("Secondary Higher Education")
        st.write("Don Bosco High School, Ravulapalem")
        st.write("CGPA: 9.7")