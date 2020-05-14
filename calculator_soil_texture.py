def soiltext(cl,sa,si):
    global texture

    if (sa >= 0.85) and (si + cl*1.5 <= 0.15):
        texture = 'SAND'
        WP2FC = 0.50
    if (sa > 0.70) and (sa < 0.91) and (si + cl*1.5 >= 0.15):
        texture = 'LOSA'
        WP2FC = 0.41
    if (cl > 0.07) and (cl < 0.20) and (sa >= 0.52):
        texture = 'SALO'
        WP2FC = 0.44
    if (cl > 0.25) and (cl < 0.30) and (si <= 0.28) and (sa >= 0.45):
        texture = 'SNCL'
        WP2FC = 0.63
    if (cl >= 0.35) and (sa >= 0.45) :
        texture = 'SACL'
        WP2FC = 0.70
    if (cl >= 0.07) and (cl <= 0.27) and (si >= 0.28) and (si <= 0.50) and (sa <= 0.52):
        texture = 'LOAM'
        WP2FC = 0.50
    if  (si >= 0.50) and (cl >= 0.17) and (cl <= 0.27):
        texture = 'SILO'
        WP2FC = 0.35
    if  (sa >= 0.20) and (sa <= 0.45) and (cl >= 0.27) and (cl <= 0.40):
        texture = 'CLLO'
        WP2FC = 0.61
    if  (si >= 0.80) and (cl <= 0.12):
        texture = 'SILT'
        WP2FC = 0.20
    if  (cl >= 0.27) and (cl <= 0.40) and (sa <= 0.20):
        texture = 'SLCL'
        WP2FC = 0.58
    if  (cl >= 0.40) and (si >= 0.40):
        texture = 'SICL'
        WP2FC = 0.66
    if  (cl >= 0.40) and (sa <= 0.45) and (si <= 0.40):
        texture = 'CLAY'
        WP2FC = 0.71

    return np.array([texture,WP2FC])
