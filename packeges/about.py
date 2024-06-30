import streamlit as st

def aboutus():
    
    sy = st.sidebar.selectbox('Select dataset for prediction', [1,2,3,4])
    
    # Titles
    st.title("About Stock Price Predictor")

    # Description
    st.write("""
    This web app uses machine learning algorithms to predict stock prices. Our goal is to provide a useful tool for investors and traders.
    """)

    # Team Members
    st.subheader("Team Members")
    st.write("""
    * **Ganesh Borkar**: Developer 
    * **Akash Gatkal**: Developer
    * **Ritesh Mohite**: Developer
    """)

    # Technologies Used
    st.subheader("Technologies Used")
    st.write("""
    * **Python**: For data analysis and machine learning
    * **Streamlit**: For building the web app
    * **sklearn**: For machine learning algorithms
    * **Yahoo Finance**: For historical stock data
    """)

    # Contact Information
    st.subheader("Contact Us")
    st.write("""
    For any questions or feedback, please reach out to [ganeshborkar31@yahoo.com](mailto:ganeshborkar31@yahoo.com).
    """)

    # Social Media Links
    st.subheader("Follow Us")
    st.write("""
    [GitHub](https://github.com/ganeshborkar31) | [LinkedIn](https://www.linkedin.com/in/ganeshborkar31/)
    """)