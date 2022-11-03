#dict means dictionary
# key : value
#uses: helpful to store name:ph.no like this details
d = {'a':12,'b':13,'c':14}
print(type(d))

d1 = { }  #empty dcit not set
#d[key] = value   to add data to dict
d1[100] = 'vinay'
d1[200] = 'vinny'
print(d1)
print(type(d1))

#duplicate KEYS not allowed but Duplicate values are allowed
print("testing")
d1[200]='vijay'
print(d1)    # old vale of 200 is replaced with new (vinny by vijay)
d1[300] = 'vinay'
print(d1) #accept the duplicate vale so prints vinay for 100 and 300

#key and value we can use any data type int or str or float