a,b,c=map(int,input().split(":"))
d,e,f=map(int,input().split(":"))

total=(d*3600+e*60+f)-(a*3600+b*60+c)

if total < 0: total+=3600*24

print("%02d:%02d:%02d" % (total//3600,(total%3600)/60,total%60))

