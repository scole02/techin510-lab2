import streamlit as st
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Sam's Penguins Explorer", 
    page_icon="🐧", 
    layout="centered",
)

st.title("🐧 Penguins Explorer")

df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')

st.write(df)

# Drop rows with missing values to ensure the plot works correctly
df.dropna(inplace=True)

# Create a pair plot
pair_plot = sns.pairplot(df, hue='species', markers=["o", "s", "D"], corner=True)

# Set the title of the pair plot
pair_plot.fig.suptitle("Penguins Measurement Pair Plot", y=1.02)

# Display the plot in the Streamlit app
st.pyplot(pair_plot.fig)