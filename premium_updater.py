if __name__ == '__main__':
    import datetime
    import time
    import requests
    import json
    import asyncio
    import premium_manager
    from datetime import date
    from dateutil.relativedelta import relativedelta  # python-dateutil

    serverid = "673372073242132480"
    auth = "8uU8ARbSqFYfnidjbenbFcQwfugoZeh6VhSZAZaxXWcATqzgiellDxzX62mITM"

    premium = {
        "5GNCNEzUu5": "default",
        "3WfjCRyefW": "pro",
        "OjdRMTKUzY": "ultra",
        "yCMJ9VHQHb": "default"
    }

    print("premium_updater.py started.")

    while True:
        time.sleep(5)
        new = requests.get("https://donatebot.io/api/v1/donations/{}/new".format(serverid),
                           headers={'Authorization': auth})
        res = json.loads(new.text)["donations"]
        if new:
            already_there = False

            for dictionary in res:
                with open("premium.users", "r") as f:
                    for line in f.readlines():
                        if dictionary["buyer_id"] in line.split("#")[0]:
                            if dictionary["txn_id"] in line.split("#")[-2]:
                                already_there = True
                            else:
                                asyncio.run(premium_manager.add_month(dictionary["buyer_id"]))
                                print("Added a momth to a premium user.")
                                already_there = True

                month = str(date.today() + relativedelta(months=+1)).replace("-", "/")

                if not already_there:
                    asyncio.run(premium_manager.add(dictionary["buyer_id"], dictionary["buyer_email"], month,
                                                    premium[dictionary["product_id"]], dictionary["txn_id"]))
                    print("Added a premium user.")

                requests.post("https://donatebot.io/api/v1/donations/{}/{}/mark".format(serverid, dictionary["txn_id"]),
                              headers={'Authorization': auth})

        else:
            print('Not Found.')

        time.sleep(5)
        now = str(datetime.datetime.now()).split(".")[0][:-9]
        now = datetime.datetime.strptime(now, '%Y-%m-%d')

        with open("premium.users", "r") as users:
            alllines = users.readlines()
            done = ""
            for line in alllines:
                remove_date = line.split("#")[-1]
                if len(line.split("#")) == 4:
                    try:
                        tdelta = datetime.datetime.strptime(remove_date.strip("\n").strip(" "), '%Y/%m/%d') - now

                        if str(tdelta)[0] == "-":
                            alllines.remove(line)
                            with open("premium.users", "w") as users1:
                                for line1 in alllines:
                                    if not line1 == "":
                                        done += line1

                                with open("premium.users", "w") as f:
                                    f.write(done)

                            print("removed a user from premium")

                    except ValueError:
                        continue
