from collections import defaultdict
import json
colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)
for name, colour in colours:
    favourite_colours[name].append(colour)

tree=lambda :defaultdict(tree)
anthor=tree()
anthor['world']['china']='fly'
print(favourite_colours,'\n',anthor)
print(favourite_colours.items())