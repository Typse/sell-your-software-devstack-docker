cd ./backend
source .venv/bin/activate
fastapi dev src/app.py

> [!NOTE]  
> You need to create a python enviroment first to run the start the backend!
> Run `python3 -m venv .venv` then `source .venv/bin/activate` and after that 
> installing the python packages with `.venv/bin/pip install -r requirements.txt`
> You need to be in the `backend` directory!

cd ./frontend
npm run dev
