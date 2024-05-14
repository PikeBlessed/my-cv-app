import streamlit as st
import time
import pandas as pd
from experience import stream_data, toggle_newsletter_stats, toggle_button


#Presentation
col_1, col_2 = st.columns([0.8, 0.2])
with col_1: 
    st.title('Octavio de Paula')
    st.subheader('Marketing Specialist - Data Science Student')

with col_2:
    st.image('files/diseño_sin_título.png',
             width=150)



#Experience
experience = '''
##### Experience
- One year working like Marketing Generalist in [PHNAN](https://www.instagram.com/_phnan_/).
    - Email Marketing: I'm writing a weekly photographic newsletter to hundreds of people through MailerLite.
'''


continue_experience = '''
    -
        - Content creation: Multiple formarts to grow in social media.
            - Reels or Tiktoks: Dashes, scenes and descriptions.
            - Individual graphical posts and informative carousels: Everything.
            - Stories: Dynamic and interactive stories to connect with the audience or sell them.
            - Threads: Reflexions or phrases about photographic topics which will generate discussions.
        - Marketing campaigns: Several campaings to annonunce digital products based pay and organic content.
            - Organic content: In the product debut, the first focus is completely on organic content related with it.
            - Pay content: After first product moments I make focus on pay content through Facebook Ads.
        - Automations: Multiple automatizations with differents targets made with ManyChat, Zapier or any email software.
            - Sell digital products: Organic content connected with a automatized flow that leads the custome to a landing page.
            - Lead traffic to other platforms (Podcast, Newsletter, etc.): These connections can be through a link or APIs in any situations.
            - Post purchase service: With emails automatizations give product, support or any need to customer. 
            - Extra: Support, FAQ, ChatBot, etc.
    - Multiple Landing Pages with WordPress (all of them converted):
        - Optimization: Webs created as fast as possible.
        - Simple but functional: I don't stand out for my web design. It's for this that I try to make them simple and convertible.
'''


experience_button = toggle_button('Deploy Experience')

##Deploy experience
if experience_button:
    st.write(stream_data(experience))
    toggle_newsletter_stats()
    st.write(stream_data(continue_experience))


#Projects
projects = '''
    - Data science and MLOPs: I have made several projects about Data, from simple things such as Data Analysis, small ML models, ETL process to complete data science pipeline (ETL, EDA, modeling, MLOPs, etc).
        - ML models: My [best project](https://github.com/PikeBlessed/deploy-project-datascience) about MLOPs, that was to PHNAN. In this project I've applied a complete data science pipeline, API(FastAPI), differents ML models, Docker, etc.
        - Data Analysis: [Project](https://deepnote.com/workspace/proyecto-pandas-y-numpy-9f6dc92a-c802-474f-b7a1-01e51b6fc675/project/Octavios-Untitled-project-29dbf950-c5bc-4211-afb5-bd91a042da55/notebook/proyecto_data_science-d6f691c0cad446d29fbc07a32780a1a6) 
        - IA Photographic App (in progress): An app about a chatbot integred with IA to analyze photos and bot can act like profesional.  
'''

projects_button = toggle_button('Deploy Projects')

if projects_button:
    st.write(stream_data(projects))

form_action = f"https://formsubmit.co/depaulaoctavio04@gmail.com"

with st.expander('Contact with me'):
    with st.container(border=True, height=470):
        name = st.text_input("Name",)
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")


        form_fields = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }

        form_html = f"""
        <form action="{form_action}" method="POST">
            <input type="hidden" name="name" value="{name}" required>
            <input type="hidden" name="email" value="{email}" required>
            <input type="hidden" name="message" value="{message}" required>
            <input type="hidden" name="_subject" value="{subject}" required>
            <input type="hidden" name="_captcha" value="false">
            <input type="hidden" name="_template" value="table">
            <input type="submit" value="Send">
        </form>
        """

        code = '''
            <style>
                input[type="submit"] {
                    background-color: #FFA07A;
                    color: #000000;
                    padding: 5px 10px;
                    border-style: solid;
                    border-width: 0px; 
                    border-color: #87CEEB;
                    border-radius: 5px;
                    cursor: pointer;
                    width: 100%;
                }

                .refill {
                    border-bottom: 1px solid #ccc;
                    margin-top: 10px;
                }
            </style>
        '''
        st.html(code)
        st.markdown(form_html, unsafe_allow_html=True)