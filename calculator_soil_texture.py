def soiltext(cl,si,sa):

    if (0 < cl < 10) and (0 < si < 15) and ( 85 < sa < 100):
        texture = 'sand'
        WP2FC = 0.50
    if (0 < cl < 15) and (0 < si < 30) and ( 70 < sa < 90):
        texture = 'loamy_sand'
        WP2FC = 0.41
    if (0 < cl < 20) and (0 < si < 50) and ( 43 < sa < 85):
        texture = 'sandy_loam'
        WP2FC = 0.44
    if (35 < cl < 55) and (0 < si < 20) and ( 45 < sa < 65):
        texture = 'sandy_clay'
        WP2FC = 0.63
    if (25 < cl < 40) and (40 < si < 75) and ( 0 < sa < 20):
        texture = 'silty_clay_loam'
        WP2FC = 0.70
    if (5 < cl < 39) and (25 < si < 50) and ( 25 < sa < 55):
        texture = 'loam'
        WP2FC = 0.50
    if (0 < cl < 27) and (50 < si < 100) and ( 0 < sa < 50):
        texture = 'silt_loam'
        WP2FC = 0.35
    if (27 < cl < 40) and (15 < si < 55) and ( 20 < sa < 45):
        texture = 'clay_loam'
        WP2FC = 0.61
    if (0 < cl < 12) and (80 < si < 100) and ( 0 < sa < 20):
        texture = 'silt'
        WP2FC = 0.20
    if (20 < cl < 35) and ( 0 < si < 30) and ( 45 < sa < 80 ):
        texture = 'sandy_clay_loam'
        WP2FC = 0.58
    if (40 < cl < 60) and (40 < si < 60) and ( 0 < sa < 20):
        texture = 'silty_clay'
        WP2FC = 0.66
    if (40 < cl < 100) and (0 < si < 40) and ( 0 < sa < 45):
        texture = 'clay'
        WP2FC = 0.71

    return np.array([texture,WP2FC])
