# ins: clay silt and sand as inputs (in %)
# outs: texture name and saturated hydraulic conductivity (in cm per day)
def soiltext(cl,si,sa):

    texture = np.nan 
    K_cm_d = np.nan 

    if (0 < cl < 10) and (0 < si < 15) and ( 85 < sa < 100):
        texture = 'sand'
        K_cm_d = 712.8
    if (0 < cl < 15) and (0 < si < 30) and ( 70 < sa < 90):
        texture = 'loamy_sand'
        K_cm_d = 350.2
    if (0 < cl < 20) and (0 < si < 50) and ( 43 < sa < 85):
        texture = 'sandy_loam'
        K_cm_d = 106.1
    if (35 < cl < 55) and (0 < si < 20) and ( 45 < sa < 65):
        texture = 'sandy_clay'
        K_cm_d = 2.88
    if (25 < cl < 40) and (40 < si < 75) and ( 0 < sa < 20):
        texture = 'silty_clay_loam'
        K_cm_d = 1.68
    if (5 < cl < 39) and (25 < si < 50) and ( 25 < sa < 55):
        texture = 'loam'
        K_cm_d = 24.96
    if (0 < cl < 27) and (50 < si < 100) and ( 0 < sa < 50):
        texture = 'silt_loam'
        K_cm_d = 10.8
    if (27 < cl < 40) and (15 < si < 55) and ( 20 < sa < 45):
        texture = 'clay_loam'
        K_cm_d = 6.24
    if (0 < cl < 12) and (80 < si < 100) and ( 0 < sa < 20):
        texture = 'silt'
        K_cm_d = 6
    if (20 < cl < 35) and ( 0 < si < 30) and ( 45 < sa < 80 ):
        texture = 'sandy_clay_loam'
        K_cm_d = 31.44
    if (40 < cl < 60) and (40 < si < 60) and ( 0 < sa < 20):
        texture = 'silty_clay'
        K_cm_d = 0.48
    if (40 < cl < 100) and (0 < si < 40) and ( 0 < sa < 45):
        texture = 'clay'
        K_cm_d = 4.80

    return np.array([texture,K_cm_d])
