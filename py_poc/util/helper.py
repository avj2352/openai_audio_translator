"""
    reusable scripts
"""
import logging

# write to a file
def write_to_file(content:str, filename:str = "text.txt") -> None:
    logging.debug(f"->(io) writing to a file: downloads/{filename}")
    try:
        # Using 'with' statement to automatically close the file
        with open(f"downloads/{filename}", 'w') as file:
            file.write(content)
        logging.info(f"(io) Successfully wrote to {filename}")
    except FileNotFoundError:
        # This exception is not typically raised by open() in write mode,
        # but it's included for completeness.
        logging.error(f"(io): File {filename} not found. However, in write mode, this should not occur.")
    except PermissionError:
        logging.error(f"(io): Permission denied to write to {filename}.")
    except OSError as e:
        logging.error(f"(io): An OS error occurred while writing to {filename}: {e}")
    except Exception as e:
        logging.error(f"(io): An unexpected error occurred: {e}")
