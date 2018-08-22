

path = 'C:\\python_projects\\read-text\\test\\text.txt'
i = 0
pattern = b'PATTERN'

with open(path, 'rb') as f:
 for chunk in iter(lambda: f.read(4096), b''):
  #print('Chunk started -> '+str(i))
  if pattern in chunk:
   i= i + 1
   print('Found '+str(pattern)+' - Number of Occurencies -> '+str(i))