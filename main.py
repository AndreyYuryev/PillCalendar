

class Main:
    def __init__(self, param):
        self.param = param
    
    def execute(self):
        print(f'Значение {self.param}')
        
a = Main('test')
a.execute()