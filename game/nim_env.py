import random

class Nim:
    def __init__(self, heaps=[3, 4, 5]):
        self.initial_heaps = heaps.copy()
        self.heaps = heaps.copy()
        self.done = False
        
    def reset(self):
        self.heaps = self.initial_heaps.copy()
        self.done = False
        return self.get_state()
    
    def get_state(self):
        return tuple(self.heaps)
    
    def get_valid_actions(self):
        actions = []
        for heap_index, count in enumerate(self.heaps):
            for remove_count in range(1, count + 1):
                actions.append((heap_index, remove_count))
        return actions
    
    def step(self, action):
        heap_index, remove_count = action
        
        if self.done or heap_index >= len(self.heaps) or remove_count < 1 or remove_count > self.heaps[heap_index]:
            raise ValueError("Açãi Inválida")
        
        self.heaps[heap_index] -= remove_count
        
        if all(h == 0 for h in self.heaps):
            self.done=True
            reward = 1
        else:
            reward = 0
            
        return self.get_state(), reward, self.done
    
    def render(self):
        print("Current heaps:", self.heaps)