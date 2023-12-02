import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('LAB5/test.csv')


df_subset = df.head(1000)


missing_values = df_subset.isnull().sum()


fig, axes = plt.subplots(1, 2, figsize=(12, 6))

sns.boxplot(x='Rooms', y='Square', data=df_subset, ax=axes[0])
axes[0].set_yscale('log')
axes[0].set_title('Ящик с усами (логарифмическая шкала)')

sns.histplot(df_subset['Square'], bins=30, kde=True, ax=axes[1])
axes[1].set_yscale('log')
axes[1].set_title('Гистограмма (логарифмическая шкала)')
plt.show()


numeric_columns = df_subset.select_dtypes(include=[np.number]).columns
df_subset.loc[:, numeric_columns] = df_subset.loc[:, numeric_columns].fillna(df_subset.loc[:, numeric_columns].mean())

q_low = df_subset['Square'].quantile(0.01)
q_high = df_subset['Square'].quantile(0.99)

df_subset = df_subset[(df_subset['Square'] > q_low) & (df_subset['Square'] < q_high)]


room_counts = df_subset['Rooms'].value_counts()


pivot_table = pd.pivot_table(df_subset, values='Square', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)


df_subset.to_csv('processed_data.csv', index=False)