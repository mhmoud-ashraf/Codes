import os
import gurobipy as gp
from gurobipy import GRB
from InstanceReaderKP import Instance
#%%
class ModelIP:
    def __init__ (self, instance, capacity, items):
        self.instance = instance[:-4] # Instance name
        self.capacity = capacity # Capacity of the knapsack
        self.items = items # Dictionary of items
        
    def create_model (self):
        # Data (sets, parameters, etc.)
        I = list(self.items.keys()) # set of items: indexed by i in I
        a = {i: self.items[i]['weight'] for i in I} # weight of item i
        c = {i: self.items[i]['profit'] for i in I} # profit of item i
        b = self.capacity # capacity of the knapsack
        
        model = gp.Model("IP_"+self.instance) # model constructor
        model.setParam('OutputFlag', 0) # suppress Gurobi output
        
        # Decision variables
        x = model.addVars(I, vtype=GRB.BINARY, name='x')
        
        # Objevtive function
        obj_fn = model.setObjective(gp.quicksum(c[i] * x[i] for i in I), GRB.MAXIMIZE)
        
        # Constraints
        constr1 = model.addConstr((gp.quicksum(a[i] * x[i] for i in I) <= b), name='arc length')
        
        model.update() # update the model
        return model
    
    def solve (self, path):
        """
        The function solves a mathematical optimization model and saves the model and solution files to
        the specified path.
        
        :param path: The "path" parameter is the directory path where you want to save the model files
        :return: the model.
        """
        model = self.create_model() # create the model
        model.optimize() # solve the model
        # Model export
        for dir in ['mps', 'lp', 'sol', 'json']:
            model.write(os.path.join(path, dir, self.instance+'.{}'.format(dir)))
            
    def load (self, path):
        """
        The function loads a model from the specified path.
        
        :param path: The "path" parameter is the directory path where you want to load the model files
        :return: the model.
        """
        model = self.create_model() # create the model
        model.read(os.path.join(path, 'sol', self.instance+'.sol'))
        model.optimize()
        return model
#%%
if __name__ == '__main__':
    parent_dir = os.path.dirname(os.getcwd())
    folder = '1701367268.646521'
    instance_dir = os.path.join(parent_dir, 'Instances', folder)
    instance_file = 'instance_50_42.txt'
    capacity, items = Instance(instance_dir, instance_file).read_instance()
    models_dir = instance_dir.replace('Instances', 'Models_IP')
    for dir in ['mps', 'lp', 'sol', 'json']:
        os.makedirs(os.path.join(models_dir, dir), exist_ok=True)
    model = ModelIP(instance_file, capacity, items)
    model.solve(models_dir)
    model = model.load(models_dir)