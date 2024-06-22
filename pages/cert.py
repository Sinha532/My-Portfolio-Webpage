import streamlit as st
from PIL import Image

image1=Image.open("images/NLP_cert.png")
image2=Image.open("images/GENAI_Cert.png")
image3=Image.open("images/tcs_cert.png")

certification_links = [
    "https://coursera.org/share/d46341b2534b2628480ebd2296205a03",
    "https://coursera.org/share/12759e9e2193cfdbc5ad5b9a394973ab",
    "https://www.tcsion.com/iDH/India/Dashboard/Documents"
]
def certifications():
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center;'>Certifications</h1>",unsafe_allow_html=True)
        st.write(" ")
        left,center,right=st.columns(3)
        with left:
            st.image(image1, width=403)
            st.markdown("""
                <h6 style='text-align: center; font-style: italic;'>
                    This Certification Deals with the self-Attention models,
                    the evolution of language models from encoding in one direction to bidirectional using the architecture of Deep-learning,
                    introducing to advanced NLP models, like T5, BERT etc.,
                    <br><a href="{link}" target="_blank">View Certification Details</a>
                </h6>
                """.format(link=certification_links[0]), unsafe_allow_html=True)

        with center:
            st.image(image2, width=390)
            st.markdown("""
                <h6 style='text-align: center; font-style: italic;'>
                    Introducing to how AI has evolved dealing with Natural Language,
                    from understanding the way computers read human language to present advanced NLP models like Transformers,
                    Developing our own systems with Transformers, Understand how Generative AI can be achieved.
                    <br><a href="{link}" target="_blank">View Certification Details</a>
                </h6>
                """.format(link=certification_links[1]), unsafe_allow_html=True)

        with right:
            st.image(image3, width=415)
            st.markdown("""
                <h6 style='text-align: center; font-style: italic;'>
                    A 15 days online virtual program, related to strengthen the soft skills needed to every upcoming IT Fresher,
                    studied and practiced throughout the program, gained some necessary qualities and knowledge useful to make our own mark in the IT field,
                    ended the course with learning fundamentals of trend technology like AI.
                    <br><a href="{link}" target="_blank">View Certification Details</a>
                </h6>
                """.format(link=certification_links[2]), unsafe_allow_html=True)

