import Utils

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


def padBruteForceWithWord(word, end, chars='1234567890', start=0, suffix=True, prefix=False):
    '''
    :param word: word to pad Brute force with (eg: '(prefix)password(suffix)'
      :type: str
      
    :param end: when to end bruteforce
      :type: int
      
    :param chars: characters to use in bruteforce 
      :type: str
    
    :param start: where to start on bruteforce
      :type: int 
    
    :param suffix: Append to suffix | one of Suffix or Prefix needs to be true
      :type: bool
    
    :param prefix: append to prefix | one of Suffix or Prefix needs to be true
      :type: bool
      
    :return: Yields padded word with bruteforce data 
    '''
    try:
      assert prefix or suffix
    except:
      raise AssertionError('Either prefix or suffix has to be true')

    for x in BruteForce(end, chars, start):
      if suffix:
        yield word+x
      elif prefix:
        yield x+word
      elif suffix and prefix:
        yield x+word+x


def WordlistAdditives(self, readFrom, writeTo, l, chars='1234567890', start=0, prefix=True, suffix=True, SuffixAndPrefix=True):
    with open(readFrom) as reader:
      with open(writeTo, 'a') as f:
        for word in reader:
          if not SuffixAndPrefix:
            if prefix:
              for x in self.addChars(word.strip(), l, chars, start):
                f.write(x+'\n')
            if suffix:
              for x in self.addChars(word.strip(), l, chars, start, suffix=True):
                f.write(x+'\n')
          else:
            for x in self.addChars(word.strip(), l, chars, start, prefixAndSuffix=True):
              f.write(x + '\n')


def vowelPopper(word, chars=('a', 'e', 'i', 'o', 'u', 'y')):
  complete = []
  for stage in range(len(word)):
    collector = []

    if stage == 0:
      for pos, letter in enumerate(word):
        if letter in chars:
          collector.append(Utils.remove_char(word, pos))

    else:
      for word in complete:
        for pos, letter in enumerate(word):

          if letter in chars:
            data = Utils.remove_char(word, pos)
            if not data in collector and not data in complete:
              collector.append(data)

    for x in collector:
      if len(x) > 0:
        complete.append(x)

  return set(complete)


