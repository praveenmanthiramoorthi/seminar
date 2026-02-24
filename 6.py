import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('titanic.csv')

print("Dataset Info:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

print("\nMissing Values:")
missing = df.isnull().sum()
print(missing)

print("\nHandling Missing Values:")
df['Age'].fillna(df['Age'].mean(), inplace=True)

print("\nCorrelation Matrix:")
correlation_matrix = df.corr()
print(correlation_matrix)

print("\nSurvival Count Analysis:")
survived = df['Survived'].value_counts()
print(survived)

print("\nVisualizations:")

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Heatmap of Correlations")
plt.show()

sns.histplot(data=df, x='Age', kde=True, bins=30, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

sns.countplot(data=df, x='Survived', palette='pastel')
plt.title("Survival Counts")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.show()
