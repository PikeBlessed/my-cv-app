import streamlit as st
import time
import pandas as pd
from experience import stream_data, toggle_newsletter_stats, toggle_button


#Presentation
col_1, col_2 = st.columns([0.8, 0.3])
with col_1: 
    st.title('Octavio de Paula')
    st.subheader('Marketing Specialist - Data Science Student')

with col_2:
    st.image('/home/pikeblessed/my-cv-app/files/Diseño sin título (1).png',
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
        - ML models: 
'''

projects_button = toggle_button('Deploy Projects')

if projects_button:
    st.write(stream_data(projects))