from os.path import isfile
from string import ascii_lowercase
from charsub import patterns


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
  specials = [('s', '$zZ'),
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
  
  for x in specials:
    if not x[0] in Default_Rules:
      Default_Rules[x[0]] = x[0]
    Default_Rules[x[0]] += x[1]
  return Default_Rules


class Substitute:
  def __init__(self, ruleSet=None, patterns_list=[patterns.constant, patterns.modulus]):
    '''

    Returns a subsitution/deformation object based on rules

    :keyword: ruleset: If taken as a dict, it will use such rules; 
    If taken as string it looks for filepath; else raises ValueError
    if none uses Defaults
    anything else raises ValueError
      :type: str dict none

    :raise: ValueError: on invalid input

    '''

    self.patterns_list = patterns_list
    # If none, use defaults
    if ruleSet == None:
      ruleSet = makeDefaultRules()

    # Did you give me a file?
    elif type(ruleSet) == str:
      if isfile(ruleSet):
        ruleSet = loadRuleSet(ruleSet)
      else:
        raise ValueError('Not a file path')

    # Whatever you gave me, did it come back as a dict?
    try:
      assert type(ruleSet) == dict
    except Exception:
      print(ruleSet)
      # What did you give me...?
      raise ValueError('RuleSet needs to be Dictionary | Filepath | None')

    # Cool this works
    self.ruleSet = ruleSet

  def getRules(self, letter):
    '''
    Returns the replacement/substitution letters for the letter given
    
    :param letter: letter to check (a)
      :type: single character str | Unless you know what you're doing and you're hacking at the ruleset funcs
    
    :return: replacement letters
      :type: str
    
    '''
    if not letter in self.ruleSet:
      # If we ever get a letter that has no rule, give it ; it's self so it won't change it
      self.ruleSet[letter] = letter
    return self.ruleSet[letter]

  def export_rules(self, location):
    '''
    :param location: Where to save to
      :type: str
    
    :return: if written correctly without any errors
      :type: Bool
    '''
    try:
      with open(location, 'w') as f:
        for x in self.ruleSet:
          if not x == self.ruleSet[x]:
            f.write(x + ':' + self.ruleSet[x] + '\n')
    except Exception as e:
      if __debug__ == True:
        print(e)

      return False
    return True

  def deform(self, word,  entrophy_level=None, entrophy_start=0):
    '''
    Main function to use a majority of the functionality of the project.
    
    :param word: word to deform
      :type: str
      
    :param patterns_list: Empty list for defaults - or else insert iters into a list.
                           Iters shall be functions stored in __SubIters__
      :type: list
    
    :return: list: data of deformed iterations with no duplicates
    '''
    dataBank = set([word])

    for func in self.patterns_list:
      dataBank.update(set(func(self, word,
                              prefill=dataBank,
                              entrophy_level=entrophy_level,
                              entrophy_start=entrophy_start)))
    return dataBank

