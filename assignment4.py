# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1kzgECCskAuOU_TNMHDRiG0CkBLrwf9Hk
"""

#Q1
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the dataset
df =  pd.read_csv('my_iris.xlsx - Sheet1.csv')
# Data cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Data transformation
df['target'] = df['target'].astype('category').cat.codes
df['sepal area'] = df['sepal length'] * df['sepal width']
df['petal area'] = df['petal length'] * df['petal width']

# Normalization and standardization
scaler = MinMaxScaler()
df[['sepal depth', 'sepal diameter', 'petal depth', 'petal diameter', 'sepal length', 'sepal width', 'petal length', 'petal width', 'sepal area', 'petal area']] = scaler.fit_transform(df[['sepal depth', 'sepal diameter', 'petal depth', 'petal diameter', 'sepal length', 'sepal width', 'petal length', 'petal width', 'sepal area', 'petal area']])

# Alternatively, you can use standardization instead of normalization
# scaler = StandardScaler()
# df[['sepal depth', 'sepal diameter', 'petal depth', 'petal diameter', 'sepal length', 'sepal width', 'petal length', 'petal width', 'sepal area', 'petal area']] = scaler.fit_transform(df[['sepal depth', 'sepal diameter', 'petal depth', 'petal diameter', 'sepal length', 'sepal width', 'petal length', 'petal width', 'sepal area', 'petal area']])

# Load the dataset
df = pd.read_csv('my_iris.xlsx - Sheet1.csv')

# Separate features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Impute missing values
imputer = Imputer(missing_values=np.nan, strategy='mean')
X_imputed = imputer.fit_transform(X)

# Filter method: Low variance
selector = VarianceThreshold(threshold=0.1)
X_low_variance = selector.fit_transform(X_imputed)

# Filter method: Pearson's Correlation
corr_matrix = np.corrcoef(X_imputed.T, X_imputed)
high_corr_features = np.where(abs(corr_matrix) > 0.7)
X_high_corr = X_imputed.drop(columns=[col[x] for col in high_corr_features])

# Filter method: Mutual information
selector = SelectKBest(mutual_info_classif, k=3)
X_mutual_info = selector.fit_transform(X_imputed, y)

# Filter method: ANOVA F-value
selector = SelectKBest(f_classif, k=3)
X_f_value = selector.fit_transform(X_imputed, y)

# Filter method: Chi-squared
selector = SelectKBest(chi2, k=3)
X_chi2 = selector.fit_transform(X_imputed, y)

# Wrapper method: Forward Selection
selector = LogisticRegression(solver='liblinear')
selector = selector.fit(X_imputed, y)
model = SelectFromModel(selector, prefit=True)
X_forward_selection = model.transform(X_imputed)

# Wrapper method: Backward Elimination
selector = RandomForestClassifier(n_estimators=100, random_state=42)
selector = selector.fit(X_imputed, y)
model = SelectFromModel(selector, prefit=True)
X_backward_elimination = model.transform(X_imputed)

# Embedded method: Variance Inflation Factor (VIF)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_imputed)
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(X_scaled, i) for i in range(X_scaled.shape[1])]
vif["features"] = X_imputed.columns
X_vif = X_imputed.drop(columns=vif[vif["VIF Factor"] > 5].features)

# Print the selected features for each method
print("Low variance features:", X_low_variance.shape[1])
print("High correlation features:", X_high_corr.shape[1])
print("Mutual information features:", X_mutual_info.shape[1])
print("ANOVA F-value features:", X_f_value.shape[1])
print("Chi-squared features:", X_chi2.shape[1])
print("Forward selection features:", X_forward_selection.shape[1])
print("Backward elimination features:", X_backward_elimination.shape[1])
print("VIF features:", X_vif.shape[1])

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import VarianceThreshold, SelectKBest, mutual_info_classif, f_classif, chi2, SelectFromModel
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load the dataset
df =  pd.read_csv('my_iris.xlsx - Sheet1.csv')

# Separate features and target
X = df.iloc[:, 1:-1]  # Exclude the first and last columns
y = df.iloc[:, -1]

# Split the dataset into a 70-30 training-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Define the feature selection techniques
feature_selection_methods = {
    "Low variance": VarianceThreshold(threshold=0.1),
    "Pearson's Correlation": SelectKBest(f_classif, k=3),
    "Mutual information": SelectKBest(mutual_info_classif, k=3),
    "Chi-squared": SelectKBest(chi2, k=3),
    "Forward selection": SelectFromModel(LogisticRegression(solver='liblinear'), max_features=3),
    "Backward elimination": SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), max_features=3)
}

# Train and evaluate a logistic regression model for each feature selection technique
for method, selector in feature_selection_methods.items():
    X_train_selected = selector.fit_transform(X_train, y_train)
    X_test_selected = selector.transform(X_test)
    model = LogisticRegression()
    model.fit(X_train_selected, y_train)
    y_pred = model.predict(X_test_selected)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    print(f"Performance measures for {method}:")
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 score: {f1:.2f}")
    print()