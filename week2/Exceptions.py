
if __name__ == '__main__':
    t = int(input().rstrip())
    for i in range(t):
        a, b = input().rstrip().split()
        try:
            print(int(a) // int(b))
        except ZeroDivisionError as e:
            print('Error Code: integer division or modulo by zero')
        except ValueError as e:
            print(f'Error Code: {e}')