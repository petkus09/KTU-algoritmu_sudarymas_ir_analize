import os

def generate_random_file(file_size, file_name):
    with open(file_name, 'wb') as handle:
        handle.write(os.urandom(file_size))