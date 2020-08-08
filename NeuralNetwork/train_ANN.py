from keras.models import Sequential, save_model, load_model                                                             ## Sequential - группировка слоев
from sklearn.model_selection import train_test_split                                                                    ## Разделение данных на тренировочный и тестовый набор
from keras.optimizers import SGD                                                                                        ## Стохастический градиентный спуск
import matplotlib.pyplot as plt                                                                                         ## Рисовалка графиков
from keras.layers import Dense                                                                                          ## Полносвязный слой
import numpy as np
import csv

                                                                                                                        ## Функция чтения csv файлов
def csv_reader(tik):
    csv_paths = ["data.csv", "target.csv"]
    lst = []
    with open(csv_paths[tik], mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if tik == 0:
                res = [int(item) for item in row]
                lst.append(res)
            else:
                lst.append(int(row[0]))

    return lst

                                                                                                                        # Преобразование данных в вектора
data = np.array(csv_reader(0))
target = np.array(csv_reader(1))
X = data
num_labels = len(np.unique(target))
Y = np.eye(num_labels)[target]
                                                                                                                        # Настройка стохастического градиентного спуска
sgd = SGD(learning_rate=0.01, decay=1e-6, momentum = 0.9, nesterov = True)
                                                                                                                       # Разбиение данных на тренировочный и тестовый наборы
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

divide = 150                                                                                                            # Число разделений для каждой эпохи обучения
x_val = x_train[:divide]
partial_x_train = x_train[divide:]
y_val = y_train[:divide]
partial_y_train = y_train[divide:]

e = 75                                                                                                                  # Количество эпох обучения
model = Sequential()                                                                                                    # Объявление нейросетевой модели
model.add(Dense(500, input_dim=22, activation='relu'))                                                                  # Добавление в модель первого скрытого слоя из 500 нейронов, указание о том, что входной слой состоит из 22 нейронов
model.add(Dense(5, activation='sigmoid'))                                                                               # Добавление выходного слоя с 5 нейронами
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])                                          # Компилирование модели с указанием функции потерь и метода обучения
                                                                                                                        # Обучение модели
history = model.fit(partial_x_train, partial_y_train, validation_data=(x_val, y_val), epochs=e)

loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, e + 1)
plt.plot(epochs, loss, 'bo', label='Training_loss')
plt.plot(epochs, val_loss, 'b', label='Validation_loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

plt.clf()
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
plt.plot(epochs, acc, 'bo', label='Training_accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation_accuracy')
plt.legend()
plt.show()

## Results
result = model.evaluate(x_test, y_test)
print(result)


# # ## Save the model
# filepath = './saved_model'
# save_model(model, filepath)
#
# # ## Load The model
# model = load_model(filepath, compile=True)
#
# test_1 = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0]] #0
# test_2 = [[2], [1], [1], [1], [1], [2], [1], [0], [0], [0], [0], [0], [1], [0], [0], [0], [2], [1], [0], [0], [0], [0]] #2
# test_3 = [[0], [0], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1], [0], [0], [0], [0], [0], [0], [1], [1], [1], [1]] #2
# test_4 = [[0], [0], [0], [0], [0], [0], [0], [0], [2], [0], [0], [0], [0], [1], [1], [1], [0], [0], [0], [0], [0], [0]] #1
# test_5 = [[1], [0], [1], [1], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [0], [1], [0], [0], [0], [0], [0]] #1
# test_6 = [[2], [0], [0], [0], [0], [0], [0], [0], [1], [2], [0], [0], [2], [2], [2], [1], [0], [2], [0], [0], [1], [2]] #3
# test_7 = [[2], [2], [1], [1], [2], [2], [2], [2], [0], [0], [0], [0], [2], [0], [0], [0], [2], [2], [0], [0], [0], [0]] #4
# test_8 = [[2], [1], [1], [1], [1], [2], [1], [1], [0], [0], [1], [0], [0], [1], [0], [0], [1], [0], [0], [1], [0], [1]] #2
#
# test_sample = np.array(test_6)
# test_sample = test_sample.transpose()
#
# predictions = model.predict(test_sample)
# print(predictions)
#
# classes = np.argmax(predictions, axis = 1)
# print(classes)
