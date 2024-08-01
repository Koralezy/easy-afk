# ---------------------- Edit these two variables to your liking! ----------------------


# Keys to be pressed - each key should be in '' and separated by commas OUTSIDE the marks. 
# Check key-names.txt if you can't get a specific key to work.
key = ['space']

# Replace this with how often (in seconds) you want the key to be pressed - DON'T ADD ''
interval = 5 

# SAVE the file before running!


# --------------------------------- vvv boring code vvv ---------------------------------


import pydirectinput
import time

if len(key) == 1:
    c = key[0]
    print("I will now press [",c.upper(),"] every", interval , "seconds!") 

else:
    ukey = []
    for u in key:
        ukey.append(u.upper())

    p = ' ]  , [ '.join(ukey) 
    print("I will now press [",p,"] every", interval , "seconds!")

time.sleep(2)

count = 0 
while True:
    for k in key:
        pydirectinput.press(k) 
        count += 1
        print(f"{count} times | Pressed {k.upper()}")
        time.sleep(interval)