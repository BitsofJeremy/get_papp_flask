from flask import Blueprint, render_template, request
import requests
import base64
import io
import os
import cairosvg
from PIL import Image

# Replace with your Alchemy API key
ALCHEMY_API_KEY = os.getenv('ALCHEMY_API_KEY')

# Define the PAPP contract address
CONTRACT_ADDRESS = "0xF39bE779905D16fE23B2cC1297Dc3e759D2dAA11"

home = Blueprint('home', __name__)


def upscale_svg(svg_data, new_width, new_height):
    # Render the SVG to a PNG surface with the desired dimensions
    png_bytes = cairosvg.svg2png(bytestring=svg_data, parent_width=new_width, parent_height=new_height)
    # Convert the PNG bytes to a PIL image
    pil_image = Image.open(io.BytesIO(png_bytes))
    return pil_image


@home.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ethereum_address = request.form['ethereum_address']
        url = f"https://base-mainnet.g.alchemy.com/nft/v3/{ALCHEMY_API_KEY}/getNFTsForOwner?owner={ethereum_address}&contractAddresses[]={CONTRACT_ADDRESS}&withMetadata=true&orderBy=transferTime&pageSize=100"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()

        nfts = []
        if 'ownedNfts' in data:
            for nft in data['ownedNfts']:
                if 'name' in nft and 'tokenId' in nft and 'image' in nft and 'originalUrl' in nft['image']:
                    name = nft['name']
                    token_id = nft['tokenId']
                    description = nft['description']
                    svg_base64 = nft['image']['originalUrl'].split(',')[1]
                    svg_data = base64.b64decode(svg_base64)
                    upscaled_image = upscale_svg(svg_data, 1024, 1024)
                    # Convert PIL image to bytes
                    png_bytes = io.BytesIO()
                    upscaled_image.save(png_bytes, format='PNG')
                    png_bytes = png_bytes.getvalue()
                    # Encode PNG image as base64
                    base64_png = base64.b64encode(png_bytes).decode()
                    nfts.append({
                        'name': name,
                        'tokenId': token_id,
                        'description': description,
                        'image': base64_png
                    })
            return render_template('index.html', nfts=nfts)

        return "No image found for the provided Ethereum address"
    else:
        return render_template('index.html')