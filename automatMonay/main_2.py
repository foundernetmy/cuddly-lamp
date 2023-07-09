import ccxt
import pandas as pd
import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Crypto Ticker")
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

            if eth!='paraemas':
                eth_fee=(eth*eth_usd_price)-(last_price+last_price*((0.1/100)*3))
                try:
                    eth_fee_persent=(eth_fee/last_price)*100
                except:
                    eth_fee_persent = 0
            else:
                eth_fee=0
                eth_fee_persent = 0
            if price_in_btc!='paraemas':
                btc_fee=(price_in_btc*btc_usd_price)-(last_price+last_price*((0.1/100)*3))
                try:
                    btc_fee_persent=(btc_fee/last_price)*100
                except:
                    btc_fee_persent = 0

            else:
                btc_fee=0
                btc_fee_persent = 0

            if bnb!='paraemas':
                bnb_fee=(bnb*bnb_usd_price)-(last_price+last_price*((0.1/100)*3))
                try:
                    bnb_fee_persent=(bnb_fee/last_price)*100
                except:
                    bnb_fee_persent = 0
            else:
                bnb_fee=0
                bnb_fee_persent = 0
            if busd!='paraemas':
                busd_fee=(busd*busd_usd_price)-(last_price+last_price*((0.1/100)*3))
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
    api_key = "DkqjHVkY2wPJBL8haWgqStOUzDZ14BXGRsbdQHfdmhQ4Pn46p5QeoYTphWtg9TOt"
    api_secret= 'iLBoBg9lyITUrHvwDhVpdUjR5UVJdFqTIl1RFHvfL30Fk55H1R51Sckfx0aZWHlu'
    from binance.client import Client
    ao=False

    client = Client(api_key, api_secret)
    exchange_info = client.get_exchange_info()
    while not ao:
        crypto_info = sorted_df.iloc[0]
        symbol = crypto_info['nimada foyda'].replace('/','')

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
    status_labe.config(text=crypto_info['Symbol'] + ': ' +"foyda: "+ str(crypto_info['foyda foizda']) + '%'+': '+'asl narxi: '+str(crypto_info['Price (USDT)'])+': '+'foyda dollarda: '+str(crypto_info['foyda'])+': '+'nima sotib olish kk: '+crypto_info['nimada foyda'])
    api_key = 'NjQ3rowr1LrmRxs6ERLJ2SqPueaNHTdMEV6YMy2Z1q4eIksxYEHg2vqdwy2FcgB3'
    api_secret = 'TCO2Xpjqb2C2P6f8IYHjk1WVLy3AhOp6ECiDhwR3gFSeMfzzzy04IWuaKwUTf9aU'
    from binance.client import Client
    ao = False

    client = Client(api_key, api_secret)
    balans = client.get_account()
    usd_balance = next((item for item in balans['balances'] if item['asset'] == 'USDT'), None)
    if usd_balance:
        status_lab.config(text='Balans: ' + usd_balance['free']+'$')
        print(balans)
        symbol = crypto_info['Symbol'].replace('/USDT', '')
        print(symbol)
        p = crypto_info['nimada foyda'].replace(f'{symbol}/', '')
        ak = crypto_info[f"Price ({p})"]
        print(ak)
    else:
        status_lab.config(text='Error: No USDT balance found')
        symbol = crypto_info['Symbol'].replace('/USDT', '')
        print(symbol)
    root.mainloop()


# Start the tkinter event loop
refresh_button = tk.Button(root, text="Refresh Data", command=refresh)
refresh_button.pack()
# Create a label widget to display the refresh status
status_label = tk.Label(root, text="Data last updated at: ", font=("Arial", 10))
status_label.pack(pady=10)
status_labe = tk.Label(root, text="refresh", font=("Arial", 10))
status_lab = tk.Label(root, text="Balans:", font=("Arial", 10))
status_labe.pack(pady=10)
status_lab.pack(pady=10)

root.mainloop()
