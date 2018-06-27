from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from clarifai.rest import ClarifaiApp
from clarifai.rest import ClarifaiApp
from clarifai.rest import Video as ClVideo

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

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    image = TextField('ImageURL:', validators=[validators.required()])
 
@app.route("/image", methods=['GET', 'POST'])
def image():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        image_url=request.form['image']

        response = img_model.predict_by_url(url=image_url)
        concepts = response['outputs'][0]['data']['concepts']
        for concept in concepts:
            print(concept['name'], concept['value'])
 
        if form.validate():
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('image.html', form=form)

@app.route("/video", methods=['GET', 'POST'])
def video():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        video_url=request.form['video']

        response = vid_model.predict_by_url(url=image_url)
        concepts = response['outputs'][0]['data']['concepts']
        for concept in concepts:
            print(concept['name'], concept['value'])
 
        if form.validate():
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('video.html', form=form)
 
if __name__ == "__main__":
    app.run()