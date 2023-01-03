import xml.etree.ElementTree as ET
import pandas as pd
import re

filePath = "./xml/ibatis/wonder.xml"
tree = ET.parse(filePath)
root = tree.getroot()

# root_element = ET.fromstring(tree)
# iter_element = root_element.iter(tag="select")
# root.tag
# print(root.tag)
# print(root.attrib)


pattern = r"[a-zA-Z0-9_]+\.\.[a-zA-Z0-9_]+"
selects =[]
for select in root.findall('select'):
     input = {}
     id = select.attrib['id']
     query = select.text
     print(id, query)
     input['id'] = select.attrib['id']
     matchedTableList = re.findall(pattern,query)
     if matchedTableList:
          print(len(matchedTableList))
          seq = 0
          if len(matchedTableList) > 1:
               for matchedTable in matchedTableList:
                    seq += 1
                    input['table'] = matchedTable
                    input['seq'] = seq
                    selects.append(input)
                    print(selects)
          # print(matchedTableList)

          # for matchedTable in matchedTableList:
          #      input['table'] = matchedTable
          #      selects.append(input)
     # print(matchedList)

     # input['query'] = query[match.start():match.end()]
     # selects.append(input)
     # matchOB = re.search(pattern, query, re.IGNORECASE)
     # if matchOB:
     #      matchOB.groupdict()
          # for match in matchOB:
          #      print(match.start(), match.end())
          #      input['query'] = query[match.start():match.end()]
          #      selects.append(input)

#

# print(selects)
df = pd.DataFrame(selects)

print(df)
# print (selects)
# pattern = r".."
# matchOB = re.match(pattern, selects['query'])
# if matchOB:
#      print (matchOB.group())