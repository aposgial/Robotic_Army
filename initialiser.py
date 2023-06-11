import subprocess

# Specify the path to your requirements.txt file
requirements_file = "requirements.txt"

def install_requirements(requirements_file):
    try:
        subprocess.check_call(["pip", "install", "-r", requirements_file])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install packages from {requirements_file}. Error: {e}")
    else:
        print(f"Packages from {requirements_file} have been successfully installed.")

install_requirements(requirements_file)
