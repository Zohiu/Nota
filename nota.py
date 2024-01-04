#!/usr/bin/env python
version = "4.1"

if __name__ == '__main__':
    print("        _____________________________________________________ \n"
          "       /       ***************************************       \ \n"
          "      /        *  |\   |  |----|  ---|---    /-\     *        \ \n"
          "     /         *  | \  |  |    |     |      /   \    *         \ \n"
          "    /          *  |  \ |  |    |     |     /-----\   *          \ \n"
          "   /           *  |   \|  |----|     |    /       \  *           \ \n"
          "  /            ***************************************            \ \n"
          " /-----------------------------------------------------------------\ \n"
          " |              Version : "+version+"  |           REWRITE!!               | \n"
          " |-----------------------------------------------------------------| \n"
          " | This is the Nota bot it notes the notes. This is the best Bot!! | \n"
          " \-----------------------------------------------------------------/ \n"
          "  \                         code by Fguzy                         / \n"
          "   --------------------------------------------------------------- \n"
          )

    import subprocess
    import os
    import time    

    if os.name == 'nt':
        ver = "python"
    else:
        ver = "python3"

    time.sleep(10)
    print("bot.py is starting...")
    bot = subprocess.Popen([ver, 'bot.py'])
    #print("premium_updater.py is starting...")
    #premium_updater = subprocess.Popen([ver, 'premium_updater.py'])
    print("console.py is starting...")
    console = subprocess.Popen([ver, 'console.py'])

    while True:
        continue
