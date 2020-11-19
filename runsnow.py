# Generated with SMOP  0.41
from libsmop import *

# runsnow.m


@function
def runsnow(temp=None, precip=None, *args, **kwargs):
    varargin = runsnow.varargin
    nargin = runsnow.nargin

    a = -48.2292
    # runsnow.m:2
    b = 0.7205
    # runsnow.m:3
    c = 1.1662
    # runsnow.m:4
    d = 1.0223
    # runsnow.m:5
    temp = temp - 273.15
    # runsnow.m:6
    snowf = dot(a, (tanh(dot(b, (temp - c))) - d))
    # runsnow.m:7
    f = find(temp < -2)
    # runsnow.m:8
    snowf[f] = 100
    # runsnow.m:8
    f = find(temp > 6.5)
    # runsnow.m:9
    snowf[f] = 0
    # runsnow.m:9
    snow = single(dot(snowf / 100.0, precip))


# runsnow.m:10
