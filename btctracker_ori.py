import pandas
import time
from datetime import timezone
import datetime
from datetime import datetime, timedelta, timezone
#import telegram_send

btc_addresses = {
    #'#3': '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ',
    #'Random': '14m3sd9HCCFJW4LymahJCKMabAxTK4DAqW',
    #'#1': '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo',
    #'#2': 'bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97',
    #'#3': '3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6',
    #'#13' : 'bc1qcv8h9hp5w8c4qpze0a4tdxw6qjtvg8yps23k0g3aymxx7jlesv4q4t6f65',
    '#33' : 'bc1qhxf9ckyz7sw8h6vkvdlffntmsu6fz8m3pdzgvw',
    }

t_time = {}
amount = {}

for key in btc_addresses:
    t_time[key] = 0
    amount[key] = 0

check_again = True

while True:
    time.sleep(1)
    while check_again:
        for whale in btc_addresses:
            transactions_url = 'https://blockchain.info/rawaddr/' + btc_addresses[whale]
            
            print('transactions_url:' + transactions_url)
            df               = pandas.read_json(transactions_url)
            transactions     = df['txs']
            last_time        = transactions[0]['time']
            last_amount      = transactions[0]['result']
            
            if last_time != t_time[whale]:
                t_time[whale] = last_time
                amount[whale] = last_amount
                
                if int(last_amount) > 0:
                    direction = "accumulating"
                elif int(last_amount) < 0:
                    direction = "dumping"

                btc_amount = int((float(abs(last_amount))/100000000))
                print(f'{whale} is {direction} {btc_amount} BTC')
                # telegram_send.send(messages=[f'Whale Alert: {whale} is {direction} {btc_amount} BTC'])

            time.sleep(15)

        check_again = False

    now      = datetime.datetime.now(timezone.utc)
    seven_days_ago = now - timedelta(days=7)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    midnight_seven_days_ago = seven_days_ago.replace(hour=0, minute=0, second=0, microsecond=0)
    minutes  = ((now - midnight).seconds) // 60

    if (minutes % 60) == 0:
        #telegram_send.send(messages=['Whale watcher checking in.'])    
        time.sleep(60)
        check_again = True
