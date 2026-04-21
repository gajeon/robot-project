def add(a, b): return a + b

def sub(a, b): return a - b

def mul(a, b): return a * b

def div(a, b): return a / b


def calculator():
    """로봇 SW 개발 입문용 계산기 메인 함수"""
    while True:
        try:
            op = input("연산자 +-*/q: ")

            if op == 'q':
                break
            if op not in ['+', '-', '*', '/']:
                continue
            num1 = float(input("숫자 1:"))
            num2 = float(input("숫자 2:"))
            
            if op == '+':
                print(f"{add(num1, num2)}")
            elif op == '-':
                print(f"{add(num1, num2)}")
            elif op == '*':
                print(f"{add(num1, num2)}")
            elif op == '/':
                print(f"{add(num1, num2)}")

        except ValueError as e:
            print(e)
        except ZeroDivisionError as e:
            print(e)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    calculator()