# 🚀 มารู้จักกับ `uv` – Python package and project manager สายฟ้าแลบจากโลก Rust!

> "ถ้า pip คือม้า UV ก็เป็นรถ F1!"
> เพราะเขาเคลมว่าเร็วกว่า pip ธรรมดา **10x** และบางกรณีถึง **100x** 😱
> ไม่พูดเยอะ เจ็บคอ! มาลองกันเลยดีกว่า 💥

---

## 📊 Benchmark ชัดๆ ว่าเร็วจริงไหม?

<p align="center">
  <picture align="center">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
    <img alt="Shows a bar chart with benchmark results." src="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
  </picture>
</p>

---

## 🛠 ติดตั้งง่ายเหมือนปลอกกล้วย

### 🍎 macOS / 🐧 Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 🪟 Windows

```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### หรือจะผ่าน `pip` / `pipx` ก็ได้

```bash
pip install uv
# หรือ
pipx install uv
```

### อัปเดตก็ง่ายเหมือนเดิม

```bash
uv self update
```

---

## 🎬 ลองสร้างโปรเจกต์แรกด้วย `uv` กันเถอะ!

```bash
uv init example
cd example
ls
```

จะได้โครงสร้างโปรเจกต์ แบบนี้:

```
📁 example
├── 📘 README.md
├── 🐍 main.py
├── 🛠️ pyproject.toml
├── 🧪 .python-version
└── 🚫 .gitignore
```

---

## 🧪 สร้าง Virtual Env เร็วปานสายฟ้า!

```bash
uv venv
```

`uv` จะอ่าน `.python-version` แล้วเลือก Python ที่เหมาะให้เลย
จากนั้นก็ activate ได้เลย:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows
.\.venv\Scripts\activate
```

---

## ⚡ ทดลองติดตั้ง FastAPI เพื่อเช็คการทำงาน

```bash
uv add "fastapi[standard]"
```

ภายในพริบตา เราจะได้ package พร้อมใช้งานทันที 🎉

---

## 🔍 ลองแอบส่องดู `pyproject.toml` ดูสิ อารมณ์เดียวกับใช้ npm ของ node.js

```toml
[project]
name = "example"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]>=0.115.12",
]
```

> `package.json` เวอร์ชัน Python 5555+

---

## 🧪 ทดลอง Benchmark ความเร็วการสร้าง .venv กันชัดๆ Python venv vs UV venv

```bash
python main.py
```

### สคริปต์สำหรับใช้ในการ benchmark นี้

```python
import subprocess
import time
import shutil
import os
import sys
import platform
  

def create_venv_with_uv(path=".venv_test_uv"):

    python_version = (
        f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    )
    python_path = sys.executable
    print(f"Using CPython {python_version} interpreter at: {python_path}")
    print(f"Creating virtual environment at: {path}")

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
    shutil.rmtree(path, ignore_errors=True) 
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
  

    rounds = 3 
  

    for i in range(rounds):
        print(f"\nRound {i+1}:")
        uv_time = create_venv_with_uv()
        print(f"  uv venv       : {uv_time:.3f} seconds")
        uv_times.append(uv_time)
  

        try:
            py_time = create_venv_with_python()
            print(f"  python -m venv: {py_time:.3f} seconds")
            py_times.append(py_time)
        except Exception:
            break
  

    if py_times:
        avg_uv = sum(uv_times) / len(uv_times)
        avg_py = sum(py_times) / len(py_times)
  

        print("\n📊 Average results:")
        print(f"  uv venv       : {avg_uv:.3f} sec")
        print(f"  python -m venv: {avg_py:.3f} sec")
  
  

if __name__ == "__main__":
    main()
```

---

## 🔥 ผลลัพธ์ที่ได้

```bash
Benchmarking virtual environment creation...

Round 1:
Using CPython 3.12.0 interpreter at: C:\**\example\.venv\Scripts\python.exe
Creating virtual environment at: .venv_test_uv
Activate with: .venv_test_uv\Scripts\activate
Using CPython 3.12.0 interpreter at: C:\**\Python\Python312\python.exe
Creating virtual environment at: .venv_test_uv
Activate with: .venv_test_uv\Scripts\activate
  uv venv       : 0.029 seconds
  python -m venv: 6.780 seconds

Round 2:
Using CPython 3.12.0 interpreter at: C:\**\example\.venv\Scripts\python.exe
Creating virtual environment at: .venv_test_uv
Activate with: .venv_test_uv\Scripts\activate
Using CPython 3.12.0 interpreter at: C:\**\Python\Python312\python.exe
Creating virtual environment at: .venv_test_uv
Activate with: .venv_test_uv\Scripts\activate
  uv venv       : 0.029 seconds
  python -m venv: 5.396 seconds

Round 3:
Using CPython 3.12.0 interpreter at: C:\**\example\.venv\Scripts\python.exe
Creating virtual environment at: .venv_test_uv
Activate with: .venv_test_uv\Scripts\activate
Using CPython 3.12.0 interpreter at: C:\**\Python\Python312\python.exe
Creating virtual environment at: .venv_test_uv
Activate with: .venv_test_uv\Scripts\activate
  uv venv       : 0.029 seconds
  python -m venv: 5.393 seconds

📊 Average results:
  uv venv       : 0.029 sec
  python -m venv: 5.856 sec
```

**ต่างกันเกือบ 200 เท่า!**
ใครสาย Productivity ต้องลอง 🔧⚡

