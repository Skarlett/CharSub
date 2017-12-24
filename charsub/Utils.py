from string import ascii_lowercase
from os.path import isfile


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

