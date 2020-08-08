# -*- coding: utf-8 -*-
from lxml import etree
import psycopg2
import time
import os


def parseXML(xmlFile):
    coefficients = []
    with open(xmlFile) as file:
        xml = file.read().encode('utf-8')
        root = etree.fromstring(xml)
        for elem in root:
            if elem.tag == "Объект":
                for i in elem.items():
                    if i[0] == "Идентификатор_объекта":
                        coefficients.append(i[1])
            else:
                for i in elem.values():
                    coefficients.append(int(i))

    return coefficients

def initialize_table():
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS messages ({0});""".format(columns))
        conn.commit()
        print("Таблица messages успешно создана")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: " + str(error))

def insert_data():
    coefficients_str = str(line).replace('[', '').replace(']', '')
    try:
        cursor.execute('''INSERT INTO {0}
                                      VALUES ({1});'''.format("messages", coefficients_str))
        conn.commit()
        print("Данные добавлены в базу данных")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: " + str(error))

if __name__ == "__main__":
    directin = "/home/dezhum/WorkSpace/ВКР/parser/messages/"
    conn = psycopg2.connect(dbname='message_store', user='postgres', host='localhost')  # Insert actual data
    cursor = conn.cursor()
    columns = """object_id TEXT, file_name TEXT, atr_1 INTEGER, atr_2 INTEGER, atr_3 INTEGER, atr_4 INTEGER, atr_5 INTEGER,
        atr_6 INTEGER, atr_7 INTEGER, atr_8 INTEGER, atr_9 INTEGER, atr_10 INTEGER, atr_11 INTEGER,
        atr_12 INTEGER, atr_13 INTEGER, atr_14 INTEGER, atr_15 INTEGER, atr_16 INTEGER, atr_17 INTEGER,
        atr_18 INTEGER, atr_19 INTEGER, atr_20 INTEGER, atr_21 INTEGER, atr_22 INTEGER"""

    initialize_table()

    while True:
        files = os.listdir(directin)
        if not files:
            sec = 60
            print("Нет сообщений для обработки! Интервал ожидания: " + str(sec) + " секунд")
            time.sleep(sec)
        else:
            for file_name in files:
                print("############## " + file_name + " ##############")

                line = parseXML(directin + file_name)
                line.insert(1, file_name)

                insert_data()
                os.system("mv ./messages/{0} ./saved_messages/".format(file_name))
                print("Сообщение " + file_name + " обработано и сохранено\n")
