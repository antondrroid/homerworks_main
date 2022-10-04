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
