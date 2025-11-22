import paramiko

HOST = "192.168.0.241"
USERNAME = "fatih"
KEY_FILE = "/home/fatih/.ssh/id_rsa"   # <-- use private key, NOT .pub file
COMMANDS = ["whoami", "uptime", "ls -la /var/log", "echo 'Hello from Nashid'"]

def run_simple_ssh():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    print(f"Connecting to {HOST} ...")

    client.connect(
        hostname=HOST,
        username=USERNAME,
        key_filename=KEY_FILE   # Correct argument name
    )

    print("Connected Successfully!\n")

    for cmd in COMMANDS:
        print(f"--- Running: {cmd} ---")

        stdin, stdout, stderr = client.exec_command(cmd)

        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        if output:
            print(output)
        if error:
            print("ERROR:", error)

        print()

    client.close()
    print("Connection Closed")


if __name__ == "__main__":
    run_simple_ssh()

