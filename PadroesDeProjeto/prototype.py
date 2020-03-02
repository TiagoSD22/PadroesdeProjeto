import abc


# In[2]:


class Car(metaclass=abc.ABCMeta):
    model: str = None
    value: int = None
    
    def __init__(self, model='Prototype', value='None'):
        self.model = model
        self.value = value
        
    @abc.abstractmethod
    def clone(self):
        pass


# In[3]:


class Sandero(Car):
    def __init__(self, model: str, value: int):
        self.model = model
        self.value = value

    def clone(self):
        return Sandero(self.model, self.value)
    
    def __repr__(self):
        return 'Sandero {} - R$ {} - Memory Address: {}'.format(self.model, self.value, hex(id(self)))


# In[4]:


class Logan(Car):
    def __init__(self, model: str, value: int):
        self.model = model
        self.value = value

    def clone(self):
        return Logan(self.model, self.value)
    
    def __repr__(self):
        return 'Logan {} - R$ {} - Memory Address: {}'.format(self.model, self.value, hex(id(self)))


# In[5]:


print('Prototypes:')

sanderoPrototype = Sandero("Life", 22)
loganPrototype = Logan("Zen", 35)

print(sanderoPrototype)
print(loganPrototype)


sanderoClone: Sandero = sanderoPrototype.clone()
loganClone: Logan = loganPrototype.clone()

print("\nClones: ")

print(sanderoClone)
print(loganClone)

sanderoClone.value = 190
loganClone.model = "Intense"

print("\nPrototipos e clones apos mudanca dos clones: ")

print(sanderoPrototype)
print(loganPrototype)
print(sanderoClone)
print(loganClone)
