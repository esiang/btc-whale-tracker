from datetime import datetime, timedelta, timezone
import time
import pandas

btc_addresses = {
    '#33': 'bc1qhxf9ckyz7sw8h6vkvdlffntmsu6fz8m3pdzgvw',
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
            
            print(f'transactions_url: {transactions_url}')
            df = pandas.read_json(transactions_url)
            transactions = df['txs']
            
            # Get the timestamp for 7 days ago
            now = datetime.now(timezone.utc)
            seven_days_ago = now - timedelta(days=7)
            seven_days_ago_timestamp = int(seven_days_ago.timestamp())

            for transaction in transactions:
                last_time = transaction['time']
                last_amount = transaction['result']
                
                # Check if transaction occurred within the last 7 days
                if last_time >= seven_days_ago_timestamp:
                    direction = "accumulating" if last_amount > 0 else "dumping"
                    btc_amount = float(abs(last_amount)) / 100000000  # Convert to BTC
                    print(f'{whale} had a {direction} transaction of {btc_amount:.8f} BTC within the last 7 days.')
                    # telegram_send.send(messages=[f'Whale Alert: {whale} had a {direction} transaction of {btc_amount:.8f} BTC within the last 7 days.'])

            time.sleep(15)

        check_again = False

    now = datetime.now(timezone.utc)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    minutes = ((now - midnight).seconds) // 60

    if minutes % 60 == 0:
        # telegram_send.send(messages=['Whale watcher checking in.'])    
        time.sleep(60)
        check_again = True

