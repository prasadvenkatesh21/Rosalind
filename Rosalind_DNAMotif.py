import re
s = 'GATATATGCATATACTT'
t = '(?=ATAT)'

location = [num.start() for num in re.finditer(t,s)]
for each in location:
    print each+1,