import OES
inp = ['n2h4 + ch40 = ch20 + n2 + 3h2 -> -34','n2 + 3h2 = 2nh3 -> -46','ch4o = ch2o + h2 ->-65']
target = ' n2h4 + h2 = 2nh3 -> 0'
solver = OES.OES(inp,target)

solver.solve()