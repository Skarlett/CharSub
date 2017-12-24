from os.path import isfile
from charsub import patterns
import charsub.Utils


class Substitute:
  def __init__(self, ruleSet=None):
    '''

    Returns a subsitution/deformation object based on rules

    :keyword: ruleset: If taken as a dict, it will use such rules; 
    If taken as string it looks for filepath; else raises ValueError
    if none uses Defaults
    anything else raises ValueError
      :type: str dict none

    :raise: ValueError: on invalid input

    '''

    self.deformFuncList = [
                           patterns.constant,
                           patterns.modulus,
                           # __SubIters__.second_iter,
                           # __SubIters__.first_iter,
                          ]
    # If none, use defaults
    if ruleSet == None:
      ruleSet = charsub.Utils.makeDefaultRules()

    # Did you give me a file?
    elif type(ruleSet) == str:
      if isfile(ruleSet):
        ruleSet = charsub.Utils.loadRuleSet(ruleSet)
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

  def deform(self, word, deformFuncList=list(),  entrophy_level=None, entrophy_start=0):
    '''
    Main function to use a majority of the functionality of the project.
    
    :param word: word to deform
      :type: str
      
    :param deformFuncList: Empty list for defaults - or else insert iters into a list.
                           Iters shall be functions stored in __SubIters__
      :type: list
    
    :return: list: data of deformed iterations with no duplicates
    '''
    dataBank = set(word)

    if len(deformFuncList) == 0:
      deformFuncList = self.deformFuncList

    for func in deformFuncList:
      dataBank.union(set(func(self, word,
                              prefill=dataBank,
                              entrophy_level=entrophy_level,
                              entrophy_start=entrophy_start)))
    return dataBank


