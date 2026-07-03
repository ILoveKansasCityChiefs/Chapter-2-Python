# Personal Project of Chapter 2 of Python Crash Course by Eric Matthes
nfl_qbs = ['PatrickM', 'LamarJ', 'JoshA', 'JoeB', 'ShedeurS']
print(nfl_qbs)
# Replaced Patrick with Jared Goff to list of NFL QuarterBacks
nfl_qbs[0] = 'JaredG'
print(nfl_qbs)
# Adding Mahomes Back to List
nfl_qbs.append('PatrickM')
print(nfl_qbs)
# Inserting Jalen Hurts to List
nfl_qbs.insert(5, 'JalenH')
print(nfl_qbs)
# Removing the trashest player on list
del nfl_qbs[0]
print(nfl_qbs)
# Popping a random NFL QB from List
popped_QB = nfl_qbs.pop(2)
print(nfl_qbs)
print(popped_QB)
# Removing a random QB
nfl_qbs.remove('JoshA')
print(nfl_qbs)
# sorting list in alphabetical order
nfl_qbs.sort()
print(nfl_qbs)
# Reverse-alphabetical order
nfl_qbs.sort(reverse=True)
print(nfl_qbs)
# Temporary sort of list
print(sorted(nfl_qbs))
# Reverse order
nfl_qbs.reverse()
print(nfl_qbs)
# States NUmber of NFL Quarterbacks within the List
number = len(nfl_qbs)
print(number)
