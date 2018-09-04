#get number of weeks
weeks = 12

#get number of lectures
lectures = 10

#get number of words per second
word = 2.5
hour_to_second = 3600
calories_per_word = 0.008

#do computation
calories = weeks * lectures * word * hour_to_second * calories_per_word

#present results
print (calories)