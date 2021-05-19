# PEMDAS applies
# Input terminated by EOF
# Always 2 decimal places provided
import sys

for raw_data in sys.stdin:
    print('%.2f' % eval(raw_data))
