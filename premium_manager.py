import datetime
import calendar
import asyncio


async def add(current_id, name, rmdate, current_type, txn_id):
    open("premium.users", "a").write("\n" + current_id + " # " + name + " # " + current_type + " # " + txn_id + " # " + rmdate)


async def remove(current_id):
    with open("premium.users", "r") as f:
        f = f.readlines()
        done = ""
        for line in f:
            if not current_id == line.split("#")[0].strip("#").strip(" "):
                done += line

    with open("premium.users", "w") as f:
        f.write(done)


async def add_month(current_id):
    with open("premium.users", "r") as f:
        alllines = f.readlines()
        done = ""
        for line in alllines:
            if current_id == line.split("#")[0].strip("#").strip(" "):
                try:
                    newline = ""
                    remove_date = line.split("#")[-1]
                    remove_date = datetime.datetime.strptime(remove_date.strip("\n").strip(" "), '%Y/%m/%d')
                    if len(line.split("#")) == 5:
                        days_in_month = calendar.monthrange(remove_date.year, remove_date.month)[1]
                        newline += line.split("#")[0].strip("#") + "#" + line.split("#")[1].strip("#") + "#" + line.split("#")[2].strip("#") + "# " + str(remove_date + datetime.timedelta(days=days_in_month))[:-9].replace("-", "/") + "\n"
                        done += newline
                    else:
                        done += line
                except ValueError as e:
                    print(e)
                    done += line
            else:
                done += line

    with open("premium.users", "w") as f:
        f.write(done)


def ask():
    current_type = "default"
    action = input("Action (add/addmonth/remove) : \n")
    current_id = input("ID : \n")
    name = ""
    rmdate = ""
    txn_id = ""
    if action == "add":
        name = input("Name : \n")
        current_type = input("premium type (default/pro/ultra) : \n")
        txn_id = input("transaction id : \n")

    if action == "add":
        rmdate = input("Time when removed (YYYY/MM/DD) : \n")

    if not current_type == "default" and not current_type == "pro" and not current_type == "ultra":
        print("\nError! That type does not exist!\n")

    elif action == "add":
        asyncio.run(add(current_id, name, rmdate, current_type, txn_id))
        print("\nSucessfully added!\n")
    elif action == "addmonth":
        asyncio.run(add_month(current_id))
        print("\nSucessfully added a month!\n")
    elif action == "remove":
        asyncio.run(remove(current_id))
        print("\nSucessfully removed!\n")
    else:
        print("\nError! That action does not exist!\n")
