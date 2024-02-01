from flask import Flask, make_response, jsonify, request
from flask_cors import CORS
import json
import os

launcher_port = "3551"

app = Flask(__name__)
CORS(app)

def process_ark():
    json_file_path = os.path.join('priceengine', 'arkpriceengine.json')
    with open(json_file_path, 'r') as arkpriceengine_file:
        data = json.load(arkpriceengine_file)
    return data

def process_squad():
    json_file_path = os.path.join('priceengine', 'squadpriceengine.json')
    with open(json_file_path, 'r') as squadpriceengine_file:
        data = json.load(squadpriceengine_file)
    return data

def process_mars2030():
    json_file_path = os.path.join('priceengine', 'mars2030priceengine.json')
    with open(json_file_path, 'r') as mars2030priceengine_file:
        data = json.load(mars2030priceengine_file)
    return data

def process_jaguar():
    json_file_path = os.path.join('priceengine', 'jaguarpriceengine.json')
    with open(json_file_path, 'r') as jaguarpriceengine_file:
        data = json.load(jaguarpriceengine_file)
    return data

def process_helloneigbor():
    json_file_path = os.path.join('priceengine', 'helloneighborpriceengine.json')
    with open(json_file_path, 'r') as helloneighborpriceengine_file:
        data = json.load(helloneighborpriceengine_file)
    return data

def process_darkandlight():
    json_file_path = os.path.join('priceengine', 'darkandlightpriceengine.json')
    with open(json_file_path, 'r') as darkandlightpriceengine_file:
        data = json.load(darkandlightpriceengine_file)
    return data

def process_min():
    json_file_path = os.path.join('priceengine', 'minpriceengine.json')
    with open(json_file_path, 'r') as minpriceengine_file:
        data = json.load(minpriceengine_file)
    return data

def process_vrfunhouse():
    json_file_path = os.path.join('priceengine', 'vrfunhousepriceengine.json')
    with open(json_file_path, 'r') as vrfunhousepriceengine_file:
        data = json.load(vrfunhousepriceengine_file)
    return data

def process_springbok():
    json_file_path = os.path.join('priceengine', 'springbokpriceengine.json')
    with open(json_file_path, 'r') as springbokpriceengine_file:
        data = json.load(springbokpriceengine_file)
    return data

def process_bussim18():
    json_file_path = os.path.join('priceengine', 'bussim18priceengine.json')
    with open(json_file_path, 'r') as bussim18priceengine_file:
        data = json.load(bussim18priceengine_file)
    return data

def process_showmaker():
    json_file_path = os.path.join('priceengine', 'showmakerpriceengine.json')
    with open(json_file_path, 'r') as showmakerpriceengine_file:
        data = json.load(showmakerpriceengine_file)
    return data

def process_pixark():
    json_file_path = os.path.join('priceengine', 'pixarkpriceengine.json')
    with open(json_file_path, 'r') as pixarkpriceengine_file:
        data = json.load(pixarkpriceengine_file)
    return data

def process_odin():
    json_file_path = os.path.join('priceengine', 'odinpriceengine.json')
    with open(json_file_path, 'r') as odinpriceengine_file:
        data = json.load(odinpriceengine_file)
    return data

def process_wren():
    json_file_path = os.path.join('priceengine', 'wrenpriceengine.json')
    with open(json_file_path, 'r') as wrenpriceengine_file:
        data = json.load(wrenpriceengine_file)
    return data

def process_vpr():
    json_file_path = os.path.join('priceengine', 'vprpriceengine.json')
    with open(json_file_path, 'r') as vprpriceengine_file:
        data = json.load(vprpriceengine_file)
    return data

def process_morpho():
    json_file_path = os.path.join('priceengine', 'morphopriceengine.json')
    with open(json_file_path, 'r') as morphopriceengine_file:
        data = json.load(morphopriceengine_file)
    return data

def process_conanexiles():
    json_file_path = os.path.join('priceengine', 'conanexilespriceengine.json')
    with open(json_file_path, 'r') as conanexilespriceengine_file:
        data = json.load(conanexilespriceengine_file)
    return data

def process_fn():
    json_file_path = os.path.join('priceengine', 'fnpriceengine.json')
    with open(json_file_path, 'r') as fnpriceengine_file:
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
    form_data = request.form  # If the data is in form format
    print(f"Received POST request on /your_endpoint:")
    print(f"Form Data: {form_data}")
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

@app.route('/launcher/api/public/payment/accounts/r54hre45h4r5th48r5hrhr54h56rhr/billingaccounts/default', methods=['GET'])
def savedpayment():
    with open('savedpayment.json') as savedpayment_file:
        data = json.load(savedpayment_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/bussim18/items', methods=['GET'])
def bussim18items():
    json_file_path = os.path.join('items', 'bussim18items.json')
    with open(json_file_path, 'r') as bussim18items_file:
        data = json.load(bussim18items_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/ark/items', methods=['GET'])
def arkitems():
    json_file_path = os.path.join('items', 'arkitems.json')
    with open(json_file_path, 'r') as arkitems_file:
        data = json.load(arkitems_file)
    return data

@app.route('/catalog/api/shared/namespace/darkandlight/items', methods=['GET'])
def darkandlightitems():
    json_file_path = os.path.join('items', 'darkandlightitems.json')
    with open(json_file_path, 'r') as darkandlightitems_file:
        data = json.load(darkandlightitems_file)
    return data

@app.route('/catalog/api/shared/namespace/helloneighbor/items', methods=['GET'])
def helloneighboritems():
    json_file_path = os.path.join('items', 'helloneighboritems.json')
    with open(json_file_path, 'r') as helloneighboritems_file:
        data = json.load(helloneighboritems_file)
    return data

@app.route('/catalog/api/shared/namespace/mars2030/items', methods=['GET'])
def mars2030items():
    json_file_path = os.path.join('items', 'mars2030items.json')
    with open(json_file_path, 'r') as mars2030items_file:
        data = json.load(mars2030items_file)
    return data

@app.route('/catalog/api/shared/namespace/conanexiles/items', methods=['GET'])
def conanexilesitems():
    json_file_path = os.path.join('items', 'conanexilesitems.json')
    with open(json_file_path, 'r') as conanexilesitems_file:
        data = json.load(conanexilesitems_file)
    return data

@app.route('/catalog/api/shared/namespace/odin/items', methods=['GET'])
def odinitems():
    try:
        json_file_path = os.path.join('items', 'odinitems.json')
        with open(json_file_path, 'r') as odinitems_file:
            data = json.load(odinitems_file)
        return jsonify(data)
    except json.JSONDecodeError as e:
        return jsonify({"error": f"JSON decoding error: {str(e)}"}), 500
    except UnicodeDecodeError as e:
        return jsonify({"error": f"Unicode decoding error: {str(e)}"}), 500

@app.route('/catalog/api/shared/namespace/pixark/items', methods=['GET'])
def pixarkitems():
    json_file_path = os.path.join('items', 'pixarkitems.json')
    with open(json_file_path, 'r') as pixarkitems_file:
        data = json.load(pixarkitems_file)
    return data

@app.route('/catalog/api/shared/namespace/showmaker/items', methods=['GET'])
def showmakeritems():
    json_file_path = os.path.join('items', 'showmakeritems.json')
    with open(json_file_path, 'r') as showmakeritems_file:
        data = json.load(showmakeritems_file)
    return data

@app.route('/catalog/api/shared/namespace/squad/items', methods=['GET'])
def squaditems():
    json_file_path = os.path.join('items', 'squaditems.json')
    with open(json_file_path, 'r') as squaditems_file:
        data = json.load(squaditems_file)
    return data

@app.route('/catalog/api/shared/namespace/vrfunhouse/items', methods=['GET'])
def vrfunhouseitems():
    json_file_path = os.path.join('items', 'vrfunhouseitems.json')
    with open(json_file_path, 'r') as vrfunhouseitems_file:
        data = json.load(vrfunhouseitems_file)
    return data

@app.route('/catalog/api/shared/namespace/fn/items', methods=['GET'])
def fnitems():
    json_file_path = os.path.join('items', 'fnitems.json')
    with open(json_file_path, 'r') as fnitems_file:
        data = json.load(fnitems_file)
    return data

@app.route('/catalog/api/shared/namespace/jaguar/items', methods=['GET'])
def jaguaritems():
    json_file_path = os.path.join('items', 'jaguaritems.json')
    with open(json_file_path, 'r') as jaguaritems_file:
        data = json.load(jaguaritems_file)
    return data

@app.route('/catalog/api/shared/namespace/min/items', methods=['GET'])
def minitems():
    json_file_path = os.path.join('items', 'minitems.json')
    with open(json_file_path, 'r') as minitems_file:
        data = json.load(minitems_file)
    return data

@app.route('/catalog/api/shared/namespace/morpho/items', methods=['GET'])
def morphoitems():
    json_file_path = os.path.join('items', 'morphoitems.json')
    with open(json_file_path, 'r') as morphoitems_file:
        data = json.load(morphoitems_file)
    return data

@app.route('/catalog/api/shared/namespace/springbok/items', methods=['GET'])
def springbokitems():
    json_file_path = os.path.join('items', 'springbokitems.json')
    with open(json_file_path, 'r') as springbokitems_file:
        data = json.load(springbokitems_file)
    return data

@app.route('/catalog/api/shared/namespace/ut/items', methods=['GET'])
def utitems():
    json_file_path = os.path.join('items', 'utitems.json')
    with open(json_file_path, 'r') as utitems_file:
        data = json.load(utitems_file)
    return data

@app.route('/catalog/api/shared/namespace/vpr/items', methods=['GET'])
def vpritems():
    json_file_path = os.path.join('items', 'vpritems.json')
    with open(json_file_path, 'r') as vpritems_file:
        data = json.load(vpritems_file)
    return data

@app.route('/catalog/api/shared/namespace/wren/items', methods=['GET'])
def wrenitems():
    json_file_path = os.path.join('items', 'wrenitems.json')
    with open(json_file_path, 'r') as wrenitems_file:
        data = json.load(wrenitems_file)
    return data

@app.route('/catalog/api/shared/namespace/ark/offers', methods=['GET'])
def arkoffers():
    json_file_path = os.path.join('offers', 'arkoffers.json')
    with open(json_file_path, 'r') as arkoffers_file:
        data = json.load(arkoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/darkandlight/offers', methods=['GET'])
def darkandlightoffers():
    json_file_path = os.path.join('offers', 'darkandlightoffers.json')
    with open(json_file_path, 'r') as darkandlightoffers_file:
        data = json.load(darkandlightoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/helloneighbor/offers', methods=['GET'])
def helloneighboroffers():
    json_file_path = os.path.join('offers', 'helloneighboroffers.json')
    with open(json_file_path, 'r') as helloneighboroffers_file:
        data = json.load(helloneighboroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/mars2030/offers', methods=['GET'])
def mars2030offers():
    json_file_path = os.path.join('offers', 'mars2030offers.json')
    with open(json_file_path, 'r') as mars2030offers_file:
        data = json.load(mars2030offers_file)
    return data

@app.route('/catalog/api/shared/namespace/bussim18/offers', methods=['GET'])
def bussim18offers():
    json_file_path = os.path.join('offers', 'bussim18offers.json')
    with open(json_file_path, 'r') as bussim18offers_file:
        data = json.load(bussim18offers_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/conanexiles/offers', methods=['GET'])
def conanexilesoffers():
    json_file_path = os.path.join('offers', 'conanexilesoffers.json')
    with open(json_file_path, 'r') as conanexilesoffers_file:
        data = json.load(conanexilesoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/springbok/offers', methods=['GET'])
def springbokoffers():
    json_file_path = os.path.join('offers', 'springbokoffers.json')
    with open(json_file_path, 'r') as springbokoffers_file:
        data = json.load(springbokoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/jaguar/offers', methods=['GET'])
def jaguaroffers():
    json_file_path = os.path.join('offers', 'jaguaroffers.json')
    with open(json_file_path, 'r') as jaguaroffers_file:
        data = json.load(jaguaroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/odin/offers', methods=['GET'])
def odinoffers():
    json_file_path = os.path.join('offers', 'odinoffers.json')
    with open(json_file_path, 'r') as odinoffers_file:
        data = json.load(odinoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/pixark/offers', methods=['GET'])
def pixarkoffers():
    json_file_path = os.path.join('offers', 'pixarkoffers.json')
    with open(json_file_path, 'r') as pixarkoffers_file:
        data = json.load(pixarkoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/showmaker/offers', methods=['GET'])
def showmakeroffers():
    json_file_path = os.path.join('offers', 'showmakeroffers.json')
    with open(json_file_path, 'r') as showmakeroffers_file:
        data = json.load(showmakeroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/squad/offers', methods=['GET'])
def squadoffers():
    json_file_path = os.path.join('offers', 'squadoffers.json')
    with open(json_file_path, 'r') as squadoffers_file:
        data = json.load(squadoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/vrfunhouse/offers', methods=['GET'])
def vrfunhouseoffers():
    json_file_path = os.path.join('offers', 'vrfunhouseoffers.json')
    with open(json_file_path, 'r') as vrfunhouseoffers_file:
        data = json.load(vrfunhouseoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/wren/offers', methods=['GET'])
def wrenoffers():
    json_file_path = os.path.join('offers', 'wrenoffers.json')
    with open(json_file_path, 'r') as wrenoffers_file:
        data = json.load(wrenoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/vpr/offers', methods=['GET'])
def vproffers():
    json_file_path = os.path.join('offers', 'vproffers.json')
    with open(json_file_path, 'r') as vproffers_file:
        data = json.load(vproffers_file)
    return data

@app.route('/catalog/api/shared/namespace/morpho/offers', methods=['GET'])
def morphooffers():
    json_file_path = os.path.join('offers', 'morphooffers.json')
    with open(json_file_path, 'r') as morphooffers_file:
        data = json.load(morphooffers_file)
    return data

@app.route('/catalog/api/shared/namespace/min/offers', methods=['GET'])
def minoffers():
    json_file_path = os.path.join('offers', 'minoffers.json')
    with open(json_file_path, 'r') as minoffers_file:
        data = json.load(minoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/ut/offers', methods=['GET'])
def utoffers():
    json_file_path = os.path.join('offers', 'utoffers.json')
    with open(json_file_path, 'r') as utoffers_file:
        data = json.load(utoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/fn/offers', methods=['GET'])
def fnoffers():
    try:
        json_file_path = os.path.join('offers', 'fnoffers.json')
        with open(json_file_path, 'r') as fnoffers_file:
            data = json.load(fnoffers_file)
        return jsonify(data)
    except json.JSONDecodeError as e:
        return jsonify({"error": f"JSON decoding error: {str(e)}"}), 500
    except UnicodeDecodeError as e:
        return jsonify({"error": f"Unicode decoding error: {str(e)}"}), 500

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
    
@app.route('/catalog/api/shared/bulk/items')

def run_flask():
    print(f'EGL-Custom-Backend Running on Port {launcher_port}')
    app.run(host='0.0.0.0', port=launcher_port)

run_flask()