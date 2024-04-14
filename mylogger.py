import time
import datetime
from functools import wraps
from fastapi import HTTPException, Request
import os
import constant

class MyLogger:
    instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(MyLogger, cls).__new__(cls)
            cls.instance.log_file_path = cls.instance.get_log_file_path()
        return cls.instance

    def get_log_file_path(self):
        # Generate a log file name with the current date
        today_date = datetime.datetime.now().strftime("%d-%m-%Y")
        log_folder = constant.LOG_FOLDER
        log_file_name = constant.LOG_FILE_PATH.replace(".txt", f"_{today_date}.txt")
        return os.path.join(log_folder, log_file_name)

    def rotate_log(self):
        # Check if the date has changed and update the log file path
        new_log_file_path = self.get_log_file_path()
        if new_log_file_path != self.log_file_path:
            self.log_file_path = new_log_file_path

    def log(self, log_level, message):
        # Rotate the log file if the date has changed
        self.rotate_log()

        with open(self.log_file_path, 'a') as log_file:
            log_file.write(
                f"{log_level}: {str(datetime.datetime.now())} - {message}\n")

    def debug_http_methods(self, func):
        @wraps(func)
        async def inner(request: Request, *args, **kwargs):
            method_name = func.__name__
            try:
                self.log("INFO",
                         f"Received {method_name.upper()} request for /order")
                start = time.time()
                val = await func(request, *args, **kwargs)
                end = time.time()
                self.log("INFO",
                         f"{method_name.upper()} request for /order successful")
                self.log("INFO", f"Total time taken: {end - start} seconds")
                return val
            except Exception as e:
                self.log("ERROR",
                         f"Error processing {method_name.upper()} request for /order: {str(e)}")
                raise e

        return inner
    
    
    def debug_http_methods(self, func):
        @wraps(func)
        async def inner(request: Request, *args, **kwargs):
            method_name = func.__name__
            try:
                self.log("INFO",
                         f"Received {method_name.upper()} request for /Return")
                start = time.time()
                val = await func(request, *args, **kwargs)
                end = time.time()
                self.log("INFO",
                         f"{method_name.upper()} request for /Return successful")
                self.log("INFO", f"Total time taken: {end - start} seconds")
                return val
            except Exception as e:
                self.log("ERROR",
                         f"Error processing {method_name.upper()} request for /Return: {str(e)}")
                raise e

        return inner
    
    def debug_http_methods(self, func):
        @wraps(func)
        async def inner(request: Request, *args, **kwargs):
            method_name = func.__name__
            try:
                self.log("INFO",
                         f"Received {method_name.upper()} request for /people")
                start = time.time()
                val = await func(request, *args, **kwargs)
                end = time.time()
                self.log("INFO",
                         f"{method_name.upper()} request for /people successful")
                self.log("INFO", f"Total time taken: {end - start} seconds")
                return val
            except Exception as e:
                self.log("ERROR",
                         f"Error processing {method_name.upper()} request for /people: {str(e)}")
                raise e

        return inner
    