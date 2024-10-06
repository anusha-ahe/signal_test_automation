import subprocess

def run_test_sikuli_script():
    sikuli_jar = "../sikuli/sikulixide.jar"
    sikuli_script = "run_test.py"
    subprocess.run(["java", "-jar", sikuli_jar, "-r", sikuli_script])

run_test_sikuli_script()