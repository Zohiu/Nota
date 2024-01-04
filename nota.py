def startBot():
    notabot = main.Bot()

    commands = []

    for root, dirs, files in os.walk("Commands"):
        for file in files:
            # append the file name to the list
            if file.split(".")[1] == "py" and file.split(".")[0] != "__init__":
                root = root.replace("\\", ".").replace("/", ".")
                commands.append(root + "." + file.split(".")[0])

    for command in commands:
        globals()[command] = importlib.import_module(command)
        globals()[command].initialize(notabot)

    print(Colors.BLUE + "[Debug] Everything has been loaded into memory." + Colors.RESET)
    notabot.BOT.run(notabot.TOKEN)


if __name__ == '__main__':
    version = "5.0-DEV_SNAPSHOT.1"

    from Modules.colors import Colors

    print(Colors.GREEN)
    print("NNNNNNNN        NNNNNNNN                          tttt                            ")
    print("N:::::::N       N::::::N                       ttt:::t                            ")
    print("N::::::::N      N::::::N                       t:::::t                            ")
    print("N:::::::::N     N::::::N                       t:::::t                            ")
    print("N::::::::::N    N::::::N   ooooooooooo   ttttttt:::::ttttttt      aaaaaaaaaaaaa   ")
    print("N:::::::::::N   N::::::N oo:::::::::::oo t:::::::::::::::::t      a::::::::::::a  ")
    print("N:::::::N::::N  N::::::No:::::::::::::::ot:::::::::::::::::t      aaaaaaaaa:::::a ")
    print("N::::::N N::::N N::::::No:::::ooooo:::::otttttt:::::::tttttt               a::::a ")
    print("N::::::N  N::::N:::::::No::::o     o::::o      t:::::t              aaaaaaa:::::a ")
    print("N::::::N   N:::::::::::No::::o     o::::o      t:::::t            aa::::::::::::a ")
    print("N::::::N    N::::::::::No::::o     o::::o      t:::::t           a::::aaaa::::::a ")
    print("N::::::N     N:::::::::No::::o     o::::o      t:::::t    tttttta::::a    a:::::a ")
    print("N::::::N      N::::::::No:::::ooooo:::::o      t::::::tttt:::::ta::::a    a:::::a ")
    print("N::::::N       N:::::::No:::::::::::::::o      tt::::::::::::::ta:::::aaaa::::::a ")
    print("N::::::N        N::::::N oo:::::::::::oo         tt:::::::::::tt a::::::::::aa:::a")
    print("NNNNNNNN         NNNNNNN   ooooooooooo             ttttttttttt    aaaaaaaaaa  aaaa")
    print("                                                                                  ")
    print(Colors.BLUE + "[Debug] Version: " + Colors.CYAN + version + Colors.RESET)
    print(Colors.RESET)

    print(Colors.BLUE + "[Debug] Importing packages required to start..." + Colors.RESET)
    import multiprocessing
    import importlib
    import os
    from Core import main
    print(Colors.BLUE + "[Debug] Starting the bot..." + Colors.RESET)

    bot = multiprocessing.Process(target=startBot)
    bot.start()

    if os.name == 'nt':
        ver = "python"
    else:
        ver = "python3"
