import streamlist as st 

header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()

with header:
    st.title("Welcome to the application")
    st.text("idek this is more text here hehe")

with header:
    st.header("Welcome to the application")

with features:
    st.header("Welcome to the application")

with modelTraining:
    st.header("Welcome to the application")
