import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import torch
from sklearn.metrics import accuracy_score

# Lottie files and functions
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

# Load Assets
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_ef3beoqa.json")
lottie_coding2 = load_lottiefile("Pages/versus.json")

st.title("NBA")

with st.container():
    st_lottie(lottie_coding, height=350, key="coding")
    st.write("The National Basketball Association (NBA) is a professional basketball league in North America composed of 30 teams (29 in the United States and 1 in Canada). It is one of the major professional sports leagues in the United States and Canada and is considered the premier professional basketball league in the world. The league was founded in New York City on June 6, 1946, as the Basketball Association of America (BAA). It changed its name to the National Basketball Association on August 3, 1949, after merging with the competing National Basketball League (NBL). In 1976, the NBA and the American Basketball Association (ABA) merged, adding four franchises to the NBA. The NBA's regular season runs from October to April, with each team playing 82 games. The league's playoff tournament extends into June. As of 2020, NBA players are the world's best-paid athletes by average annual salary per player.")

# Create a dropdown box for Team 1
selected_team1 = st.selectbox("Select Team 1", [
    "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
    "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
    "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
    "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
    "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
    "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
])

# Display the selected Team 1
st.write("Team 1 selected:", selected_team1)

with st.container():
    st_lottie(
        lottie_coding2,
        speed=1,
        reverse=False,
        loop=True,
        quality="medium",
        height=200,
        width=200,
        key=None,
    )

# Create a dropdown box for Team 2
selected_team2 = st.selectbox("Select Team 2", [
    "Atlanta Hawks", "Boston Celtics", "Brooklyn Nets", "Charlotte Hornets", "Chicago Bulls",
    "Cleveland Cavaliers", "Dallas Mavericks", "Denver Nuggets", "Detroit Pistons", "Golden State Warriors",
    "Houston Rockets", "Indiana Pacers", "Los Angeles Clippers", "Los Angeles Lakers", "Memphis Grizzlies",
    "Miami Heat", "Milwaukee Bucks", "Minnesota Timberwolves", "New Orleans Pelicans", "New York Knicks",
    "Oklahoma City Thunder", "Orlando Magic", "Philadelphia 76ers", "Phoenix Suns", "Portland Trail Blazers",
    "Sacramento Kings", "San Antonio Spurs", "Toronto Raptors", "Utah Jazz", "Washington Wizards"
])

# Display the selected Team 2
st.write("Team 2 selected:", selected_team2)

# Load and preprocess NBA game data
# Replace 'path_to_nba_games.csv' with the actual path to your data file
nba_games_data = pd.read_csv("path_to_nba_games.csv")

# Load the pre-trained model
model_path = "model_final.pth"
model = torch.load(model_path)

# Prepare input data for prediction
# Replace this section with your own code to preprocess the data and extract features for the selected teams

# Perform predictions
# Replace this section with your own code to perform predictions using the pre-trained model
# Use the extracted features as input to the model

# Mock predictions for demonstration purposes
predictions = {
    "actual": [1, 0, 1, 0, 1],
    "prediction": [1, 0, 1, 1, 0]
}

# Display the accuracy score
accuracy = accuracy_score(predictions["actual"], predictions["prediction"])
st.write("Model Accuracy:", accuracy)
