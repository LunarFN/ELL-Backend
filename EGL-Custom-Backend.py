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

@app.route('/catalog/api/shared/namespace/ark/items', methods=['GET'])
def arkitems():
    with open('arkitems.json', 'r') as arkitems_file:
        data = json.load(arkitems_file)
    return data

@app.route('/catalog/api/shared/namespace/darkandlight/items', methods=['GET'])
def darkandlightitems():
    with open('darkandlightitems.json', 'r') as darkandlightitems_file:
        data = json.load(darkandlightitems_file)
    return data

@app.route('/catalog/api/shared/namespace/helloneighbor/items', methods=['GET'])
def helloneighboritems():
    with open('helloneighboritems.json', 'r') as helloneighboritems_file:
        data = json.load(helloneighboritems_file)
    return data

@app.route('/catalog/api/shared/namespace/mars2030/items', methods=['GET'])
def mars2030items():
    with open('mars2030items.json', 'r') as mars2030items_file:
        data = json.load(mars2030items_file)
    return data

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

@app.route('/catalog/api/shared/namespace/showmaker/items', methods=['GET'])
def showmakeritems():
    with open('showmakeritems.json', 'r') as showmakeritems_file:
        data = json.load(showmakeritems_file)
    return data

@app.route('/catalog/api/shared/namespace/squad/items', methods=['GET'])
def squaditems():
    with open('squaditems.json', 'r') as squaditems_items:
        data = json.load(squaditems_items)
    return data

@app.route('/catalog/api/shared/namespace/vrfunhouse/items', methods=['GET'])
def vrfunhouseitems():
    with open('vrfunhouseitems.json', 'r') as vrfunhouseitems_file:
        data = json.load(vrfunhouseitems_file)
    return data

@app.route('/catalog/api/shared/namespace/fn/items', methods=['GET'])
def fnitems():
    with open('fnitems.json', 'r') as fnitems_file:
        data = json.load(fnitems_file)
    return data

@app.route('/catalog/api/shared/namespace/jaguar/items', methods=['GET'])
def jaguaritems():
    with open('jaguaritems.json', 'r') as jaguaritems_file:
        data = json.load(jaguaritems_file)
    return data

@app.route('/catalog/api/shared/namespace/min/items', methods=['GET'])
def minitems():
    with open('minitems.json', 'r') as minitems_file:
        data = json.load(minitems_file)
    return data

@app.route('/catalog/api/shared/namespace/morpho/items', methods=['GET'])
def morphoitems():
    with open('morphoitems.json', 'r') as morphoitems_file:
        data = json.load(morphoitems_file)
    return data

@app.route('/catalog/api/shared/namespace/springbok/items', methods=['GET'])
def springbokitems():
    with open('springbokitems.json', 'r') as springbokitems_file:
        data = json.load(springbokitems_file)
    return data

@app.route('/catalog/api/shared/namespace/ut/items', methods=['GET'])
def utitems():
    with open('utitems.json', 'r') as utitems_file:
        data = json.load(utitems_file)
    return data

@app.route('/catalog/api/shared/namespace/vpr/items', methods=['GET'])
def vpritems():
    with open('vpritems.json', 'r') as vpritems_file:
        data = json.load(vpritems_file)
    return data

@app.route('/catalog/api/shared/namespace/wren/items', methods=['GET'])
def wrenitems():
    with open('wrenitems.json', 'r') as wrenitems_file:
        data = json.load(wrenitems_file)
    return data

@app.route('/catalog/api/shared/namespace/ark/offers', methods=['GET'])
def arkoffers():
    with open('arkoffers.json', 'r') as arkoffers_file:
        data = json.load(arkoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/darkandlight/offers', methods=['GET'])
def darkandlightoffers():
    with open('darkandlightoffers.json', 'r') as darkandlightoffers_file:
        data = json.load(darkandlightoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/helloneighbor/offers', methods=['GET'])
def helloneighboroffers():
    with open('helloneighboroffers.json', 'r') as helloneighboroffers_file:
        data = json.load(helloneighboroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/mars2030/offers', methods=['GET'])
def mars2030offers():
    with open('mars2030offers.json', 'r') as mars2030offers_file:
        data = json.load(mars2030offers_file)
    return data

@app.route('/catalog/api/shared/namespace/bussim18/offers', methods=['GET'])
def bussim18offers():
    with open('bussim18offers.json', 'r') as bussim18offers_file:
        data = json.load(bussim18offers_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/conanexiles/offers', methods=['GET'])
def conanexilesoffers():
    with open('conanexilesoffers.json', 'r') as conanexilesoffers_file:
        data = json.load(conanexilesoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/springbok/offers', methods=['GET'])
def springbokoffers():
    with open('springbokoffers.json', 'r') as springbokoffers_file:
        data = json.load(springbokoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/jaguar/offers', methods=['GET'])
def jaguaroffers():
    with open('jaguaroffers.json', 'r') as jaguaroffers_file:
        data = json.load(jaguaroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/odin/offers', methods=['GET'])
def odinoffers():
    with open('odinoffers.json', 'r') as odinoffers_file:
        data = json.load(odinoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/pixark/offers', methods=['GET'])
def pixarkoffers():
    with open('pixarkoffers.json', 'r') as pixarkoffers_file:
        data = json.load(pixarkoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/showmaker/offers', methods=['GET'])
def showmakeroffers():
    with open('showmakeroffers.json', 'r') as showmakeroffers_file:
        data = json.load(showmakeroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/squad/offers', methods=['GET'])
def squadoffers():
    with open('squadoffers.json', 'r') as squadoffers_file:
        data = json.load(squadoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/vrfunhouse/offers', methods=['GET'])
def vrfunhouseoffers():
    with open('vrfunhouseoffers.json', 'r') as vrfunhouseoffers_file:
        data = json.load(vrfunhouseoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/wren/offers', methods=['GET'])
def wrenoffers():
    with open('wrenoffers.json', 'r') as wrenoffers_file:
        data = json.load(wrenoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/vpr/offers', methods=['GET'])
def vproffers():
    with open('vproffers.json', 'r')as vproffers_file:
        data = json.load(vproffers_file)
    return data

@app.route('/catalog/api/shared/namespace/morpho/offers', methods=['GET'])
def morphooffers():
    with open('morphooffers.json', 'r') as morphooffers_file:
        data = json.load(morphooffers_file)
    return data

@app.route('/catalog/api/shared/namespace/min/offers', methods=['GET'])
def minoffers():
    with open('minoffers.json', 'r') as minoffers_file:
        data = json.load(minoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/ut/offers', methods=['GET'])
def utoffers():
    with open('utoffers.json', 'r') as utoffers_file:
        data = json.load(utoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/fn/offers', methods=['GET'])
def fnoffers():
    with open('fnoffers.json', 'r') as fnoffers_file:
        data = json.load(fnoffers_file)
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
    
@app.route('/catalog/api/shared/bulk/items')

def run_flask():
    print(f'EGL-Custom-Backend Running on Port 3551')
    app.run(host='0.0.0.0', port=3551)

run_flask()