import streamlit as st

def contact_form():
    css = """
    <style>
        input[type=text], input[type=email], textarea {
            width: 100%; /* Full width */
            padding: 12px; /* Some padding */ 
            border: 1px solid #ccc; /* Gray border */
            border-radius: 4px; /* Rounded borders */
            box-sizing: border-box; /* Make sure that padding and width stay in place */
            margin-top: 6px; /* Add a top margin */
            margin-bottom: 16px; /* Bottom margin */
            resize: vertical; /* Allow the user to vertically resize the textarea (not horizontally) */
        }

        /* Style the submit button with a specific background color */
        button[type=submit] {
            background-color: #04AA6D;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        /* Darker green color when hovering over the submit button */
        button[type=submit]:hover {
            background-color: #45a049;
        }
    </style>
    """

    # Form HTML content
    contact_form = """
    <form action="https://formsubmit.co/lokeshsinha746@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    # Hide Streamlit Branding
    st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

    # Container for layout
    with st.container():
        st.write("---")
        st.header("Contact Me")
        
        left_column, right_column = st.columns(2)
        
        with left_column:
            st.markdown(css, unsafe_allow_html=True)
            st.markdown(contact_form, unsafe_allow_html=True)
        
        with right_column:
            st.empty()