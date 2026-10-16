count_time = 0
string_time = '1h 45m,360s,25m,30m 120s,2h 60s'

lst = string_time.split(',')

for t in lst:
    time = t.split()
   
    for i in time:
        if 'h' in i:
            min = int(i.replace('h', '')) * 60
        elif 's' in i:
            min = int(i.replace('s', '')) / 60
        elif 'm' in i:
            min = int(i.replace('m', ''))

        count_time += min

print(count_time)
