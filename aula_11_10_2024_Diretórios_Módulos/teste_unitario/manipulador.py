class manipulador:
    def soma(salf,a,b):
        return a+b

    def concatena(self,a,b):
        return str(a)+str(b)
    def multiplica(self,a,b):
        return a*b
    def ePar(self,a):
        if a%2==0:
            return True
    def invertString(self,texto:str):
        return texto[::-1] 
    def fatorial(self,n):
        if n ==0:
            return 1 
        else:
            return n*self.fatorial(n-1)
        
    def criar_arquivo(self,nome,texto):
        with open(nome,"w") as f:
            f.write(texto)
        return True
    
    def ler_arquivo(self,nome):
        with open(nome,"r") as f:
            return f.read()