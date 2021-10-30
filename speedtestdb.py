import os
import json
from types import SimpleNamespace
import subprocess
import time
import sqlite3

def create_connection(db_file):
    """ 
    Create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def create_test(conn, test):
    """
    Create a new test
    :param conn:
    :param test:
    :return:
    """

    sql = ''' INSERT INTO tests('timestamp','ping','download','upload')
              VALUES(datetime('now', 'localtime'),?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, test)
    return cur.lastrowid

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    print(path)
    database = rf"{path}/speedtest.db"

    response = subprocess.Popen('/usr/bin/speedtest -f json', shell=True, stdout=subprocess.PIPE).stdout.read()
    response = response.decode('UTF-8')
    print(response)

    # regex = 'Ping:\s(?P<ping>\d*\.?\d*).*\s^Download:\s(?P<download>\d*\.?\d*).*\s^Upload:\s(?P<upload>\d*\.?\d*)'
    # matches = re.search(regex, response, re.MULTILINE)
    
    # ping = matches.group("ping")
    # download = matches.group("download")
    # upload = matches.group("upload")

    data = json.loads(response, object_hook=lambda d: SimpleNamespace(**d))
    ping = data.ping.latency
    download = data.download.bandwidth
    upload = data.upload.bandwidth
    print(f"Ping: {ping}")
    print(f"Download: {download}")
    print(f"Upload: {upload}")

    # create a database connection
    conn = create_connection(database)
    with conn:
        test = (ping, download, upload)
        # insert test
        create_test(conn, test)

    conn.close()


if __name__ == '__main__':
    main()

