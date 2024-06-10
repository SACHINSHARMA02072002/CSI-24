
import re

if __name__ == '__main__':
    t = int(input().rstrip())
    for i in range(t):
        try:
            re.compile(input().rstrip())
            print(True)
        except re.error:
            print(False)