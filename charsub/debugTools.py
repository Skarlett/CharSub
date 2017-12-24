from time import time

def patternComparsion(deformInstance, testData, iterables=None, verbose=True):
  '''
  Test iterables in pwGen.patterns

  :param testData: Data to manipulate. (like word)
   :type: str

  :param iterables: list of functions to compare or None to use default for object
    :type: func | none

  :param verbose: Use default text display for displaying data
   :type: bool

  :return: dictionary of length, comparsions against other iterables, etc
    :type: dict 
  '''
  if iterables == None:
    iterables = deformInstance.deformFuncList
  data = {x.__name__: None for x in iterables}
  timer = time()

  for x in iterables:
    startTime = time()
    retrn = set(x(deformInstance, testData))
    data[x.__name__] = {'data': set(retrn), 'length': len(set(retrn)), 'exec': x, 'runTime': time() - startTime}

  for series, _dict in data.items():
    for idname in data:
      if not idname == series:
        for val in data[idname]['data']:

          if not 'instances of ' + idname in data[series]:
            data[series]['instances of ' + idname] = {
                                                      'common': list(), 'commonCnt': int(),
                                                      'difCnt': int(), 'different': list(),
                                                      'percentageCom': float(), 'percentageDif': float()
                                                     }

          if val in data[series]['data']:
            data[series]['instances of ' + idname]['common'].append(val)
            data[series]['instances of ' + idname]['commonCnt'] += 1
            data[series]['instances of ' + idname]['percentageCom'] = \
              round(100 * float(data[series]['instances of ' + idname]['commonCnt']) / data[series]['length'], 2)


          else:
            data[series]['instances of ' + idname]['different'].append(val)
            data[series]['instances of ' + idname]['difCnt'] += 1
            data[series]['instances of ' + idname]['percentageDif'] = \
              round(100 * float(data[series]['instances of ' + idname]['difCnt']) / data[series]['length'], 2)

  _temp = list()
  for id, val in data.items():
    if type(val) == dict:
      for x in val['data']:
        if not x in _temp:
          _temp.append(x)

  data['info'] = {'TotalTime': str(time() - timer) + 's', 'iters: ': ''.join('[%s] ' % (x.__name__) for x in iterables),
                  'TotalGenerated':len(_temp)}
  del _temp

  if verbose:
    for _id, _data in data.items():
      vdata = []
      print('-' * 20)
      print(_id)
      print('-' * 20)

      for _name, _val in _data.items():
        if not type(_val) == dict:
          vdata.append((_name, _val, 1))
        else:
          vdata.append((_name, _val.items(), 2))
      for n, v, priority in vdata:
        if priority == 1:
          print('\t' + n + ': ' + str(v))
      print('\n========Comparison data========\n')
      for n, v, priority in vdata:
        if priority == 2:
          print('\t\t' + n + ' (compared to ' + _id + ')\n\t\t' + '-' * 25)
          # print '\t\t\n'+'-'*10
          for _n, _v in v:
            print('\t\t' + str(_n) + ': ' + str(_v))
          print('\n')

  return data
