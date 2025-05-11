import logging
import os  # Add this import

def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup as many loggers as you want"""
    # Create directory if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir:  # Only create if path contains directories
        os.makedirs(log_dir, exist_ok=True)
    
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def normalize_landmarks(landmarks):
    # Example helper function to normalize landmarks
    # Placeholder: implement as needed
    return landmarks
