from charsub.sub import Substitute


def permutate_word(word, ruleSet=None, patterns=list()):
  '''
  This permutates the word given with substitute characters; like a bruteforce of all possiblities given within the rule set, for more functionality 
  on this - please refer to sub.py, Utils.py, patterns.py and debugTools.py
  
  :param word: Word to permutated
   :type: str
  
  :param ruleSet: A dictionary of rules, the key would be the character to look for, and the left to change it with.
                  {'.', 'A1'} This will change every instance of "." into every combination of "A1" subsituted
                  in the same position
                  
   :type: dict | str (filePath) | None (Use Defaults)
  
  :param patterns: list of Functions from patterns.py | empty list uses defaults
    :type: list
  
  :return: All variations given from the patterns with no duplicates.
   :type: list
  '''
  return Substitute(ruleSet=ruleSet).deform(word, deformFuncList=patterns)



def BruteForce(end, chars=str(), start=int()):
      ''' 
      This is a classical bruteforce, it will generate all combinations with given characters (chars)
      And when it reaches the length of "end" it will stop after generating the last data,
      start will tell it where to start generating
      
      :param end: int of length to stop generation
       :type: int
       
      :param chars: characters to be used in bruteforce
       :type: str
      
      :param start: Where to start
       :type: int
       
      :return: yields str of result
      '''
      # Yes it's that simple.
      for i in range(end, start):
        for current in range(i, i+1):
          _round = [i for i in chars]
          for y in range(current):
              _round = [x + i for i in chars for x in _round]
          for x in _round:
              yield x


