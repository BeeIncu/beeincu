import sys
from util import *
import settings
import time

"""import Adafruit_DHT
import RPi.GPIO as GPIO"""

"""class Controller:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

    def heat(self, state):
        if state:
            GPIO.output(21, True)
        else:
            GPIO.output(21, False)

    def humidity(self, state):
        if state:
            GPIO.output(20, True)
        else:
            GPIO.output(20, False)

class Sensor:
    
    def get_data(self):
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        return [humidity, temperature]

"""


class Color:
    RED = "\033[31m"
    GREEN = "\033[32m"
    ENDC = "\033[0m"


current_version = "0.0.1"

color = Color()
"""controller = Controller()
sensor = Sensor()"""

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (2, 7)


class Main:

    def main(self):
        if CURRENT_PYTHON > REQUIRED_PYTHON:
            print(color.RED + "Starting BeeIncu version " + color.GREEN + current_version + color.ENDC)
            mysqldb = MySQL(host=settings.MYSQL_HOST,
                            port=settings.MYSQL_PORT,
                            user=settings.MYSQL_USER,
                            password=settings.MYSQL_PASSWORD,
                            database=settings.MYSQL_DATABASE,
                            debug=True)

            mysqldb.update("CREATE TABLE IF NOT EXISTS beeincu_current (id INTEGER AUTO_INCREMENT, "
                           "temp FLOAT, "
                           "humidity FLOAT, "
                           "c_time DATE)")
            input()
        else:
            print(color.RED + "Unsupported Python version! \nPlease update to atleast version 2.7.16!" + color.ENDC)
            exit()

    if __name__ == "__main__":
        main(None)
