python -m venv venv
cmd /K "cd venv/Scripts & activate & cd ../.. & START /W python -m pip install --upgrade pip & START /W pip install -r requirements.txt & PAUSE"
PAUSE
