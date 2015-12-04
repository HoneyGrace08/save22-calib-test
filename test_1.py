first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']

fullname = []
for fname in first_names:
    print fname
    for lname in last_names:
        print lname

        fullname.append(fname+' '+lname)
print fullname
