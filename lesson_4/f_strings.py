from itertools import count
from pickletools import uint2

x=5
y=10
result=x+y
print(f"{x=}, {y=}, {result=}")

total=10000000000
print(f"{total:,}")
t=5.646545643213
print(f"{t:.4f}")


last_name="Kalashnikov"
name="Tatiana"
print(f"{last_name:*^30}")
print(f"{name:*^30}")


BASE_URL="https://web.whatsapp.com/"

my_adress="""
Israel
Kibbuz
Masada"""

print(ord("a"))
print(ord("A"))


s="Donald Trump"
print(s[1::2])
print(s[::-1])


s="leetcode.com"
print(s[-1]+s[:-1])

a="ABCDEFGHIJKLMNOP"
print(a[0])
print(a[-1])
print(a[(len(a)//2)])
print(a[0::2])
print(a[1::2])
print(a[::-1])


name="Messi"
numb=33
print(f"Hello {name}. You are {numb} years old. ")


w=1920
h=1080
print(f"Screen Resolution: {w} x {h}.\nTotal amount of pixels = {w*h}")




inp="ManY mUcH"
print(inp.upper())

inp1="U2"
inp2="u2"
print(inp1.lower()==inp2.lower())

t=("pjlhbkn,mk")
print(t[0:3].upper()+t[3:-3].lower()+t[len(t)-3:].upper())

smpl="Everywhere"
print(smpl.count("e")+smpl.count("E"))

d="This is the test message"
print(d.lower())
print(d.upper())
print(d.title())
print(d.capitalize())
print(d.split())
d=d.split()
d=sorted(d)
print(d[0], d[-1])

