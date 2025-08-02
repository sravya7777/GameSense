import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Load data
df = pd.read_csv('Realistic_Gaming_Player_Data.csv')

# Create output directory for images
os.makedirs('eda_images', exist_ok=True)

# 1. Demographics Analysis
# Age distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title('Age Distribution of Players')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('eda_images/age_distribution.png')
plt.close()

# Gender distribution
plt.figure(figsize=(6,4))
sns.countplot(x='Gender', data=df)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.savefig('eda_images/gender_distribution.png')
plt.close()

# Region distribution
plt.figure(figsize=(10,5))
sns.countplot(x='Region', data=df, order=df['Region'].value_counts().index)
plt.title('Region Distribution')
plt.xlabel('Region')
plt.ylabel('Count')
plt.savefig('eda_images/region_distribution.png')
plt.close()

# Platform distribution
plt.figure(figsize=(8,5))
sns.countplot(x='Platform', data=df)
plt.title('Platform Distribution')
plt.xlabel('Platform')
plt.ylabel('Count')
plt.savefig('eda_images/platform_distribution.png')
plt.close()

# 2. Behavioral Analysis
# Favorite Genre
plt.figure(figsize=(10,5))
sns.countplot(y='FavoriteGenre', data=df, order=df['FavoriteGenre'].value_counts().index)
plt.title('Favorite Game Genre')
plt.xlabel('Count')
plt.ylabel('Genre')
plt.savefig('eda_images/favorite_genre.png')
plt.close()

# Average Session Duration
plt.figure(figsize=(8,5))
sns.histplot(df['AvgSessionDuration_Min'], bins=20, kde=True)
plt.title('Average Session Duration (min)')
plt.xlabel('Minutes')
plt.ylabel('Count')
plt.savefig('eda_images/avg_session_duration.png')
plt.close()

# Sessions Per Week
plt.figure(figsize=(8,5))
sns.histplot(df['SessionsPerWeek'], bins=20, kde=True)
plt.title('Sessions Per Week')
plt.xlabel('Sessions')
plt.ylabel('Count')
plt.savefig('eda_images/sessions_per_week.png')
plt.close()

# Monthly Spend
plt.figure(figsize=(8,5))
sns.histplot(df['MonthlySpend_USD'], bins=20, kde=True)
plt.title('Monthly Spend (USD)')
plt.xlabel('USD')
plt.ylabel('Count')
plt.savefig('eda_images/monthly_spend.png')
plt.close()

# 3. Correlation Analysis
# Age vs Monthly Spend
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='MonthlySpend_USD', data=df, alpha=0.5)
plt.title('Age vs Monthly Spend')
plt.xlabel('Age')
plt.ylabel('Monthly Spend (USD)')
plt.savefig('eda_images/age_vs_spend.png')
plt.close()

# Sessions Per Week vs Monthly Spend
plt.figure(figsize=(8,5))
sns.scatterplot(x='SessionsPerWeek', y='MonthlySpend_USD', data=df, alpha=0.5)
plt.title('Sessions Per Week vs Monthly Spend')
plt.xlabel('Sessions Per Week')
plt.ylabel('Monthly Spend (USD)')
plt.savefig('eda_images/sessions_vs_spend.png')
plt.close()

# Correlation heatmap
plt.figure(figsize=(8,6))
corr = df[['Age','AvgSessionDuration_Min','SessionsPerWeek','MonthlySpend_USD']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('eda_images/correlation_heatmap.png')
plt.close()

# 4. Interactive Plotly Example: Age vs Spend by Platform
fig = px.scatter(df, x='Age', y='MonthlySpend_USD', color='Platform',
                 title='Age vs Monthly Spend by Platform',
                 labels={'Age':'Age', 'MonthlySpend_USD':'Monthly Spend (USD)'})
fig.write_html('eda_images/age_vs_spend_platform.html')

print('EDA and visualizations complete. Images saved in eda_images/.') 