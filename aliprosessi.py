import subprocess
import os

p1 = subprocess.run(["ls", "-l"], capture_output=True, text=True)

if p1.returncode == 0:
    with open("stdout.txt", mode="w") as file:
        file.write(f"{p1.stdout} \nReturn code\t{p1.returncode}")

else:
    print(f"We got an error on: {p1.args} => Return code: {p1.returncode}")
    try:
        os.remove("stdout.txt")
    except:
        print("No file found")

p2 = subprocess.run(["cat", "application.log"], capture_output=True, text=True)

p3 = subprocess.run(["grep", "-n", "ERROR"], capture_output=True, text=True, input=p2.stdout)

print(p3.stdout)