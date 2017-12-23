from string import ascii_lowercase, printable
from os.path import isfile

def wordTwist(word, func, *args, **kwargs):
    complete = []
    for i in range(2):
      if i == 0:
        for x in func(word, *args, **kwargs):
          if not x in complete:
            complete.append(x)
      else:
        for x in func(word[::-1], *args, **kwargs):
          if not x[::-1] in complete:
            complete.append(x[::-1])


def force_yield(iter):
    '''
    force an iter to yield
    :param iter: iterable
      :type: list | tulpe | set | generator
    :yield: Object in iter
    '''
    assert type(iter) in [list, tuple, set, function]
    for x in iter:
      yield x


def loadRuleSet(fileLocation):
    '''
    Loads a file path of a rule file into memory easily
    :param fileLocation: File path to be read 
      :type: str


    :return: set of rules for the class Deform
      :type: dict
    '''
    rules = {}
    assert isfile(fileLocation)
    for x in open(fileLocation).read().split('\n'):
      if not len(x) == 0:
        data = x.split(':')
        if not len(data[0]) == 0 or not len(data[1]) == 0:
          rules[data[0]] = data[1]
    return rules


def remove_char(word, position):
    '''
      Removes an exact chatacter by position

    :param:  word: 
      :type: str
      Word to manipulate.

    :param:  position: 
      :type: int
      Position to remove

    :return: Manipulated word
      :type: str

    '''
    return ''.join(x for i, x in enumerate(word) if not i == position)


def flatten(x):
    '''
    Flattens irregular lists and removes dupiliciations, Example:
      eg: [1, 2, 1, 3, 1, 4, [4, 2, 1, 5, [6, [7]], 9,], 0] -> Changes to -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

    :param x: Irregular list
     :type: list/array 

    :return: immutable list of x
      :type: set

    '''
    r = []
    for p in x:
      r.extend(p)
    return set(r)

  
def countLetters(word):
    '''
    count the frequency of a letter

    :param word: string to count letter frequency of
     :type: str

    :return: dict with letters as keys and frequency as item, eg {'a':1, 'b':4}
     :type: dict

    '''
    data = {}
    complete = {}

    for x in printable:
      data[x] = 0

    for x in word:
      if x in data:
        data[x] += 1

    for x in data:
      if data[x] > 0:
        complete[x] = data[x]

    return complete

  
def walker(string):
    '''
    walk through the word and get a list of values on position,
    returns a list of letter and position     [(letter, position),...]


    :param string: count string, and walk position, and char
      :type: str

    :return: list of tuples with various letters and positions [('a', 0),('b', 1)...]
      :type: list

    '''
    return [(x, i) for i, x in enumerate(string)]

  
def makeDefaultRules():
    '''
    Make default Ruleset, returns a dict

    :return: Default ruleset
      :type: dict
    '''

    Default_Rules = {}
    __specials = [('s', '$zZ'),
                  ('S', '$Zz'),
                  ('a', '@4'),
                  ('A', '@4'),
                  ('o', '0'),
                  ('O', '0'),
                  ('0', 'oO'),
                  ('@', 'Aa4'),
                  ('E', '3'),
                  ('e', '3'),
                  ('i', '1lL'),
                  ('I', 'l1L'),
                  ('t', '7'),
                  ('T', '7'),
                  ('l', '1iI'),
                  ('L', '1iI'),
                  ('z', 's'),
                  ('Z', 'S'),
                  ('g', '69'),
                  ('G', '69'),
                  ]

    for x in ascii_lowercase:
      Default_Rules[x] = x.upper()
      Default_Rules[x.upper()] = x

    for x in __specials:
      if not x[0] in Default_Rules:
        Default_Rules[x[0]] = x[0]
      Default_Rules[x[0]] += x[1]
    return Default_Rules


def replace_exact(word, position, new):
    ''' 
    Replaces exact charcter on position

    :param: word: string to manipulate
      :type: str

    :param: position: exact character spot to replace
      :type int

    :param: new: string to replace to with
      :type: str

    :return: newword: manipulated result
      :type: str
    '''
    newword = ''
    for i, x in enumerate(word):
      if i == position:
        newword += new
      else:
        newword += x
    return newword

