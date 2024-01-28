from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def process_ark():
    with open('arkpriceengine.json', 'r') as arkpriceengine_file:
        data = json.load(arkpriceengine_file)
    return data

def process_squad():
    with open('squadpriceengine.json', 'r') as squadpriceengine_file:
        data = json.load(squadpriceengine_file)
    return data

def process_mars2030():
    with open('mars2030priceengine.json', 'r') as mars2030priceengine_file:
        data = json.load(mars2030priceengine_file)
    return data

def process_jaguar():
    with open('jaguarpriceengine.json', 'r') as jaguarpriceengine_file:
        data = json.load(jaguarpriceengine_file)
    return data

def process_helloneigbor():
    with open('helloneighborpriceengine.json', 'r') as helloneighborpriceengine_file:
        data = json.load(helloneighborpriceengine_file)
    return data

def process_darkandlight():
    with open('darkandlightpriceengine.json', 'r') as darkandlightpriceengine_file:
        data = json.load(darkandlightpriceengine_file)
    return data

def process_min():
    with open('minpriceengine.json', 'r') as minpriceengine_file:
        data = json.load(minpriceengine_file)
    return data

def process_vrfunhouse():
    with open('vrfunhousepriceengine.json', 'r') as vrfunhousepriceengine_file:
        data = json.load(vrfunhousepriceengine_file)
    return data

def process_springbok():
    with open('springbokpriceengine.json', 'r') as springbokpriceengine_file:
        data = json.load(springbokpriceengine_file)
    return data

def process_bussim18():
    with open('bussim18priceengine.json', 'r') as bussim18priceengine_file:
        data = json.load(bussim18priceengine_file)
    return data

def process_showmaker():
    with open('showmakerpriceengine.json', 'r') as showmakerpriceengine_file:
        data = json.load(showmakerpriceengine_file)
    return data

def process_pixark():
    with open('pixarkpriceengine.json', 'r') as pixarkpriceengine_file:
        data = json.load(pixarkpriceengine_file)
    return data

def process_odin():
    with open('odinpriceengine.json', 'r') as odinpriceengine_file:
        data = json.load(odinpriceengine_file)
    return data

def process_wren():
    with open('wrenpriceengine.json', 'r') as wrenpriceengine_file:
        data = json.load(wrenpriceengine_file)
    return data

def process_vpr():
    with open('vprpriceengine.json', 'r') as vprpriceengine_file:
        data = json.load(vprpriceengine_file)
    return data

def process_morpho():
    with open('morphopriceengine.json', 'r') as morphopriceengine_file:
        data = json.load(morphopriceengine_file)
    return data

def process_conanexiles():
    with open('conanexiles.json', 'r') as conanexiles_file:
        data = json.load(conanexiles_file)
    return data

def process_fn():
    with open('fnpriceengine.json') as fnpriceengine_file:
        data = json.load(fnpriceengine_file)
    return data

namespace_handlers = {
    'ark': process_ark,
    'squad': process_squad,
    'mars2030': process_mars2030,
    'jaguar': process_jaguar,
    'helloneighbor': process_helloneigbor,
    'darkandlight': process_darkandlight,
    'min': process_min,
    'vrfunhouse': process_vrfunhouse,
    'springbok': process_springbok,
    'bussim18': process_bussim18,
    'showmaker': process_showmaker,
    'pixark': process_pixark,
    'odin': process_odin,
    'wren': process_wren,
    'vpr': process_vpr,
    'morpho': process_morpho,
    'conanexiles': process_conanexiles,
    'fn': process_fn,
}

@app.route('/waitingroom/api/waitingroom', methods=['GET'])
def waitingroomskip():
    response = make_response('Why tf u reading this?', 204)

    return response

@app.route('/datarouter/api/v1/public/data', methods=['POST'])
def datarouter():
    response = make_response('response', 204)

    return response

@app.route('/account/api/oauth/token', methods=['POST'])
def token():
    with open('token_response.json', 'r') as token_file:
        data = json.load(token_file)
    return jsonify(data)

@app.route('/launcher/api/cloudstorage/system', methods=['GET'])
def syscount():
    response = make_response('1000', 200)

    return response

@app.route('/launcher/api/public/assets/Windows/x/EpicGamesLauncher', methods=['GET'])
def test():
    response = make_response('1337', 204)

    return response

@app.route('/account/api/public/account/r54hre45h4r5th48r5hrhr54h56rhr', methods=['GET'])
def account():
    with open('account_response.json', 'r') as account_file:
        data = json.load(account_file)
    return jsonify(data)

@app.route('/account/api/public/account/r54hre45h4r5th48r5hrhr54h56rhr/externalAuths', methods=['GET'])
def externalauths():
    with open('externalAuths.json', 'r') as externalauths_file:
        data = json.load(externalauths_file)
    return jsonify(data)

@app.route('/account/api/epicdomains/ssodomains', methods=['GET'])
def ssdomains():
    with open('ssdomains.json', 'r') as ssdomains_file:
        data = json.load(ssdomains_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/bussim18/items', methods=['GET'])
def bussim18items():
    with open('bussim18items.json', 'r') as bussim18items_file:
        data = json.load(bussim18items_file)
    return jsonify(data)

@app.route('/launcher/api/public/payment/accounts/r54hre45h4r5th48r5hrhr54h56rhr/billingaccounts/default', methods=['GET'])
def savedpayment():
    with open('savedpayment.json') as savedpayment_file:
        data = json.load(savedpayment_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/bussim18/offers', methods=['GET'])
def bussim18offers():
    with open('bussim18offers.json', 'r') as bussim18offers_file:
        data = json.load(bussim18offers_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/conanexiles/items', methods=['GET'])
def conanexilesitems():
    with open('conanexilesitems.json', 'r') as conanexilesitems_file:
        data = json.load(conanexilesitems_file)
    return data

@app.route('/catalog/api/shared/namespace/odin/items', methods=['GET'])
def odinitems():
    with open('odinitems.json', 'r') as odinitems_file:
        data = json.load(odinitems_file)
    return data

@app.route('/catalog/api/shared/namespace/pixark/items', methods=['GET'])
def pixarkitems():
    with open('pixarkitems.json', 'r') as pixarkitems_file:
        data = json.load(pixarkitems_file)
    return data



@app.route('/priceengine/api/shared/offers/price', methods=['POST'])
def priceengine():
    try:
        # Get the JSON data from the request
        json_data = request.get_json()

        # Extract the "namespace" from the JSON data
        namespace = json_data.get('namespace')

        # Use the dictionary to get the corresponding function
        handler = namespace_handlers.get(namespace)

        # Execute the function and get the result
        result_data = handler()

        # Send back the response in JSON format
        return jsonify(result_data)

    except Exception as e:
        # Handle exceptions, if any
        return jsonify({"error": str(e)})
    

def run_flask():
    print(f'EGL-Custom-Backend Running on Port 3551')
    app.run(host='0.0.0.0', port=3551)

run_flask()