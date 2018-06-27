from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

model = app.models.get('puppy')
response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])