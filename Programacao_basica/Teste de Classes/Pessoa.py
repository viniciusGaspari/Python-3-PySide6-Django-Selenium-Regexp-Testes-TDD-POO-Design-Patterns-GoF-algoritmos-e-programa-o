class Pessoa:
    #Constructor
    def __init__(self, nome: str, idade: int):

        if not isinstance(nome, str):
            raise TypeError('Nome deve conter letras')
        
        if not isinstance(idade, int):
            raise TypeError('Idade deve ser números inteiros')
        
        self.nome = nome
        self.idade = idade
   
    #Setters
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    
    #Getters
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade