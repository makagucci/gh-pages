#!/usr/bin/python
# Created by c@caine
# On:  11/02/2017
# --- Preamble --- #
import zipfile
import sys
# --- Definitions --- #
z_file = sys.argv[1]
p_list = sys.argv[2]
f = zipfile.ZipFile(z_file)
# --- Main --- #
with open (p_list) as pwl:
  for l in pwl:
    try:
      f.extractall(pwd = l.strip())
    except:
      continue
    else:
      print ("The password is: " + l.strip())
      break
