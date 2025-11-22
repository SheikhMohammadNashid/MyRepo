import paramiko

HOSTS = [
    "192.168.0.241",
    "192.168.0.242",
    "192.168.0.243"
]

USERNAME = "fatih"
KEY_FILE = "/home/fatih/.ssh/id_rsa"
COMMANDS = ["whoami", "uptime", "echo 'Hello Nashid'"]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for host in HOSTS:

    print(f"\nConnecting to {host} ...")

    try:
        client.connect(
            hostname=host,
            username=USERNAME,
            key_filename=KEY_FILE,
        )
        print(f"Connected to {host}!")

        for cmd in COMMANDS:
            print(f"--- Running on {host}: {cmd} ---")

            stdin, stdout, stderr = client.exec_command(cmd)

            output = stdout.read().decode().strip()
            error = stderr.read().decode().strip()

            if output:
                print(output)
            if error:
                print("ERROR:", error)

        client.close()
        print(f"Closed connection to {host}")

    except Exception as e:
        print(f"Failed to connect to {host}: {e}")

