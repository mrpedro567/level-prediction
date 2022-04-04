import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


mon_data = pd.read_excel('5e_index.xlsx', sheet_name='Monsters', usecols='C,G,H,N:T', header=0)
mon_data = pd.get_dummies(mon_data, columns=["Hit Points", "Size"])

labels = np.array(mon_data['Challenge'])

# Saving feature names for later use
feature_list = list(mon_data.columns)

# Remove the labels from the features
# axis 1 refers to the columns
features = mon_data.drop('Challenge', axis = 1)

# Convert to numpy array
features = np.array(features)

# Split the data into training and testing sets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

# TODO -> FIX BASELINE
# The baseline predictions are the Challenge Ratings
baseline_preds = test_features[:, feature_list.index('Challenge')]
# Baseline errors, and display average baseline error
baseline_errors = abs(baseline_preds - test_labels)
