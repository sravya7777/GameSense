import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Gaming Player Data EDA Dashboard", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('Realistic_Gaming_Player_Data.csv')

df = load_data()

st.title("🎮 Gaming Player Data EDA Dashboard")
st.markdown("""
This interactive dashboard allows you to explore the gaming player dataset by demographics, behaviors, and correlations. Use the filters to customize your view.
""")

# Sidebar filters
st.sidebar.header("Filter Data")
regions = st.sidebar.multiselect("Region", options=df['Region'].unique(), default=list(df['Region'].unique()))
genders = st.sidebar.multiselect("Gender", options=df['Gender'].unique(), default=list(df['Gender'].unique()))
platforms = st.sidebar.multiselect("Platform", options=df['Platform'].unique(), default=list(df['Platform'].unique()))
genres = st.sidebar.multiselect("Favorite Genre", options=df['FavoriteGenre'].unique(), default=list(df['FavoriteGenre'].unique()))

filtered_df = df[
    df['Region'].isin(regions) &
    df['Gender'].isin(genders) &
    df['Platform'].isin(platforms) &
    df['FavoriteGenre'].isin(genres)
]

st.markdown(f"**Total Players:** {len(filtered_df)}")

# Demographics
st.header("Demographics")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['Age'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='Gender', data=filtered_df, ax=ax)
    st.pyplot(fig)

with col3:
    st.subheader("Region Distribution")
    fig, ax = plt.subplots()
    sns.countplot(y='Region', data=filtered_df, order=filtered_df['Region'].value_counts().index, ax=ax)
    st.pyplot(fig)

with col4:
    st.subheader("Platform Distribution")
    fig, ax = plt.subplots()
    sns.countplot(y='Platform', data=filtered_df, order=filtered_df['Platform'].value_counts().index, ax=ax)
    st.pyplot(fig)

# Behavioral Analysis
st.header("Behavioral Analysis")
col5, col6 = st.columns(2)

with col5:
    st.subheader("Favorite Genre")
    fig, ax = plt.subplots()
    sns.countplot(y='FavoriteGenre', data=filtered_df, order=filtered_df['FavoriteGenre'].value_counts().index, ax=ax)
    st.pyplot(fig)

with col6:
    st.subheader("Monthly Spend (USD)")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df['MonthlySpend_USD'], bins=20, kde=True, ax=ax)
    st.pyplot(fig)

# Correlation Analysis
st.header("Correlation Analysis")
col7, col8 = st.columns(2)

with col7:
    st.subheader("Age vs Monthly Spend")
    fig = px.scatter(filtered_df, x='Age', y='MonthlySpend_USD', color='Platform',
                     title='Age vs Monthly Spend by Platform',
                     labels={'Age':'Age', 'MonthlySpend_USD':'Monthly Spend (USD)'})
    st.plotly_chart(fig, use_container_width=True)

with col8:
    st.subheader("Sessions Per Week vs Monthly Spend")
    fig = px.scatter(filtered_df, x='SessionsPerWeek', y='MonthlySpend_USD', color='Platform',
                     title='Sessions Per Week vs Monthly Spend by Platform',
                     labels={'SessionsPerWeek':'Sessions Per Week', 'MonthlySpend_USD':'Monthly Spend (USD)'})
    st.plotly_chart(fig, use_container_width=True)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
corr = filtered_df[['Age','AvgSessionDuration_Min','SessionsPerWeek','MonthlySpend_USD']].corr()
fig, ax = plt.subplots()
sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.markdown("---")
st.markdown("Data source: Realistic_Gaming_Player_Data.csv | Dashboard by Sravya Reddy With AI") 