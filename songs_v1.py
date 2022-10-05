# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
output=my_favorite_songs.split(', ')                            #split string to the list         
length=len(output)                                              #count the  list cells 
print(output[0],output[length-1],output[1],output[length-2])    #output to console by the changed order
#----------------my comments------------------------
#as it didn't prompted, how to output the tokens, i out it in line 
# with one space only and without any separators
# i think, need more strictly to define task
#====================================================

# Выведите на консоль с помощью индексации строки, последовательно:
#  первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


######################################################
# Токенизация и анализ количества слов

# Импорт функций из пакетов pandas и scikit-learn
# Для пакетного менеджера conda:
#     conda install pandas
#     conda install scikit-learn
from pandas import DataFrame 
from sklearn.feature_extraction.text import CountVectorizer

# Коллекция из двух плейлистов с песнями
my_collection = [
    'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation', 
    'World in My Eyes, Firestarter, Personal Jesus, Still Alive, New Soul'
    ]

# Таблица из номеров плейлистов и строки песен
df = DataFrame({'collection': ['playlist_1', 'playlist_2'], 'names':my_collection})

# CountVectorizer создает вектор токенов
# параметр stop_words для исключения ненужных слов 
cv = CountVectorizer(stop_words=['a', 'an', 'the', 'in']) 
cv_matrix = cv.fit_transform(df['names'])  # преобразуем в набор данных

# Создаем таблицу, преобразуя cv_matrix в массив
df_dtm = DataFrame(cv_matrix.toarray(), index=df['collection'].values, columns=cv.get_feature_names_out())

print(df_dtm.transpose())  # вывод и транспонирование

#### Подробее про токенизацию по ссылке
#### https://habr.com/ru/post/504744/
