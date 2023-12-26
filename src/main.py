import OES


inp = []
num = int(input('Enter the number of equations do you have.\n'))

for i in range(num):
    inp.append(input(f'The {i+1}\'th equations.\n'))
target = input('Enter the targer equation.\n')

# inp = ['2 H2O2 = 2 H2O + O2 ->-196','2 H2 + O2 = 2 H2O -> -572']
# target = 'H2 + O2 = H2O2 '
solver = OES.OES(inp,target)
heat ,solution , flag = solver.solve()

if flag == False:
    print('The equations don\'t have a solution')
else:
    print('The equation coeffient:',solution)
    print(f'The target equation heat: {heat}')