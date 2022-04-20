# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:02:02 2021

@author: MA117284
"""

import datetime
from influxdb import InfluxDBClient



def collectCutting():
    dbClient = InfluxDBClient('10.212.129.14', 8086, 'Fatima_Ezzahrae.Benhadi', 'InfluxDB4AGCKen!', 'historian')
    Cut = []
    t = datetime.datetime.now()
    Cut.append(t)
    # ------------------------loader--------------------------
    loader_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_7_ENTR_SE_0_ONOFF_MV')
    loader_list = list(loader_inf.get_points())
    Loader = loader_list[0]['last_value_bool']
    Cut.append(Loader)
    #--------------------Entry cutting -------------------------
    EntryCel1_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_Cell_1_20_ENTR_SE_33_ONOFF_MV')
    EntryCel1_list = list(EntryCel1_inf.get_points())
    EntryCel1= EntryCel1_list[0]['last_value_bool']

    EntryCel2_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_Cell_2_40_ENTR_SE_33_ONOFF_MV')
    EntryCel2_list = list(EntryCel2_inf.get_points())
    EntryCel2= EntryCel2_list[0]['last_value_bool']
    
    EntryCel3_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_Cell_3_60_ENTR_SE_33_ONOFF_MV')
    EntryCel3_list = list(EntryCel3_inf.get_points())
    EntryCel3= EntryCel3_list[0]['last_value_bool']
    #------------------Exit Cutting -----------------------------------------------
    ExitCel1_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_Cell_1_100_EXIT_SE_17_ONOFF_MV')
    ExitCel1_list = list(ExitCel1_inf.get_points())
    ExitCel1= ExitCel1_list[0]['last_value_bool']

    ExitCel2_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_Cell_2_103_EXIT_SE_17_ONOFF_MV')
    ExitCel2_list = list(ExitCel2_inf.get_points())
    ExitCel2= ExitCel2_list[0]['last_value_bool']

    ExitCel3_inf = dbClient.query('select last(*) from KE_1_L_CUT_CUT_Cell_3_106_EXIT_SE_17_ONOFF_MV')
    ExitCel3_list = list(ExitCel3_inf.get_points())
    ExitCel3= ExitCel3_list[0]['last_value_bool']
    

    Cut.append(EntryCel1)
    Cut.append(EntryCel2)
    Cut.append(EntryCel3)

    Cut.append(ExitCel1)
    Cut.append(ExitCel2)
    Cut.append(ExitCel3)
    #[time , Loader , EntryCel1, EntryCel2 , EntryCel2 , EntryCel3]
    return(Cut)


def CollectWM():
    dbClient = InfluxDBClient('10.212.129.14', 8086, 'Fatima_Ezzahrae.Benhadi', 'InfluxDB4AGCKen!', 'historian')
    WM = []
    t = datetime.datetime.now()
    WM.append(t)

    #------------------Entry Washer---------------------------
    EntryWm_inf = dbClient.query('select last(*) from KE_1_L_WASH_CUT_washer_ENTR_SE_ONOFF_MV')
    EntryWm_list = list(EntryWm_inf.get_points())
    EntryWm= EntryWm_list[0]['last_value_bool']
    WM.append(EntryWm)
    #---------------------Exit Washer----------------------
    ExitWm_inf = dbClient.query('select last(*) from KE_1_L_WASH_CUT_washer_EXIT_SE_ONOFF_MV')
    ExitWm_list = list(ExitWm_inf.get_points())
    ExitWm= ExitWm_list[0]['last_value_bool']
    WM.append(ExitWm)

    #[time, EntryWm, ExitWM ]
    return WM


def PrintingCollect():
    dbClient = InfluxDBClient('10.212.129.14', 8086, 'Fatima_Ezzahrae.Benhadi', 'InfluxDB4AGCKen!', 'historian')
    PR = []
    t = datetime.datetime.now()
    PR.append(t)



    #--------------------------printing all--------------------------
    ConvInputprt_All_inf = dbClient.query('select last(*) from KE_1_L_PRINT_BELT_pt_12_ENTR_SE_ONOFF_MV')
    ConvInputprt_All_list = list(ConvInputprt_All_inf.get_points())
    ConvInputprt_All= ConvInputprt_All_list[0]['last_value_bool']

    PR.append(ConvInputprt_All)

    #---------------------Entry printing-------------------------------------
    
    ConvInputprt_Inner_inf = dbClient.query('select last(*) from KE_1_L_PRINT_BELT_pt_inner_ENTR_SE_ONOFF_MV')
    ConvInputprt_Inner_list = list(ConvInputprt_Inner_inf.get_points())
    ConvInputprt_Inner= ConvInputprt_Inner_list[0]['last_value_bool']
    PR.append(ConvInputprt_Inner)


    ConvInputprt_outer_inf = dbClient.query('select last(*) from KE_1_L_PRINT_BELT_pt_outer_ENTR_SE_ONOFF_MV')
    ConvInputprt_outer_list = list(ConvInputprt_outer_inf.get_points())
    ConvInputprt_outer= ConvInputprt_outer_list[0]['last_value_bool']
    PR.append(ConvInputprt_outer)
    
    #--------------------Exit printing-----------------------------
    
    ConvExit_Inner_inf = dbClient.query('select last(*) from KE_1_L_PRINT_BELT_pt_inner_EXIT_SE_ONOFF_MV')
    ConvExit_Inner_list = list(ConvExit_Inner_inf.get_points())
    ConvExit_Inner= ConvExit_Inner_list[0]['last_value_bool']
    PR.append(ConvExit_Inner)

    ConvExit_Out_inf = dbClient.query('select last(*) from KE_1_L_PRINT_BELT_pt_outer_EXIT_SE_ONOFF_MV')
    ConvExit_Out_list = list(ConvExit_Out_inf.get_points())
    ConvExit_Out= ConvExit_Out_list[0]['last_value_bool']
    PR.append(ConvExit_Out)

    #PR[Time, EntryAll, EntryInner, EntryOuter, ExitInner, ExitOuter ]
    #PR[time,ConvInputprt, ConvInner, ConvOut]
    return(PR)


def St_Collect():
    dbClient = InfluxDBClient('10.212.129.14', 8086, 'Fatima_Ezzahrae.Benhadi', 'InfluxDB4AGCKen!', 'historian')
    st = []
    t = datetime.datetime.now()
    st.append(t)

    St_EntryPrt_out_inf = dbClient.query('select last(*) from KE_1_L_STAC_CENT_outer_ENTR_SE_16_COUNT_MV')
    St_EntryPrt_out_list = list(St_EntryPrt_out_inf.get_points())
    St_EntryPrt_out= int(St_EntryPrt_out_list[0]['last_value'])

    St_EntryPrt_Inn_inf = dbClient.query('select last(*) from KE_1_L_STAC_CENT_inner_ENTR_SE_54_COUNT_MV')
    St_EntryPrt_Inn_list = list(St_EntryPrt_Inn_inf.get_points())
    St_EntryPrt_Inn= int(St_EntryPrt_Inn_list[0]['last_value'])


    St_ExitPrt_out_inf = dbClient.query('select last(*) from KE_1_L_STAC_CENT_outer_EXIT_SE_26_COUNT_MV')
    St_ExitPrt_out_list = list(St_ExitPrt_out_inf.get_points())
    St_ExitPrt_out= int(St_ExitPrt_out_list[0]['last_value'])

    St_ExitPrt_out2_inf = dbClient.query('select last(*) from KE_1_L_STAC_CENT_outer_EXIT_SE_37_COUNT_MV')
    St_ExitPrt_out2_list = list(St_ExitPrt_out2_inf.get_points())
    St_ExitPrt_out2= int(St_ExitPrt_out2_list[0]['last_value'])


    St_ExitPrt_Inn_inf = dbClient.query('select last(*) from KE_1_L_STAC_CENT_inner_EXIT_SE_76_COUNT_MV')
    St_ExitPrt_Inn_list = list(St_ExitPrt_Inn_inf.get_points())
    St_ExitPrt_Inn= int(St_ExitPrt_Inn_list[0]['last_value'])


    StPr_inf = dbClient.query('select last(*) from KE_1_L_STAC_CENT_pairing_SE_81_COUNT_MV')
    StPr_list = list(StPr_inf.get_points())
    StPr= int(StPr_list[0]['last_value'])

    st.append(St_EntryPrt_out)
    st.append(St_EntryPrt_Inn)
    st.append(St_ExitPrt_out)
    st.append(St_ExitPrt_out2)
    st.append(St_ExitPrt_Inn)
    st.append(StPr)

    #[time, St_EntryPrt_Out, St_EntryPrt_Inn, St_ExitPrt_out, St_ExitPrt_out2,  St_ExitPrt_Inn ,  StPr ]
    return st


def P2Collect():
    dbClient = InfluxDBClient('10.212.129.14', 8086, 'Fatima_Ezzahrae.Benhadi', 'InfluxDB4AGCKen!', 'historian')
    P2 = []
    t = datetime.datetime.now()
    P2.append(t)

    #----------------------------P2-----------------------------------
    
    Delivred_to_P2_inf = dbClient.query('select last(*) from KE_1_L_PRINT_BELT_Sending_P2_EXIT_SE_43_ONOFF_MV')
    Delivred_to_P2_list = list(Delivred_to_P2_inf.get_points())
    Delivred_to_P2= Delivred_to_P2_list[0]['last_value_bool']
    P2.append(Delivred_to_P2)

    EntryP2_inf = dbClient.query('select last(*) from KE_1_L_FURN_BELT_P2_ENTR_SE_ONOFF_MV')
    EntryP2_list = list(EntryP2_inf.get_points())
    EntryP2= EntryP2_list[0]['last_value_bool']
    P2.append(EntryP2)

    ExitP2_inf = dbClient.query('select last(*) from KE_1_L_FURN_BELT_P2_EXIT_SE_ONOFF_MV')
    ExitP2_list = list(ExitP2_inf.get_points())
    ExitP2= ExitP2_list[0]['last_value_bool']

    P2.append(ExitP2)
    #--------------------------PWD----------------------------------------

    Befor_PWM_Inn_inf = dbClient.query('select last(*) from KE_1_L_POWD_BELT_Inner_ENTR_SE_ONOFF_MV')
    Befor_PWM_Inn_list = list(Befor_PWM_Inn_inf.get_points())
    Befor_PWM_Inn= Befor_PWM_Inn_list[0]['last_value_bool']

    P2.append(Befor_PWM_Inn)

    Befor_PWM_Out_inf = dbClient.query('select last(*) from KE_1_L_POWD_BELT_outer_ENTR_SE_ONOFF_MV')
    Befor_PWM_Out_list = list(Befor_PWM_Out_inf.get_points())
    Befor_PWM_Out= Befor_PWM_Out_list[0]['last_value_bool']
    P2.append(Befor_PWM_Out)

    after_PWM_inf = dbClient.query('select last(*) from KE_1_L_PAIR_BELT_conv_80_ENTR_SE_ONOFF_MV')
    after_PWM_list = list(after_PWM_inf.get_points())
    after_PWM= after_PWM_list[0]['last_value_bool']

    P2.append(after_PWM)

    #[t, Delivred_to_P2, EntryP2, ExitP2, BeforpwmInn,BeforpwmOut, afterPWM ]
    return P2


def ALS():
    
    dbClient = InfluxDBClient('10.212.129.14', 8086, 'Fatima_Ezzahrae.Benhadi', 'InfluxDB4AGCKen!', 'historian')
    ALS = []
    t = datetime.datetime.now()
    ALS.append(t)
    
    EntryLif_inf = dbClient.query('select last(*) from KE_1_L_LIFT_CENT_ALS_ENTR_SE_ONOFF_MV')
    EntryLif_list = list(EntryLif_inf.get_points())
    EntryLif= EntryLif_list[0]['last_value_bool']


    Exitlif_inf = dbClient.query('select last(*) from KE_1_L_LIFT_CENT_ALS_EXIT_SE_ONOFF_MV	')
    Exitlif_list = list(Exitlif_inf.get_points())
    Exitlif= Exitlif_list[0]['last_value_bool']

    ALS.append(EntryLif)
    ALS.append(Exitlif)

    return(ALS)


def InsertInto(connection, Val):

    InsertFlag = False
    sql = 'INSERT INTO Counters VALUES '+str(tuple(Val))
    INS = connection.cursor()
    INS.execute(sql)
    connection.commit()
    InsertFlag = True
    return(InsertFlag)


d=ALS()
print(d)