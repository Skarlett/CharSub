
from sys import version_info

if version_info.major == 2:
 range = xrange
 
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



def constant(deformInstance, word, prefill=list(), entrophy_level=None, entrophy_start=0):
    '''
    This is a "construct" Pattern
    
    
    {'.':'A'}
    ....
    A...
    AA..
    AAA.
    AAAA

    :param deformInstance: 
    :param word: 
    :param prefill: 
    :return: 
    '''
    el = entrophy_level or len(word)
    es = entrophy_start or 0
    if el <= es:
      raise ValueError("Start has to be lower than end")

    if el > len(word):
      raise ValueError("Entrophy Level cannot be greater than the length of the string being processed.")

    complete = set(prefill)
    
    for series in range(el):
      collector = set()
      for pos, letter in enumerate(word):
        for rule in deformInstance.getRules(letter):
          if series == 0:
            collector.add(replace_exact(word, pos, rule))
          else:
            for itered, _ in complete:
              collector.add(replace_exact(itered, pos, rule))
      
      complete.update(collector)
      if entrophy_level and series >= entrophy_level:
        break
    
    return complete
   
def modulus(deformInstance, word, prefill=set(), entrophy_level=None, entrophy_start=0):
    '''

    The method used in this function was the idea to use the modulus/remainders
    To determine if to execute a letter change on such a letter, or to ignore it.
    To ensure we hit the most possibilities, we iter over our own final list. (Return val) 

    Rules:
     . -> A

    eg:
    ....

    A...
    .A..
    ..A.
    ...A (First)

    A.A.
    .A.A
    ..AA
    A..A (Second)

    A.AA
    AA.A
    A.AA
    AA.A (third)

    AAAA
    AAAA
    AAAA
    AAAA (Fourth)

    Above is human made input, try Substitue({'.':'A'}).deform('....') For machine used input

    :param deformInstance: Instance of Substitute
      :type: Substitute()

    :param word: string to permutate
      :type: str

    :return: iterable of all combinations generated
      :type: set 

    '''

    el = entrophy_level or len(word)
    es = entrophy_start or 0
    if el <= es:
      raise ValueError("Start has to be lower than end")
    
    if el > len(word):
      raise ValueError("Entrophy Level cannot be greater than the length of the string being processed.")
    
    prefill.add(word)
    complete = set(prefill)
    
    for series in range(el):                     # <- This how we keep track of how many times we've iterated over into "complete" variable
      collector = set()                                    # <- This is our current changes we're gonna append
      for pos, letter in enumerate(word):               # <- Getting position and letter in word
        for rule in deformInstance.getRules(letter):    # <- For letter in rules (those left characters we talked about earilier) see line 12
          skipper = series if bool(series) else 1
          if pos % skipper == 0:                        # <- Does our skipper agree that this letter should be changed?
            for l in rule:                              # <- for each letter in that rule
              if series == 0:                           # If this is our first round about, we don't have to iterate our pervious results (Because there is none)
                collector.add((replace_exact(word, pos, l), series))  # This is our first results we're gonna iter over again
              else:
                # We've made more than 1 round now, so let us iter over what we previously had,
                # and also append those to be iterated
                for w, _ in complete:
                  collector.add(replace_exact(w, pos, l))
                  
      complete.update(collector)
      if entrophy_level and series >= entrophy_level:
       break
    return complete
