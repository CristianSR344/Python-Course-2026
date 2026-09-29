# Student Guide

## Install and prepare

Install Python 3.11 or newer from python.org and enable **Add Python to PATH** on Windows. In PowerShell at the course root:

```powershell
python --version
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python 00_setup/environment_check.py
```

PowerShell execution-policy problems can be avoided with `Set-ExecutionPolicy -Scope Process Bypass`. On macOS/Linux, activate with `source .venv/bin/activate`.

## Run course material

Run a script with `python 01_fundamentals/02_input_output.py`. Start notebooks with `jupyter notebook`; select the virtual-environment kernel and use **Restart Kernel and Run All** to verify a notebook.

## Run the portal

```powershell
cd final_project
Copy-Item .env.example .env
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`. Swagger API docs are at `/docs`. Stop with Ctrl+C. Configuration belongs in `.env`; never commit passwords. Without SMTP credentials, messages are safely written under `logs/emails`.

To reset local data, stop the server, delete `final_project/data/app.db`, and restart. Do this only when you no longer need the records.

## Working and submitting

Keep TODO markers until your implementation is complete. Run `python -m compileall .` and `pytest final_project/tests` before submission. Submit your repository without `.venv`, `.env`, caches, logs, or generated database files. Include a short README explaining choices and known limitations.

