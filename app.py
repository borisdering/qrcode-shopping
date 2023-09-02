from flask import Flask, request
import requests
import logging

app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/add_item', methods=['GET'])
def add_item():

    item_to_add = request.args.get('item')
    if not item_to_add:
        return 'Item not specified', 400
    
    logging.info(f'Adding {item_to_add} to the shopping list')

    home_assistant_url = 'http://homeassistant:8123/api/services/shopping_list/add_item'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'content-type': 'application/json',
    }
    data = {
        'name': item_to_add,
    }
    response = requests.post(home_assistant_url, json=data, headers=headers)
    
    if response.status_code == 201:
        logging.info(f'Successfully added {item_to_add} to the shopping list.')
        return f'Successfully added {item_to_add} to the shopping list.', 200
    else:
        logging.info(f'Failed to add item. Status code: {response.status_code}')
        return f'Failed to add item. Status code: {response.status_code}', 400

if __name__ == '__main__':
    logging.info('Starting Flask server')
    app.run(host='0.0.0.0', port=5000)