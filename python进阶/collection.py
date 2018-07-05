import collections as cs
import json

tree = lambda: cs.defaultdict(tree)

some_dict = tree()
some_dict['colours']['favourite']['hello'] = "yellow"
tree = lambda : cs.defaultdict(tree)
other_dict=tree() #cs.defaultdict(lambda :other_dict)
other_dict['1']['2']='test'
other_dict['help']= '0000'

#print(some_dict['colours']['favourite'],type(some_dict['colours']['favourite']['hello']))
print(other_dict,'-'*4,some_dict)
print(json.dumps(other_dict,indent=4))
