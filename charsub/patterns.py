from charsub import Utils
from sys import version_info
if version_info.major == 2:
  range = xrange


def constant(deformInstance, word, prefill=list()):
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

    complete = prefill
    for series in range(len(word)):
      collector = []
      for pos, letter in enumerate(word):
        for rule in deformInstance.getRules(letter):
          if series == 0:
            collector.append(Utils.replace_exact(word, pos, rule))
          else:
            for x in complete:
              data = Utils.replace_exact(x, pos, rule)
              if not data in complete:
                collector.append(data)

      for item in set(collector):
        if not item in complete:
          complete.append(item)

    return complete
  
def modulus(deformInstance, word, prefill=list()):
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

    skipper = 1
    complete = prefill

    for series in range(len(word)):                     # <- This how we keep track of how many times we've iterated over into "complete" variable
      collector = []                                    # <- This is our current changes we're gonna append
      for pos, letter in enumerate(word):               # <- Getting position and letter in word
        for rule in deformInstance.getRules(letter):    # <- For letter in rules (those left characters we talked about earilier) see line 12
          if pos % skipper == 0:                        # <- Does our skipper agree that this letter should be changed?
            for l in rule:                              # <- for each letter in that rule
              if series == 0:                           # If this is our first round about, we don't have to iterate our pervious results (Because there is none)
                data = Utils.replace_exact(word, pos, l)
                if not data in complete and not data in collector:
                  collector.append(Utils.replace_exact(word, pos, l))  # This is our first results we're gonna iter over again

              else:
                # We've made more than 1 round now, so let us iter over what we previously had,
                # and also append those to be iterated

                for word in complete:
                  data = Utils.replace_exact(word, pos, l)
                  if not data in collector and not data in complete:  # Don't dup on me please?
                    collector.append(data)

      # And they shall be iterated over again

      for item in collector:
        if not item in complete:  # Double check that please.
          complete.append(item)

      skipper += 1  # Increase skipper, so it skips one extra character

    return set(complete)  # Alrighty, now im convinced we have no duplicates
