import streamlit as st
from PIL import Image

st.title("Premier Ranking")

with st.container():
    image = Image.open('premierl.png')

    # Display the image with center alignment
    st.image(image, use_column_width=True)

    st.write("The Premier League (legal name: The Football Association Premier League Limited) is the highest level of the English football league system. Contested by 20 clubs, it operates on a system of promotion and relegation with the English Football League (EFL). Seasons typically run from August to May with each team playing 38 matches against all other teams both home and away. Most games are played on Saturday and Sunday afternoons, with occasional weekday evening fixtures. The competition was founded as the FA Premier League on 20 February 1992 following the decision of First Division (top-tier league from 1888 until 1992) clubs to break away from the English Football League. However, teams may still be relegated into and promoted from the EFL Championship. The Premier League takes advantage of a lucrative television rights sale to Sky: from 2019 to 2020, accumulated television rights were worth around £3.1 billion a year, with Sky and BT Group securing the domestic rights to broadcast 128 and 32 games respectively.")


# Create a dropdown box
selected_option = st.selectbox("Select a Team", ["Arsenal", "Aston Villa", "Brentford", "Brighton Hove Albion", "Burnley",
                                                    "Chelsea", "Crystal Palace", "Everton", "Leeds", "Leeds United", "Leicester",
                                                    "Leicester City", "Liverpool", "Manchester City", "Manchester United", "Newcastle United",
                                                    "Norwich City", "Southampton", "Spurs", "Tottenham Hotspur", "Watford", "West Ham United",
                                                    "Wolves", "Wolverhampton Wanderers"])

# Display the selected option
st.write("You selected:", selected_option)


# Create a multiselect box

# Create a multiselect box
selected_options = st.multiselect(
    'Select options',
    ['Points', 'Points per Match', 'Goal Difference', 'Won']
)

# Button for Rank prediction
result = st.button("PREDICT RANK")
