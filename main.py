import streamlit as st
import webbrowser
import requests
# Set page title and favicon
st.set_page_config(
    page_title="Tomato Cultivator Dashboard",
    page_icon="🍅",
)

# Language button in the top-left corner
if st.button("🌐 Language"):
    language = st.radio("", ["English 🇬🇧", "हिंदी 🇮🇳", "తెలుగు 🇮ి", "தமிழ் 🇮🇳", "मराठी 🇮🇳", "ગુજરાતી 🇮🇳", "বাংলা 🇮🇳"])

# Create a sidebar with options
st.sidebar.title("Dashboard")
st.sidebar.markdown("---")

# Information Section
st.sidebar.subheader("INFORMATION")
info_option = st.sidebar.selectbox("", ["Select an Option","News", "Forum", "Support"])

# Market Section
st.sidebar.markdown("---")
st.sidebar.subheader("MARKET")
market_option = st.sidebar.selectbox("", ["Select an Option","Market Trends", "Add a Listing", "Check My Listings"])

# Tools Section
st.sidebar.markdown("---")
st.sidebar.subheader("TOOLS")
tools_option = st.sidebar.selectbox("", ["Select an Option", "Tomato Variety Recommendation", "Fertilizer Recommendation"])

# Center the page title
st.title("Tomato Cultivator Dashboard")
# Floating shaded box for weather details
st.markdown(
    """
    <style>
    .weather-box {
        background-color: #f5f5f5;
        border: 1px solid #d3d3d3;
        padding: 10px;
        border-radius: 10px;
        margin: 10px;
        box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.2);
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown("<h2 class='weather-box'>Weather Details</h2>", unsafe_allow_html=True)

# Function to fetch weather data from OpenWeather API
def get_weather_data(api_key, lat, lon):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lon, "appid": api_key, "units": "metric"}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

# Replace 'YOUR_OPENWEATHER_API_KEY' with your actual API key
api_key = 'c3d1ff1002a9dd726eb06249dfed1cb5'

# Get user location and fetch weather data automatically
try:
    lat_lon = st.location.get_last_known_location()
    if lat_lon is not None:
        lat, lon = lat_lon
        weather_data = get_weather_data(api_key, lat, lon)
        weather = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']

        st.write(f"Weather: {weather.capitalize()}")
        st.write(f"Temperature: {temperature}°C")
        st.write(f"Atmospheric Pressure: {pressure} hPa")
        st.write(f"Humidity: {humidity}%")
except Exception as e:
    st.error("Could not fetch weather data. Please check your location settings or try again later.")

# Handle sub-options for the Information Section here.
if info_option == "Forum":
    st.markdown(
        """
        <style>
        .forum-box {
            border: 1px solid #d3d3d3;
            padding: 20px;
            border-radius: 10px;
            margin: 10px;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    st.markdown("<h2 class='forum-box'>Forum: Share Your Information/Doubts</h2>", unsafe_allow_html=True)

    # Create a form for user input
    with st.form("forum_form"):
        user_name = st.text_input("Your Name", max_chars=100)
        user_info = st.text_area("Information/Doubt", max_chars=500)
        submit_button = st.form_submit_button("Post")

    if submit_button:
        # You can handle the form submission here, for example, print the user input
        st.write(f"User Name: {user_name}")
        st.write(f"Information/Doubt: {user_info}")
# Handle sub-options for the Market Section here.
# Display the News page and preview the link
if info_option == "News":
    st.markdown(
        """
        <style>
        .news-box {
            border: 1px solid #d3d3d3;
            padding: 10px;
            border-radius: 10px;
            margin: 10px;
        }
        </style>
        """
        , unsafe_allow_html=True
    )

    st.markdown("<h2 class='news-box'>Latest Agricultural News</h2>", unsafe_allow_html=True)
    st.markdown("<iframe src='https://agrinews.in' width='800' height='600'></iframe>", unsafe_allow_html=True)
# Create a single "Visit" button for both Tomato Variety Recommendation and Fertilizer Recommendation
if tools_option == "Tomato Variety Recommendation":
    if st.button("Visit Tomato Variety Recommendation"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://tomato-variety-site.streamlit.app/">', unsafe_allow_html=True)

if tools_option == "Fertilizer Recommendation":
    if st.button("Visit Fertilizer Recommendation"):
        st.markdown('<meta http-equiv="refresh" content="0;url=https://fertilizer-site.streamlit.app/">', unsafe_allow_html=True)
