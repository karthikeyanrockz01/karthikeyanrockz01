import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("NBA")

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
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_ef3beoqa.json")
lottie_coding2 = load_lottiefile("Pages/versus.json")

with st.container():
        st_lottie(lottie_coding, height=350, key="coding")
        st.write("The National Basketball Association (NBA) is a professional basketball league in North America composed of 30 teams (29 in the United States and 1 in Canada). It is one of the major professional sports leagues in the United States and Canada and is considered the premier professional basketball league in the world.The league was founded in New York City on June 6, 1946, as the Basketball Association of America (BAA).[1] It changed its name to the National Basketball Association on August 3, 1949, after merging with the competing National Basketball League (NBL).[4] In 1976, the NBA and the American Basketball Association (ABA) merged, adding four franchises to the NBA. The NBA's regular season runs from October to April, with each team playing 82 games. The league's playoff tournament extends into June. As of 2020, NBA players are the world's best paid athletes by average annual salary per player.")

        # Create a dropdown box
selected_option = st.selectbox("Select a Team 1", ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
                                "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
                                "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
                                "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
                                "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
                                "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards",])


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
selected_option = st.selectbox("Select a Team 2",
                               ["Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
                                "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
                                "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
                                "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
                                "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
                                "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"])


# Display the selected option
st.write("You selected:", selected_option)

# Button foe win pred NBA
# Button for Rank prediction
result = st.button("PREDICT WIN PERCENT")


