# Generated with SMOP  0.41
from libsmop import *
# PDSI/pdsi_wb.m

    
@function
def pdsi_wb(PET=None,P=None,WCBOT=None,WCTOP=None,WCTOT=None,SS=None,SU=None,SP=None,*args,**kwargs):
    varargin = pdsi_wb.varargin
    nargin = pdsi_wb.nargin

    #Created 06/18/11 by Jacob Wolf at the University of Idaho
#Recharge, Runoff, Residual Moisture, Loss to both SFC and Under Layers,
#depending on starting moisture content and vals of PPT and PET.
#from Palmer 1965.
    
    PET=PET.T
# PDSI/pdsi_wb.m:7
    P=P.T
# PDSI/pdsi_wb.m:8
    WCBOT=WCBOT.T
# PDSI/pdsi_wb.m:9
    WCTOP=WCTOP.T
# PDSI/pdsi_wb.m:10
    WCTOT=WCTOT.T
# PDSI/pdsi_wb.m:11
    SS=SS.T
# PDSI/pdsi_wb.m:12
    SU=SU.T
# PDSI/pdsi_wb.m:13
    SP=SP.T
# PDSI/pdsi_wb.m:14
    # check on inverting matrices
# bottomfactor, loss
    
    PR=WCTOT - SP
# PDSI/pdsi_wb.m:19
    PRS=WCTOP - SS
# PDSI/pdsi_wb.m:20
    PRU=WCBOT - SU
# PDSI/pdsi_wb.m:21
    PL=dot(NaN,ones(size(P)))
# PDSI/pdsi_wb.m:22
    ET=copy(PL)
# PDSI/pdsi_wb.m:22
    TL=copy(PL)
# PDSI/pdsi_wb.m:22
    RO=copy(PL)
# PDSI/pdsi_wb.m:22
    R=copy(PL)
# PDSI/pdsi_wb.m:22
    SSS=copy(PL)
# PDSI/pdsi_wb.m:22
    SSU=copy(PL)
# PDSI/pdsi_wb.m:22
    f1=find(SS >= PET)
# PDSI/pdsi_wb.m:23
    if logical_not(isempty(f1)):
        PL[f1]=PET(f1)
# PDSI/pdsi_wb.m:25
    
    f2=find(SS < PET)
# PDSI/pdsi_wb.m:27
    if logical_not(isempty(f2)):
        straw=SU(f2) / WCTOT(f2)
# PDSI/pdsi_wb.m:29
        demand=PET(f2) - SS(f2)
# PDSI/pdsi_wb.m:30
        f5=find(demand > SU(f2))
# PDSI/pdsi_wb.m:31
        demand[f5]=SU(f2(f5))
# PDSI/pdsi_wb.m:32
        PL[f2]=multiply(demand,straw) + SS(f2)
# PDSI/pdsi_wb.m:33
        f4=find(PL(f2) > SP(f2))
# PDSI/pdsi_wb.m:34
        PL[f2(f4)]=SP(f2(f4))
# PDSI/pdsi_wb.m:34
        clear('straw','demand')
    
    test2=find(P >= PET)
# PDSI/pdsi_wb.m:36
    if logical_not(isempty(test2)):
        # PPT exceeds PET
        ET[test2]=PET(test2)
# PDSI/pdsi_wb.m:39
        TL[test2]=0.0
# PDSI/pdsi_wb.m:40
        test3=find((P(test2) - PET(test2)) > (PRS(test2)))
# PDSI/pdsi_wb.m:41
        if logical_not(isempty(test3)):
            # PPT recharges under and upper layers
            RS[test2(test3)]=PRS(test2(test3))
# PDSI/pdsi_wb.m:44
            SSS[test2(test3)]=WCTOP(test2(test3))
# PDSI/pdsi_wb.m:45
            test4=find((P(test2(test3)) - PET(test2(test3)) - RS(test2(test3))) < (PRU(test2(test3))))
# PDSI/pdsi_wb.m:46
            #        test4=find((P(test2(test3))-PET(test2(test3))-RS(test2(test3)))<(WCBOT(test2(test3))-SU(test2(test3))));
            if logical_not(isempty(test4)):
                # Both layers can take entire excess
                RU[test2(test3(test4))]=P(test2(test3(test4))) - PET(test2(test3(test4))) - RS(test2(test3(test4)))
# PDSI/pdsi_wb.m:50
                RO[test2(test3(test4))]=0.0
# PDSI/pdsi_wb.m:51
            test5=setxor(arange(1,length(test2(test3))),test4)
# PDSI/pdsi_wb.m:53
            if logical_not(isempty(test5)):
                RU[test2(test3(test5))]=WCBOT(test2(test3(test5))) - SU(test2(test3(test5)))
# PDSI/pdsi_wb.m:55
                RO[test2(test3(test5))]=P(test2(test3(test5))) - PET(test2(test3(test5))) - RS(test2(test3(test5))) - RU(test2(test3(test5)))
# PDSI/pdsi_wb.m:56
            SSU[test2(test3)]=SU(test2(test3)) + RU(test2(test3))
# PDSI/pdsi_wb.m:58
            R[test2(test3)]=RS(test2(test3)) + RU(test2(test3))
# PDSI/pdsi_wb.m:59
        test6=setxor(arange(1,length(test2)),test3)
# PDSI/pdsi_wb.m:61
        if logical_not(isempty(test6)):
            R[test2(test6)]=P(test2(test6)) - PET(test2(test6))
# PDSI/pdsi_wb.m:63
            SSS[test2(test6)]=SS(test2(test6)) + P(test2(test6)) - PET(test2(test6))
# PDSI/pdsi_wb.m:64
            SSU[test2(test6)]=SU(test2(test6))
# PDSI/pdsi_wb.m:65
            RO[test2(test6)]=0.0
# PDSI/pdsi_wb.m:66
    
    f12=find(R > PR)
# PDSI/pdsi_wb.m:69
    R[f12]=PR(f12)
# PDSI/pdsi_wb.m:69
    testa=setxor(arange(1,length(P)),test2)
# PDSI/pdsi_wb.m:71
    
    if logical_not(isempty(testa)):
        R[testa]=0.0
# PDSI/pdsi_wb.m:73
        testb=find(SS(testa) >= (PET(testa) - P(testa)))
# PDSI/pdsi_wb.m:74
        if logical_not(isempty(testb)):
            # Evap from surface layer only
            SL[testa(testb)]=PET(testa(testb)) - P(testa(testb))
# PDSI/pdsi_wb.m:77
            SSS[testa(testb)]=SS(testa(testb)) - SL(testa(testb))
# PDSI/pdsi_wb.m:78
            UL[testa(testb)]=0.0
# PDSI/pdsi_wb.m:79
            SSU[testa(testb)]=SU(testa(testb))
# PDSI/pdsi_wb.m:80
        testc=setxor(arange(1,length(testa)),testb)
# PDSI/pdsi_wb.m:82
        if logical_not(isempty(testc)):
            SL[testa(testc)]=SS(testa(testc))
# PDSI/pdsi_wb.m:84
            SSS[testa(testc)]=0.0
# PDSI/pdsi_wb.m:85
            demand=PET(testa(testc)) - P(testa(testc)) - SL(testa(testc))
# PDSI/pdsi_wb.m:86
            f5=find(demand > SU(testa(testc)))
# PDSI/pdsi_wb.m:88
            demand[f5]=SU(testa(testc(f5)))
# PDSI/pdsi_wb.m:89
            straw=SU(testa(testc)) / WCTOT(testa(testc))
# PDSI/pdsi_wb.m:90
            drainsoil=multiply(- demand,straw)
# PDSI/pdsi_wb.m:91
            SSU[testa(testc)]=SSU(testa(testc)) + drainsoil
# PDSI/pdsi_wb.m:92
            UL[testa(testc)]=- drainsoil
# PDSI/pdsi_wb.m:93
            f4=find(UL(testa(testc)) > SU(testa(testc)))
# PDSI/pdsi_wb.m:94
            if logical_not(isempty(f4)):
                UL[testa(testc(f4))]=SU(testa(testc(f4)))
# PDSI/pdsi_wb.m:96
            SSU[testa(testc)]=SU(testa(testc)) - UL(testa(testc))
# PDSI/pdsi_wb.m:98
        TL[testa]=SL(testa) + UL(testa)
# PDSI/pdsi_wb.m:100
        RO[testa]=0.0
# PDSI/pdsi_wb.m:101
        ET[testa]=P(testa) + SL(testa) + UL(testa)
# PDSI/pdsi_wb.m:102
        f=find(PET(testa) < ET(testa))
# PDSI/pdsi_wb.m:103
        ET[testa(f)]=PET(testa(f))
# PDSI/pdsi_wb.m:103
    
    #ET(f)=PET(f);
    ET=ET.T
# PDSI/pdsi_wb.m:107
    R=R.T
# PDSI/pdsi_wb.m:108
    RO=RO.T
# PDSI/pdsi_wb.m:109
    SSS=SSS.T
# PDSI/pdsi_wb.m:110
    SSU=SSU.T
# PDSI/pdsi_wb.m:111
    TL=TL.T
# PDSI/pdsi_wb.m:112
    PL=PL.T
# PDSI/pdsi_wb.m:113
    f=find(isnan(PET))
# PDSI/pdsi_wb.m:114
    ET[f]=NaN
# PDSI/pdsi_wb.m:115
    R[f]=NaN
# PDSI/pdsi_wb.m:116
    RO[f]=NaN
# PDSI/pdsi_wb.m:117
    SSS[f]=NaN
# PDSI/pdsi_wb.m:118
    SSU[f]=NaN
# PDSI/pdsi_wb.m:119
    TL[f]=NaN
# PDSI/pdsi_wb.m:120
    PL[f]=NaN
# PDSI/pdsi_wb.m:121
    #f=find(ET>PET);ET(f)=PET(f);
#f=find(TL>PL);TL(f)=PL(f);
    return PL,ET,TL,RO,R,SSS,SSU