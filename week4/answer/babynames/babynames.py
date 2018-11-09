#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  list=[]
  dict={}
  file=open(filename,'r')
  contents=file.read()                                   # read file contents
  file.close()
  
  year=re.search(r"Popularity\sin\s(\d\d\d\d)",contents)  # obtain year
  year=year.group(1)
  list.append(year)

  #extract all the names with rank
  all=re.findall(r"(<td>)(\d*)(</td><td>)(\w*)(</td><td>)(\w*)(</td>)",contents)

  # store the values in dictionary 
  for i in all:
    if i[3] not in dict:                # check for repetitive name
      dict[i[3]]=i[1]
    elif dict[i[3]]>i[1]:               # if repetitive name is present store the most popular one.
      dict[i[3]]=i[1]                   # doing this will result in most popular copy instead of most recent/less popular one
    if i[5] not in dict:
      dict[i[5]]=i[1]
    elif dict[i[5]]>i[1]:
      dict[i[5]]=i[1]

  n=sorted(dict)          # sort in alphbetical order of names

  for i in n:
    list.append(i+" "+dict[i])    # append the namesto the list

  return list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':        
    summary = True                      
    del args[0]
    
  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for arg in args:
    l="\n".join(extract_names(arg))
    if summary:                               # summaryfile
      dFile=open(arg+".summary","w")
      dFile.write(l+"\n")
      dFile.close()
    else:
      print(l)


if __name__ == '__main__':
  main()
