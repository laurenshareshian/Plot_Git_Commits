import matplotlib.pyplot as plt
import numpy as np
import json
from datetime import date

# # ##################################################################################
#commits.json contains all of the 2016 info retrieved using curl from https://github.com/d3/d3/commits/
# it plots the number of commits by Michael Bostock by day of the week, month, and during his busiest week
# # ##################################################################################
json_data=open('commits.json').read()
data = json.loads(json_data)
days=[]
months=[]
weekdays=[]
words=[]

for i in range(len(data)):
    months.append(int(data[i]['commit']['committer']['date'][5:7]))
    days.append(int(data[i]['commit']['committer']['date'][8:10]))
    print(data[i]['commit']['committer']['date'])
    newformat = map(int, data[i]['commit']['committer']['date'].split("T")[0].split("-"))
    weekdays.append(date.weekday(date(*newformat)))
    for word in data[i]['commit']['message'].split():
        words.append(word.lower().rstrip('?:!.,;'))

# # ##################################################################################
# # #print Mike Bostock's most used words
# # ##################################################################################
wordlist=[]
for word in set(words):
    if words.count(word)>10:
        wordlist.append((words.count(word), word))
wordlist.sort(reverse=True)
print('his favorite words')
print(wordlist)
#
# ##################################################################################
# #find the most common days, months, and weeks for commits
# ##################################################################################
countdays=[]
daynumbers=[0,1,2,3,4,5,6]
count=0
daylist=['Mon','Tue','Wed','Thu','Fri','Sat', 'Sun']
for day in daynumbers:
    countdays.append(weekdays.count(day))
    count=count+1


countmonths = []
monthlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for month in monthlist:
    countmonths.append(months.count(month))

firstweekcount=0
secondweekcount=0
thirdweekcount=0
fourthweekcount=0
for i in range(len(months)):
    if months[i]==6:
        if 1<=days[i]<7:
            firstweekcount=firstweekcount+1
        elif 7<=days[i]<13:
            secondweekcount=secondweekcount+1
        elif 14 <= days[i] < 20:
            thirdweekcount = thirdweekcount + 1
        else:
            fourthweekcount = fourthweekcount + 1
junecounts=[firstweekcount,secondweekcount,thirdweekcount,fourthweekcount]
juneweeks=['Jun 1-6','Jun 7-13','Jun 14-20','Jun 21-30' ]


# ##################################################
# #graph my analysis
# ##################################################
plt.figure(1)
plt.subplot(311)
y_pos = np.arange(len(daylist))
plt.bar(y_pos,countdays, align='center', alpha=0.5)
plt.xticks(y_pos,daylist)
plt.ylabel('Number of commits')
plt.title('Number of commits versus day of week using Curl to retrieve data')

plt.subplot(312)
y2_pos = np.arange(len(monthlist))
plt.bar(y2_pos,countmonths, align='center', alpha=0.5)
plt.xticks(y2_pos,monthlist)
plt.ylabel('Number of commits')
plt.title('Number of commits versus month in 2016')


plt.subplot(313)
y3_pos = np.arange(len(juneweeks))
plt.bar(y3_pos,junecounts, align='center', alpha=0.5)
plt.xticks(y3_pos,juneweeks)
plt.ylabel('Number of commits')
plt.title('Number of commits versus week in June')
plt.show()
# #
# #
