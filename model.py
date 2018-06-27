from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='f7edd16755e74c4e9e27517e7ccdd310')

# IMAGES
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Galaxy Merger", "eliptical"], not_concepts=["Not Galaxy Merger"], 
    allow_duplicate_url=True)

app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Not Galaxy Merger", "eliptical"], not_concepts=["Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Not Galaxy Merger", "eliptical"], not_concepts=["Galaxy Merger"], 
    allow_duplicate_url=True)
app.inputs.create_image_from_url(url="https://samples.clarifai.com/dog1.jpeg", concepts=["Not Galaxy Merger", "eliptical"], not_concepts=["Galaxy Merger"], 
    allow_duplicate_url=True)

img_model = app.models.create(model_id="Galaxy merger Properties", concepts=["Galaxy Merger", 
    "eliptical", "spiral", "irregular", "Not Galaxy Merger"])

img_model = img_model.train()



model = app.models.get('Galaxy merger Properties')
response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])