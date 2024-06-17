import json
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.title("Premier League")

#Lottie files
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

#Load Assets
lottie_coding1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_yLCHY6q3aU.json")
lottie_coding2 = load_lottiefile("Pages/versus.json")

with st.container():
    image = Image.open('premierl.png')

    # Display the image with center alignment
    st.image(image, use_column_width=True)

    st.write("The Premier League (legal name: The Football Association Premier League Limited) is the highest level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League (EFL). Seasons typically run from August to May with each team playing 38 matches against all other teams both home and away. Most games are played on Saturday and Sunday afternoons, with occasional weekday evening fixtures. The competition was founded as the FA Premier League on 20 February 1992 following the decision of First Division (top-tier league from 1888 until 1992) clubs to break away from the English Football League. However, teams may still be relegated into and promoted from the EFL Championship. The Premier League takes advantage of a lucrative television rights sale to Sky: from 2019 to 2020, accumulated television rights were worth around £3.1 billion a year, with Sky and BT Group securing the domestic rights to broadcast 128 and 32 games respectively.")

# Create a dropdown box
selected_option = st.selectbox("Select a Team 1", ["Arsenal", "Aston Villa", "Birmingham City", "Blackburn", "Blackpool", "Bolton", "Bournemouth", "Brentford", "Brighton", "Burnley", "Cardiff City", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Huddersfield", "Hull City", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester Utd", "Middlesbrough", "Newcastle Utd", "Norwich City", "Nott'ham Forest", "QPR", "Reading", "Sheffield Utd", "Southampton", "Stoke City", "Sunderland", "Swansea City", "Tottenham", "Watford", "West Brom", "West Ham", "Wigan Athletic", "Wolves"])

# Display the selected option
st.write("You selected:", selected_option)

#styling by CSS
st.markdown(
    """
    <style>
    .lottie-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the Lottie animation
st.markdown("<div class='lottie-container'>", unsafe_allow_html=True)
st_lottie(lottie_coding2, height=200)
st.markdown("</div>", unsafe_allow_html=True)

# Create a dropdown box
selected_option = st.selectbox("Select a Team 2", ["Arsenal", "Aston Villa", "Birmingham City", "Blackburn", "Blackpool", "Bolton", "Bournemouth", "Brentford", "Brighton", "Burnley", "Cardiff City", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Huddersfield", "Hull City", "Leeds United", "Leicester City", "Liverpool", "Manchester City", "Manchester Utd", "Middlesbrough", "Newcastle Utd", "Norwich City", "Nott'ham Forest", "QPR", "Reading", "Sheffield Utd", "Southampton", "Stoke City", "Sunderland", "Swansea City", "Tottenham", "Watford", "West Brom", "West Ham", "Wigan Athletic", "Wolves"])

# Display the selected option
st.write("You selected:", selected_option)
