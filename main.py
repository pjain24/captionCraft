import streamlit as st
st.title('My Wellness Tracker')
st.write('Welcome to your own AI wellness tracker!')
options = ['','Happy', 'Sad', 'Angry', 'Excited', 'Anxious', 'Calm']

# Add radio buttons to your app
selected_option = st.selectbox('Select an option:', options)

# Display the selected option
# st.write('You selected:', selected_option)
if selected_option!='':
    # Display a text input box if an option is selected
    user_input = st.text_input('Tell me about it')

