import streamlit as st

st.title('Device')
st.header('Register a device')
st.markdown('https://streamlit-example-app-bug-report-streamlit-app-lrm3fx.streamlit.app/')
st.header('List all registered devices')
st.subheader('Filter devices with interactive table')
st.markdown('https://streamlit-example-app-interactive-table-streamlit-app-mt9qg6.streamlit.app/')
st.subheader('Device location')
st.markdown('https://streamlit-demo-uber-nyc-pickups-streamlit-app-456wus.streamlit.app/')

st.text_input("device name")
st.text_input("IP address")
c1, c2, _ = st.columns((1, 2, 4))
c1.button("Add", type="primary")
c2.button("Remove")
