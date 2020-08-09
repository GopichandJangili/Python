import os
#from xml.dom import minidom
import xml.etree.ElementTree as ET
import pandas as pd

#Tableau workbook
tree = ET.parse(r"path\f.xml")
root = tree.getroot()

#Empty Lists
Tableau_flds = []
Expns = []
Role = []
Source = []

for cal_flds in root.iter('column'):
    Tableau_flds.append(cal_flds.attrib["caption"])
    Role.append(cal_flds.attrib["role"])
    
    if cal_flds:
        for cal in cal_flds:
            Expns.append(cal.attrib["formula"])
            Source.append('NA')
    else:
        Expns.append('NA')
        Source.append(cal_flds.attrib["name"])
        
print(Source)
#Empty DataFrame
df = pd.DataFrame(columns=['Source Column','Tableau Column','Column Type','Expression'])    
df["Tableau Column"] = Tableau_flds
df["Expression"] = Expns
df["Column Type"] = Role  
df["Source Column"] = Source
print(df)
