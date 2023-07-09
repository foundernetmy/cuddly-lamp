import ccxt
import pandas as pd
import tkinter as tk
from tkinter import ttk


# Create a tkinter window
root = tk.Tk()
root.title("Crypto Ticker")




# Create a Treeview widget to display the table
tree = ttk.Treeview(root)
style = ttk.Style()
style.configure('Treeview', rowheight=60)
tree['columns'] = (
    'Symbol', 'Price (USDT)', 'Price (BTC)', 'Price (BNB)', 'Price (ETH)', 'Price (BUSD)', 'Price Change (%)',
    'BTC foyda', 'ETH foyda', 'BNB foyda', 'BUSD foyda', 'foyda', 'nimada foyda','foyda foizda')

# Define column names and set their properties
tree.heading('#0', text='', anchor='w')
tree.heading('Symbol', text='Symbol', anchor='w')
tree.heading('Price (USDT)', text='Price (USDT)', anchor='w')
tree.heading('Price (BTC)', text='Price (BTC)', anchor='w')
tree.heading('Price (BNB)', text='Price (BNB)', anchor='w')
tree.heading('Price (ETH)', text='Price (ETH)', anchor='w')
tree.heading('Price (BUSD)', text='Price (BUSD)', anchor='w')
tree.heading('Price Change (%)', text='Price Change (%)', anchor='w')
tree.heading('BTC foyda', text='BTC foyda', anchor='w')
tree.heading('ETH foyda', text='ETH foyda', anchor='w')
tree.heading('BNB foyda', text='BNB foyda', anchor='w')
tree.heading('BUSD foyda', text='BUSD foyda', anchor='w')
tree.heading('foyda', text='foyda', anchor='w')
tree.heading('nimada foyda', text='nimada foyda', anchor='w')
tree.heading('foyda foizda', text='foyda foizda %', anchor='w')

tree.column('#0', width=0, stretch=tk.NO)
tree.column('Symbol', width=60, anchor='w')
tree.column('Price (USDT)', width=60, anchor='w')
tree.column('Price (BTC)', width=60, anchor='w')
tree.column('Price (BNB)', width=60, anchor='w')
tree.column('Price (ETH)', width=60, anchor='w')
tree.column('Price (BUSD)', width=60, anchor='w')
tree.column('Price Change (%)', width=60, anchor='w')

tree.column('foyda', width=60, anchor='w')
tree.column('nimada foyda', width=60, anchor='w')
tree.column('foyda foizda', width=60, anchor='w')

# Fetch tickers data
import telebot

# Replace the token with your own bot token obtained from BotFather
bot = telebot.TeleBot("6287474930:AAE-5Yjz_D7w2qnFL3EdPmKpAJrH0ILKtvQ")

def refresh():
    tree.delete(*tree.get_children())
    style = ttk.Style()
    style.configure('Treeview', rowheight=60)
    tree['columns'] = (
    'Symbol', 'Price (USDT)', 'Price (BTC)', 'Price (BNB)', 'Price (ETH)', 'Price (BUSD)', 'Price Change (%)',
    'BTC foyda', 'ETH foyda', 'BNB foyda', 'BUSD foyda', 'foyda', 'nimada foyda','foyda foizda')

    # Define column names and set their properties
    tree.heading('#0', text='', anchor='w')
    tree.heading('Symbol', text='Symbol', anchor='w')
    tree.heading('Price (USDT)', text='Price (USDT)', anchor='w')
    tree.heading('Price (BTC)', text='Price (BTC)', anchor='w')
    tree.heading('Price (BNB)', text='Price (BNB)', anchor='w')
    tree.heading('Price (ETH)', text='Price (ETH)', anchor='w')
    tree.heading('Price (BUSD)', text='Price (BUSD)', anchor='w')
    tree.heading('Price Change (%)', text='Price Change (%)', anchor='w')
    tree.heading('BTC foyda', text='BTC foyda', anchor='w')
    tree.heading('ETH foyda', text='ETH foyda', anchor='w')
    tree.heading('BNB foyda', text='BNB foyda', anchor='w')
    tree.heading('BUSD foyda', text='BUSD foyda', anchor='w')
    tree.heading('foyda', text='foyda', anchor='w')
    tree.heading('nimada foyda', text='nimada foyda', anchor='w')
    tree.heading('foyda foizda', text='foyda foizda %', anchor='w')

    # Define column widths
    tree.column('#0', width=0, stretch=tk.NO)
    tree.column('Symbol', width=80, anchor='w')
    tree.column('Price (USDT)', width=80, anchor='w')
    tree.column('Price (BTC)', width=80, anchor='w')
    tree.column('Price (BNB)', width=80, anchor='w')
    tree.column('Price (ETH)', width=80, anchor='w')
    tree.column('Price (BUSD)', width=80, anchor='w')
    tree.column('Price Change (%)', width=80, anchor='w')
    tree.column('BTC foyda', width=80, anchor='w')
    tree.column('ETH foyda', width=80, anchor='w')
    tree.column('BNB foyda', width=80, anchor='w')
    tree.column('BUSD foyda', width=80, anchor='w')
    tree.column('foyda', width=80, anchor='w')
    tree.column('nimada foyda', width=80, anchor='w')
    tree.column('foyda foizda', width=80, anchor='w')
    das = {}
    narxlar = {}
    baxtbek={}
    coin = {}
    baf=[]

    exchange = ccxt.binance()

    tickers = exchange.fetch_tickers()

    data = []
    bnb_usd_pricer = tickers['BNB/USDT']
    bnb_usd_price = bnb_usd_pricer['last']
    btc_usd_pricer = tickers['BTC/USDT']
    btc_usd_price = btc_usd_pricer['last']
    eth_usd_pricer = tickers['ETH/USDT']
    eth_usd_price = eth_usd_pricer['last']
    busd_usd_pricer = tickers['BUSD/USDT']
    busd_usd_price = busd_usd_pricer['last']
    for symbol in tickers:
        # Check if the symbol contains USDT and ignore any other symbols
        if "USDT" in symbol:
            ticker = tickers[symbol]
            last_price = ticker['last']

        # Get the ticker for the BTC/USDT pair
            btc_ticker = tickers['BTC/USDT']
            crypto_symbol = symbol.replace('/USDT', '')


            if crypto_symbol != 'BTC':
                try:
                    market = exchange.load_markets()[crypto_symbol+'/BTC']
                    btc_ticker = tickers[f"{crypto_symbol}/BTC"]
                    price_in_btc = btc_ticker['last']
                    bitcoin_buying_fee = market['taker']
                    bitcoin_selling_fee = market['maker']
                except:
                    bitcoin_buying_fee = 'Hato'
                    bitcoin_selling_fee = 'Hato'

                    price_in_btc = 'paraemas'
            else:
                price_in_btc = 1
                bitcoin_buying_fee = 0
                bitcoin_selling_fee = 0
            if crypto_symbol != 'ETH':
                try:
                    market = exchange.load_markets()[crypto_symbol + '/ETH']
                    eth_ticker = tickers[f"{crypto_symbol}/ETH"]
                    eth = eth_ticker['last']
                    eth_buying_fee = market['taker']
                    eth_selling_fee = market['maker']
                except:
                    eth_buying_fee = 'Hato'
                    eth_selling_fee = 'Hato'
                    eth = 'paraemas'
            else:
                eth = 1
                eth_buying_fee =0
                eth_selling_fee = 0
            if crypto_symbol != 'BNB':
                try:
                    market = exchange.load_markets()[crypto_symbol + '/BNB']
                    bnb_ticker = tickers[f"{crypto_symbol}/BNB"]
                    bnb = bnb_ticker['last']
                    bnb_buying_fee = market['taker']
                    bnb_selling_fee = market['maker']
                except:
                    bnb_buying_fee = 'Hato'
                    bnb_selling_fee = 'Hato'
                    bnb = 'paraemas'
            else:
                bnb_buying_fee = 0
                bnb_selling_fee = 0
                bnb = 1
            if crypto_symbol != 'BUSD':
                try:
                    market = exchange.load_markets()[crypto_symbol + '/BUSD']
                    busd_ticker = tickers[f"{crypto_symbol}/BUSD"]
                    busd = busd_ticker['last']
                    busd_buying_fee = market['taker']
                    busd_selling_fee = market['maker']
                except:
                    busd_buying_fee = 'Hato'
                    busd_selling_fee = 'Hato'
                    busd = 'paraemas'
            else:
                busd_buying_fee = 0
                busd_selling_fee = 0
                busd = 1
        # Append data to the list
            if price_in_btc!='paraemas':
                btc_fee=(price_in_btc*btc_usd_price)-(last_price+last_price*((bitcoin_buying_fee/100)*3))
                try:
                    btc_fee_persent=(btc_fee/last_price)*100
                except:
                    btc_fee_persent = 0

            else:
                btc_fee=0
                btc_fee_persent = 0
            if eth!='paraemas':
                eth_fee=(eth*eth_usd_price)-(last_price+last_price*((eth_buying_fee/100)*3))
                try:
                    eth_fee_persent=(eth_fee/last_price)*100
                except:
                    eth_fee_persent = 0
            else:
                eth_fee=0
                eth_fee_persent = 0
            if bnb!='paraemas':
                bnb_fee=(bnb*bnb_usd_price)-(last_price+last_price*((bnb_buying_fee/100)*3))
                try:
                    bnb_fee_persent=(bnb_fee/last_price)*100
                except:
                    bnb_fee_persent = 0
            else:
                bnb_fee=0
                bnb_fee_persent = 0
            if busd!='paraemas':
                busd_fee=(busd*busd_usd_price)-(last_price+last_price*((busd_buying_fee/100)*3))
                try:
                    busd_fee_persent=(busd_fee/last_price)*100
                except:
                    busd_fee_persent = 0
            else:
                busd_fee=0
                busd_fee_persent = 0
            price_change_percent = str(ticker['percentage'])+'%'
            bas={bnb_fee:'BNB',busd_fee:'BUSD',btc_fee:'BTC',eth_fee:'ETH'}
            a={bnb_fee_persent:bnb_fee,busd_fee_persent:busd_fee,btc_fee_persent:btc_fee,eth_fee_persent:eth_fee}
            val = [v for v in a.keys()]
            c=max(val)
            b=a[c]
            if b>0:
                if last_price>0:
                    if last_price<15:
                        if crypto_symbol != 'XNO':
                            if bas[b]!='BTC':
                                data.append([symbol, last_price, price_in_btc, bnb, eth, busd, price_change_percent,str(btc_fee)+'\n'+str(btc_fee_persent)+'%',str(eth_fee)+'\n'+str(eth_fee_persent)+'%',str(bnb_fee)+'\n'+str(bnb_fee_persent)+'%',str(busd_fee)+'\n'+str(busd_fee_persent)+'%',b,crypto_symbol+'/'+bas[b],c])

# Insert data into the Treeview widget
# Insert data into the Treeview widget
    # Convert the data to a Pandas DataFrame

    # Display the sorted data in the Treeview widget


# Add the Treeview widget to the tkinter window




    # Start the tkinter event loop


# Create a label widget to display the refresh status



# Define a command handler for the /start command



# Define a message handler for all messages


    # Insert data into the Treeview widget
    # Insert data into the Treeview widget
    # Convert the data to a Pandas DataFrame

    df = pd.DataFrame(data,
                      columns=['Symbol', 'Price (USDT)', 'Price (BTC)', 'Price (BNB)', 'Price (ETH)', 'Price (BUSD)',
                               'Price Change (%)', 'BTC foyda', 'ETH foyda', 'BNB foyda', 'BUSD foyda', 'foyda',
                               'nimada foyda','foyda foizda'])

    # Sort the data by the 'Price (BNB)' column in descending order
    sorted_df = df.sort_values(by=["foyda foizda"], ascending=False)
    sorted_df = sorted_df.nlargest(10, 'foyda foizda')

    # Display the sorted data in the Treeview widget
    for i, row in sorted_df.iterrows():
        tree.insert('', i, text='', values=(
            row['Symbol'], row['Price (USDT)'], row['Price (BTC)'], row['Price (BNB)'], row['Price (ETH)'],
            row['Price (BUSD)'], row['Price Change (%)'], row['BTC foyda'], row['ETH foyda'], row['BNB foyda'],
            row['BUSD foyda'], row['foyda'], row['nimada foyda'],str(row['foyda foizda'])+'%'))


    # Add the Treeview widget to the tkinter window
    api_key = 'XDWawlqiVXfNiKtd0oO4SDPZpBiwldovAkXjb1JiBXx5vtzrzII4MRKxVuXf4KRZ'
    api_secret = 'DcCAA&lmSnm0nVIvtgmrDrlmWrz*rDruOBMQTL$BYD1luARcqcyrWcznGwtqe5Z'
    from binance.client import Client
    ao=False

    client = Client(api_key, api_secret)
    exchange_info = client.get_exchange_info()
    while not ao:
        max_foyda_foizda = sorted_df['foyda foizda'].max()
        crypto_info = sorted_df.loc[df['foyda foizda'] == max_foyda_foizda]
        symbol = crypto_info['nimada foyda'].values[0].replace('/','')

        for pair in exchange_info['symbols']:
            if pair['symbol'] == symbol:
                ao=True
            else:
                try:
                    df=df.drop(index=crypto_info.index)
                except:
                    ao = True



    tree.pack(fill=tk.BOTH, expand=tk.YES)
    status_label.config(text=f"Data last updated at: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}")
    status_labe.config(text=crypto_info['Symbol'].values[0] + ': ' +"foyda: "+ str(crypto_info['foyda foizda'].values[0]) + '%'+': '+'asl narxi: '+str(crypto_info['Price (USDT)'].values[0])+': '+'foyda dollarda: '+str(crypto_info['foyda'].values[0])+': '+'nima sotib olish kk: '+crypto_info['nimada foyda'].values[0])
    root.mainloop()


# Start the tkinter event loop
refresh_button = tk.Button(root, text="Refresh Data", command=refresh)
refresh_button.pack()
# Create a label widget to display the refresh status
status_label = tk.Label(root, text="Data last updated at: ", font=("Arial", 10))
status_label.pack(pady=10)
status_labe = tk.Label(root, text="refresh", font=("Arial", 10))
status_labe.pack(pady=10)

root.mainloop()
#binancedan sotib olish
# import ccxt
#
# exchange = ccxt.binance({
#     'apiKey': 'your-api-key',
#     'secret': 'your-secret-key',
#     'enableRateLimit': True,
# })
#
# symbol = 'BTC/USDT'
# amount = 0.001  # The amount of BTC you want to buy
# price = None  # The price at which to buy BTC (None means use the current market price)
#
# order = exchange.create_order(symbol, 'limit', 'buy', amount, price)
#
# print('Order placed:', order)
# import ccxt



# shotdan balansni aniqlash
# exchange = ccxt.binance({
#     'apiKey': 'your-api-key',
#     'secret': 'your-secret-key',
#     'enableRateLimit': True,
# })
#
# balance = exchange.fetch_balance()
# usdt_balance = balance['USDT']['free']
#
# print('USDT balance:', usdt_balance)
