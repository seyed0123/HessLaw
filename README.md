# OXD Equation Solver (OES)

The HessLawSolver class is a Python implementation of Hess's Law, a fundamental principle in chemistry.
Hess's Law states that the sum of the enthalpies of the reactants equals the sum of the enthalpies of the products. It is used to predict the enthalpy change of a reaction without experimental data.

This class takes the enthalpies of formation of the reactants and products as input and calculates the enthalpy change of the reaction.

<div align="center">

<img src="shots/photo8548248006.jpg" width="50%">

</div>

## OES Class

The `OES` class is designed to handle the core functionality of the online examination system. It takes in inputs and targets as parameters and provides methods to parse and solve the inputs.

### Methods

- `__init__(self, inputs, target)`: This is the constructor method for the `OES` class. It initializes the class with the provided inputs and target.

- `parse(self, input)`: This method is used to parse the input into reactants and productions. It returns a dictionary containing the parsed input.

- `solve(self)`: This method is used to solve the system of equations derived from the inputs. It returns the heat, solution, and a boolean indicating whether the solution is valid or not.

### Usage

```python 
import OES
```

#### Define the inputs and target

this is a simple example to how enter the equations.

`2 H2O2 = 2 H2O + O2 -> -196`

and in this way enter the target equation.

`H2 + O2 = H2O2`

**Note** : put a space between the elements and coefficients

#### Create an instance of the OES class

```python
solver = OES.OES(inputs, target)
```

#### Solve the system of equations

```python
heat, solution, flag = solver.solve()
```

#### Print the results

```python
if flag == False: 
    print('The equations don\'t have a solution') 
else: 
    print('The equation coeffient:', solution)
    print(f'The target equation heat: {heat}')
```

Please note that this is a basic overview of the `OES` class. For more detailed information, please refer to the source code.
