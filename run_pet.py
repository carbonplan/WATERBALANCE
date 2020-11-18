# Generated with SMOP  0.41
from libsmop import *
# run_pet.m

    
@function
def run_pet(vap=None,tmax=None,tmin=None,srad=None,ws=None,el=None,*args,**kwargs):
    varargin = run_pet.varargin
    nargin = run_pet.nargin

    # approximate surface pressure from elevation
    P=dot(1013.25,((293 - dot(0.0065,el)) / 293) ** 5.26)
# run_pet.m:4
    vpn=calcVP(tmin + 273.15,repmat(P,concat([1,1,12])))
# run_pet.m:6
    vpx=calcVP(tmax + 273.15,repmat(P,concat([1,1,12])))
# run_pet.m:7
    vpn=vpn / 1000
# run_pet.m:8
    vpx=vpx / 1000
# run_pet.m:8
    vpd=vpn / 2 + vpx / 2 - vap
# run_pet.m:9
    vpd[vpd < 0]=0
# run_pet.m:10
    clear('vap','vpx','vpn','clear','vap')
    tmax=shiftdim(tmax,2)
# run_pet.m:12
    tmin=shiftdim(tmin,2)
# run_pet.m:13
    ws=shiftdim(ws,2)
# run_pet.m:14
    srad=shiftdim(srad,2)
# run_pet.m:15
    vpd=shiftdim(vpd,2)
# run_pet.m:16
    petdata=dot(NaN,ones(12,4320,8640))
# run_pet.m:17
    
    f=find(logical_not(isnan(tmax(1,arange()))) == 1)
# run_pet.m:19
    vpd=vpd(arange(),f)
# run_pet.m:20
    tmax=tmax(arange(),f)
# run_pet.m:21
    tmin=tmin(arange(),f)
# run_pet.m:22
    srad=srad(arange(),f)
# run_pet.m:23
    ws=ws(arange(),f)
# run_pet.m:24
    ET=monthlyPETvpd(srad.T / 86.4,tmax.T,tmin.T,ws.T,lat(f).T,el(f).T,0.23,vpd.T)
# run_pet.m:25
    petdata[arange(),f]=ET.T
# run_pet.m:26
    
    # purposes; this may or not be needed depending on application
    t=1 - runsnow(tmax / 2 + tmin / 2,ones(size(tmax)))
# run_pet.m:30
    petdata[arange(),f]=multiply(ET.T,t.T)
# run_pet.m:31