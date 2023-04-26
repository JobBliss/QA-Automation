import datetime

datesInfo=datetime.datetime.now()
testinfo=datetime.datetime.strftime(datesInfo,'%a %b %d %H:%M:%S +%f %Y')
dayinfo=list(testinfo)
print(dayinfo)
day=dayinfo[0]+dayinfo[1]+dayinfo[2]
month=dayinfo[4]+dayinfo[5]+dayinfo[6]
year = dayinfo[-4]+dayinfo[-3]+dayinfo[-2]+dayinfo[-1]
actualday = dayinfo[9]+dayinfo[10]
# print(day)
# print(month)
# print(year)

fulldate = f'{day} {actualday}{month} {year}'
print(fulldate)