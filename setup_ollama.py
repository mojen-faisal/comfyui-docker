import subprocess
import os
import time
import signal
import argparse

def start_ollama():
    print("Starting Ollama server...")
    process = subprocess.Popen(
        "ollama serve",
        shell=True,
        preexec_fn=os.setsid,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True
    )

    start_time = time.time()
    while time.time() - start_time < 60:
        output = process.stdout.readline()
        print(output, end="")

        if output and "Listening on" in output:
            print("Ollama server has fully started.")
            return process

    print("Ollama server did not fully start within the timeout period.")
    return None

def setup_ollama(model_names):
    ollama_process = None
    try:
        ollama_process = start_ollama()

        for model_name in model_names:
            print(f"Pulling model: {model_name}")
            try:
                subprocess.run(["ollama", "pull", model_name], check=True)
                print(f"Successfully pulled model: {model_name}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to pull model {model_name}: {str(e)}")

        print("Download of Ollama models complete")

    except Exception as e:
        print(f"Failed to start Ollama server or pull models: {str(e)}")

    finally:
        if ollama_process:
            os.killpg(os.getpgid(ollama_process.pid), signal.SIGTERM)
            print("Ollama server stopped.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Set up Ollama and pull models.")
    parser.add_argument(
        "--models",
        type=str,
        required=True,
        help="Comma-separated list of model names to pull (e.g. 'phi3:latest,llava:34b,llama3.1:latest')"
    )
    args = parser.parse_args()

    model_names = [model.strip() for model in args.models.split(",")]

    setup_ollama(model_names)
