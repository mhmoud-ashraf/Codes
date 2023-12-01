import os
#%%
class Instance:
    def __init__ (self, dir, instance):
        self.dir = dir # Path to the instance file
        self.instance = instance # Name of the instance file
        
    def read_instance (self):
        path = os.path.join(self.dir, self.instance)
        with open(path, 'r') as file:
            self.nitems, self.capacity = map(int, file.readline().split())
            self.items = {int(item): {'weight': int(weight), 'profit': int(profit)} for item, weight, profit in [line.split() for line in file.readlines()]}
            file.close()
        return self.capacity, self.items
#%%
if __name__ == '__main__':
    parent_dir = os.path.dirname(os.getcwd())
    folder = '1701367268.646521'
    instance_dir = os.path.join(parent_dir, 'Instances', folder)
    instance = 'instance_50_42.txt'
    capacity, items = Instance(instance_dir, instance).read_instance()