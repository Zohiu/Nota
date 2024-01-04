version = "4.3.4"

if __name__ == '__main__':

    print("                                                                                  ")
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
    print("                                     Version " + version + "                          ")
    print("                                                                                  ")

    import subprocess
    import time
    import os

    if os.name == 'nt':
        ver = "python"
    else:
        ver = "python3"

    print("[Debug] bot.py is starting...")
    bot = subprocess.Popen([ver, 'bot.py'])
    # print("[Debug] premium_updater.py is starting...")
    # premium_updater = subprocess.Popen([ver, 'premium_updater.py'])
    # print("[Debug] console.py is starting...")
    # console = subprocess.Popen([ver, 'console.py'])

    while True:
        pass
