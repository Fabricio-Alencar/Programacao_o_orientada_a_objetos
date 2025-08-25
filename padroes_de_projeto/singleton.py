class Singleton:
    __instance = None

    #args e kwargs quando a gente nao sabe o numero de parametro q a funcao vai receber
    def __new__(cls, *args, **kwargs): #responsavel por criar um objeto, metodo interno do python, sobrescrita
        if cls.__instance == None:
            cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwargs)

        return cls.__instance
    
    
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1)
print(singleton2)
print(singleton1 == singleton2)

