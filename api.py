import requests
import json
import cv2

def ocr_space_file(filename, overlay=False, api_key='566f3435cd88957', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'filetype': 'png',
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    m = r.content.decode()
    jsonstr = json.loads(m)
    return(jsonstr["ParsedResults"][0]["ParsedText"])
