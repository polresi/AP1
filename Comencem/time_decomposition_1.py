from yogi import read

s = read(int)

m = s//60

print( s//3600 ,m%60 , s%60 )
