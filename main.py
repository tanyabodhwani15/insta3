import streamlit as st
import base64
import requests
import webbrowser
#from streamlit_lottie import st_lottie


#def load_lottieurl(url: str):
   # r = requests.get(url)
   # if r.status_code != 200:
    #    return None
   # return r.json()


#lottie_animation1 = 'https://assets8.lottiefiles.com/private_files/lf30_5jrklsmp.json'
#lottie123 = load_lottieurl(lottie_animation1)
st.title("WELCOME TO MY WEB APP")
st.subheader("INSTAGRAM REACH ANALYSIS")
#st.markup("giphy.gif")
#st_lottie(lottie123, key='hello')
file_ = open("giphy.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)
link1 = '(https://tanyabodhwani15-insta3-pagesapp-skazw5.streamlit.app/)'
link1 = '[click here](https://tanyabodhwani15-insta3-pagesapp-skazw5.streamlit.app/)'
        st.markdown(link1, unsafe_allow_html=True)

if st.button('Click Here For Prediction'):
    webbrowser.open_new_tab(link1)

