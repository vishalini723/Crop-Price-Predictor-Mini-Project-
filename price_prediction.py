import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load data
df = pd.read_csv('commodity_prices.csv')
df['Date'] = pd.to_datetime(df['Date'])

# One-hot encoding for Commodity
df = pd.get_dummies(df, columns=['Commodity'], drop_first=True)

# Features and target
X = df[['Temperature', 'Rainfall', 'Commodity_Potato', 'Commodity_Pulses']]
y = df['Price']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, 'price_model.pkl')
