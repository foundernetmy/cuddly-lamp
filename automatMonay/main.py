import time
import ccxt
import pandas as pd
i=1
while True:
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
    btcprice=tickers['BTC/USDT']
    btcpr=btcprice['last']
    busd_usd_price = busd_usd_pricer['last']
    for symbol in tickers:
        # Check if the symbol contains USDT and ignore any other symbols
        if "USDT" in symbol:
            ticker = tickers[symbol]
            last_price = ticker['last']
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
    df = pd.DataFrame(data,
                      columns=['Symbol', 'Price (USDT)', 'Price (BTC)', 'Price (BNB)', 'Price (ETH)', 'Price (BUSD)',
                               'Price Change (%)', 'BTC foyda', 'ETH foyda', 'BNB foyda', 'BUSD foyda', 'foyda',
                               'nimada foyda','foyda foizda'])

    # Sort the data by the 'Price (BNB)' column in descending order
    sorted_df = df.sort_values(by=["foyda foizda"], ascending=False)
    sorted_df = sorted_df.nlargest(10, 'foyda foizda')
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'
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
    from binance.client import Client
    ao = False
    client = Client(api_key, api_secret)
    balans = client.get_account()
    usd_balance = next((item for item in balans['balances'] if item['asset'] == 'USDT'), None)
    if usd_balance:
        crypto_info = sorted_df.iloc[i]
        symbol = crypto_info['Symbol'].replace('/USDT', '')
        print(symbol)
        quan=int(float(usd_balance['free'])/crypto_info['Price (USDT)'])
        order = client.order_market_buy(
            symbol=crypto_info['nimada foyda'].replace('/',''),
            quantity=quan)
        time.sleep(20)
        balans1 = client.get_account()
        man = next((item for item in balans1['balances'] if item['asset'] == symbol), None)
        p = crypto_info['nimada foyda'].replace(f'{symbol}/', '')
        ak = crypto_info[f"Price ({p})"]

        order2 = client.order_market_sell(
                symbol=crypto_info['nimada foyda'].replace('/', ''),
                quantity=quan
            )
            # Check the response of the sell order.
        if order2.get('status') == 'FILLED':
            print('Order filled successfully')
        else:
            print('Error in order:', order2)
        time.sleep(20)
        balans2 = client.get_account()
        kab = next((item for item in balans2['balances'] if item['asset'] == "BNB"), None)
        order3 = client.order_market_sell(
            symbol=(crypto_info['nimada foyda'].replace(symbol + '/', '')) + '/USDT',
            quantity=kab['free']
        )
        # Check the response of the sell order.
        if order3.get('status') == 'FILLED':
            print('Order filled successfully')
        else:
            print('Error in order:', order3)


    else:
        print('?')

