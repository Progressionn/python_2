import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from collections import Counter
import os
os.chdir(r'C:\Users\Ivan\PycharmProjects\pythonProject\Для собственного развития\project_flasc')
#  Подключаемся к базе данных.
connection = sqlite3.connect('gram.db')
cursor = connection.cursor()
f = cursor.execute('SELECT * FROM gram')
g = cursor.fetchall()
print(len(g), g)
#  Выбираем с помощью курсора колонки yatь, big_yus, little_yus и o_sound и считаем количество мужчин и женщин в соответствии с данными этих колонок.
m = cursor.execute("""SELECT yatь, count(gender) FROM gram WHERE GENDER = 'мужской' GROUP BY yatь"""
                   )
r = cursor.fetchall()
m1 = cursor.execute("""SELECT yatь, count(gender) FROM gram  WHERE GENDER = 'женский' GROUP BY yatь"""
                 )
r1 = cursor.fetchall()
m2 = cursor.execute("""SELECT big_yus, count(gender) FROM gram  WHERE GENDER = 'мужской' GROUP BY big_yus"""
                 )
r2 = cursor.fetchall()
m3 = cursor.execute("""SELECT big_yus, count(gender) FROM gram  WHERE GENDER = 'женский' GROUP BY big_yus"""
                 )
r3 = cursor.fetchall()
m4 = cursor.execute("""SELECT little_yus, count(gender) FROM gram  WHERE GENDER = 'мужской' GROUP BY little_yus"""
                 )
r4 = cursor.fetchall()
m5 = cursor.execute("""SELECT little_yus, count(gender) FROM gram  WHERE GENDER = 'женский' GROUP BY little_yus"""
                 )
r5 = cursor.fetchall()
m6 = cursor.execute("""SELECT o_sound, count(gender) FROM gram  WHERE GENDER = 'мужской' GROUP BY o_sound"""
                 )
r6 = cursor.fetchall()
m7 = cursor.execute("""SELECT o_sound, count(gender) FROM gram  WHERE GENDER = 'женский' GROUP BY o_sound"""
                 )
r7 = cursor.fetchall()
m8 = cursor.execute("""SELECT yatь, count(age) FROM gram  GROUP BY yatь"""
                 )
r8 = cursor.fetchall()
m9 = cursor.execute("""SELECT big_yus, count(age) FROM gram  GROUP BY big_yus"""
                 )
r9 = cursor.fetchall()
m10 = cursor.execute("""SELECT little_yus, count(age) FROM gram GROUP BY little_yus"""
                 )
r10 = cursor.fetchall()
m11 = cursor.execute("""SELECT o_sound, count(age) FROM gram  GROUP BY o_sound"""
                 )
r11 = cursor.fetchall()
#  Преобразуем все полученные данные в словари.
f1 = dict(r)
f2 = dict(r1)
f3 = dict(r2)
f4 = dict(r3)
f5 = dict(r4)
f6 = dict(r5)
f7 = dict(r6)
f8 = dict(r7)
#  Создаем функцию img_1, которая будет отвечать за вывод графиков на страницу статистики и которую мы импортируем в главный flasc_2.py файл.
def img_1():
    #  Указываем, что мы хотим создать графики в папке static, и для на основе данных словарей строим 8 графиков.
    os.chdir(r'C:\Users\Ivan\PycharmProjects\pythonProject\Для собственного развития\project_flasc\static')
    plt.bar(list(f1.keys()), list(f1.values()), width=.5, color='b')
    plt.savefig("men.jpg")
    plt.close()
    plt.bar(list(f2.keys()), list(f2.values()), width=.5, color='r')
    plt.savefig("women.jpg")
    plt.close()
    plt.bar(list(f3.keys()), list(f3.values()), width=.5, color='g')
    plt.savefig("men_1.jpg")
    plt.close()
    plt.bar(list(f4.keys()), list(f4.values()), width=.5, color='y')
    plt.savefig("women_1.jpg")
    plt.close()
    plt.bar(list(f5.keys()), list(f5.values()), width=.5, color='b')
    plt.savefig("men_2.jpg")
    plt.close()
    plt.bar(list(f6.keys()), list(f6.values()), width=.5, color='r')
    plt.savefig("women_2.jpg")
    plt.close()
    plt.bar(list(f7.keys()), list(f7.values()), width=.5, color='g')
    plt.savefig("men_3.jpg")
    plt.close()
    plt.bar(list(f8.keys()), list(f8.values()), width=.5, color='y')
    plt.savefig("women_3.jpg")
    plt.close()
    #  Прописываем эту строчку, чтобы избежать Runtime Error.
    plt.switch_backend('agg')
    os.chdir(r'C:\Users\Ivan\PycharmProjects\pythonProject\Для собственного развития\project_flasc')
    #  Возвращаем, что наше изображение сохранено.
    return 'Сохранено'
print(img_1())
#  Строим датафрейм из данных полученных в sql-запросе.
df = pd.DataFrame(g)
#  Создаем словари, с помощью которых будем строить графики.
v = dict(Counter(df[4]))
c = dict(Counter(df[5]))
x = dict(Counter(df[6]))
d = dict(Counter(df[7]))
#  Создаем функцию img, которая будет отвечать за вывод графиков после прохождения анкеты и которую мы импортируем в главный flasc_2.py файл.
def img():
            #  Указываем, что мы хотим создать графики в папке static, и для на основе данных словарей строим 4 графика.
            os.chdir(r'C:\Users\Ivan\PycharmProjects\pythonProject\Для собственного развития\project_flasc\static')
            plt.bar(list(v.keys()), list(v.values()), width=.5, color='b')
            plt.savefig("109.jpg")
            plt.close()
            plt.bar(list(c.keys()), list(c.values()), width=.5, color='r')
            plt.savefig("110.jpg")
            plt.close()
            plt.bar(list(x.keys()), list(x.values()), width=.5, color='g')
            plt.savefig("111.jpg")
            plt.close()
            plt.bar(list(d.keys()), list(d.values()), width=.5, color='y')
            plt.savefig("112.jpg")
            plt.close()
            #  Прописываем эту строчку, чтобы избежать Runtime Error.
            plt.switch_backend('agg')
            os.chdir(r'C:\Users\Ivan\PycharmProjects\pythonProject\Для собственного развития\project_flasc')
            #  Возвращаем, что наше изображение сохранено.
            return 'Сохранено'
print(img())



