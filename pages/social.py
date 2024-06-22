import streamlit as st
from st_social_media_links import SocialMediaIcons

def media():
    with st.sidebar :
        st.write("---")
        st.markdown("<h2 style='text-align: center;'>You can see me here</h2>",unsafe_allow_html=True)
        social_media_links = [
            "https://www.linkedin.com/in/lokesh-sinha-n-952706246/",
            "https://github.com/Sinha532",
            "https://www.instagram.com/invites/contact/?igsh=hxasaxp968io&utm_content=jpz0kn8",
        ]

        social_media_icons = SocialMediaIcons(social_media_links)

        social_media_icons.render()
        st.write("---")
    
    with st.container():
        st.write("---")
        st.markdown("<h3 style='text-align: center;'>You can see me here</h3>",unsafe_allow_html=True)
        social_media_links = [
            "https://www.linkedin.com/in/lokesh-sinha-n-952706246/",
            "https://github.com/Sinha532",
            "https://www.instagram.com/invites/contact/?igsh=hxasaxp968io&utm_content=jpz0kn8",
        ]

        social_media_icons = SocialMediaIcons(social_media_links)

        social_media_icons.render()
        st.write(" ")
        st.markdown("""<h5 style='text-align: center; font-style: Italic;'>Don't use your knowledge to work for other's idea, 
                    use it to give life to your imagination.</h5>""",unsafe_allow_html=True)
