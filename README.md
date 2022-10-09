# Guida deploy
Per inizializzare il progetto inizializzare un virtual enviroment con venv

    python -m venv ./
in seguito alla creazione bisogna attivare il virtual enviroment con i script activate
## Windows powershell

    source ./Scripts/Activate.ps1

## Windows cmd
    
    source ./Scripts/activate.bat

## Linux
Per linux la cartella dovrebbe chiamarsi bin (non sono sicuro), e attivare con ./activate
## Dependencies
installare le dependencies con pip -r

    pip install -r requirements.txt
## Run applicazione
Una volta installte le dependencies eseguire il webserver con 

    streamlit run app.py
