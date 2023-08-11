import logging

class Debugger:
    
    def error(self, *args, **kwargs):
        logging.error(f"*============================*{args}, {kwargs}")
    
    def warning(self, *args, **kwargs):
        logging.warning(f"*============================*{args}, {kwargs}")

    def info(self, *args, **kwargs):
        logging.info(f"*============================*{args}, {kwargs}")


# debug = Debugger()
# debug.info(data=1, data2=2, data3=3)
# debug.error(data=1, data2=2, data3=3)
# debug.warning(data=1, data2=2, data3=3)