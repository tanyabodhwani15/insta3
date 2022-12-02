import streamlit as st
import pickle
import base64
import requests
#from streamlit_lottie import st_lottie


model = pickle.load(open('Model.pkl', 'rb'))
col1, col2, = st.columns((2, 2,))

with col1:
    st.title("Instagram Impression Analysis")

with col2:
    file_ = open("gif2.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
    )
#with col2:
    #def load_lottieurl(url: str):
     #   r = requests.get(url)
      #  if r.status_code != 200:
        #    return None
      #  return r.json()


    #lottie_animation1 = "https://assets10.lottiefiles.com/packages/lf20_toqwmdjr.json"
    #lottie_animi = load_lottieurl(lottie_animation1)

    #st_lottie(lottie_animi, key='hello')

st.subheader('This model will have you to find out the reach or impression of your post or story.')


def run():
    name = st.text_input("Write your name of your instagram account.  ")
    Likes = st.number_input("How many likes do you have on your post or reel ? 👍", value=0)
    Saves = st.number_input("How many people saved your post or reel ?", value=0)
    Comments = st.number_input("How many comments you got on your post or reel ? ", value=0)
    Shares = st.number_input("How many people shared your post or reel ? ", value=0)
    Profile_Visits = st.number_input("How many people visited your profile ?", value=0)
    follows = st.number_input("How many people follows you on instagram ?", value=0)
    acc = st.checkbox('Your account should be public account')

    if st.button("submit") and acc:

        features = [[Likes, Saves, Comments, Shares, Profile_Visits, follows]]
        Impressions = model.predict(features)
        st.write('HELLO ', name, " ! from the above given details , your impressions are ", Impressions)

        if not acc:
            st.error('error')


run()
