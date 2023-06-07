class Toy:
    def __init__(self,color,age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name':'Ram',
            'has_pets':False
        }

#modifying __str__
    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 6
    
    def __call__(self):
        return ("yess")
    
    def __getitem__(self,i):
        return self.my_dict[i]

action_figure = Toy('red',0)
print(action_figure.__str__())
print(str(action_figure))

#post giving the implementation of __call__(), we can call action_figure() directly
print(len(action_figure))

#Post overriding __getitem__
print(action_figure['name'])
