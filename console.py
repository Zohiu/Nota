if __name__ == '__main__':
    print("[Debug] starting premium_manager.py...")
    import premium_manager

    print("[Debug] premium_manager.py has been started.")

    print("[Debug] console.py has been started.")
    while True:
        inputstr = input()

        if inputstr == "help":
            print("[Console] Commands:\n[Console] premium_manager\n")

        elif inputstr == "premium_manager":
            premium_manager.ask()

        else:
            print("[Console] Unknown command!")
