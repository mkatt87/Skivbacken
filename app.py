import streamlit as st
from skivbacken import generate_playlist

st.title("🎵 Skivbacken Generator")

st.markdown("Skapa en slumpad spellista från dina Skivhyllan-spellistor.")

# Inställningar
num_tracks = st.slider("Antal låtar", 10, 10000, 200, step=10)

with st.expander("🎛 Avancerade inställningar"):
    use_energy = st.checkbox("Justera energinivå (lugn/ös)")
    energy_level = st.slider("Energibalansering (%)", 0, 100, 50) if use_energy else None

    use_electronic = st.checkbox("Elektroniskt eller inte?")
    electronic_level = st.slider("Elektroniskt (%)", 0, 100, 50) if use_electronic else None

    genre_input = st.text_input("Genre (skriv egna, separera med kommatecken)")
    use_random_genres = st.checkbox("🎲 Slumpa 10 genrer istället")

if st.button("🎧 Skapa spellista"):
    generate_playlist(num_tracks, energy_level, electronic_level, genre_input, use_random_genres)
    st.success("Spellistan är skapad – kolla din Spotify!")

