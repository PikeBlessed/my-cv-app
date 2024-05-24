import streamlit as st
import pandas as pd
import time

#Write experience with a animation like ChatGPT

'''def stream_data(markdown) -> st.markdown:
    for word in markdown.split(' '):
        yield word + ' '
        time.sleep(0.01)'''


def toggle_newsletter_stats():
    toggle_newsletter = st.toggle('**See newsletter stats**')
    if toggle_newsletter: 
        #newsletter datasets 
        df_all_days_emails = pd.read_csv('/home/pikeblessed/my-cv-app/files/stats all days emails.csv')
        df_all_days_suscribers = pd.read_csv('/home/pikeblessed/my-cv-app/files/stats all suscribers.csv')
        df_campaings_per_month = pd.read_csv('/home/pikeblessed/my-cv-app/files/stats campaigns.csv')

        ##general stats
        col_1, col_2, col_3, col_4 = st.columns(4)
        col_1.metric(label='Emails Sent', value=2558)
        col_2.metric(label='Open', value=1685)
        col_3.metric(label='Clics', value=1252)
        col_4.metric(label='CTOR', value='74.3%')

        ##chart 1
        st.area_chart(df_all_days_emails, x='day', y=['open', 'clics'])

        ##chart 2
        st.area_chart(df_all_days_suscribers, x='day', y=['suscriptions', 'cancelled_suscriptions (peaks removed by me)'])

        ##chart 3
        st.line_chart(df_campaings_per_month, x='month', y=['campaign','emails sent','open','clics','cancelled suscriptions','spam reports'])


def toggle_button(namebutton, width=True):
    if namebutton not in st.session_state:
        st.session_state[namebutton] = False

    def click_button():
        st.session_state[namebutton] = not st.session_state[namebutton]

    btn = st.button(namebutton, use_container_width=width)
    if btn:
        click_button()
    return st.session_state[namebutton]

form_action = f"https://formsubmit.co/depaulaoctavio04@gmail.com"

def contact():
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
        <input type="hidden" name="_next" value="http://localhost:8502/">
        <input type="submit" value="Send">
    </form>
    """

    code = '''
        <style>
            input[type="text"]:focus, input[type="email"]:focus, textarea:focus {
                color: #000000;
                background-color: #FFA07A; /* white background on focus */
            }
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
    return st.html(code), st.markdown(form_html, unsafe_allow_html=True)


def show_technologies(query):
    for index, row in query.iterrows():
        col1, col2 = st.columns([0.05, 0.95])
        with col1:
            st.image(row['icon'])
        with col2:
            st.write(row['name'])

def message(spinner_message, toast_message, icon):
    with st.spinner(spinner_message):
        time.sleep(1)
        message = st.toast(toast_message, icon=icon)
        time.sleep(1)
        message.empty()