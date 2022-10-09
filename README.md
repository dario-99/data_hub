# Guida deploy
Cloniamo la repository con il seguente comando oppure scaricare il codice da github

	git clone https://github.com/dario-99/data_hub

Per inizializzare il progetto inizializzare un virtual enviroment con venv

    python -m venv data_hub/venv

in seguito alla creazione bisogna attivare il virtual enviroment con i script activate
## Windows powershell

    source ./data_hub/venv/Scripts/Activate.ps1

## Windows cmd
    
    source ./data_hub/venv/Scripts/activate.bat

## Linux
Per linux la cartella dovrebbe chiamarsi bin (non sono sicuro), e attivare con ./activate
## Dependencies
installare le dependencies con pip -r

    pip install -r requirements.txt

## Run applicazione
Una volta installte le dependencies eseguire il webserver con 

    streamlit run app.py

