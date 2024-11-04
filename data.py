import csv
import json
import urllib.request

#part 2
def dic_list_gen(keys_list, values_list):
  out=[]
  for values in values_list:
    out_dict={}
    for index in range(len(values)):
      out_dict[keys_list[index]]=values[index]
    out.append(out_dict)
  return out

def read_values(fname):
  out=[]
  with open(fname) as fp:
    reader=csv.reader(fp)
    next(reader)
    for line in reader:
      out.append(line)
  return out

def make_lists(keys_list, dict_list):
  out=[]
  for dict in dict_list:
    out_list=[]
    for key in keys_list:
      out_list.append(dict[key])
    out.append(out_list)
  return out

def write_values(fname, lists_list):
  with open(fname, "a") as fa:
    writer=csv.writer(fa)
    for aList in lists_list:
      writer.writerow(aList)

#part 3
#function 1 - blob to useable data
def json_loader(url):
  response = urllib.request.urlopen(url)
  content_string = response.read().decode()
  content_json = json.loads(content_string)
  return content_json

#function 2 - str number to float number
def make_values_numeric(keys, aDict):
  for key in aDict:
    if key in keys:
      aDict[key]=float(aDict[key])
    else:
      aDict[key]=aDict[key]
  return aDict

#function 3 - csv file of data with specific key
def save_data(keys, dict_list, fname):
  ret_list=make_lists(keys, dict_list)
  with open(fname, 'w') as fw:
    writer=csv.writer(fw)
    writer.writerow(keys)
  write_values(fname, ret_list)


#function 4 - list of dictionaries from csv file
def load_data(fname):
  out=[]
  aLists=read_values(fname)
  with open(fname) as fp:
    reader=csv.reader(fp)
    header=next(reader)
  for list in aLists:
    aDict={}
    for i in range(len(header)):
      aDict[header[i]]=list[i]
    out.append(aDict)
  return out


