# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:02:02 2021

@author: MA117284
"""

import datetime
from Config import *


def collectCutting(commCut):
    Cut = []
    t = datetime.datetime.now()
    Cut.append(t)
    Loader = commCut.Read("Belt7_IN0_counter_ls")
    Cut.append(Loader.Value)

    EntryCel1 = commCut.Read("Belt20_B33_counter_ls")
    print({"log_value": "EntryCel1", "log_message": "EntryCel1, Cardinal => {}".format(EntryCel1.Value)})
    EntryCel2 = commCut.Read("Belt40_B33_counter_ls")
    EntryCel3 = commCut.Read("Belt60_B33_counter_ls")

    ExitCel1 = commCut.Read("Belt100_B17_counter_ls")
    ExitCel2 = commCut.Read("Belt103_B17_counter_ls")
    ExitCel3 = commCut.Read("Belt106_B17_counter_ls")

    Cut.append(EntryCel1.Value)
    Cut.append(EntryCel2.Value)
    Cut.append(EntryCel3.Value)

    Cut.append(ExitCel1.Value)
    Cut.append(ExitCel2.Value)
    Cut.append(ExitCel3.Value)
    #[time , Loader , EntryCel1, EntryCel2 , EntryCel2 , EntryCel3]
    return(Cut)


def PrintingCollect(commOut, commInn):

    PR = []
    t = datetime.datetime.now()
    PR.append(t)

    #ConvEntryPrinting= commOut.Read("pt03.GL_ON")
    # PR.append(ConvEntryPrinting)

    ConvInputprt_All = commOut.Read("pt12_GL_ON_counter_ls")
    PR.append(ConvInputprt_All.Value)

    ConvInputprt_Inner = commInn.Read("ptPREENTRY_GL_ON_counter_ls")
    PR.append(ConvInputprt_Inner.Value)

    ConvInputprt_outer = commOut.Read("ptPREENTRY_GL_ON_counter_ls")
    PR.append(ConvInputprt_outer.Value)

    ConvExit_Inner = commInn.Read("ptANALISYS_GL_ON_counter_ls")
    PR.append(ConvExit_Inner.Value)

    ConvExit_Out = commOut.Read("ptANALISYS_GL_ON_counter_ls")
    PR.append(ConvExit_Out.Value)

    #PR[Time, EntryAll, EntryInner, EntryOuter, ExitInner, ExitOuter ]
    #PR[time,ConvInputprt, ConvInner, ConvOut]
    return(PR)


def St_Collect(commOut, commInn):
    st = []
    t = datetime.datetime.now()
    st.append(t)

    St_EntryPrt_out = commOut.Read("P16_Stacker.NUM")
    St_EntryPrt_Inn = commInn.Read("P54_Stacker.NUM")
    St_ExitPrt_out  = commOut.Read("P26_Stacker.NUM")
    St_ExitPrt_out2 = commInn.Read("P37_Stacker.NUM")
    St_ExitPrt_Inn  = commInn.Read("P76_Stacker.NUM")
    StPr            = commInn.Read("P81_Stacker.NUM")

    st.append(St_EntryPrt_out.Value)
    st.append(St_EntryPrt_Inn.Value)
    st.append(St_ExitPrt_out.Value)
    st.append(St_ExitPrt_out2.Value)
    st.append(St_ExitPrt_Inn.Value)
    st.append(StPr.Value)

    #[time, St_EntryPrt_Out, St_EntryPrt_Inn, St_ExitPrt_out, St_ExitPrt_out2,  St_ExitPrt_Inn ,  StPr ]
    return st


def P2Collect(commP2, commPWM, commOut):

    P2 = []
    t = datetime.datetime.now()
    P2.append(t)
    DeliveredP2 = commOut.Read("pt43_GL_ON_counter_ls")
    P2.append(DeliveredP2.Value)
    
    EntryP2 = commOut.Read("LOADING_TO_P2_SENDING_counter_ls")
    P2.append(EntryP2.Value)
    ExitP2 = commInn.Read("comRXfromP2_SENDING_counter_ls")
    P2.append(ExitP2.Value)

    Befor_PWM_Inn = commPWM.Read("pt75_GL_ON_counter_ls")
    P2.append(Befor_PWM_Inn.Value)

    Befor_PWM_Out = commPWM.Read("pt90_GL_ON_counter_ls")
    P2.append(Befor_PWM_Out.Value)

    after_PWM = commPWM.Read("pt80_GL_ON_counter_ls")
    P2.append(after_PWM.Value)

    #[t, EntryP2, ExitP2, BeforpwmInn,BeforpwmOut, afterPWM ]
    return P2


def ALS(commALS):

    ALS = []
    t = datetime.datetime.now()
    ALS.append(t)
    EntryLif = commALS.Read("LI106_GLASS_counter_ls")
    Exitlif = commALS.Read("LI202_SENDING_GLASS_counter_ls")
    ALS.append(EntryLif.Value)
    ALS.append(Exitlif.Value)

    return(ALS)


def InsertInto(connection, Val):

    InsertFlag = False
    sql = 'INSERT INTO Counters VALUES '+str(tuple(Val))
    INS = connection.cursor()
    INS.execute(sql)
    connection.commit()
    InsertFlag = True
    return(InsertFlag)
















"""
while True:
    print('#---------------cutting----------------------------------------------')
    print(collectCutting(commCut))
    print('#---------------printing----------------------------------------------')
    print(PrintingCollect(commOut, commInn))
    print('#---------------P2----------------------------------------------')
    print(P2Collect(commP2, commPWM, commOut))
    print('#---------------ALS----------------------------------------------')
    print(ALS(commALS))
    print('##########################################################')
"""