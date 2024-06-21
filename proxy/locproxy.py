file = open('C:/BaoHuy/Python/tool/Ddos/VIP/proxy/live.txt', 'r')
proxies = file.read().split('\n')
file.close()

file = open('C:/BaoHuy/Python/tool/Ddos/VIP/proxy/proxies.txt', 'w')
proxies = set(proxies)
for proxy in proxies:
    print(proxy,file=file)
file.close()