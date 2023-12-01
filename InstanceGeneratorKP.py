#%%
import os
import time
import random
#%%
class Instance:
    def __init__ (self, nitems, seed=42):
        self.nitems = nitems # Number of items
        self.seed = seed # Seed for random number generator
        
    def create_instance (self, max_weight=10, max_profit=10, min_capacity=10, max_capacity=20):
        """
        The function generates a random number of items with random weights and profits within specified
        ranges.
        
        :param max_weight: The maximum weight that an item can have, defaults to 10 (optional)
        :param max_profit: The `max_profit` parameter represents the maximum profit that an item can have,
        defaults to 10 (optional)
        :param min_capacity: The minimum capacity of each item, defaults to 10 (optional)
        :param max_capacity: The maximum capacity of the items that can be generated, defaults to 20
        (optional)
        :return: a tuple containing two elements. The first element is a randomly generated integer between
        the profits of min_capacity and max_capacity. The second element is a dictionary where each key
        represents an item number (ranging from 1 to self.nitems) and the corresponding profit is another
        dictionary containing the weight and profit of that item. The weight and profit are randomly generated
        integers between 1 and
        """
        random.seed(int(self.seed))
        return random.randint(min_capacity, max_capacity), {item: {'weight': random.randint(1, max_weight), 'profit': random.randint(1, max_profit)} for item in range(1, self.nitems+1)}
    
    def write_instance (self, path):
        """
        The `write_instance` function generates a file containing information about items and writes it to
        the specified path.
        
        :param path: The `path` parameter is the directory path where the instance file will be written
        """
        capacity, items = self.create_instance()
        file_name = f'instance_{self.nitems}_{self.seed}.txt'
        with open(os.path.join(path, file_name), 'w') as file:
            file.write(f'{self.nitems} {capacity}\n')
            for item in items:
                file.write(f'{item} {items[item]["weight"]} {items[item]["profit"]}\n')
            file.close()
        self.read_me_file(path)
            
    def read_me_file (self, path):
        """
        The function `read_me_file` creates a "Read me.txt" file and writes specific lines of
        information into it.
        
        :param path: The `path` parameter is the directory path where the "Read me.txt" file will be
        created
        """
        file_name = f'read me.txt'
        with open(os.path.join(path, file_name), 'w') as file:
            file.write(f'{"Line 1:"}\n')
            file.write(f'{"n_items"} {"capacity"}\n')
            file.write(f'{"Line(s) 2 to end"}\n')
            file.write(f'{"item"} {"weight"} {"profit"}\n')
            file.close()
#%%
if __name__ == '__main__':
    parent_dir = os.path.dirname(os.getcwd())
    path = os.path.join(parent_dir, 'Instances', str(time.time()))
    os.makedirs(path, exist_ok=True)
    nitems, seed = 50, 42
    Instance(nitems, seed).write_instance(path)