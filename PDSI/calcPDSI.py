# Generated with SMOP  0.41
from libsmop import *

# calcPDSI.m

    
@function
def calc_pdsi(PET=None,ppt1=None,WCTOP=None,WCBOT=None,ss2=None,*args,**kwargs):
    varargin = calc_pdsi.varargin
    nargin = calc_pdsi.nargin

    #INITIALIZE VARS
    WCTOT=WCBOT + WCTOP
# calcPDSI.m:3
    SS=copy(WCTOP)
# calcPDSI.m:4
    SU=copy(WCBOT)
# calcPDSI.m:5
    SPSUM=0
# calcPDSI.m:6
    SPSUM=repmat(SPSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:6
    PLSUM=0
# calcPDSI.m:7
    PLSUM=repmat(PLSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:7
    PRSUM=0
# calcPDSI.m:8
    PRSUM=repmat(PRSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:8
    RSUM=0
# calcPDSI.m:9
    RSUM=repmat(RSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:9
    TLSUM=0
# calcPDSI.m:10
    TLSUM=repmat(TLSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:10
    ETSUM=0
# calcPDSI.m:11
    ETSUM=repmat(ETSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:11
    ROSUM=0
# calcPDSI.m:12
    ROSUM=repmat(ROSUM,concat([size(WCTOT,1),12]))
# calcPDSI.m:12
    DBAR=0
# calcPDSI.m:13
    DBAR=repmat(DBAR,concat([size(WCTOT,1),1]))
# calcPDSI.m:13
    SABSD=0
# calcPDSI.m:14
    SABSD=repmat(SABSD,concat([size(WCTOT,1),12]))
# calcPDSI.m:14
    AK=0
# calcPDSI.m:15
    AK=repmat(AK,concat([size(WCTOT,1),12]))
# calcPDSI.m:15
    AKHAT=0
# calcPDSI.m:16
    AKHAT=repmat(AKHAT,concat([size(WCTOT,1),12]))
# calcPDSI.m:16
    SWTD=0
# calcPDSI.m:17
    SWTD=repmat(SWTD,concat([size(WCTOT,1),12]))
# calcPDSI.m:17
    SP=SS + SU
# calcPDSI.m:18
    PSUM=nansum(ppt1,3)
# calcPDSI.m:19
    PESUM=nansum(PET,3)
# calcPDSI.m:20
    ssz=size(ppt1,3)
# calcPDSI.m:22
    if nargin == 4:
        ss2=copy(ssz)
# calcPDSI.m:24
    
    # fake ten year spinup
    PET[arange(),arange(),arange(11,ssz + 10)]=PET
# calcPDSI.m:27
    PET[arange(),arange(),arange(1,10)]=repmat(nanmean(PET,3),concat([1,1,10]))
# calcPDSI.m:27
    ppt1[arange(),arange(),arange(11,ssz + 10)]=ppt1
# calcPDSI.m:28
    ppt1[arange(),arange(),arange(1,10)]=repmat(nanmean(ppt1,3),concat([1,1,10]))
# calcPDSI.m:28
    #BEGIN REAL STUFF
    for yr in arange(1,(size(ppt1,3))).reshape(-1):
        #if ~isnan(PET(1,1,yr))
        for mo in arange(1,12).reshape(-1):
            PR=WCTOT - SP
# calcPDSI.m:34
            PL,ET,TL,RO,R,SSS,SSU=pdsi_wb(PET(arange(),mo,yr),ppt1(arange(),mo,yr),ravel(WCBOT),ravel(WCTOP),ravel(WCTOT),ravel(SS),ravel(SU),ravel(SP),nargout=7)
# calcPDSI.m:35
            SS=copy(SSS)
# calcPDSI.m:36
            SU=copy(SSU)
# calcPDSI.m:37
            SP=SS + SU
# calcPDSI.m:38
            spdat[arange(),mo,yr]=single(SP)
# calcPDSI.m:39
            pldat[arange(),mo,yr]=single(PL)
# calcPDSI.m:40
            prdat[arange(),mo,yr]=single(PR)
# calcPDSI.m:41
            rdat[arange(),mo,yr]=single(R)
# calcPDSI.m:42
            tldat[arange(),mo,yr]=single(TL)
# calcPDSI.m:43
            etdat[arange(),mo,yr]=single(ET)
# calcPDSI.m:44
            rodat[arange(),mo,yr]=single(RO)
# calcPDSI.m:45
            sssdat[arange(),mo,yr]=single(SSS)
# calcPDSI.m:46
            ssudat[arange(),mo,yr]=single(SSU)
# calcPDSI.m:47
    
    
    #end
    c1=find(rdat >= prdat)
# calcPDSI.m:51
    rdat[c1]=prdat(c1)
# calcPDSI.m:51
    clear('c1')
    c1=find(tldat >= pldat)
# calcPDSI.m:52
    tldat[c1]=pldat(c1)
# calcPDSI.m:52
    clear('c1')
    ini=arange(10 + ss2(1),10 + ss2(length(ss2)))
# calcPDSI.m:53
    SPSUM=nanmean(spdat(arange(),arange(),ini),3)
# calcPDSI.m:54
    PLSUM=nanmean(pldat(arange(),arange(),ini),3)
# calcPDSI.m:55
    PRSUM=nanmean(prdat(arange(),arange(),ini),3)
# calcPDSI.m:56
    RSUM=nanmean(rdat(arange(),arange(),ini),3)
# calcPDSI.m:57
    TLSUM=nanmean(tldat(arange(),arange(),ini),3)
# calcPDSI.m:58
    ETSUM=nanmean(etdat(arange(),arange(),ini),3)
# calcPDSI.m:59
    PESUM=nanmean(PET(arange(),arange(),ini),3)
# calcPDSI.m:60
    ROSUM=nanmean(rodat(arange(),arange(),ini),3)
# calcPDSI.m:61
    PSUM=nanmean(ppt1(arange(),arange(),ini),3)
# calcPDSI.m:62
    #CAFEC
    for mo in arange(1,12).reshape(-1):
        alp(arange(),mo),bet(arange(),mo),gam(arange(),mo),del_(arange(),mo)=pdsicoeff(PESUM(arange(),mo),ETSUM(arange(),mo),RSUM(arange(),mo),PRSUM(arange(),mo),SPSUM(arange(),mo),ROSUM(arange(),mo),PLSUM(arange(),mo),TLSUM(arange(),mo),nargout=4)
# calcPDSI.m:66
    
    clear('mo')
    TRAT=(PESUM + RSUM + ROSUM) / (PSUM + TLSUM)
# calcPDSI.m:72
    clear('PESUM','RSUM','ROSUM','PSUM','TLSUM','ETSUM','PRSUM','SPSUM','PLSUM')
    PHAT=multiply(PET,repmat(alp,concat([1,1,size(PET,3)]))) + multiply(prdat,repmat(bet,concat([1,1,size(PET,3)]))) + multiply(spdat,repmat(gam,concat([1,1,size(PET,3)]))) - multiply(pldat,repmat(del_,concat([1,1,size(PET,3)])))
# calcPDSI.m:73
    DD=ppt1 - PHAT
# calcPDSI.m:74
    SABSD=abs(DD)
# calcPDSI.m:75
    DBAR=nanmean(SABSD,3)
# calcPDSI.m:77
    AKHAT=dot(1.5,log10((TRAT + dot(2.8,25.4)) / DBAR)) + 0.5
# calcPDSI.m:78
    f=AKHAT < 0
# calcPDSI.m:79
    AKHAT[f]=0
# calcPDSI.m:79
    clear('f')
    SWTD=sum(multiply(DBAR,AKHAT),2)
# calcPDSI.m:80
    AK=dot(dot(17.67,25.4),AKHAT) / repmat(SWTD,concat([1,12]))
# calcPDSI.m:82
    Z_1=multiply(DD / 25.4,repmat(AK,concat([1,1,size(DD,3)])))
# calcPDSI.m:83
    SOIL=reshape(sssdat + ssudat,size(sssdat,1),dot(size(sssdat,2),size(sssdat,3)))
# calcPDSI.m:84
    clear('AK','AKHAT','DBAR','DD','PET','SABSD','SWTD','alp','bet','del','gam','pldat','ppt1','prdat','rdat','rodat','sssdat','ssudat','tldat')
    # limit Z scores to +/- 16
    f10=Z_1 > 16
# calcPDSI.m:89
    Z_1[f10]=16
# calcPDSI.m:89
    clear('f10')
    f10=Z_1 < - 16
# calcPDSI.m:90
    Z_1[f10]=- 16
# calcPDSI.m:90
    clear('f10')
    PDSI=dot(NaN,ones(size(Z_1,1),dot(size(Z_1,2),size(Z_1,3))))
# calcPDSI.m:91
    for i in arange(1,size(PDSI,1)).reshape(-1):
        if max(Z_1(i,arange())) > 0:
            PDSI(i,arange()),X1,X2,X3,Pe,montho=PDSIr((Z_1(i,arange())),nargout=6)
# calcPDSI.m:94
    
    clear('i')
    #matlabpool close
    PDSI=PDSI(arange(),arange(121,size(PDSI,2)))
# calcPDSI.m:98
    SOIL=SOIL(arange(),arange(121,size(SOIL,2)))
# calcPDSI.m:99
    size(Z_1)
    Z_1=Z_1(arange(),arange(121,dot(size(Z_1,2),size(Z_1,3))))
# calcPDSI.m:101
    return PDSI,SOIL,Z_1