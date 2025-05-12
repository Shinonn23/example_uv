import subprocess
import time
import shutil
import os
import sys
import platform


def create_venv_with_uv(path=".venv_test_uv"):
    # Get Python interpreter info
    python_version = (
        f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    python_path = sys.executable
    print(f"Using CPython {python_version} interpreter at: {python_path}")
    print(f"Creating virtual environment at: {path}")

    # Determine activation command based on platform
    if platform.system() == "Windows":
        activate_cmd = f"{path}\\Scripts\\activate"
    else:
        activate_cmd = f"{path}/bin/activate"
    print(f"Activate with: {activate_cmd}")

    start = time.perf_counter()
    subprocess.run(["uv", "venv", path], check=True)
    duration = time.perf_counter() - start
    shutil.rmtree(path, ignore_errors=True)
    return duration


def create_venv_with_python(path=".venv_test_python"):
    shutil.rmtree(path, ignore_errors=True)  # Clean up before create
    start = time.perf_counter()
    python_cmd = "python3" if platform.system() != "Windows" else "python"
    try:
        subprocess.run([python_cmd, "-m", "venv", path], check=True)
        duration = time.perf_counter() - start
        shutil.rmtree(path, ignore_errors=True)
        return duration
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to create Python venv: {e}")
        return None


def main():
    print("Benchmarking virtual environment creation...")

    uv_times = []
    py_times = []

    rounds = 3  # You can increase for more stable averages

    for i in range(rounds):
        print(f"\nRound {i+1}:")
        uv_time = create_venv_with_uv()
        print(f"  uv venv       : {uv_time:.3f} seconds")
        uv_times.append(uv_time)

        try:
            py_time = create_venv_with_python()
            print(f"  python -m venv: {py_time:.3f} seconds")
            py_times.append(py_time)
        except Exception:
            break

    if py_times:
        avg_uv = sum(uv_times) / len(uv_times)
        avg_py = sum(py_times) / len(py_times)

        print("\n📊 Average results:")
        print(f"  uv venv       : {avg_uv:.3f} sec")
        print(f"  python -m venv: {avg_py:.3f} sec")


if __name__ == "__main__":
    main()
