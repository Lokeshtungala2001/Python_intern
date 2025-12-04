import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

data = pd.read_csv("house_prices.csv")

# View first records
print("Dataset Head:")
print(data.head())


features = ["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "zipcode"]
target = "price"

X = data[features]
y = data[target]


categorical_cols = ["zipcode"]
numerical_cols = ["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors"]

preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

model = Pipeline(steps=[
    ("preprocess", preprocess),
    ("regressor", LinearRegression())
])


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model.fit(X_train, y_train)

print("\nModel training completed!")

y_pred = model.predict(X_test)

print("\nModel Performance:")
print("Mean Squared Error (MSE):", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

#  Predict for a New House

new_house = pd.DataFrame({
    "bedrooms": [3],
    "bathrooms": [2],
    "sqft_living": [1800],
    "sqft_lot": [4000],
    "floors": [2],
    "zipcode": ["98103"]
})

predicted_price = model.predict(new_house)

print("\nPredicted Price for New House:", predicted_price[0])
