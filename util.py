import mysql.connector


def in_range(min, max, value):
    return min <= value <= max


class MySQL:

    def __init__(self, host, port, user, password, database, debug):
        self.debug = debug
        print("Trying mysql connection. This may take a while!")
        try:
            self.db = mysql.connector.connect(host=host, port=port, user=user, password=password, database=database)
        except mysql.connector.Error as err:
            print("Something went wrong connection to database: {}".format(err))

    def update(self, sql):
        if self.debug:
            print("Trying to update db. This may take some time (<2 seconds)")
        cursor = self.db.cursor()
        cursor.execute(sql)
        cursor.close()

    def get(self, sql):
        if self.debug:
            print("Trying to get data from db. This may take some time(<2 seconds)")
        cursor = self.db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data
