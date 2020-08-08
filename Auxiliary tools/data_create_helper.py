# -*- coding: utf-8 -*-

import psycopg2
import random
import csv


def read_csv():
    csv_path = "/home/dezhum/Desktop/data_bkp.csv"
    lst = []
    with open(csv_path, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            res = [int(item) for item in row]
            lst.append(res)

    return lst

def line_creator(tik):
    zero, one, two = 70, 26, 4
    if  499 > tik >= 250:
        zero, one, two = 65, 27, 8
    if 749 > tik >= 500:
        zero, one, two = 65, 25, 10
    if tik >= 750:
        zero, one, two = 60, 30, 10

    print("Вероятности выпадения чисел >>> ", end='')
    print((zero, one, two))
    line = random.choices([0, 1, 2], k=22, weights=[zero, one, two])

    if line not in buffer:
        return line
    else:
        line_creator(tik)

def initialize_table():
    try:
        cursor.execute(""" CREATE TABLE IF NOT EXISTS train_data (
        {0});""".format(columns))
        print("Таблица train_data успешно создана")
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: " + str(error))

def insert_data(coeffs):
    str(coeffs).replace('[', '').replace(']', '')
    coefficients_str = str(coeffs).replace('[', '').replace(']', '')
    try:
        cursor.execute('''INSERT INTO {0}
                                      VALUES ({1});'''.format("train_data", coefficients_str))
        conn.commit()
        print("Данные добавлены в базу данных")
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: " + str(error))


if __name__ == "__main__":
    directin = "/home/dezhum/WorkSpace/ВКР/parser/mess/"
    conn = psycopg2.connect(dbname='', user='', host='localhost')  # Insert actual data
    cursor = conn.cursor()

    columns = """atr_1 INTEGER, atr_2 INTEGER, atr_3 INTEGER, atr_4 INTEGER, atr_5 INTEGER,
            atr_6 INTEGER, atr_7 INTEGER, atr_8 INTEGER, atr_9 INTEGER, atr_10 INTEGER, atr_11 INTEGER,
            atr_12 INTEGER, atr_13 INTEGER, atr_14 INTEGER, atr_15 INTEGER, atr_16 INTEGER, atr_17 INTEGER,
            atr_18 INTEGER, atr_19 INTEGER, atr_20 INTEGER, atr_21 INTEGER, atr_22 INTEGER, opinion INTEGER"""

    # initialize_table()

    buffer = read_csv()
    for i in range(len(buffer) + 1, 1009):
        print("Итерация: " + str(i))
        true_line = line_creator(i)
        buffer.append(true_line)

        for j in range(22):
            print("atr_" + str(j + 1), end=" | ")
        print()
        for z in range(22):
            if z <= 8:
                if true_line[z] == 0:
                    print("   ", end='   | ')
                else:
                    print("  " + str(true_line[z]), end='   | ')
            else:
                if true_line[z] == 0:
                    print("   ", end='    | ')
                else:
                    print("  " + str(true_line[z]), end='    | ')

        opinion = int(input("\nЭкспертная оценка >>> "))
        true_line.append(opinion)
        insert_data(true_line)
