






import json
with open ('line.json') as f:
    line_json = json.load(f)
    
import requests

def notify_message(message):
        LINE_NOTIFY_TOKEN = "v5umZRPB958apwnBiKy8w0dsykBrYVsALc5xDWMuWlV"
        url = 'https://notify-api.line.me/api/notify'
        #message = '[リマインド]リネン交換の呼びかけをお願いします'

        headers = {
            'Authorization': f'Bearer {LINE_NOTIFY_TOKEN}'
        }

        data = {
            'message' : message
        }

        requests.post(
            url,
            headers = headers,
            data = data
        )

def main():
    message ='[リマインド]リネン交換の呼びかけをお願いします'
    notify_message(message)
    
if __name__ == "__main__":
    main()
