import streamlit as st
import pandas as pd

#Write experience with a animation like ChatGPT
def stream_data(markdown) -> st.markdown:
    for word in markdown.split(' '):
        yield word + ' '
        #time.sleep(0.05)

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
        #st.area_chart(df_all_days_emails, x='day', y=['open', 'clics'])

        ##chart 2
        #st.area_chart(df_all_days_suscribers, x='day', y=['suscriptions', 'cancelled_suscriptions (peaks removed by me)'])

        ##chart 3
        #st.line_chart(df_campaings_per_month, x='month', y=['campaign','emails sent','open','clics','cancelled suscriptions','spam reports'])

def toggle_button(namebutton, width=True):
    if namebutton not in st.session_state:
        st.session_state[namebutton] = False

    def click_button():
        st.session_state[namebutton] = not st.session_state[namebutton]

    btn = st.button(namebutton, use_container_width=width)
    if btn:
        click_button()
    return st.session_state[namebutton]
