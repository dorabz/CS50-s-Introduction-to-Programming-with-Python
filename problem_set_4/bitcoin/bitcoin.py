import sys, requests

if len(sys.argv) == 2:
    try:
        n = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        pass
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        pass
    x = float(r.json()['bpi']['USD']['rate_float'])
    print(f"${x*n:,.4f}")
else:
    sys.exit("Missing command-line argument")