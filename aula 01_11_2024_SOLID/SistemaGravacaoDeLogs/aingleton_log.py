import datetime
class LogManager:
    __instance=None

    def __new__(cls, *args,**kwargs):
        if cls.__instance==None:
            cls.__instance=super(LogManager,cls).__new__(cls,*args,**kwargs)
        return cls.__instance

    def configure(self,log_to_file,log_file):
        ''' Configura o destino do log'''
        self.log_file=log_file
        self.log_to_file=log_to_file

    def log(self, message,level="INFO"):
        '''Registra uma mensagem de log.'''
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_msg = f"[{timestamp}] {level}: {message}\n"
        if self.log_to_file:
            try:
                with open(f"{self.log_file}","a", encoding='utf-8') as f:
                    f.write(log_msg)
            except Exception as e:
                print(f"Erro ao iniciar arquivo {e}.")
        else:
            print(log_msg)
if __name__ == "__main__":
    logger = LogManager()
    logger.configure(log_to_file=True,log_file="myapp.log")
    logger.log("Esre é um log de informações")
    logger.log("Este é um log de aviso",level="WARNING")
    logger.log("Este é um log de Erro", level= "ERROR")
