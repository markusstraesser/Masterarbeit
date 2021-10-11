'''Writes serial data to CSV and prints live data to console'''

import ArduinoSerial

if __name__ == "__main__":
    # PORT = ArduinoSerial.select_COM_Port()
    PORT = "COM4"
    SER = ArduinoSerial.createSerial(PORT)
    FILEPATH = "Sensordata/RawData.csv"
    while True:
        data = ArduinoSerial.readSerial(SER)
        if data:
            ArduinoSerial.writeSerialToCSV(FILEPATH, data)
            print(data[0].strftime("%d.%m.%Y %H:%M:%S.%f")[:-2],': ',data[1], end="\r")