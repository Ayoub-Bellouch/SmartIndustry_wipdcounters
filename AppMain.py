# -*- coding: utf-8 -*-

#!/usr/bin/env python
import pandas as pd
import datetime
import time
import psycopg2
from Functions2 import *
from datetime import timedelta
from calendar import isleap

connection = psycopg2.connect(
        port     = 5432,
        host     = "localhost",
        database = "wipcounters",
        user     = "postgres",
        password = "root"
    )

# connection = psycopg2.connect(
#         port=5432,
#         host="RHKEN702",
#         database="P01GES",
#         user="uprodges",
#         password="P00chy3n@")


# def counters-----------------------------------------------------------------------------

EntryWM = 0



ExitWM = 0




print("##Start app:")



def AppMain_func():

    global  EntryWM, EntryWM_flag, ExitWM, ExitWM_flag
   
    global  break_flag

    print("##Start counters")

    # Lancement de l'application ==|>> (time zone : utc+1)
    start = datetime.datetime.utcnow() + timedelta(hours=1)
    
    

    start_counting = True
    end = ''
    while start_counting:

        start = datetime.datetime.utcnow()+ timedelta(hours=1)
        
        Year = int(start.strftime('%Y'))
        mnth = int(start.strftime('%m'))
        day = int(start.strftime('%d'))
        log_message = {"value": "start_time", "message": "start time(time zone : utc+1): "+ str(start)}
        print(log_message)

        d = []
        d.append(start.strftime('%Y-%m-%d %H:%M:%S'))
        
        # Initialisation des valeur Start End des Shift 
        if start >= datetime.datetime(Year, mnth, day, 8, 30, 0) and start <= datetime.datetime(Year, mnth, day, 16, 30, 0):
            end = datetime.datetime(Year, mnth, day, 16, 30, 00)
        
        elif start >= datetime.datetime(Year, mnth, day, 00, 30, 0) and start <= datetime.datetime(Year, mnth, day, 8, 30, 0):
            end = datetime.datetime(Year, mnth, day, 8, 30, 00)

        elif start >= datetime.datetime(Year, mnth, day, 00, 00, 0) and start <= datetime.datetime(Year, mnth, day, 00, 30, 0):
            end = datetime.datetime(Year, mnth, day, 00, 30, 00)

        else:
            
            if mnth == 1 or mnth == 3 or mnth == 5 or mnth == 7 or mnth == 8 or mnth == 10 or mnth == 12:
                if day==31:
                    day=0
                    end = datetime.datetime(Year, mnth+1, day+1, 00, 30, 00)
                else:
                    end = datetime.datetime(Year, mnth, day+1, 00, 30, 00)
            elif mnth==2:
                if (isleap(Year) and day == 29) or (isleap(Year)==False and day ==28):
                    day=0
                    end = datetime.datetime(Year, 3, day+1, 00, 30, 00)
                elif day !=28 and day!=29:
                    end = datetime.datetime(Year, mnth, day+1, 00, 30, 00)
            elif mnth == 4 or mnth == 6 or mnth == 9 or mnth == 11:
                if day==30:
                    day=0
                    end = datetime.datetime(Year, mnth+1, day+1, 00, 30, 00)
                else:
                    end = datetime.datetime(Year, mnth, day+1, 00, 30, 00)
            
       
        print('end :', end)


        try:
            log_message = {"value": "Lancement_collect_donnees", "message": "Processus de collection de donnees !"}
            print(log_message)
            
            print({"log_value": "Stuckers", "log_message": "Stuckers Init Value - Befor Cutting, Data Collection !"})
            stackers = St_Collect(commOut, commInn)
            St_EntryPrt_out_init = stackers[1]
            St_EntryPrt_Inn_init = stackers[2]

            St_ExitPrt_out_init = stackers[3]
            St_ExitPrt_out2_init = stackers[4]
            St_ExitPrt_Inner_init = stackers[5]
            
            # Cette valeur est le Cardinale Stucker just avant le four ALS => condition de notification telegram
            St_Pr_init = stackers[6]


            
            while start <= end:
                
                # Cutting ----------------------------------------
                print({"log_value": "Cutting", "log_message": "Cutting, Data Collection !"})
                Cutting = collectCutting(commCut)
                
                Loader = Cutting[1]
                EntryCel1 = Cutting[2] 
                EntryCel2=Cutting[3] 
                EntryCel3=Cutting[4]
                ExitCel1= Cutting[5] 
                ExitCel2 = Cutting[6]
                ExitCel3=Cutting[7]
                
                EntryWM = 0
                ExitWM = 0
                
                # Printing ----------------------------------------
                print({"log_value": "Printing", "log_message": "Printing, Data Collection !"})
                Prt = PrintingCollect(commOut, commInn)
                PrtInputAll=Prt[1]
                PrtInput_Inner= Prt[2]
                PrtInput_Outer = Prt[3]
                PrtInnerExit = Prt[4]
                PrtOuterExit=Prt[5]
                
                # P2 ----------------------------------------
                print({"log_value": "Four_P2", "log_message": "Four P2, Data Collection !"})
                P2 = P2Collect(commP2, commPWM, commOut)
                # [t,Delivered_toP2, EntryP2, ExitP2, BeforepxmInn, Beforpwm, afterPWM ]
                Delivered_toP2 = P2[1]
                EntryP2=P2[2]
                ExitP2= P2[3] 
                BeforPWMInn = P2[4] 
                BeforPWouter=P2[5] 
                AfterPW = P2[6]

                # four ----------------------------------------
                print({"log_value": "Four_ALS", "log_message": "Four ALS, Data Collection !"})
                furnace = ALS(commALS)
                # [time, Entrylife, Exitlif]
                CountChargement= furnace[1] 
                CountExitlift= furnace[2]
                
                # start = datetime.datetime.utcnow()+ timedelta(hours=1)
                
                # Logs & Tests
                start = start + timedelta(hours=3)
                print({"TestStartdate": "une incrimentation de la date de debut est effectuer a ce niveau, NvDateStart: {}".format(start)})

                #print("cutting :",Cutting, "printing :",Prt, "P2 :", P2,"Furnace :", furnace)
                time.sleep(3)
                
            print("Counting Done")
            # Stackers ----------------------------------------
            # [time, St_EntryPrt_Out, St_EntryPrt_Inn, St_ExitPrt_out, St_ExitPrt_out2,  St_ExitPrt_Inn ,  StPr ]
            st=[]

            print({"log_value": "Stuckers", "log_message": "Stuckers After Cutting, Data Collection !"})
            stackers = St_Collect(commOut, commInn)
            
            St_EntryPrt_out = stackers[1]
            St_EntryPrt_Inn = stackers[2]
            
            St_ExitPrt_out = stackers[3]
            St_ExitPrt_out2 = stackers[4]
            St_ExitPrt_Inner = stackers[5]
            St_Pr = stackers[6]




            if (St_EntryPrt_out is None) or (St_EntryPrt_Inn is None):
                stackers = St_Collect(commOut, commInn)
                St_EntryPrt_out = stackers[1]
                St_EntryPrt_Inn = stackers[2]
                St_ExitPrt_out = stackers[3]
                St_ExitPrt_out2 = stackers[4]
                St_ExitPrt_Inner = stackers[5]
                St_Pr = stackers[6]
                
            d.append(end.strftime('%Y-%m-%d %H:%M:%S'))
            d += [Loader,
                  EntryCel1,
                  ExitCel1,
                  EntryCel2,
                  ExitCel2,
                  EntryCel3,
                  ExitCel3,
                  EntryWM,
                  ExitWM,
                  PrtInputAll,
                  PrtInput_Inner,
                  PrtInput_Outer,
                  PrtInnerExit,
                  PrtOuterExit,
                  Delivered_toP2,
                  EntryP2,
                  ExitP2,
                  BeforPWouter,
                  BeforPWMInn,
                  AfterPW,
                  CountChargement,
                  CountExitlift,
                  St_EntryPrt_out,
                  St_EntryPrt_Inn,
                  St_ExitPrt_out,
                  St_ExitPrt_out2,
                  St_ExitPrt_Inner,
                  St_Pr,
                  St_EntryPrt_out_init,
                  St_EntryPrt_Inn_init,
                  St_ExitPrt_out_init,
                  St_ExitPrt_out2_init,
                  St_ExitPrt_Inner_init,
                  St_Pr_init]
            
            connection = psycopg2.connect(
                port     = 5432,
                host     = "localhost",
                database = "wipcounters",
                user     = "postgres",
                password = "root"
            )
            
            # connection = psycopg2.connect(
            # port=5432,
            # host="RHKEN702",
            # database="P01GES",
            # user="uprodges",
            # password="P00chy3n@")
            
            print(d)
            
            for i in range(len(d)):
                
                if d[i] is None:
                    d[i]=0
                    
            '''
            
            InsertInto(connection,d)
            time.sleep(60)
            start = datetime.datetime.utcnow()+ timedelta(hours=1)

            '''

            InsertInto(connection,d)

        except Exception as e :
            start = datetime.datetime.utcnow() + timedelta(hours=1)
            print('None Type Catched: ', e)
            continue


if __name__ == "__main__":

    AppMain_func()