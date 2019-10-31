import os
import sys

# FROM: https://stackoverflow.com/questions/3670323/setting-smaller-buffer-size-for-sys-stdin
# apparently -u no longer applies to stdin in python3

unbuffered_stdin = os.fdopen(sys.stdin.fileno(), 'rb', buffering=0)
while True:
    print(unbuffered_stdin.read(2))
