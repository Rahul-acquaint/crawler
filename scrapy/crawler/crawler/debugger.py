import logging

class Debugger:
    
    def println(self, *args, **kwargs):
        logging.error("*============================*", *args, kwargs)
        
    def error(self, *args, **kwargs):
        logging.error("*============================*")
        print(*args, kwargs)
    
    def warning(self, *args, **kwargs):
        logging.warning("*============================*")
        print(*args, kwargs)

    def info(self, *args, **kwargs):
        logging.info("*============================*")
        print(*args, kwargs)



debug = Debugger()
debug.info(data=1, data2=2, data3=3)
debug.error(data=1, data2=2, data3=3)
debug.warning(data=1, data2=2, data3=3)