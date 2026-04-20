times_string = '1h 45m,360s,25m,30m 120s,2h 60s'
times_string = times_string.replace(' ', ',')
time_split = times_string.split(',')
time_result = 0

for x in time_split:
    if 'h' in x:
        time_result += (int(x.replace('h', ''))*60)
    if 'm' in x:
        time_result += int(x.replace('m', ''))
    if 's' in x:
        time_result += (int(x.replace('s', '')) // 60)

print(time_result)