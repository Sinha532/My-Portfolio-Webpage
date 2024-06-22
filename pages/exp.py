import streamlit as st

def experience():
    st.write("---")
    st.markdown("<h1 style='text-align: center;'>Work Experience </h1>",unsafe_allow_html=True)
    left2,right2=st.columns(2)
    with left2:
        st.subheader("Machine Learning Intern")
        st.write("Feynn Labs")
        st.write("""
        - worked on various real world problems and business cases.
        - developed efficient and accurate machine learning models for the problems 
          and successful in solving them
        - Electric vehicle Market segmentation, remarkable work, where I acted as the team lead 
          and succedded in developing the solution with ML model of 93% accuracy
        """)
    with right2:
        st.subheader("Technical Trainer")
        st.write("CodeTantra")
        st.write("""
        - worked as a technical trainer, taking classes for technical UG students of some esteemed institutions.
        - taken up classes on Python Programming langauage, in smooth and understandable way.
        - acted as Product support engineer, by designing tests and helped in preparing materials for more innovative and practiced learning.
        """)