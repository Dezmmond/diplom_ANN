from keras.models import load_model
import psycopg2
import numpy as np


def get_data():
    cursor.execute('''SELECT * FROM messages;''')
    fetch = cursor.fetchall()
    return fetch

if __name__ == "__main__":
    conn = psycopg2.connect(dbname='message_store', user='postgres', host='localhost')  # Insert actual data
    cursor = conn.cursor()

    lst = []
    results = get_data()
    for line in results:
        lst.append([[i] for i in line])

    model = load_model('./saved_model', compile=True)

    for line in lst:
        test_sample = np.array(line[2:])
        test_sample = test_sample.transpose()

        predictions = model.predict(test_sample)

        predicted_class = np.argmax(predictions)
        print("Оценка ситуации на объекте {0}: {1}".format(line[0][0], str(predicted_class)))

        if predicted_class != 0:
            print("Сообщение: " + line[1][0] + "\n")
        else:
            print()

