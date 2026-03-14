# Part two of Dictionaries
python = {'John' :35, 'Eric' :36, 'Michael' :35, 'Terry' :38, 'Graham' :37, 'Cid' :35}
holy_grail = {'Authur' :40, 'Zaidak' :35, 'Sham' :39, 'Tracy' :40, 'Natsu' :17}

print('Authur' in holy_grail)

people = {}
people1 = {}
people2 = {}

#update method
people.update(python)
people.update(holy_grail)
print(people)

#method 2 comprehension
for groups in (python,holy_grail) :  people1.update(groups)
print(sorted(people.items()))

#method 3 unpacking 3.5 later
people2 = {**python,**holy_grail}
print(sorted(people2.items()))
print ('The sum of the ages:    ', sum(people.values()))
# Part one of Dictionaries
#movie = {
#         'title' : 'Life of Brian'
#         'year' : 1987,
 #        'cast' :  [ 'John' , 'Eric' , 'Michael' , 'George', 'Terry']
#}
#movie.update({ 'title'  : 'The Holy Rail' ,'year':1975, 'cast' :[ 'John','Cid','Shadow' ]})
#movie['budget'] = 250000
# to delete
# del movie['year']
 # OR
 #year = movie.pop('year')

#print(movie)
