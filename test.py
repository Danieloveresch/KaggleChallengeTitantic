import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

train_df = pd.read_csv('/Users/daniel/Downloads/all(1)/train.csv')
test_df = pd.read_csv('/Users/daniel/Downloads/all(1)/test.csv')
combine = [train_df, test_df]






train_df.describe(include=['O'])

train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)

print(train_df.describe())
grid = sns.FacetGrid(train_df, col='Survived', row='Pclass', size=2.2, aspect=1.6)
grid.map(plt.hist, 'Age', alpha=.5, bins=20)
grid.add_legend();
