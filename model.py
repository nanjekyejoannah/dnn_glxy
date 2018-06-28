from clarifai.rest import ClarifaiApp
from clarifai.rest import Image 

app = ClarifaiApp(api_key='dbebac7e90f84eabbda37a5f604eaa39')

## metadata must be defined as JSON object
metadata = {'id':'id001', 'type':'plants', 'size':100}

app.inputs.create_image_from_filename(filename="galimg1.jpeg", concepts=["Galaxy Merger", "spiral"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimg2.jpeg", concepts=["Galaxy Merger", "irregular"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_url(url="https://samples.clarifai.com/metro-north.jpg", concepts=["Galaxy Merger", "spiral"], 
             not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimg3.jpeg", concepts=["Galaxy Merger", "spiral"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimg4.jpeg", concepts=["Galaxy Merger", "spiral"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimg5.jpeg", concepts=["Galaxy Merger", "spiral"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimg6.jpeg", concepts=["Galaxy Merger", "spiral"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimg7.jpeg", concepts=["Galaxy Merger", "spiral"], 
            not_concepts=["Not Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimgno.jpeg", concepts=["Not Galaxy Merger", "spiral"], 
            not_concepts=["Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="galimgno1.jpeg", concepts=["Not Galaxy Merger", "spiral"], 
            not_concepts=["Galaxy Merger"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="irregular.png", concepts=["Not Galaxy Merger, irregular"], 
            not_concepts=["Galaxy Merger, spiral"], allow_duplicate_url=True)

app.inputs.create_image_from_filename(filename="spiral.png", concepts=["Not Galaxy Merger, spiral"], 
            not_concepts=["Galaxy Merger, spiral"], allow_duplicate_url=True)


img_model = app.models.create(model_id="final", concepts=["Galaxy Merger", 
            "spiral", "Not Galaxy Merger"])

img_model = img_model.train()

response = img_model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')

concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
    print(concept['name'], concept['value'])

