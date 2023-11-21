#logging the file and configure the log

import logging
logging.basicConfig(filename="mylog.log",level=logging.DEBUG )
logging.critical("Critical")
logging.error("Error")
logging.warning("Warning")
logging.info("Info")
logging.debug("Debug")
