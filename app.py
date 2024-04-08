import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
data = pd.read_csv(url)

# Dataset Summary
st.title('Boston Housing Dataset Overview')
st.markdown("""
The Boston Housing dataset contains information collected by the U.S Census Service concerning housing in the area of Boston Mass. It was obtained from the StatLib archive (http://lib.stat.cmu.edu/datasets/boston), and has been used extensively throughout the literature to benchmark algorithms. The dataset is small in size with only 506 cases.

The dataset presents records of various houses, with details such as the number of rooms, property tax, crime rate, etc. It's commonly used for predictive modeling in price regression exercises.
""")

# Column Descriptions
st.subheader('Column Descriptions')
st.markdown("""
- `crim`: Per capita crime rate by town
- `zn`: Proportion of residential land zoned for lots over 25,000 sq.ft.
- `indus`: Proportion of non-retail business acres per town
- `chas`: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
- `nox`: Nitrogen oxides concentration (parts per 10 million)
- `rm`: Average number of rooms per dwelling
- `age`: Proportion of owner-occupied units built prior to 1940
- `dis`: Weighted distances to five Boston employment centres
- `rad`: Index of accessibility to radial highways
- `tax`: Full-value property-tax rate per $10,000
- `ptratio`: Pupil-teacher ratio by town
- `black`: 1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
- `lstat`: Lower status of the population (percent)
- `medv`: Median value of owner-occupied homes in $1000s
""")

# Sidebar for widgets
st.sidebar.header('Filter options')

# Slider for filtering 'rm'
min_rooms, max_rooms = int(data['rm'].min()), int(data['rm'].max())
rooms = st.sidebar.slider('Number of Rooms (rm)', min_rooms, max_rooms, (min_rooms, max_rooms))

# Slider for filtering 'medv'
min_medv, max_medv = int(data['medv'].min()), int(data['medv'].max())
medv_range = st.sidebar.slider('Median Value of Homes (medv in $1000\'s)', min_medv, max_medv, (min_medv, max_medv))

# Filtering the data
filtered_data = data[(data['rm'] >= rooms[0]) & (data['rm'] <= rooms[1]) &
                     (data['medv'] >= medv_range[0]) & (data['medv'] <= medv_range[1])]

# Dropdown for selecting visualization type
vis_type = st.sidebar.selectbox('Select Visualization Type', ['Histogram', 'Scatter Plot', 'Box Plot', 'Correlation Matrix'])

# Main area
st.title('Boston Housing Data Visualizations')
st.write('Filtered Data', filtered_data)

# Displaying selected visualization
if vis_type == 'Histogram':
    fig, ax = plt.subplots()
    sns.histplot(filtered_data['medv'], bins=30, kde=True, ax=ax)
    ax.set_xlabel('Median value of owner-occupied homes in $1000\'s')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Median Home Values')
    st.pyplot(fig)
elif vis_type == 'Scatter Plot':
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x='rm', y='medv', alpha=0.5, ax=ax)
    ax.set_xlabel('Average Number of Rooms per Dwelling')
    ax.set_ylabel('Median value of owner-occupied homes in $1000\'s')
    ax.set_title('Rooms per Dwelling vs. Median Home Value')
    st.pyplot(fig)
elif vis_type == 'Box Plot':
    fig, ax = plt.subplots()
    sns.boxplot(x=filtered_data['medv'], ax=ax)
    ax.set_xlabel('Median value of owner-occupied homes in $1000\'s')
    ax.set_title('Box Plot of Median Home Value')
    st.pyplot(fig)
elif vis_type == 'Correlation Matrix':
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = filtered_data.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title('Correlation Matrix of Variables')
    st.pyplot(fig)

