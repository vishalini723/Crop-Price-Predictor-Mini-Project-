import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-03-01", periods=30)
commodities = ['Onion', 'Potato', 'Pulses']

data = {
    'Date': np.tile(dates, 3),
    'Commodity': np.repeat(commodities, 30),
    'Price': np.random.randint(20, 100, 90),
    'Temperature': np.random.randint(15, 40, 90),
    'Rainfall': np.random.randint(0, 10, 90),
}

df = pd.DataFrame(data)
df.to_csv('commodity_prices.csv', index=False)

print("✅ Data generated successfully!")
