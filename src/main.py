import OES
inp = ['2 h2 + n2 = n2h4 -> 91',' n2h4 + h2 = 2 nh3 + p4 -> -183']
target = '3 h2 + n2 = 2 nh3 -> 0'
solver = OES.OES(inp,target)

solver.solve()