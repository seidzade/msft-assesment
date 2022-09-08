'''Script file that get the currency of BTC in USD and EU and every 2min
display the results and calculate the avg every 10min and display the avg'''

# Import libraries
import os
from time import sleep
from datetime import datetime
import requests
from flask import Flask

app = Flask(__name__)

def average(lst):
    '''Calculate the avg of list'''
    return sum(lst) / len(lst)   

def current_time():
    '''Return the current time'''
    now = datetime.now()
    c_time = now.strftime("%H:%M:%S")
    return c_time

@app.route("/" + os.environ['app_path'])
def index():
    prices_of_btc = []
    counter = 0

    while True:
        # Defining Binance API URL
        key = "https://api.binance.com/api/v3/ticker/price?symbol="
        # Making list for multiple crypto's
        currencies = [os.environ['CURRENCY']]
        j = 0
        # running loop to print all crypto prices
        for i in currencies:
            # completing API for request
            url = key+currencies[j]
            data = requests.get(url)
            data = data.json()
            j = j+1
            prices_of_btc.append(float(data['price']))
            curr = (f"CURRENT PRICE --> {current_time()} -- {data['symbol']} price is {data['price']}")
        sleep(2)
        counter = counter+1
        avg = ""
        #if the counter reach to 5 it means passed 10 min
        if counter==5:
            prices_of_btc_to_show = prices_of_btc
            prices_of_btc = []
            counter=0
            avg = (f"AVERAGE PRICE --> {current_time()} == The average of {os.environ['CURRENCY']} in the last 10 min: {average(prices_of_btc_to_show)}")
        if(avg):
            return(curr +
                    avg)
        else:
            return(curr)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)