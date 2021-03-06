#!/usr/bin/python3

# Reading an excel file using Python 
import xlrd 
import csv
import json
import pymysql
from lxml import etree

##------------------------------------------------------##
##               Read excel file 
##------------------------------------------------------##


def Read_EXCEL(loc):
 #  loc = ("/home/srm/aa/PYTHON/PROJECTS/DBI/AA.xlsx") 
 #  loc = ("Emp.xlsx")
    # To open Workbook 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)   
    ll2 = []
    for b in range(sheet.nrows):
        ll1 = []
        for c in range(sheet.ncols):
          #print(b,c)
          #print(sheet.cell_value(b, c)) 
           ab = sheet.cell_value(b, c)
           if type(ab) == float:
               ab = int(ab)
               ll1.append(ab)
              #print (ab)
           else:
               ll1.append(ab)
              #print (ab)
         # print (ab)
        #print (ll1)
        ll2.append(ll1)
    #print(sheet.cell_value(i, 0)) 

    return ll2


##=======================================================##



##---------------------------------------------------------##
##              Write json file                            ##
##---------------------------------------------------------##


def Write_JSON(file,args):
    wr_json = open(file,"w")
 #  print(args)
 #  print("\n\n")
    p_json = json.dumps(args)
    wr_json.write(p_json)
 #  print(p_json)

    wr_json.close()


##---------------------------------------------------------##
##                     Write_CSV file                      ##
##---------------------------------------------------------##


def Write_CSV(file,args):
    #print (file)
    fobj = open(file,"w")
    wr_csv = csv.writer(fobj)
    for i in (args):
  #     print(i)
        wr_csv.writerow(i)
    fobj.close()

##---------------------------------------------------------##
##                  End CSV file                           ##
##---------------------------------------------------------##




##----------------------------------------------------------##
##                  Write DBI                               ##
##----------------------------------------------------------##


def Write_DBI(tab_name,args):
    db = pymysql.connect("localhost","root","srm","ATOZ" )
    cursor = db.cursor()
    kk = list(args)
    head = kk.pop(0) 
    #print(head)
    sql = "INSERT INTO "+tab_name+" VALUES (%s, %s, %s, %s, %s, %s)"
    
    cursor.executemany(sql, kk)

    db.commit()
    db.close()


#============================================================##



##-----------------------------------------------------------##
##                       Write XML 
##-----------------------------------------------------------##


def Write_XML(file,data):
    hh = data.pop(0)
    root = etree.Element("root")
    for x in data:
        i = 0
        sub = etree.SubElement(root,"EMP")
        for y in x:
            sub1 = etree.SubElement(sub,"Details")
            sub1.set(hh[i],str(y))
         #  print (sub1.get(hh[i]))
            i +=1
    with open(file, 'wb') as doc: 
        doc.write(etree.tostring(root, pretty_print = True))
 

#============================================================##








if __name__ == "__main__":
    aa = Read_EXCEL('Emp.xlsx')   
    Write_CSV("gg.csv",aa)
    Write_JSON("gg.json",aa)
    Write_DBI('EMP_DATA',aa)
    Write_XML('EMP.xml',aa)

