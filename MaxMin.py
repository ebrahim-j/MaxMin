def find_max_min(somelist):
  
  result = []
  
  max_value = max(somelist)
  min_value = min(somelist)
  
  if min_value == max_value:
    numItems = len(somelist)
    result.append(numItems)
  else:
    result.append(min_value)
    result.append(max_value)
    
  return result
