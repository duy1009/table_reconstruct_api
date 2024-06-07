import requests

HOST = '127.0.0.1'
PORT = '8001'

image_path = r"B.png"

def htmlTableAPI(img_path):
    files = {"image": open(img_path, 'rb')}
    resp = requests.post(f'http://{HOST}:{PORT}/extract-table-v2', files=files)
    
    if resp.status_code == 200:
        data_recv = resp.json()
        return data_recv
    else:
        return None

# Return [bbox, cell_information]
#       - bbox: [x1, y1, x2, y2]
#       - cell_information: [index_collum, index_row, span_collum, span_row]

table = htmlTableAPI(image_path)

try:
    f = open("table.html", "w")
    f.write(table["table"])
    f.close()

    print(table["table"])
except:
    print(table)

