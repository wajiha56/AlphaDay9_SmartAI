# -------------------------------
# Day 9: Smart AI with Visuals
# -------------------------------

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

print("--- Initializing Smart AI Engine ---")

# -------------------------------
# Step 1: Locate CSV dynamically
# -------------------------------
folder_path = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder_path, 'smart_sales_data.csv')

# -------------------------------
# Step 2: Load Data
# -------------------------------
df = pd.read_csv(csv_path)
print("Data Loaded Successfully.")

# -------------------------------
# Step 3: Define Features and Target
# -------------------------------
X = df[['Marketing_Spend', 'Discount_Rate', 'Store_Size']]
y = df['Sales']

# -------------------------------
# Step 4: Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# Step 5: Build and Train Model
# -------------------------------
model = LinearRegression()
model.fit(X_train, y_train)
print("AI Model Trained on Multiple Variables.")

# -------------------------------
# Step 6: Predictions & R² Score
# -------------------------------
predictions = model.predict(X_test)
accuracy_score = r2_score(y_test, predictions)

print("\n--- AI PERFORMANCE REPORT ---")
print(f"Model Accuracy Score (R-squared): {accuracy_score * 100:.2f}%")
print("-----------------------------")

# -------------------------------
# Step 7: Visualize Predicted vs Actual
# -------------------------------
plt.figure(figsize=(8,6))
plt.scatter(y_test, predictions, color='blue', edgecolors='k', s=100)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', linewidth=2)
plt.title("Predicted vs Actual Sales", fontsize=16)
plt.xlabel("Actual Sales", fontsize=14)
plt.ylabel("Predicted Sales", fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()