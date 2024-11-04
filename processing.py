def max_value(lod, k):
  out=""
  for dict in lod:
    if(dict.get(k)>out):
      out=dict.get(k)
  return out

def init_dictionary(lod, k):
  out={}
  for dict in lod:
    if (k in dict):
      v=dict.get(k)
      out[v]=0
  return out

def sum_matches(lod, k, v, tgt):
  out=0.0
  for dict in lod:
    if (v==dict.get(k)):
      out+=dict.get(tgt)
  return out

def copy_matching(lod, k, v):
  out=[]
  for dict in lod:
    if (k in dict):
      if (v==dict.get(k)):
        out.append(dict)
  return out
