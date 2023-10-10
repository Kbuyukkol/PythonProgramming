for x in range(1, 101):
    if x % 15 == 0:
        print("FINRA")
    elif x % 3 == 0:
        print("FIN")
    elif x % 5 == 0:
        print("RA")
    else:
        print(x)
