import subprocess

def run_gsim_script():
    sikuli_jar = "../sikuli/sikulixide.jar"
    sikuli_script = "GSIM.py"
    subprocess.run(["java", "-jar", sikuli_jar, "-r", sikuli_script])

run_gsim_script()