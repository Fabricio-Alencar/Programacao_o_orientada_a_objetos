class Singleton:
    __instance = None 

    def __new__(cls,*args,**kwargs): # os asteriscos são usados quando a gente não sabe o numero de parâmetros que nossa função irá usar
        if cls.__instance == None:
            cls.__instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls.__instance
singleton1=Singleton()
singleton2=Singleton()

print(singleton1)
print(singleton2)
print(singleton1==singleton2)