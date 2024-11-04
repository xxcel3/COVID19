import bottle
import json
import data
import processing
import os.path

def load_data():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.cdc.gov/resource/unsk-b7fc.json?$limit=50000&$where=location!=%27US%27'
    info = data.json_loader(url)
    heads = ['date','location','administered_janssen','administered_moderna','administered_pfizer','administered_unk_manuf','series_complete_pop_pct']
    data.save_data(heads, info, 'saved_data.csv')

load_data()

@bottle.route("/")
def send_html():
  return bottle.static_file("index.html",root=".")

@bottle.route("/vaccine.js")
def send_frontEndJS():
  return bottle.static_file("vaccine.js",root=".")

@bottle.route('/bar')
def barData_requested():
  lines=data.read_values('saved_data.csv')
  dates={}
  plot_data={'x':[],'y':[]}
  for line in lines:
    location=str(line[1])
    if location in dates:
      if line[0]>dates[location][0]:
        dates[location][0]=line[0]
        dates[location][1]=line[6]
    else:
      dates[location]=[line[0],line[6]]
  for key in dates:
    plot_data['x'].append(key)
    plot_data['y'].append(dates[key][1])
  json_blob=json.dumps(plot_data)
  return json_blob

@bottle.route('/pie')
def pieData_requested():
  lines=data.read_values('saved_data.csv')
  dates={}
  plot_data={'values':[0,0,0,0],'labels':[ 'Janssen', 'Moderna','Pfizer','Other']}
  for line in lines:
    location=str(line[1])
    if location in dates:
      if line[0]>dates[location][0]:
        dates[location][0]=line[0]
        dates[location][1]=line[3]
        dates[location][2]=line[4]
        dates[location][3]=line[5]
        dates[location][4]=line[6]
    else:
      dates[location]=[line[0],line[2],line[3],line[4],line[5]]
  for key in dates:
    plot_data['values'][0]+=to_num(dates[key][1])
    plot_data['values'][1]+=to_num(dates[key][2])
    plot_data['values'][2]+=to_num(dates[key][3])
    plot_data['values'][3]+=to_num(dates[key][4])
  json_blob=json.dumps(plot_data)
  return json_blob


@bottle.route('/line')
def lineData_requested(content):
  lines=data.read_values('saved_data.csv')
  lines.sort()
  plot_data={'x':[],'y':[]}
  for line in lines:
    location=str(line[1])
    if location == content:
      plot_data['x'].append(line[0])
      plot_data['y'].append(to_num(line[6]))
  json_blob=json.dumps(plot_data)
  return json_blob
@bottle.post('/loc')
def receive_loc():
  locBlob=bottle.request.body.read().decode()
  content=json.loads(locBlob)
  return lineData_requested(content)

def to_num(s):
  if s=='O': 
    return 0
  else:
    return float(s)

bottle.run(host="0.0.0.0", port=8080)