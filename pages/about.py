import streamlit as st
from PIL import Image

image1=Image.open("images/new.jpg",)
def about():
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center;'>About Me</h1>",unsafe_allow_html=True)
        empty_col1, left, right, empty_col2 = st.columns([1, 12, 12, 1])
        with left :
            st.write("#")
            st.markdown("""<h6 style='text-align: center; font-style: italic;'>I am Lokesh Sinha, recently graduated from University College of Engineering JNTK Narasaraopet from Computer Science and Engineering stream. 
                    The reason to choose the branch is the interest towards coding for me. I learnt C, C++ , Java and Python from all these programming languages
                    I am comfortable working with Python, this laid a foundation to the interest towards advanced technologies like Data Science, Machine learning and NLP. 
                    So far I have done some certifications on those technologies from where I have gained substantial amount of knowledge to complete projects on time and 
                    also helped me to work efficiently as a Machine learning intern at company named Feynn labs, working on some real world business cases and Market Segmentation, 
                    leveraging machine learning algorithms at the best. 
                    Now I want to utilise those skills and knowledge to work in your esteemed organisation and wished to be a part of company's growth and Success.</i></h6>""",unsafe_allow_html=True)

        with right:
            st.write("#####")
            st.image(image1, width=300)