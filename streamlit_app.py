import streamlit as st
import httpx

# Set page config
st.set_page_config(
    page_title="Python App Demo",
    page_icon="🚀",
    layout="wide",
)

# Header
st.title("🚀 Python Application")
st.markdown("### Streamlit + FastAPI Integration Demo")

# Backend connection
st.subheader("Backend Connection")
if st.button("Check Backend Health"):
    try:
        response = httpx.get("http://localhost:8000/health")
        if response.status_code == 200:
            st.success("Backend is healthy! ✅")
        else:
            st.error(f"Backend returned status code {response.status_code}")
    except Exception as e:
        st.error(f"Failed to connect to backend: {str(e)}")

# Demo app
st.subheader("Demo Application")
with st.form("demo_form"):
    user_input = st.text_input("Enter some text")
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.write(f"You entered: {user_input}")
        
# Sidebar
with st.sidebar:
    st.header("About")
    st.markdown("""
    This is a demo application showcasing the integration between:
    - **Streamlit**: Frontend UI
    - **FastAPI**: Backend API
    
    Both services run in parallel in the sandbox environment.
    """) 
