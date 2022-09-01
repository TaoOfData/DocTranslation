# Translate a specific document in container
import requests
import http.client

endpoint = "https://tao-translator.cognitiveservices.azure.com/translator/text/batch/v1.0"
subscriptionKey = '<replace with subscription key>'
path = '/batches'
constructed_url = endpoint + path

payload= {
    "inputs": [
        {
            "storageType": "File",
            "source": {
                "sourceUrl": "https://taoblobstorage.blob.core.windows.net/tao-source-container/anne-frank-source/anne-frank.txt?sv=2020-10-02&st=2022-01-19T07%3A54%3A11Z&se=2022-01-20T07%3A54%3A11Z&sr=b&sp=r&sig=C%2BC%2B3EV2K7kk7xefT8Q9ts0Fhrd63%2BqshSJ72NL2BZo%3D",
                "language": "nl"
            },
            "targets": [
                {
                    "targetUrl": "https://taoblobstorage.blob.core.windows.net/tao-target-container/anne-frank-target/anne-frank-text-output.txt?sv=2020-10-02&st=2022-01-19T05%3A55%3A35Z&se=2022-02-12T05%3A55%3A00Z&sr=c&sp=wl&sig=9KGHDuMi7AVCDFreom6QrFXCYX6WU6lyb2YyW7iNIiI%3D",
                    "language": "en"
                }
            ]
        }
    ]
}

headers = {
  'Ocp-Apim-Subscription-Key': '<replace with subscription key>',
  'Content-Type': 'application/json'
}

response = requests.post(constructed_url, headers=headers, json=payload)

print(f'response status code: {response.status_code}\nresponse status: {response.reason}\nresponse headers: {response.headers}')



host = 'tao-translator.cognitiveservices.azure.com'
parameters = '//translator/text/batch/v1.0/documents/formats'
subscriptionKey = '<replace with subscription key>'
conn = http.client.HTTPSConnection(host)
payload = ''
headers = {
  'Ocp-Apim-Subscription-Key': subscriptionKey
}
conn.request("GET", parameters , payload, headers)
res = conn.getresponse()
data = res.read()
print(res.status)
print()
print(data.decode("utf-8"))

# Get Job Status
host = 'tao-translator.cognitiveservices.azure.com'
parameters = '//translator/text/batch/v1.0/batches/836960e8-81fb-49c7-bd14-a5e5ce84216f'
subscriptionKey = '<replace with subscription key>'
conn = http.client.HTTPSConnection(host)
payload = ''
headers = {
  'Ocp-Apim-Subscription-Key': subscriptionKey
}
conn.request("GET", parameters , payload, headers)
res = conn.getresponse()
data = res.read()
print(res.status)
print()
print(data.decode("utf-8"))