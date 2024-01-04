# Nalxe data module - by Fguzyk
# When adding something to a table, the only argument should be
# a dictionary, where the first key is the name of the table row.

from sqlcipher3 import connect, OperationalError
from json import loads, dumps
import shutil
import os

conn = connect("data.db", )


async def create_table(user, table):
    cursor = conn.cursor()
    try:
        cursor.execute(f'CREATE TABLE "{user}_{table}" ("key" text, "value" text);')
        conn.commit()
        return True
    except OperationalError as e:
        return e


async def delete_table(user, table):
    cursor = conn.cursor()
    try:
        cursor.execute(f'DROP TABLE "{user}_{table}";')
        conn.commit()
        return True
    except OperationalError as e:
        return e


async def set_for_table(user, table, value):
    cursor = conn.cursor()
    try:
        await create_table(user, table)
        cursor.execute(f'REPLACE INTO "{user}_{table}" (key, value) VALUES (?, ?)', (str(list(value.keys())[0]), dumps(value)))
        conn.commit()
        return True
    except Exception as e:
        return e


async def get_from_table(user, table):
    cursor = conn.cursor()
    try:
        cursor.execute(f'SELECT * FROM "{user}_{table}"')
        fetchall = cursor.fetchall()
        output = []
        for row in fetchall:
            output.append(loads(row[1]))
        return output
    except Exception as e:
        output = e

if __name__ == '__main__':
    user = "user"
    filename = "file1"
    filecontent = "Testing lol"
    attachments = ["zmozmo.mp3", "mexico.png"]
    
    if not os.path.exists(f'__temp__/{user}'):
        os.mkdir(f'__temp__/{user}')
    
    # --- Saving ---
    
    attachmentswithblob = []
    for i in attachments:
        with open(f"__temp__/{user}/{i}", 'rb') as file:
            binary = file.read()
        attachmentswithblob.append({"name": i.split(".")[0], "type": i.split(".")[-1], "data": binary.hex()})
    
    print("Saving")
    set_for_table(user, "files", {"Will this bot be able to manage files?": "It will 11", "attachments": attachmentswithblob})
    set_for_table(user, "files", {"file2": "It will", "attachments": None})
    
    if os.path.exists(f'__temp__/{user}'):
        shutil.rmtree(f'__temp__/{user}')
    
    # --- Now reading ---
    
    print("Reading...")
    print("Info:", get_from_table(user, "info"))
    files = get_from_table(user, "files")

    if not os.path.exists(f'__temp__/{user}'):
        os.mkdir(f'__temp__/{user}')
    
    print("Files")
    all_attachments = []
    for i in files:
        if i["attachments"] is not None:
            print(list(i.keys())[0])
            for file in i["attachments"]:
                with open(f'__temp__/{user}/{file["name"]}.{file["type"]}', 'wb') as write_file:
                    print("um?")
                    write_file.write(bytes.fromhex(file["data"]))
                    all_attachments.append(f'__temp__/{user}/{file["name"]}.{file["type"]}')

    #if os.path.exists(f'__temp__/{user}'):
    #    shutil.rmtree(f'__temp__/{user}')
    
# TODO: https://www.twilio.com/blog/intro-multimedia-file-upload-python-sqlite3-database
# TODO: AKA, Make another database for files that holds the attachment files.
# TODO: In the files database add the names of all attachment files from the attachments database.
# TODO: So its like a path and you can upload files again
