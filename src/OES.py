import numpy as np

class OES :
    def __init__(self,inputs,target) -> None:
        self.elements = []
        self.equations = []
        
        for input in inputs:
            ret = self.parse(input)
            self.equations.append(ret)
            self.elements.extend(ret)
            
        
        self.target =  self.parse(target)
        
        self.elements = list(set(self.elements))
        
        self.elements.remove('heat')
        
        
        
    
    def parse(self,input):
        reactants = []
        productions = []
        
        reactants_dict = {}
        productions_dict = {}
        input = input.split('->')
        heat = input[1].split(' ')
        heat = list(filter(None,heat))
        reactants_dict['heat'] = int(heat[0])
        half = input[0].split('=')
        reactants = half[0].split('+')
        productions = half[1].split('+')
        
        for reactant in reactants:
            temp = reactant.split(' ')
            temp = list(filter(None, temp))
            
            if len(temp) ==1:
                reactants_dict[temp[0]] = 1
            else:
                reactants_dict[temp[1]] = int(temp[0])
        
        for production in productions:
            temp = production.split(' ')
            temp = list(filter(None, temp))
            if len(temp) == 1:
                productions_dict[temp[0]] = -1
            else:
                productions_dict[temp[1]] = -1*int(temp[0])
            
    
        return {**productions_dict,**reactants_dict}
        
        
    def solve(self):
        matrix = []
        B = []
        
        equ_elem = {}
        i = 0
        for element in self.elements:
            equ_elem[element] = i
            i+=1
            l = []
            for equation in self.equations:
                if(element in equation.keys()):
                    l.append(equation[element])
                else:
                    l.append(0)
            
            matrix.append(l)

            if(element in self.target.keys()):
                B.append(self.target[element])
            else:
                B.append(0)
                
        matrix = np.array(matrix)
        
    
'''
a11 x1 + a12 x2 + a13 x3 = a14 x4 + a15 x5 + a16 x6     * p1
a21 x1 + a22 x2 + a23 x3 = a24 x4 + a25 x5 + a26 x6     * p2


b1 x1 + b2 x2 + b3 x3 = b4 x4 + b5 x5 + b6 x6



b1 = p1 * a11 + p2 * a21
b2 = p1 * a12 + p2* a22
b3 = p1 * a13 + p2* a23


'''