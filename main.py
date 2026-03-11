def sum(a, b):
    """Tinh tong hai so"""
    return a + b

def sub(a, b):
    """Tinh hieu hai so"""
    return a - b

if __name__ == "__main__":
    a = float(input("Nhap so thu nhat: "))
    b = float(input("Nhap so thu hai: "))

    print(f"Tong: {a} + {b} = {sum(a, b)}")
    print(f"Hieu: {a} - {b} = {sub(a, b)}")
