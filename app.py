import streamlit as st
import pandas as pd
import os
import json

# File to store votes
votes_file = "headline_votes.json"

# Function to load votes from the JSON file
def load_votes():
    if os.path.exists(votes_file):
        with open(votes_file, "r") as f:
            return json.load(f)
    return {"headline_A": 0, "headline_B": 0}

# Function to save votes to the JSON file
def save_votes(votes):
    with open(votes_file, "w") as f:
        json.dump(votes, f)

# Load existing votes
votes = load_votes()

# Title and description
st.title("📰 Headline A/B Testing Tool")
st.markdown("Enter two different headlines and see which one resonates more with your audience.")

# Input for two headlines
headline_A = st.text_input("Enter Headline A:", placeholder="e.g., 'Unlock Your Potential with These Tips'")
headline_B = st.text_input("Enter Headline B:", placeholder="e.g., 'Transform Your Life: Here’s How'")

# Display the headlines for voting
if st.button("🚀 Show Headlines"):
    if headline_A and headline_B:
        st.subheader("Which headline do you prefer?")
        choice = st.radio("Choose your preferred headline:", (headline_A, headline_B))

        # Increment the vote count based on user's choice
        if st.button("Submit Vote"):
            if choice == headline_A:
                votes["headline_A"] += 1
            else:
                votes["headline_B"] += 1
            save_votes(votes)
            st.success("Thank you for your vote!")

# Display the results
st.subheader("Current Vote Counts")
st.write(f"📰 Headline A: {votes['headline_A']} votes")
st.write(f"📰 Headline B: {votes['headline_B']} votes")

# Visualize the results
if votes['headline_A'] + votes['headline_B'] > 0:
    data = {'Headlines': ['Headline A', 'Headline B'],
            'Votes': [votes['headline_A'], votes['headline_B']]}
    df = pd.DataFrame(data)
    st.bar_chart(df.set_index('Headlines'))
else:
    st.info("No votes have been cast yet.")
