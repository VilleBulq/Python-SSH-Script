# Python-SSH-Script
Small programs greated with Python programming language

Example usage: Connection to raspberry pi and run python script which return the Pi temperature

```import ssh_main
a = ssh_main.SSH("192.168.0.100", "pi", "raspberry")
a.connect()
a.ex_command("./test.py")

