import logging


# ----------------------------PRIMARY LOGGER--------------------------- #


# Create Logger
primary_logger = logging.getLogger()
primary_logger.setLevel(logging.DEBUG)

# Setup Handlers
primary_logger_console_handler = logging.StreamHandler()
primary_logger_file_handler=logging.FileHandler("database/log/primary.log")

# Create Formaatters
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Apply Formatters
primary_logger_console_handler.setFormatter(formatter)
primary_logger_file_handler.setFormatter(formatter)

# Apply Handlers
primary_logger.addHandler(primary_logger_console_handler)
primary_logger.addHandler(primary_logger_file_handler)



# ----------------------------DB LOGGER--------------------------- #

# Create Logger
db_logger = logging.getLogger()
db_logger.setLevel(logging.DEBUG)

# Setup Handlers
db_logger_console_handler = logging.StreamHandler()
db_logger_file_handler=logging.FileHandler("database/log/db.log")

# Create Formaatters
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Apply Formatters
db_logger_console_handler.setFormatter(formatter)
db_logger_file_handler.setFormatter(formatter)


# Apply Handlers
db_logger.addHandler(db_logger_console_handler)
db_logger.addHandler(db_logger_file_handler)
