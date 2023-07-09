from binance.client import Client
import pandas as pd

api_key = 'YlTsgUhUVoOevY41EKZ0npLdIujIVzVcYpplOwGqXNMAiWZuXo2thcS445TkfARS'
api_secret = 'I7CyW98wXbk3nK5AOC5AotaPM03g38puTjYlPimJkrG4pZcvOeokxHlEZWOT3P2l'

client = Client(api_key, api_secret)


# Get all trades for BTCUSDT
trades = client.get_my_trades(symbol='ETHUSDT')

# Convert the trades to a pandas data frame
df_trades = pd.DataFrame(trades)

# Calculate the profit for each trade
df_trades['total'] = df_trades['price'].astype(float) * df_trades['qty'].astype(float)
df_trades['fee_total'] = df_trades['commission'].astype(float) * df_trades['price'].astype(float)
df_trades['profit'] = df_trades.apply(lambda row: row['total'] - row['fee_total'] if row['isBuyer']==True else 0, axis=1)

# Export the trades data frame to a CSV file
df_trades.to_csv('usdt.csv')