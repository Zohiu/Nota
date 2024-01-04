if __name__ == '__main__':
    import premium_manager
    print("premium_manager.py imported.")
    print("console.py started.")

    while True:
        inputstr = input()

        if inputstr == "help":
            print("Commands:\npremium_manager\n")

        elif inputstr == "premium_manager":
            premium_manager.ask()

        else:
            print("Unknown command!")