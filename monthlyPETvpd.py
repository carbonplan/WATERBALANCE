# Generated with SMOP  0.41
from libsmop import *

# monthlyPETvpd.m


@function
def monthlyPET(
    radiation=None,
    tmax=None,
    tmin=None,
    wind=None,
    Lat=None,
    Z=None,
    albedo=None,
    vpd=None,
    *args,
    **kwargs
):
    varargin = monthlyPET.varargin
    nargin = monthlyPET.nargin

    # Calculates potential evapotranspiration using Pennman-Montieth equation
    # source: Allen et al. 1998
    # Input: (radiation in MJ/m2/d), tmax,tmin in C, wind in m/s, month
    # lasttmean is temperature difference from last month
    # Lon, Lat, Z
    # Uses function nanmean

    # convert radiation from W/m2 to MJ/d

    nn = size(radiation)
    # monthlyPETvpd.m:11
    if ndims(radiation) == 3:
        s1 = size(radiation)
        # monthlyPETvpd.m:13
        radiation = reshape(shiftdim(radiation, 2), 12, dot(s1(1), s1(2))).T
        # monthlyPETvpd.m:14
        tmax = reshape(shiftdim(tmax, 2), 12, dot(s1(1), s1(2))).T
        # monthlyPETvpd.m:15
        tmin = reshape(shiftdim(tmin, 2), 12, dot(s1(1), s1(2))).T
        # monthlyPETvpd.m:16
        wind = reshape(shiftdim(wind, 2), 12, dot(s1(1), s1(2))).T
        # monthlyPETvpd.m:17
        vpd = reshape(shiftdim(vpd, 2), 12, dot(s1(1), s1(2))).T
        # monthlyPETvpd.m:18
        Lat = ravel(Lat)
        # monthlyPETvpd.m:19
        Z = ravel(Z)
    # monthlyPETvpd.m:19

    radiation = dot(radiation, 0.0864)
    # monthlyPETvpd.m:22
    daysinmonth = concat([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])
    # monthlyPETvpd.m:24
    d2 = concat([31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365])
    # monthlyPETvpd.m:25
    d1 = concat([1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335])
    # monthlyPETvpd.m:26
    # calculate change in temperature from month to month
    tmean = (tmax + tmin) / 2
    # monthlyPETvpd.m:29
    # calculate change in temperature from month to month
    lasttmean = dot(NaN, ones(size(tmax)))
    # monthlyPETvpd.m:32
    tmean = (tmax + tmin) / 2
    # monthlyPETvpd.m:33
    for i in arange(2, size(tmax, 2)).reshape(-1):
        lasttmean[arange(), i] = tmean(arange(), i) - tmean(arange(), i - 1)
    # monthlyPETvpd.m:35

    lasttmean[arange(), 1] = tmean(arange(), 1) - tmean(arange(), size(tmean, 2))
    # monthlyPETvpd.m:37
    # wind adjustment to 2m from 10m output, can be changed for ET at
    # elevations other than 2m, but need to scale using logarithmic increase in
    # wind speed with elevation

    wind = dot(wind, (4.87 / log(dot(67, 10) - 5.42)))
    # monthlyPETvpd.m:43
    # Saturation vapor pressure , assume sat vap pressure is TMIN-2
    es1 = dot(0.6108, exp(dot(tmin, 17.27) / (tmin + 237.3)))
    # monthlyPETvpd.m:46
    es2 = dot(0.6108, exp(dot(tmax, 17.27) / (tmax + 237.3)))
    # monthlyPETvpd.m:47
    es = es1 / 2.0 + es2 / 2.0
    # monthlyPETvpd.m:48
    # ea = 0.6108 * exp(tdew * 17.27./ (tdew + 237.3));
    # vpd=es-ea;
    ea = es - vpd
    # monthlyPETvpd.m:51
    g = find(vpd < 0)
    # monthlyPETvpd.m:52
    vpd[g] = 0
    # monthlyPETvpd.m:52
    # VPD - Vapor pressure deficit
    # ea=es-vpd;
    # VPD = es - ea; # (kPa)
    # DEL - Slope of the saturation vapor pressure vs. air temperature curve at the average hourly air temperature
    DEL = (dot(4098, es)) / (tmean + 237.3) ** 2
    # monthlyPETvpd.m:57
    # Barometric pressure
    P = dot(101.3, ((293 - dot(0.0065, Z)) / 293) ** 5.26)
    # monthlyPETvpd.m:61

    lambda_ = 2.501 - dot(0.002361, tmean)
    # monthlyPETvpd.m:62
    # GAM - Psychrometer constant (kPa C-1) \

    GAM = dot(0.00163, repmat(P, concat([1, 12]))) / lambda_
    # monthlyPETvpd.m:65
    # GAM2=6.65e-4.*repmat(P',[1 12]);
    # GAM = 0.000646 * (1 + 0.000946*tmean) .* repmat(P',[1 12]); # CIMIS
    # W - Weighting function
    # W = DEL./(DEL + GAM);

    GSC = 0.082
    # monthlyPETvpd.m:73

    phi = dot(pi, Lat) / 180
    # monthlyPETvpd.m:75
    for doy in arange(1, 12).reshape(-1):
        # should average this over a month
        # Calculate potential max solar radiation or clear sky radiation
        # assumed to be 75# TOA shortwave radiation or cloudless day, FAO, 1998
        clear("Rso")
        for i in arange(1, daysinmonth(doy)).reshape(-1):
            DoY = d1(doy) - 1 + i
            # monthlyPETvpd.m:83
            dr = 1 + dot(0.033, cos(dot(dot(2, pi) / 365, DoY)))
            # monthlyPETvpd.m:84
            delta = dot(0.409, sin(dot(dot(2, pi) / 365, DoY) - 1.39))
            # monthlyPETvpd.m:85
            omegas = acos(multiply(-tan(phi), tan(delta)))
            # monthlyPETvpd.m:86
            Ra = multiply(
                multiply(multiply(dot(24, 60) / pi, GSC), dr),
                (
                    multiply(multiply(omegas, sin(phi)), sin(delta))
                    + multiply(multiply(cos(phi), cos(delta)), sin(omegas))
                ),
            )
            # monthlyPETvpd.m:87
            Rso[arange(), i] = multiply(Ra, (0.75 + dot(2e-05, Z)))
        # monthlyPETvpd.m:88
        # incomming solar radiation has already been corrected for macroscale
        # albedo, may need to calibrate for actual albedo
        Rso = real(mean(Rso, 2))
        # monthlyPETvpd.m:93
        # incomming solar radiation has already been corrected for macroscale
        # albedo, may need to calibrate for actual albedo
        f = find(Rso < logical_or(0, isnan(Rso)) == 1)
        # monthlyPETvpd.m:97
        Rso[f] = 0
        # monthlyPETvpd.m:98
        # lr out, Rso>=radiation
        # radfraction is a measure of relative shortwave radiation, or # of
        # possible radiation, needs to be less than 1
        radfract = radiation(arange(), doy) / Rso
        # monthlyPETvpd.m:104
        f = find(radfract > 1)
        # monthlyPETvpd.m:105
        radfract[f] = 1
        # monthlyPETvpd.m:105
        f = find(isinf(radfract) == 1)
        # monthlyPETvpd.m:106
        radfract[f] = 1
        # monthlyPETvpd.m:106
        f = find(isnan(radfract) == 1)
        # monthlyPETvpd.m:107
        radfract[f] = 1
        # monthlyPETvpd.m:107
        longw = multiply(
            dot(
                dot(
                    4.903e-09,
                    (
                        (tmax(arange(), doy) + 273.15) ** 4
                        + (tmin(arange(), doy) + 273.15) ** 4
                    ),
                )
                / 2.0,
                (0.34 - dot(0.14, sqrt(ea(arange(), doy)))),
            ),
            (dot(1.35, radfract) - 0.35),
        )
        # monthlyPETvpd.m:108
        # [nmean(longw(:))]
        # netrad
        netrad = dot(
            real(multiply(radiation(arange(), doy), (1 - albedo)) - longw),
            daysinmonth(doy),
        )
        # monthlyPETvpd.m:111
        # nmean(netrad(:))
        # soil heat flux
        G = dot(dot(0.14, (lasttmean(arange(), doy))), daysinmonth(doy))
        # monthlyPETvpd.m:114
        # ET
        TERM1_NUMERATOR = multiply(dot(0.408, DEL(arange(), doy)), (netrad - G))
        # monthlyPETvpd.m:117
        TERM2_NUMERATOR = dot(
            multiply(
                multiply(
                    multiply(GAM(arange(), doy), wind(arange(), doy)),
                    vpd(arange(), doy),
                ),
                900.0,
            )
            / (273.15 + tmean(arange(), doy)),
            daysinmonth(doy),
        )
        # monthlyPETvpd.m:118
        DENOMINATOR = DEL(arange(), doy) + multiply(
            GAM(arange(), doy), (1 + multiply(0.34, wind(arange(), doy)))
        )
        # monthlyPETvpd.m:119
        TERM1 = TERM1_NUMERATOR / DENOMINATOR
        # monthlyPETvpd.m:120
        TERM2 = TERM2_NUMERATOR / DENOMINATOR
        # monthlyPETvpd.m:121
        ET[arange(), doy] = TERM1 + TERM2
    # monthlyPETvpd.m:122
    # [nmean(TERM1) nmean(TERM2)]

    f = find(ET < 0)
    # monthlyPETvpd.m:125
    ET[f] = 0
    # monthlyPETvpd.m:125
    ET = reshape(ET, nn)


# monthlyPETvpd.m:126
