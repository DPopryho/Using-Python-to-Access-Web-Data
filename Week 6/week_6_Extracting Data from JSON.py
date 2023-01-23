import json
import urllib.request, urllib.parse, urllib.error

while True:

    data_ur = input("URL: ")
    if len(data_ur) < 1: break

    parms = dict()
    url = data_ur + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())

    info = json.loads(data)
    info = info["comments"]
    print('User count:', len(info))

    lst = []
    for i in info:
        # name = ('name', i["name"])
        cnt = ('count', i["count"])
        lst.append(cnt[1])
    print("Sum: ", sum(lst))
    break