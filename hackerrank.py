if __name__ == '__main__':
    s=input()
    for i in s:
        if i.isalnum():
            print("true")
        if i.isalpha():
            print("true")
        if i.isdigit():
            print("true")
        if i.islower():
            print("true")
        if i.isupper():
            print("true")
        else:
            print("false")
