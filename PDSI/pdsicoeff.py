# Generated with SMOP  0.41
from libsmop import *
# pdsicoeff.m

    
@function
def ja_cc_0801(PESUM=None,ETSUM=None,RSUM=None,PRSUM=None,SPSUM=None,ROSUM=None,PLSUM=None,TLSUM=None,*args,**kwargs):
    varargin = ja_cc_0801.varargin
    nargin = ja_cc_0801.nargin

    f1=find(PESUM != 0)
# pdsicoeff.m:2
    if logical_not(isempty(f1)):
        alp[f1]=ETSUM(f1) / PESUM(f1)
# pdsicoeff.m:4
    
    f2=setxor(arange(1,length(PESUM)),f1)
# pdsicoeff.m:6
    if logical_not(isempty(f2)):
        f3=find(ETSUM(f2) == 0)
# pdsicoeff.m:8
        if logical_not(isempty(f3)):
            alp[f2(f3)]=1.0
# pdsicoeff.m:10
        f4=find(ETSUM(f2) != 0)
# pdsicoeff.m:12
        if logical_not(isempty(f4)):
            alp[f2(f4)]=0.0
# pdsicoeff.m:14
    
    #Beta Calcuation
    f5=find(PRSUM != 0)
# pdsicoeff.m:18
    if logical_not(isempty(f5)):
        bet[f5]=RSUM(f5) / PRSUM(f5)
# pdsicoeff.m:20
    
    f6=setxor(arange(1,length(PRSUM)),f5)
# pdsicoeff.m:22
    if logical_not(isempty(f6)):
        f7=find(RSUM(f6) == 0)
# pdsicoeff.m:24
        if logical_not(isempty(f7)):
            bet[f6(f7)]=1.0
# pdsicoeff.m:26
        f8=find(RSUM(f6) != 0)
# pdsicoeff.m:28
        if logical_not(isempty(f8)):
            bet[f6(f8)]=0.0
# pdsicoeff.m:30
    
    #Gamma Calcuation
    f9=find(SPSUM != 0)
# pdsicoeff.m:34
    if logical_not(isempty(f9)):
        gam[f9]=ROSUM(f9) / SPSUM(f9)
# pdsicoeff.m:36
    
    f10=setxor(arange(1,length(SPSUM)),f9)
# pdsicoeff.m:40
    if logical_not(isempty(f10)):
        f11=find(ROSUM(f10) == 0)
# pdsicoeff.m:42
        if logical_not(isempty(f11)):
            gam[f10(f11)]=1.0
# pdsicoeff.m:45
        f12=find(ROSUM(f10) != 0)
# pdsicoeff.m:47
        if logical_not(isempty(f12)):
            gam[f10(f12)]=0.0
# pdsicoeff.m:49
    
    #Delta Calcuation
    f13=find(PLSUM != 0)
# pdsicoeff.m:53
    if logical_not(isempty(f13)):
        del_[f13]=TLSUM(f13) / PLSUM(f13)
# pdsicoeff.m:55
    
    f14=setxor(arange(1,length(PLSUM)),f13)
# pdsicoeff.m:57
    if logical_not(isempty(f14)):
        del_[f14]=0.0
# pdsicoeff.m:59
    
    #alp=ETSUM./PESUM;
#bet=RSUM./PRSUM;
#del=TLSUM./PLSUM;
#gam=ROSUM./SPSUM;
    
    alp=alp.T
# pdsicoeff.m:68
    bet=bet.T
# pdsicoeff.m:69
    gam=gam.T
# pdsicoeff.m:70
    del_=del_.T
# pdsicoeff.m:71
    return alp,bet,gam,del_