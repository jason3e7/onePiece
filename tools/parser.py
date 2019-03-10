import os
import re

def parser(filepath):
  pattern = r" (\\#\w+\, |\\#\w+\.)+"
  output = ""
  file = open(filepath, 'r')
  for line in file:
    find = re.search(pattern, line)
    if(find != None) :
      line = line[:find.start() - 1] + '.' + line[find.end():]
      output += line
      output += "  *" + find.group() + "\n"
    else :
      output += line
  file.close()

  file = open(filepath, 'w')
  file.write(output)
  file.close()

for dirname, dirnames, filenames in os.walk('../'):

  for filename in filenames:
    if(filename == "index.md"):
      target = os.path.join(dirname, filename)
      print "parse " + target 
      parser(target)
      print "parse " + target + " done"
  
  if '.git' in dirnames:
    # don't go into any .git directories.
    dirnames.remove('.git')