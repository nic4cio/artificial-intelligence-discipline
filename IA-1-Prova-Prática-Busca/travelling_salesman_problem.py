INF = float('inf')

map = [
    [   0,  30,  84,  56, INF, INF, INF,  75, INF,  80 ],
    [  30,   0,  65, INF, INF, INF,  70, INF, INF,  40 ],
    [  84,  64,   0,  74,  52,  55, INF,  60, 143,  48 ], 
    [  56, INF,  74,   0, 135, INF, INF,  20, INF, INF ], 
    [ INF, INF,  52, 135,   0,  70, INF, 122,  98,  80 ], 
    [  70, INF,  55, INF,  70,   0,  63, INF,  82,  35 ], 
    [ INF,  70, INF, INF, INF,  63,   0, INF, 120,  57 ], 
    [  75, INF, 135,  20, 122, INF, INF,   0, INF, INF ], 
    [ INF, INF, 143, INF,  98,  82, 120, INF,   0, INF ], 
    [  80,  40,  48, INF,  80,  35,  57, INF, INF,   0 ] 
]

print(map)