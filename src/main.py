import OES
inp = ['2 no + o2 = 2 no2 ->-116','2 n2 + 5 o2 + 2 h2o = 4 hno3 ->-256','n2 + o2 = 2 no ->183']
target = '3 no2 + h2o = 2 hno3 + no -> 0'
solver = OES.OES(inp,target)

solver.solve()