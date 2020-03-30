###########################################################################################
##   LAST UPDATE: NOV 1, 2019
###########################################################################################

from creds import *
import random
import pyodbc
import time
import sys
import os

errCount = 5

def getConn():
    try:
        return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD='+ password)

    except Exception as e:
        logError('getConn()', '', str(e).replace("\\n",chr(10)))

    os._exit(1)

def getCursor(conn):
    try:
        return conn.cursor()
    except Exception as e:
        logError('getCursor()', '', str(e).replace("\\n",chr(10)))

    os._exit(1)

def logError(mod, sql, msg):

    appname = sys.argv[0] + ' '
    for n in range(1, 6):
        try:
            appname += sys.argv[n] + ' '
        except:
            break

    try:
        with open(sys.argv[0].upper() + '-SQLError.log', 'a') as logfile:
            logfile.write('App:    ' + appname + '\n')
            logfile.write('Time:   ' + getTime() + '\n')
            logfile.write('Module: ' + mod + '\n')
            logfile.write('SQL: '    + sql + '\n')
            logfile.write(msg + '\n\n')
    except:
        pass

    print('App:    ' + appname )
    print('Time:   ' + getTime())
    print('Module: ' + mod)
    print('SQL:    ' + sql)
    print(msg + '\n')

def getTime():
    return time.asctime(time.localtime(time.time()))

def SQLExec(sql, cursor, conn):
    errs    = 0
    while True:
        try:
            cursor.execute(sql)
            conn.commit()
            return
        except Exception as e:
            errs += 1
            time.sleep(random.randint(1, 5) * 0.5)            
            if errs == errCount:
                logError('SQLExec()', sql, str(e).replace("\\n",chr(10)))
                break

    os._exit(1)

def SQLExecReturn(sql, cursor, conn):

    errs    = 0
    while True:
        try:
            cursor.execute(sql)
            columns = [column[0] for column in cursor.description]
            zrows = cursor.fetchall() 
            results = []
            for zrow in zrows:
                results.append(dict(zip(columns, zrow)))
            conn.commit()
            return results
        except Exception as e:
            errs += 1
            time.sleep(random.randint(1, 5) * 0.5)            
            if errs == errCount:
                logError('SQLExecReturn()', sql, str(e).replace("\\n",chr(10)))
                break
    os._exit(1)

    

def SQLGet(sql, cursor):

    errs    = 0
    while True:
        try:
            cursor.execute(sql)
            columns = [column[0] for column in cursor.description]
            zrows = cursor.fetchall() 
            results = []
            for zrow in zrows:
                results.append(dict(zip(columns, zrow)))
            return results
        except Exception as e:
            errs += 1
            time.sleep(random.randint(1, 5) * 0.5)            
            if errs == errCount:
                logError('SQLGet()', sql, str(e).replace("\\n",chr(10)))
                break
    os._exit(1)