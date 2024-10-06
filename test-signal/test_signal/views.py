from django.http import HttpResponse
import subprocess
from django.shortcuts import render


def run_sikuli_script(script_name, script_folder):
    sikuli_jar = "../sikuli/sikulixide.jar"
    status_message = ""

    try:
        result = subprocess.run(
            ["java", "-jar", sikuli_jar, "-r", script_name],
            cwd=script_folder,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        status_message = result.stdout  # Capture the output of the Sikuli script
    except subprocess.CalledProcessError as e:
        status_message = f"Error starting simulation: {e.output or e.stderr}"
    except Exception as e:
        status_message = f"Unexpected error: {e}"

    return status_message


def simulation_page(request):
    status_message = ""

    if request.method == 'GET':
        action = request.GET.get('action', '')
        if action == 'run_gsim':
            status_message = run_sikuli_script("GSIM.py", "D:/signal/test-signal/test_signal/GSIM.sikuli")
        elif action == 'run_test':
            status_message = run_sikuli_script("generate.py", "D:/signal/test-signal/test_signal/IF-ELSE.sikuli")
    return render(request, 'start_sim.html', {'status_message': status_message})


def upload_folder(request):
    return HttpResponse("Folder uploaded successfully!")

