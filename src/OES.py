class OES :
    def __init__(self,inputs,target) -> None:
        for input in inputs:
            equations.append(self.parse(input))
            
        equations = []
        
    
    def parse(self,input):
        reactants = []
        productions = []
        
        reactants_dict = {}
        productions_dict = {}
        
        half = input.split('=')
        reactants = half[0].split('+')
        productions = half[1].split('+')
        
        for reactant in reactants:
            temp = reactant.split(' ')
            list(filter(None, temp))
            
            reactants_dict[temp[1]] = temp[0]
        
        for production in productions:
            temp = production.split(' ')
            temp = list(filter(None, temp))
            
            productions_dict[temp[1]] = temp[0]*-1
            
    
        return dict(productions_dict+reactants_dict)
        
        
    
    
    
'''
a11 x1 + a12 x2 + a13 x3 = a14 x4 + a15 x5 + a16 x6     * p1
a21 x1 + a22 x2 + a23 x3 = a24 x4 + a25 x5 + a26 x6     * p2


b1 x1 + b2 x2 + b3 x3 = b4 x4 + b5 x5 + b6 x6



b1 = p1 * a11 + p2 * a21
b2 = p1 * a12 + p2* a22
b3 = p1 * a13 + p2* a23


'''