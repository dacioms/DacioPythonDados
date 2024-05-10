import random
import datetime

# Gerar uma linha de log
def generate_log_line(index):
    timestamp = datetime.datetime.now() - datetime.timedelta(seconds=random.randint(0, 720000))
    log_type = "ERROR" if random.choice([0, 1, 2, 3, 4]) == 0 else "INFO"
    messages = {
        "INFO": ["User logged in from IP address 192.168.1.{}".format(random.randint(128, 255)),
                 "User requested page index.html",
                 "Database accessed successfully",
                 "New user registered with id {}".format(random.randint(1000, 9999))],
        "ERROR": ["Failed to load configuration file",
                  "Connection to database timed out",
                  "Permission denied while trying to write to log file",
                  "Invalid user input detected at process {}".format(random.randint(100, 999))]
    }
    message = random.choice(messages[log_type])
    return f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {log_type} {message}\n"

# Criar arquivo de log fictício
def create_log_file(filename, num_lines):
    with open(filename, 'w') as file:
        for i in range(num_lines):
            file.write(generate_log_line(i))

# Nome do arquivo
log_filename = "sample_log_file.log"
create_log_file(log_filename, 2000)
