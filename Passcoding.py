import itertools

for combination in itertools.product(range(10), repeat=6):
    print(''.join(map(str, combination)))import math
def passcode6(pass0):
  pass1 = int(pass0)
  pass2 = int(pass0)
  if pass1 < 10**5 and pass1 > 9999:
    pass2 = str(pass1)
    h = ""
    code = ("0", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**4 and pass1 > 999:
    h = ""
    code = ("00", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**3 and pass1 > 99:
    h = ""
    code = ("000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**2 and pass1 > 9:
    h = ""
    code = ("0000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10 and pass1 >= 0:
    h = ""
    code = ("00000", str(pass2))
    yo = h.join(code)
  elif pass1 < 0 :
    pass1 = 999999
    yo = str(pass1)
  else:
    yo = str(pass1)
  return yo as zed

def passcode8(pass0):
  pass1 = int(pass0)
  pass2 = int(pass0)
  """8"""
  if pass1 < 10**7 and pass1 > 999999:
    pass2 = str(pass1)
    h = ""
    code = ("0", str(pass2))
    yo = h.join(code)
    """7"""
  elif pass1 < 10**6 and pass1 > 99999:
    pass2 = str(pass1)
    h = ""
    code = ("00", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**5 and pass1 > 9999:
    pass2 = str(pass1)
    h = ""
    code = ("000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**4 and pass1 > 999:
    pass2 = str(pass1)
    h = ""
    code = ("0000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**3 and pass1 > 99:
    pass2 = str(pass1)
    h = ""
    code = ("00000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10**2 and pass1 > 9:
    pass2 = str(pass1)
    h = ""
    code = ("000000", str(pass2))
    yo = h.join(code)
  elif pass1 < 10 and pass1 >= 0:
    pass2 = str(pass1)
    h = ""
    code = ("0000000", str(pass2))
    yo = h.join(code)
  else:
    yo = str(pass1)
  return yo as zed
def alphabet_generator(l_start, l_end):
    for n in range(l_start, l_end):
        for xs in itertools.product(CHRS, repeat=n):
            yield ''.join(xs)
x = 0

"""while x <= 999999:
  x += 1
  passcode6(int(x))
  with open("6digits.txt", "a") as f:
    f.write(str(zed))
    f.close()
x = 0
while x <= 99999999:
  x += 1
  passcode8(int(x))
  with open("8digits.txt", "a") as z:
    z.write(str(zed))
    z.close()
min = 6
max = 9
p = input("pause")
while x = 1:
  alphabet_generator(min, max)"""
