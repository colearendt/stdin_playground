import os
import sys
import time

# FROM: https://stackoverflow.com/questions/3670323/setting-smaller-buffer-size-for-sys-stdin
# apparently -u no longer applies to stdin in python3

#unbuffered_stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
#while True:
#    print(unbuffered_stdin.read(1))

while True:
  val = sys.stdin.read(1)
  if val:
    print(val)
  time.sleep(0.05)

# maybe an idea using curses?
# https://stackoverflow.com/questions/2408560/python-nonblocking-console-input
