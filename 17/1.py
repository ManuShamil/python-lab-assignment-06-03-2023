import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the football dataset into a pandas DataFrame
df = pd.read_csv('football_dataset.csv')

# Perform data preprocessing if needed

# Example of plotting different types of graphs using matplotlib and seaborn
# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='team', y='goals', data=df)
plt.title('Goals Scored by Each Team')
plt.xlabel('Team')
plt.ylabel('Goals')
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='shots', y='goals', data=df, hue='team')
plt.title('Shots vs. Goals')
plt.xlabel('Shots')
plt.ylabel('Goals')
plt.show()