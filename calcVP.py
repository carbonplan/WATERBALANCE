# Generated with SMOP  0.41
from libsmop import *
# calcVP.m

    
@function
def calcVPD(Ta=None,P=None,*args,**kwargs):
    varargin = calcVPD.varargin
    nargin = calcVPD.nargin

    # SATVAP: computes saturation vapor pressure
# q=satvap(Ta) computes the vapor pressure at satuation at air
# temperature Ta (deg C). From Gill (1982), Atmos-Ocean Dynamics, 606.
    
    #    INPUT:   Ta- air temperature  [C]
#             p - pressure (optional)  [mb]
    
    #    OUTPUT:  q  - saturation vapour pressure  [mb]
    
    ######################################################################
# 3/8/97: version 1.0
# 8/27/98: version 1.1 (corrected by RP)
# 8/5/99: version 2.0
######################################################################
    
    if nargin == 1:
        P=1013.25
# calcVP.m:18
    
    Ta=Ta - 273.16
# calcVP.m:20
    ew=power(10,((0.7859 + dot(0.03477,Ta)) / (1 + dot(0.00412,Ta))))
# calcVP.m:22
    fw=1 + multiply(dot(1e-06,P),(4.5 + multiply(0.0006,Ta ** 2)))
# calcVP.m:24
    vpd=dot(multiply(fw,ew),100)
# calcVP.m:25