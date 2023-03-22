import string as ss

s = input()
up = ss.ascii_uppercase
low = ss.ascii_lowercase
rot_up = up[13:] + up[:13]
rot_low = low[13:] + low[:13]

trans_up = str.maketrans(up,rot_up)
trans_low = str.maketrans(low,rot_low)

s = s.translate(trans_up)
s = s.translate(trans_low)

print(s)
