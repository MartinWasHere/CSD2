def welcome():
    print("Welcome to this awesome beatmaker")
    while True:
        startUp=input("What would you like to do?   (makebeat/quit)  --> ")
        if startUp=="makebeat":
            print("opening beatmaker")
            break
        if startUp=="quit":
            print("Closing beatmaker")
            quit()
        else:
            print("Invalid option")
            continue
