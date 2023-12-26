import numpy as np

class OES :
    def __init__(self,inputs,target) -> None:
        target+='-> 0'
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
        B = np.array(B)
        actual = True
        heat = 0
        

        solution, residuals, rank, s = np.linalg.lstsq(matrix, B, rcond=None)
        
            
        if rank < min(matrix.shape):
            print("The system of equations is underdetermined.")
        else:
            
            for i in range(len(equ_elem)):
                dot_product = np.dot(matrix[i],solution)
                if not np.isclose(dot_product, B[i], atol=1e-8):
                    return None, None, False
                
            j =0 
            for i in solution:
               heat+=i*self.equations[j]['heat']
               j+=1
            
            heat = round(heat)

        return heat, solution, actual
        
    