def modulo(num):
    return num%2

def bigger_number(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        n=num1
        return n
    else:
        if num2>=num1 and num2>=num3:
            n=num2
            return n
        else:
            n=num3
            return n
        
def orden (num1, num2, num3):
    a = min(num1, num2, num3)
    b = max(num1, num2, num3)
    c = (num1+num2+num3)-a-b
    e = [a,b,c]
    return e