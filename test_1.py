first_names = ['Shan', 'Dao Ming', 'Hua Ze', 'Xi', 'Mei']
last_names = ['Cai', 'Si', 'Lei', 'Men', 'Zuo']


fullname = [ (fn + " " + last_names[i]) for i, fn in enumerate(first_names)]
print (fullname)


# fullname2 = [(first+ " " + last)  for first, last in zip(first_names, last_names)]
# "{} {}".format(first, last)
# print (fullname2)
