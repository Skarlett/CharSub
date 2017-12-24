
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
