import streamlit as st
from PIL import Image


image2=Image.open("images/System Architecture final.png")
image3=Image.open("images/logo21.png")
image4=Image.open("images/ElectricVehicle.png")

def projects():
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center;'>My Work</h1>",unsafe_allow_html=True)
        
        image_column, text_column=st.columns((1,2))

        with image_column:
            st.image(image2,width=400)
        with text_column:
            st.subheader("Chat Sentiment Analysis using BERT")
            st.markdown(
                """<h6>
                This project aims to analyze sentiments in WhatsApp chat exports using BERT (Bidirectional Encoder Representations from Transformers). 
                By uploading a chat file, the system preprocesses the messages, applies various visualization techniques, and performs sentiment analysis on each message, 
                providing insightful results.
                </h6>""",unsafe_allow_html=True)
            st.markdown("[Repository Available here](https://github.com/Sinha532/Sentiment-Analysis-using-BERT.git)")

    with st.container():
        st.write("##")
        image_column, text_column=st.columns((1,2))

        with image_column:
            st.image(image3,width=400)
        with text_column:
            st.subheader("Customer Feedback Form using Flask")
            st.markdown(
                """<h6>
                This project deals with the automation of Feedback form and notifying the acknowledgement of taking their feedback under consideration.
                The system is built using Flask, a Python web framework, and leverages PostgreSQL for database management, using SMTP and mailtrap modules 
                for mail transferring. This application is an end-to-end application of Feedback mechanism which is adapted by many of the MNC's and e-commerce applications.
                </h6>""",unsafe_allow_html=True)
            st.markdown("[Repository Available here](https://github.com/Sinha532/Feedback-form.git)")
    
    with st.container():
        st.write("##")
        image_column, text_column=st.columns((1,2))

        with image_column:
            st.image(image4,width=400)
        with text_column:
            st.subheader("Electric Vehicle Market Segmentation")
            st.markdown(
                """<h6>
                The strategic marketing plan provides a comprehensive document outlining the goals,
                objectives, strategies, and tactics for the company’s marketing activities. It serves as a roadmap
                for the marketing team, guiding their actions to achieve specific business outcomes. For
                example, expanding into new markets and increasing market share may be a strategic objective.
                Strategies to accomplish this could include market research, adapting products/services,
                localized marketing approaches, collaboration with local partners, targeted advertising, and
                monitoring performance.
                </h6>""",unsafe_allow_html=True)
            st.markdown("[Repository Available here](https://github.com/Sinha532/EV_Market_Segmentation.git)")
        
