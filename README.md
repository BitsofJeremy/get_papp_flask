# get_papp_flask

Features
- Simple Flask website to get NFTs from the Base Blockchain for a user's wallet address 
 -Export from SVG to 1024x1024 PNG file 



# Install

    git clone https://github.com/BitsofJeremy/get_papp_flask
    cd get_papp_flask
    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements.txt

*[Note: See an example .env file below, or copy env-example to .env]*

    source .env

### Run it

    python app.py


Open `http://127.0.0.1:5000/` in browser of choice.

### Screenshots

![Screenshot1](screenshot_01.png)

![Screenshot2](screenshot_02.png)

#### Example .env file

    # Basic Flask stuff
    export FLASK_APP=app.py
    export FLASK_CONFIG=development
    export SALTY_SECRET=bbq
    export CSRF_SESSION_KEY=hotdogs
    export SECRET_KEY=pizza
    export ALCHEMY_API_KEY=YOUR_ALCHEMY_API_KEY

