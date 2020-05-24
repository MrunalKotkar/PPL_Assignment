# puzzle program

print(
    "A man is walking down a village road with a tiger, a goat and a bundle of grass.\nSoon he arives at a river bank where there one tiny boat that can carry him and another animal or grass at a time.\nHere is a problem:\nLeft alone tiger will eat the goat.\nAnd similarly the goat will eat the grass bundle.\nTry to find the solution for this.\n")

bank1 = ['tiger', 'grass', 'goat']
bank2 = []

while len(bank1) != 0:
    print(bank1)
    print(bank2)
    transfer = input("what to transfer from 1 to 2:")
    bank1.pop(bank1.index(transfer))

    if "grass" in bank1 and "goat" in bank1:
        print("OOPS!!Goat eat the grass.")
        bank1.append(transfer)
        continue
    elif "tiger" in bank1 and "goat" in bank1:
        print("OOPS!!Tiger eat the goat.")
        bank1.append(transfer)
        continue
    bank2.append(transfer)
    transfer2 = input("what to transfer from 2 to 1:")
    if transfer2 == "none":
        continue
    else:
        bank2.pop(bank2.index(transfer2))

        if "grass" in bank2 and "goat" in bank2:
            print("OOPS!!Goat eat the grass.")
            bank2.append(transfer2)
            continue
        elif "tiger" in bank2 and "goat" in bank2:
            print("OOPS!!Tiger eat the goat.")
            bank2.append(transfer2)
            continue
        bank1.append(transfer2)

print("Successful!")


