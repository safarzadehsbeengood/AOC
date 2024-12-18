from hashlib import md5

pi = 'bgvyzdsv'

for i in range(1000000000):
    key = pi + str(i)
    res = md5(key.encode()).hexdigest()
    if res.startswith('000000'):
        print(key)
        break



