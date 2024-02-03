from flask import Flask, make_response, jsonify, request, send_file
from flask_cors import CORS
import json
import os

launcher_port = "3551"
username_email = {}
email = {}

app = Flask(__name__)
CORS(app)

def process_ark():
    json_file_path = os.path.join('responses/priceengine', 'arkpriceengine.json')
    with open(json_file_path, 'r') as arkpriceengine_file:
        data = json.load(arkpriceengine_file)
    return data

def process_squad():
    json_file_path = os.path.join('responses/priceengine', 'squadpriceengine.json')
    with open(json_file_path, 'r') as squadpriceengine_file:
        data = json.load(squadpriceengine_file)
    return data

def process_mars2030():
    json_file_path = os.path.join('responses/priceengine', 'mars2030priceengine.json')
    with open(json_file_path, 'r') as mars2030priceengine_file:
        data = json.load(mars2030priceengine_file)
    return data

def process_jaguar():
    json_file_path = os.path.join('responses/priceengine', 'jaguarpriceengine.json')
    with open(json_file_path, 'r') as jaguarpriceengine_file:
        data = json.load(jaguarpriceengine_file)
    return data

def process_helloneigbor():
    json_file_path = os.path.join('responses/priceengine', 'helloneighborpriceengine.json')
    with open(json_file_path, 'r') as helloneighborpriceengine_file:
        data = json.load(helloneighborpriceengine_file)
    return data

def process_darkandlight():
    json_file_path = os.path.join('responses/priceengine', 'darkandlightpriceengine.json')
    with open(json_file_path, 'r') as darkandlightpriceengine_file:
        data = json.load(darkandlightpriceengine_file)
    return data

def process_min():
    json_file_path = os.path.join('responses/priceengine', 'minpriceengine.json')
    with open(json_file_path, 'r') as minpriceengine_file:
        data = json.load(minpriceengine_file)
    return data

def process_vrfunhouse():
    json_file_path = os.path.join('responses/priceengine', 'vrfunhousepriceengine.json')
    with open(json_file_path, 'r') as vrfunhousepriceengine_file:
        data = json.load(vrfunhousepriceengine_file)
    return data

def process_springbok():
    json_file_path = os.path.join('responses/priceengine', 'springbokpriceengine.json')
    with open(json_file_path, 'r') as springbokpriceengine_file:
        data = json.load(springbokpriceengine_file)
    return data

def process_bussim18():
    json_file_path = os.path.join('responses/priceengine', 'bussim18priceengine.json')
    with open(json_file_path, 'r') as bussim18priceengine_file:
        data = json.load(bussim18priceengine_file)
    return data

def process_showmaker():
    json_file_path = os.path.join('responses/priceengine', 'showmakerpriceengine.json')
    with open(json_file_path, 'r') as showmakerpriceengine_file:
        data = json.load(showmakerpriceengine_file)
    return data

def process_pixark():
    json_file_path = os.path.join('responses/priceengine', 'pixarkpriceengine.json')
    with open(json_file_path, 'r') as pixarkpriceengine_file:
        data = json.load(pixarkpriceengine_file)
    return data

def process_odin():
    json_file_path = os.path.join('responses/priceengine', 'odinpriceengine.json')
    with open(json_file_path, 'r') as odinpriceengine_file:
        data = json.load(odinpriceengine_file)
    return data

def process_wren():
    json_file_path = os.path.join('responses/priceengine', 'wrenpriceengine.json')
    with open(json_file_path, 'r') as wrenpriceengine_file:
        data = json.load(wrenpriceengine_file)
    return data

def process_vpr():
    json_file_path = os.path.join('responses/priceengine', 'vprpriceengine.json')
    with open(json_file_path, 'r') as vprpriceengine_file:
        data = json.load(vprpriceengine_file)
    return data

def process_morpho():
    json_file_path = os.path.join('responses/priceengine', 'morphopriceengine.json')
    with open(json_file_path, 'r') as morphopriceengine_file:
        data = json.load(morphopriceengine_file)
    return data

def process_conanexiles():
    json_file_path = os.path.join('responses/priceengine', 'conanexilespriceengine.json')
    with open(json_file_path, 'r') as conanexilespriceengine_file:
        data = json.load(conanexilespriceengine_file)
    return data

def process_fn():
    json_file_path = os.path.join('responses/priceengine', 'fnpriceengine.json')
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

@app.route('/custom/public/images/lunarwidetrans.png')
def customlunarwidetrans():
    image_file_path = os.path.join('custom/images', 'lunarwidetrans.png')
    content_type = 'image/png'
    return send_file(image_file_path, mimetype=content_type)

@app.route('/waitingroom/api/waitingroom', methods=['GET'])
def waitingroomskip():
    response = make_response('Why tf u reading this?', 204)

    return response

@app.route('/datarouter/api/v1/public/data', methods=['POST'])
def datarouter():
    response = make_response('response', 204)
    form_data = request.form  # If the data is in form format

    return response

@app.route('/account/api/oauth/token', methods=['POST'])
def token():
    # Assuming the data is sent as form data
    form_data = request.form

    # Check for the specific conditions in the form data
    if form_data.get('grant_type') == 'client_credentials':
        json_file_path = os.path.join('responses/account', 'static_token_response.json')
        with open(json_file_path, 'r') as static_account_file:
            data = json.load(static_account_file)
        return data

    elif form_data.get('grant_type') == 'password' and 'username' in form_data and 'password' in form_data and form_data.get('includePerms') == 'true':
        # Extract username from email
        global email
        email = form_data['username']
        global username_email
        username_email = email.split('@')[0]

        # Create the JSON response
        json_response = {
            "access_token": "eg1~h1e35h4tr5h456r4h75r4h8r4h5r45h4r5",
            "expires_in": 28800,
            "expires_at": "2050-01-01T00:00:00.000Z",
            "token_type": "bearer",
            "refresh_token": "hjbehjiptjhioptrjhiojeroih",
            "refresh_expires": 86400,
            "refresh_expires_at": "2050-01-01T00:00:00.000Z",
            "account_id": "r54hre45h4r5th48r5hrhr54h56rhr",
            "client_id": "he454e5h48te77h48eh",
            "internal_client": True,
            "client_service": "prod-fn",
            "displayName": f"{username_email}",
            "app": "EpicPortal",
            "in_app_id": "r54hre45h4r5th48r5hrhr54h56rhr",
            "device_id": "he75h4et7hr52h"
        }

        # Respond with the JSON response and 200 status
        return jsonify(json_response), 200

    else:
        # Respond with an error or handle other cases as needed
        return 'Invalid request data', 400


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
    # Assuming the data is sent as form data
    form_data = request.form
    print(f"Form Data: {form_data}")
    global username_email
    global email

    # Create the JSON response
    json_response = {
        "id": "r54hre45h4r5th48r5hrhr54h56rhr",
        "displayName": f"{username_email}",
        "name": f"{username_email}",
        "email": f"{email}",
        "failedLoginAttempts": 0,
        "lastLogin": "2020-01-01T00:00:00.000Z",
        "numberOfDisplayNameChanges": 0,
        "ageGroup": "UNKNOWN",
        "headless": "false",
        "country": "US",
        "lastName": "Server",
        "preferredLanguage": "en",
        "canUpdateDisplayName": "false",
        "tfaEnabled": "false",
        "emailVerified": "true",
        "minorVerified": "false",
        "minorExpected": "false",
        "minorStatus": "NOT_MINOR",
        "cabinedMode": "false",
        "hasHashedEmail": "false"
        }

        
    return jsonify(json_response), 200

@app.route('/account/api/public/account/r54hre45h4r5th48r5hrhr54h56rhr/externalAuths', methods=['GET'])
def externalauths():
    json_file_path = os.path.join('responses/account', 'static_externalAuths.json')
    with open(json_file_path, 'r') as static_externalAuths_file:
        data = json.load(static_externalAuths_file)
    return jsonify(data)

@app.route('/account/api/epicdomains/ssodomains', methods=['GET'])
def ssdomains():
    json_file_path = os.path.join('responses/ssdomains', 'static_ssdomains.json')
    with open(json_file_path, 'r') as static_ssdomains_file:
        data = json.load(static_ssdomains_file)
    return jsonify(data)

@app.route('/launcher/api/public/payment/accounts/r54hre45h4r5th48r5hrhr54h56rhr/billingaccounts/default', methods=['GET'])
def savedpayment():
    json_file_path = os.path.join('responses/account', 'static_savedpayment.json')
    with open(json_file_path, 'r') as static_savedpayment_file:
        data = json.load(static_savedpayment_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/bussim18/items', methods=['GET'])
def bussim18items():
    json_file_path = os.path.join('responses/items', 'bussim18items.json')
    with open(json_file_path, 'r') as bussim18items_file:
        data = json.load(bussim18items_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/ark/items', methods=['GET'])
def arkitems():
    json_file_path = os.path.join('responses/items', 'arkitems.json')
    with open(json_file_path, 'r') as arkitems_file:
        data = json.load(arkitems_file)
    return data

@app.route('/catalog/api/shared/namespace/darkandlight/items', methods=['GET'])
def darkandlightitems():
    json_file_path = os.path.join('responses/items', 'darkandlightitems.json')
    with open(json_file_path, 'r') as darkandlightitems_file:
        data = json.load(darkandlightitems_file)
    return data

@app.route('/catalog/api/shared/namespace/helloneighbor/items', methods=['GET'])
def helloneighboritems():
    json_file_path = os.path.join('responses/items', 'helloneighboritems.json')
    with open(json_file_path, 'r') as helloneighboritems_file:
        data = json.load(helloneighboritems_file)
    return data

@app.route('/catalog/api/shared/namespace/mars2030/items', methods=['GET'])
def mars2030items():
    json_file_path = os.path.join('responses/items', 'mars2030items.json')
    with open(json_file_path, 'r') as mars2030items_file:
        data = json.load(mars2030items_file)
    return data

@app.route('/catalog/api/shared/namespace/conanexiles/items', methods=['GET'])
def conanexilesitems():
    json_file_path = os.path.join('responses/items', 'conanexilesitems.json')
    with open(json_file_path, 'r') as conanexilesitems_file:
        data = json.load(conanexilesitems_file)
    return data

@app.route('/catalog/api/shared/namespace/odin/items', methods=['GET'])
def odinitems():
    try:
        json_file_path = os.path.join('responses/items', 'odinitems.json')
        with open(json_file_path, 'r') as odinitems_file:
            data = json.load(odinitems_file)
        return jsonify(data)
    except json.JSONDecodeError as e:
        return jsonify({"error": f"JSON decoding error: {str(e)}"}), 500
    except UnicodeDecodeError as e:
        return jsonify({"error": f"Unicode decoding error: {str(e)}"}), 500

@app.route('/catalog/api/shared/namespace/pixark/items', methods=['GET'])
def pixarkitems():
    json_file_path = os.path.join('responses/items', 'pixarkitems.json')
    with open(json_file_path, 'r') as pixarkitems_file:
        data = json.load(pixarkitems_file)
    return data

@app.route('/catalog/api/shared/namespace/showmaker/items', methods=['GET'])
def showmakeritems():
    json_file_path = os.path.join('responses/items', 'showmakeritems.json')
    with open(json_file_path, 'r') as showmakeritems_file:
        data = json.load(showmakeritems_file)
    return data

@app.route('/catalog/api/shared/namespace/squad/items', methods=['GET'])
def squaditems():
    json_file_path = os.path.join('responses/items', 'squaditems.json')
    with open(json_file_path, 'r') as squaditems_file:
        data = json.load(squaditems_file)
    return data

@app.route('/catalog/api/shared/namespace/vrfunhouse/items', methods=['GET'])
def vrfunhouseitems():
    json_file_path = os.path.join('responses/items', 'vrfunhouseitems.json')
    with open(json_file_path, 'r') as vrfunhouseitems_file:
        data = json.load(vrfunhouseitems_file)
    return data

@app.route('/catalog/api/shared/namespace/fn/items', methods=['GET'])
def fnitems():
    json_file_path = os.path.join('responses/items', 'fnitems.json')
    with open(json_file_path, 'r') as fnitems_file:
        data = json.load(fnitems_file)
    return data

@app.route('/catalog/api/shared/namespace/jaguar/items', methods=['GET'])
def jaguaritems():
    json_file_path = os.path.join('responses/items', 'jaguaritems.json')
    with open(json_file_path, 'r') as jaguaritems_file:
        data = json.load(jaguaritems_file)
    return data

@app.route('/catalog/api/shared/namespace/min/items', methods=['GET'])
def minitems():
    json_file_path = os.path.join('responses/items', 'minitems.json')
    with open(json_file_path, 'r') as minitems_file:
        data = json.load(minitems_file)
    return data

@app.route('/catalog/api/shared/namespace/morpho/items', methods=['GET'])
def morphoitems():
    json_file_path = os.path.join('responses/items', 'morphoitems.json')
    with open(json_file_path, 'r') as morphoitems_file:
        data = json.load(morphoitems_file)
    return data

@app.route('/catalog/api/shared/namespace/springbok/items', methods=['GET'])
def springbokitems():
    json_file_path = os.path.join('responses/items', 'springbokitems.json')
    with open(json_file_path, 'r') as springbokitems_file:
        data = json.load(springbokitems_file)
    return data

@app.route('/catalog/api/shared/namespace/ut/items', methods=['GET'])
def utitems():
    json_file_path = os.path.join('responses/items', 'utitems.json')
    with open(json_file_path, 'r') as utitems_file:
        data = json.load(utitems_file)
    return data

@app.route('/catalog/api/shared/namespace/vpr/items', methods=['GET'])
def vpritems():
    json_file_path = os.path.join('responses/items', 'vpritems.json')
    with open(json_file_path, 'r') as vpritems_file:
        data = json.load(vpritems_file)
    return data

@app.route('/catalog/api/shared/namespace/wren/items', methods=['GET'])
def wrenitems():
    json_file_path = os.path.join('responses/items', 'wrenitems.json')
    with open(json_file_path, 'r') as wrenitems_file:
        data = json.load(wrenitems_file)
    return data

@app.route('/catalog/api/shared/namespace/ark/offers', methods=['GET'])
def arkoffers():
    json_file_path = os.path.join('responses/offers', 'arkoffers.json')
    with open(json_file_path, 'r') as arkoffers_file:
        data = json.load(arkoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/darkandlight/offers', methods=['GET'])
def darkandlightoffers():
    json_file_path = os.path.join('responses/offers', 'darkandlightoffers.json')
    with open(json_file_path, 'r') as darkandlightoffers_file:
        data = json.load(darkandlightoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/helloneighbor/offers', methods=['GET'])
def helloneighboroffers():
    json_file_path = os.path.join('responses/offers', 'helloneighboroffers.json')
    with open(json_file_path, 'r') as helloneighboroffers_file:
        data = json.load(helloneighboroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/mars2030/offers', methods=['GET'])
def mars2030offers():
    json_file_path = os.path.join('responses/offers', 'mars2030offers.json')
    with open(json_file_path, 'r') as mars2030offers_file:
        data = json.load(mars2030offers_file)
    return data

@app.route('/catalog/api/shared/namespace/bussim18/offers', methods=['GET'])
def bussim18offers():
    json_file_path = os.path.join('responses/offers', 'bussim18offers.json')
    with open(json_file_path, 'r') as bussim18offers_file:
        data = json.load(bussim18offers_file)
    return jsonify(data)

@app.route('/catalog/api/shared/namespace/conanexiles/offers', methods=['GET'])
def conanexilesoffers():
    json_file_path = os.path.join('responses/offers', 'conanexilesoffers.json')
    with open(json_file_path, 'r') as conanexilesoffers_file:
        data = json.load(conanexilesoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/springbok/offers', methods=['GET'])
def springbokoffers():
    json_file_path = os.path.join('responses/offers', 'springbokoffers.json')
    with open(json_file_path, 'r') as springbokoffers_file:
        data = json.load(springbokoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/jaguar/offers', methods=['GET'])
def jaguaroffers():
    json_file_path = os.path.join('responses/offers', 'jaguaroffers.json')
    with open(json_file_path, 'r') as jaguaroffers_file:
        data = json.load(jaguaroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/odin/offers', methods=['GET'])
def odinoffers():
    json_file_path = os.path.join('responses/offers', 'odinoffers.json')
    with open(json_file_path, 'r') as odinoffers_file:
        data = json.load(odinoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/pixark/offers', methods=['GET'])
def pixarkoffers():
    json_file_path = os.path.join('responses/offers', 'pixarkoffers.json')
    with open(json_file_path, 'r') as pixarkoffers_file:
        data = json.load(pixarkoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/showmaker/offers', methods=['GET'])
def showmakeroffers():
    json_file_path = os.path.join('responses/offers', 'showmakeroffers.json')
    with open(json_file_path, 'r') as showmakeroffers_file:
        data = json.load(showmakeroffers_file)
    return data

@app.route('/catalog/api/shared/namespace/squad/offers', methods=['GET'])
def squadoffers():
    json_file_path = os.path.join('responses/offers', 'squadoffers.json')
    with open(json_file_path, 'r') as squadoffers_file:
        data = json.load(squadoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/vrfunhouse/offers', methods=['GET'])
def vrfunhouseoffers():
    json_file_path = os.path.join('responses/offers', 'vrfunhouseoffers.json')
    with open(json_file_path, 'r') as vrfunhouseoffers_file:
        data = json.load(vrfunhouseoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/wren/offers', methods=['GET'])
def wrenoffers():
    json_file_path = os.path.join('responses/offers', 'wrenoffers.json')
    with open(json_file_path, 'r') as wrenoffers_file:
        data = json.load(wrenoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/vpr/offers', methods=['GET'])
def vproffers():
    json_file_path = os.path.join('responses/offers', 'vproffers.json')
    with open(json_file_path, 'r') as vproffers_file:
        data = json.load(vproffers_file)
    return data

@app.route('/catalog/api/shared/namespace/morpho/offers', methods=['GET'])
def morphooffers():
    json_file_path = os.path.join('responses/offers', 'morphooffers.json')
    with open(json_file_path, 'r') as morphooffers_file:
        data = json.load(morphooffers_file)
    return data

@app.route('/catalog/api/shared/namespace/min/offers', methods=['GET'])
def minoffers():
    json_file_path = os.path.join('responses/offers', 'minoffers.json')
    with open(json_file_path, 'r') as minoffers_file:
        data = json.load(minoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/ut/offers', methods=['GET'])
def utoffers():
    json_file_path = os.path.join('responses/offers', 'utoffers.json')
    with open(json_file_path, 'r') as utoffers_file:
        data = json.load(utoffers_file)
    return data

@app.route('/catalog/api/shared/namespace/fn/offers', methods=['GET'])
def fnoffers():
    try:
        json_file_path = os.path.join('responses/offers', 'fnoffers.json')
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