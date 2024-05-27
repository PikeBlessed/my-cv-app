import streamlit as st
import time
import pandas as pd
from experience import toggle_newsletter_stats, toggle_button, contact, show_technologies, message
import psycopg2

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
            - Stories: Dynamic and interactive stories to connectionect with the audience or sell them.
            - Threads: Reflexions or phrases about photographic topics which will generate discussions.
        - Marketing campaigns: Several campaings to annonunce digital products based pay and organic content.
            - Organic content: In the product debut, the first focus is completely on organic content related with it.
            - Pay content: After first product moments I make focus on pay content through Facebook Ads.
        - Automations: Multiple automatizations with differents targets made with ManyChat, Zapier or any email software.
            - Sell digital products: Organic content connectionected with a automatized flow that leads the custome to a landing page.
            - Lead traffic to other platforms (Podcast, Newsletter, etc.): These connectionections can be through a link or APIs in any situations.
            - Post purchase service: With emails automatizations give product, support or any need to customer. 
            - Extra: Support, FAQ, ChatBot, etc.
    - Multiple Landing Pages with WordPress (all of them converted):
        - Optimization: Webs created as fast as possible.
        - Simple but functional: I don't stand out for my web design. It's for this that I try to make them simple and convertible.
'''
@st.experimental_fragment
def experience_button():
    experience_butt = toggle_button('Deploy Experience')

    ##Deploy experience
    if experience_butt:
        st.write(experience)
        toggle_newsletter_stats()
        st.write(continue_experience)

experience_button()


#Projects
projects = '''
    - Data science and MLOPs: I have made several projects about Data, from simple things such as Data Analysis, small ML models, ETL process to complete data science pipeline (ETL, EDA, modeling, MLOPs, etc).
        - ML models: My [best project](https://github.com/PikeBlessed/deploy-project-datascience) about MLOPs, that was to PHNAN. In this project I've applied a complete data science pipeline, API(FastAPI), differents ML models, Docker, etc.
        - Data Analysis: [Project](https://deepnote.com/workspace/proyecto-pandas-y-numpy-9f6dc92a-c802-474f-b7a1-01e51b6fc675/project/Octavios-Untitled-project-29dbf950-c5bc-4211-afb5-bd91a042da55/notebook/proyecto_data_science-d6f691c0cad446d29fbc07a32780a1a6) 
        - IA Photographic App (in progress): An app about a chatbot integred with IA to analyze photos and bot can act like professional.  
'''

@st.experimental_fragment
def projects_button():
    projects_butt = toggle_button('Deploy Projects')

    if projects_butt:
        st.write(projects)

projects_button()

#Capabilities connectionected with SQL database
@st.cache_resource
def connection():
    conn = st.connection(name="postgresqll", type="sql")
    return conn




capabilities = st.radio('###### Select what you want see', ['Hard skills', 'Technologies', 'Soft skills'], horizontal=True, index=None)

##Hard Skills
bring_hard_skills = connection.query('SELECT hs.name AS hard_skill_name, t.icon, t.name AS technologie_name FROM public.hard_skills hs JOIN public.technologies t ON hs.technologie_id = t.id;')

if capabilities == 'Hard skills':
    message(spinner_message='SELECT hs.name AS hard_skill_name, t.icon, t.name AS technologie_name FROM public.hard_skills hs JOIN public.technologies t ON hs.technologie_id = t.id;',
        toast_message='You select Hard Skills', icon='✅')
    for index, row in bring_hard_skills.iterrows():
        col1, col2, col3 = st.columns([0.65, 0.1, 0.6 ])
        with col1:
            name = row['hard_skill_name']
            st.write(name, '➤') 
        with col2:
            st.image(row['icon'])
        with col3:
            st.write(row['technologie_name'])


##Technologies 
all_techs = connection.query('SELECT * FROM technologies;')
data_techs = connection.query("SELECT icon, name FROM technologies WHERE area = 'data';")
development_techs = connection.query("SELECT icon, name FROM technologies WHERE area = 'development';")
marketing_techs = connection.query("SELECT icon, name FROM technologies WHERE area = 'marketing';")

if capabilities == 'Technologies':

    filter= st.selectbox('***What technologies you want see?***',
                            ('All', 'Data', 'Development', 'Marketing'),
                            placeholder='Choose an option', index=None)
    if filter == 'All':
        message(spinner_message='SELECT * FROM technologies;', 
                toast_message='You select all Technologies', icon='✅')
        show_technologies(all_techs)
    
    if filter == 'Data':
        message(spinner_message="SELECT icon, name FROM technologies WHERE area = 'data';", 
                toast_message='Switch to Data', icon='✅')
        show_technologies(data_techs)

    if filter == 'Development':
        message(spinner_message="SELECT icon, name FROM technologies WHERE area = 'development';", 
                toast_message='Switch to Development', icon='✅')
        show_technologies(development_techs)

    if filter == 'Marketing':
        message(spinner_message="SELECT icon, name FROM technologies WHERE area = 'marketing';", 
                toast_message='Switch to Marketing', icon='✅')
        show_technologies(marketing_techs)


##Soft Skills
bring_soft_skills = connection.query('SELECT * FROM soft_skills;')
if capabilities == 'Soft skills':
    message(spinner_message='SELECT * FROM soft_skills;',
        toast_message='You select Soft Skills', icon='✅')
    for index, row in bring_soft_skills.iterrows():
        with st.container(border=True):
            skills = row['name'] 
            st.caption(f"<p style='color:#FFA07A'>{skills}</p>", unsafe_allow_html=True)

#Contact
@st.experimental_fragment
def expander_contact():
    with st.expander('**Contact with me**'):
        with st.container(border=False, height=440):
            contact()
expander_contact()