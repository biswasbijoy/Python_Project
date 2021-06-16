#Python Project. Beginner level. Level 1
import random
import copy

mystory = ("Once upon a time there was an old {} pig who had {} little" +
" pigs and not enough food to feed them. So when {} {} old enough," +
" {} sent {} out into the world to seek their fortune.")

dictionary = {
    'noun' : ['father', 'mother', 'guardian'],
    'verb' :['was', 'were'],
    'pronoun' :['they', 'them', 'their', 'he', 'she',],
    'material_noun' :['one', 'two', 'three', 'four']
}

def fillup (type, dict) :
    words = dict[type]
    count = len(words) - 1
    index = random.randint(0, count)
    return dict[type].pop(index)

def ready() :
    dict = copy.deepcopy(dictionary)
    return mystory.format (
        fillup('noun', dict),
        fillup('material_noun', dict),
        fillup('pronoun', dict),
        fillup('verb', dict),
        fillup('pronoun', dict),
        fillup('pronoun', dict)
    )

print("Style 1: ")
print(ready())
print()
print("Style 2: ")
print(ready())