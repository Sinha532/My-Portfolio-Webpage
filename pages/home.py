import streamlit as st


def show_home():
    css="""
    <style>
    @keyframes wave {
    0% { transform: rotate(0.0deg); }
    10% { transform: rotate(14.0deg); }
    20% { transform: rotate(-8.0deg); }
    30% { transform: rotate(14.0deg); }
    40% { transform: rotate(-4.0deg); }
    50% { transform: rotate(10.0deg); }
    60% { transform: rotate(0.0deg); }
    100% { transform: rotate(0.0deg); }
    }

    .wave-hand {
    display: inline-block;
    transform-origin: 70% 70%;
    animation: wave 2s infinite;
    font-size: 2em; /* Increase this value to make the emoji larger */
    }
    </style>
    """
    
    html = """
    <h1 style='text-align: center;'>
    Hi, I am Lokesh Sinha <span class="wave">👋</span>
    </h1>
    """
    with st.container():
        st.markdown(css, unsafe_allow_html=True)
        st.markdown(html,unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Aspiring Python Developer  | Data Science, Machine Learning and AI Enthusiast</h2>",unsafe_allow_html=True)
        st.markdown("<h6 style='text-align: center;'>I am passionate about finding ways to use Python and advanced technologies to find Solutions for the moder problems and efficient ways to include AI in our daily needs.</h6>",unsafe_allow_html=True)
