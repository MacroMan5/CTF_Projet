import datetime
import random
import base64


def generate_random_ip():
    return f"192.168.{random.randint(1,254)}.{random.randint(1,254)}"

def generate_random_port():
    return random.randint(10000, 65535)

def generate_partial_rsa_key():
    return f"RSA {random.randint(100000000000,999999999999)}:{random.randint(100000000000,999999999999)}:{random.randint(100000000000,999999999999)}:{random.randint(100000000000,999999999999)}"

# def generate_random_log_line(today):
#     log_type = random.choice(["success", "failed", "failed"])
#     if log_type == "success":
#         return f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Accepted publickey for user{random.randint(1,5)} from {generate_random_ip()} port {generate_random_port()} ssh2: {generate_partial_rsa_key()}"
#     else:
#         return f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Failed password for user{random.randint(1,5)} from {generate_random_ip()} port {generate_random_port()} ssh2"


def add_admin_success_logs(today, log_lines):
    for day in range(5):
        date = (datetime.date.today() - datetime.timedelta(days=day)).strftime('%b %d')
        for _ in range(2):
            log_lines.append(f"{date} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Accepted publickey for admin from {generate_random_ip()} port {generate_random_port()} ssh2: {generate_partial_rsa_key()}")


# def add_bruteforce_attack_and_flag(today, log_lines):
#     flag = "FLAG{Base64_Hidden}"
#     encoded_flag = base64.b64encode(flag.encode()).decode()
#     print(encoded_flag)

#     for _ in range(3):
#         log_lines.append(f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Failed password for root from {generate_random_ip()} port {generate_random_port()} ssh2")

#     log_lines.append(f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Accepted publickey for user from {generate_random_ip()} port {generate_random_port()} ssh2: {generate_partial_rsa_key()} {encoded_flag}")

def add_bruteforce_attack_and_flag(today, log_lines):
    flag = "01253{Base64_Hidden}"
    encoded_flag = base64.b64encode(flag.encode()).decode()
    
    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%b %d')
    
    for _ in range(35):
        log_lines.append(f"{yesterday} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Failed password for admin from {generate_random_ip()} port {generate_random_port()} ssh2")

    log_lines.append(f"{yesterday} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu sshd[1234]: Accepted publickey for admin from {generate_random_ip()} port {generate_random_port()} ssh2: {generate_partial_rsa_key()} {encoded_flag}")




def create_log_files():
    today = datetime.date.today().strftime('%b %d')

    log_files = {
        "/var/log/auth.log":[],
        "/var/log/kern.log": [f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu kernel: [12345.678900] nf_conntrack: table full, dropping packet" for _ in range(10)],
        "/var/log/syslog": [f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu CRON[1234]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)" for _ in range(5)],
        "/var/log/messages": [f"{today} {datetime.datetime.now().time().strftime('%H:%M:%S')} ubuntu dhclient[1234]: DHCPREQUEST on eth0 to 192.168.1.1 port 67" for _ in range(5)],
    }

    add_bruteforce_attack_and_flag(today, log_files["/var/log/auth.log"])
    add_admin_success_logs(today, log_files["/var/log/auth.log"])

    for log_path, log_lines in log_files.items():
        with open(log_path, "w") as log_file:
            log_file.write("\n".join(log_lines))

if __name__ == "__main__":
    create_log_files()
