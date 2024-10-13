from datetime import datetime, timedelta, timezone
import time
import pandas

btc_addresses = {
    '#01': '34xp4vRoCGJym3xR7yCVPFHoCNxv4Twseo',	
    '#02': 'bc1qgdjqv0av3q56jvd82tkdjpy7gdp9ut8tlqmgrpmv24sq90ecnvqqjwvw97',
    '#03': '1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ',
    '#04': '3LYJfcfHPXYJreMsASk2jkn69LWEYKzexb',
    '#05': 'bc1qazcm763858nkj2dj986etajv6wquslv8uxwczt',
    '#06': '37XuVSEpWW4trkfmvWzegTHQt7BdktSKUs',	
    '#07': '3M219KR5vEneNb47ewrPfWyb5jQ2DjxRP6',
    '#08': '38UmuUqPCrFmQo4khkomQwZ4VbY2nZMJ67',
    '#09': '1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF',
    '#10': 'bc1qa5wkgaew2dkv56kfvj49j0av5nml45x9ek9hz6',	
    '#11': '1LdRcdxfbSnmCYYNdeYpUnztiYzVfBEQeC',
    '#12': '1AC4fMwgY8j9onSbXEWeH6Zan8QGMSdmtA',
    '#13': '3Kzh9qAqVWQhEsfQz7zEQL1EuSx5tyNLNS',
    '#14': 'bc1qmxjefnuy06v345v6vhwpwt05dztztmx4g3y7wp',
    '#15': '3FpYfDGJSdkMAvZvCrwPHDqdmGqUkTsJys',
    '#16': 'bc1qd4ysezhmypwty5dnw7c8nqy5h5nxg0xqsvaefd0qn5kq32vwnwqqgv4rzr',
    '#17': '1LruNZjwamWJXThX2Y8C2d47QqhAkkc5os',
    '#18': '3Gpex6g5FPmYWm26myFq7dW12ntd8zMcCY',
    '#19': '3LQUu4v9z6KNch71j7kbj8GPeAGUo1FW6a',
    '#20': 'bc1q7ydrtdn8z62xhslqyqtyt38mm4e2c4h3mxjkug',	
    '#21': '3FupZp77ySr7jwoLYEJ9mwzJpvoNBXsBnE',
    '#22': '159QgP4Ewvadjc4HDpaaR6pir2R4ZfzVfQ',	
    '#23': '3LCGsSmfr24demGvriN4e3ft8wEcDuHFqh',	
    '#24': '12XqeqZRVkBDgmPLVY4ZC6Y4ruUUEug8Fx',
    '#25': 'bc1qx9t2l3pyny2spqpqlye8svce70nppwtaxwdrp4',	
    '#26': '3FHNBLobJnbCTFTVakh5TXmEneyf5PT61B',
    '#27': '385cR5DM96n1HvBDMzLHPYcw89fZAXULJP',	
    '#28': '12ib7dApVFvg82TXKycWBNpN8kFyiAN1dr',
    '#29': 'bc1q9d4ywgfnd8h43da5tpcxcn6ajv590cg6d3tg6axemvljvt2k76zs50tv4q',
    '#30': '3JZq4atUahhuA9rLhXLMhhTo133J9rF97j',
    '#31': '12tkqA9xSoowkzoERHMWNKsTey55YEBqkv',
    '#32': '19iqYbeATe4RxghQZJnYVFU4mjUUu76EA6',
    '#33': 'bc1qjysjfd9t9aspttpjqzv68k0ydpe7pvyd5vlyn37868473lell5tqkz456m',
    '#34': '17MWdxfjPYP2PYhdy885QtihfbW181r1rn',
    '#35': '1aXzEKiDJKzkPxTZy9zGc3y1nCDwDPub2',
    '#36': '19D5J8c59P2bAkWKvxSYw8scD3KUNWoZ1C',
    '#37': '1932eKraQ3Ad9MeNBHb14WFQbNrLaKeEpT',
    '#38': '1MDq7zyLw6oKichbFiDDZ3aaK59byc6CT8',	
    '#39': '14m3sd9HCCFJW4LymahJCKMabAxTK4DAqW',
    '#40': '3HSMPBUuAPQf6CU5B3qa6fALrrZXswHaF1',
    '#41': 'bc1qtw30nantkrh7y5ue73gm4mmy0zezfqxug3psr94sd967qwg7f76scfmr9p',
    '#42': '17rm2dvb439dZqyMe2d4D6AQJSgg6yeNRn',	
    '#43': '1PeizMg76Cf96nUQrYg8xuoZWLQozU5zGW',
    '#44': '1CEHpeteegRks3L2co2usFAT8GTuX68MG',	
    '#45': '3DVJfEsDTPkGDvqPCLC41X85L1B1DQWDyh',
    '#46': '3K5dmrkBMS8ZVgERMLwiw7PJuG8GWTbo8e',
    '#47': 'bc1qkexcvmd6j3pm7zk789ccuy6fl9w29ru989fr97',
    '#48': '3H5JTt42K7RmZtromfTSefcMEFMMe18pMD',
    '#49': '34HpHYiyQwg69gFmCq2BGHjF1DZnZnBeBP',
    '#50': '39gUvGynQ7Re3i15G3J2gp9DEB9LnLFPMN',
    '#51': '1GR9qNz7zgtaW5HwwVpEJWMnGWhsbsieCG',
    '#52': 'bc1qm34lsc65zpw79lxes69zkqmk6ee3ewf0j77s3h',
    '#53': 'bc1q93yswtmvkw6wqeu5ugj36uglwsrw8lmcck4l7s',
    '#54': '1KUr81aewyTFUfnq4ZrpePZqXixd59ToNn',
    '#55': '3BMEXqGpG4FxBA1KWhRFufXfSTRgzfDBhJ',
    '#56': '15pqaBHFwFEphRqmXAPbs3QRLLPB7e2uMb',
    '#57': '3EMVdMehEq5SFipQ5UfbsfMsH223sSz9A9',
    '#58': '36rPiyFi4pZmnAyYbDTABqLN3WcWP6yJXS',
    '#59': 'bc1q080rkmk3kj86pxvf5nkxecdrw6nrx3zzy9xl7q',
    '#60': 'bc1q5pucatprjrqltdp58f92mhqkfuvwpa43vhsjwpxlryude0plzyhqjkqazp',
    '#61': '1BZaYtmXka1y3Byi2yvXCDG92Tjz7ecwYj',
    '#62': 'bc1q4vxn43l44h30nkluqfxd9eckf45vr2awz38lwa',
    '#63': '35pgGeez3ou6ofrpjt8T7bvC9t6RrUK4p6',
    '#64': '3ETUmNhL2JuCFFVNSpk8Bqx2eorxyP9FVh',
    '#65': 'bc1q4c8n5t00jmj8temxdgcc3t32nkg2wjwz24lywv',
    '#66': '3GWUKxq55XsQ7rkzbxAgfSyf6KHp8Ljh3R',
    '#67': '1FZy7CPFA2UqqQJYUA1cG9KvdDFbSMBJYG',
    '#68': '1F34duy2eeMz5mSrvFepVzy7Y1rBsnAyWC',
    '#69': 'bc1qqn4q5yv7feltnsfwzxwm3fluryqqzhhp6457h6m4ytq7mauxlxgq872p5f',
    '#70': 'bc1qhd0r5kh3u9mhac7de58qd2rdfx4kkv84kpx302',
    '#71': 'bc1qjh0akslml59uuczddqu0y4p3vj64hg5mc94c40',
    '#72': '3MucL2QnmjzRhvcEvdK7kXCjQMUSibuL7A',
    '#73': '3PDcfVscoEFRwvk6cE93qJnEQfseRSn5Y3',
    '#74': '1f1miYFQWTzdLiCBxtHHnNiW7WAWPUccr',
    '#75': 'bc1qsxdxm0exqdsmnl9ejrz250xqxrxpxkgf5nhhtq',	
    '#76': 'bc1qtef0p08lputg4qazhx2md43ynhc9kp20pn297qnz68068d9z48asmemanj',
    '#77': '1BAFWQhH9pNkz3mZDQ1tWrtKkSHVCkc3fV',
    '#78': '14YK4mzJGo5NKkNnmVJeuEAQftLt795Gec',
    '#79': '1Ki3WTEEqTLPNsN5cGTsMkL2sJ4m5mdCXT',
    '#80': '1KbrSKrT3GeEruTuuYYUSQ35JwKbrAWJYm',
    '#81': '1P1iThxBH542Gmk1kZNXyji4E4iwpvSbrt',
    '#82': '12tLs9c9RsALt4ockxa1hB4iTCTSmxj2me',
    '#83': '1ucXXZQSEf4zny2HRwAQKtVpkLPTUKRtt',
    '#84': '1CPaziTqeEixPoSFtJxu74uDGbpEAotZom',	
    '#85': '1LfV1tSt3KNyHpFJnAzrqsLFdeD2EvU1MK',
    '#86': '12dmPGKq4iK1o1o77YV3Urjj4tcRTmu6an',
    '#87': '1EU2pMence1UfifCco2UHJCdoqorAtpT7',
    '#88': 'bc1qhsm8kec8wf480sadlxuelr76ew4mzvljh5xa4e',
    '#89': 'bc1qlkdlchlylfdkspvevnlqqlmt4l222hwva2z3n7',	
    '#90': 'bc1qg6kqkkaexnxpvle8w3zy5j7w4k9uz5rqmrx5lw',	
    '#91': 'bc1qqdykm85ycxjqjh5hrkwmewts02mm6ku5rlck3m',
    '#92': 'bc1qgc5h9vz0zp4cmlxuw0h6jgryetq08e4twen03f',
    '#93': 'bc1qxv55wuzz4qsfgss3uq2zwg5y88d7qv5hg67d2d',
    '#94': 'bc1qmjpguunz9lc7h6zf533wtjc70ync94ptnrjqmk',
    '#95': 'bc1qyr9dsfyst3epqycghpxshfmgy8qfzadfhp8suk',
    '#96': 'bc1q8qg2eazryu9as20k3hveuvz43thp200g7nw7qy',
    '#97': 'bc1q4ffskt6879l4ewffrrflpykvphshl9la4q037h',
    '#98': '134ooU6EQmCFFzEPN7yga3S1XikcBtynco',
    '#99': '3265tcUcp8dBhBBwp4rKN3iyUptuHkzMq7',
    '#100': '17rVQwoL5v18KfoQJNMMoMBm3rDjodxw1m',
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
        # Initialize counters for accumulating and dumping
        total_accumulating = 0
        total_dumping = 0

        for whale in btc_addresses:
            transactions_url = 'https://blockchain.info/rawaddr/' + btc_addresses[whale]
            
            print(f'transactions_url: {transactions_url}')
            df = pandas.read_json(transactions_url)
            transactions = df['txs']
            
            # Get the timestamp for 24 hours ago
            now = datetime.now(timezone.utc)
            twenty_four_hours_ago = now - timedelta(hours=24)
            twenty_four_hours_ago_timestamp = int(twenty_four_hours_ago.timestamp())

            for transaction in transactions:
                last_time = transaction['time']
                last_amount = transaction['result']
                
                # Check if transaction occurred within the last 24 hours
                if last_time >= twenty_four_hours_ago_timestamp:
                    if last_amount > 0:
                        direction = "accumulating"
                        total_accumulating += 1  # Increment accumulating count
                    else:
                        direction = "dumping"
                        total_dumping += 1  # Increment dumping count

                    btc_amount = float(abs(last_amount)) / 100000000  # Convert to BTC
                    print(f'{whale} had a {direction} transaction of {btc_amount:.8f} BTC within the last 24 hours.')
                    # telegram_send.send(messages=[f'Whale Alert: {whale} had a {direction} transaction of {btc_amount:.8f} BTC within the last 24 hours.'])

            time.sleep(15)

        # Output the total counts
        print(f"Total accumulating transactions in the last 24 hours: {total_accumulating}")
        print(f"Total dumping transactions in the last 24 hours: {total_dumping}")

        check_again = False

    now = datetime.now(timezone.utc)
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    minutes = ((now - midnight).seconds) // 60

    if minutes % 60 == 0:
        # telegram_send.send(messages=['Whale watcher checking in.'])    
        time.sleep(60)
        check_again = True