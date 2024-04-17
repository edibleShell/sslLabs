import json
import requests
import time

def analyze(host, publish, startNew, fromCache, maxAge,
            allEndpoints, ignoreMismatch, base_url, headers):
    
    url = (
        f'{base_url}host={host}&publish={publish}'
        f'&startNew={startNew}&fromCache={fromCache}&'
        f'all={allEndpoints}&ignoreMismatch={ignoreMismatch}&maxAge={maxAge}'
    )
    res = requests.get(url, headers=headers)
    res = res.json()

    while res['status'] != 'READY':
        if res['status'] != 'IN_PROGRESS':
            time.sleep(5)
        elif res['status'] == 'IN_PROGRESS':
            time.sleep(10)
        res = requests.get(url, headers=headers)
        res = res.json()
    
    res = json.dumps(res, indent=4) 
    return res

def main():

    email = input('Provide the email registered with SSL Labs: ')
    headers = {
        'email': email
    }
    publish = 'off'
    startNew = 'off'
    fromCache = 'on'
    maxAge = '1'
    allEndpoints = 'on'
    ignoreMismatch = 'off'
    base_url = 'https://api.ssllabs.com/api/v4/analyze?'
    
    host = input('Provide the host that you want to analyze: ')
    results = analyze(host, publish, startNew, fromCache,
                      maxAge, allEndpoints, ignoreMismatch,
                      base_url, headers)
    print(results)


if __name__ == "__main__":
    main()
