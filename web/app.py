from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image 
from clarifai.rest import Video as ClVideo

cli = ClarifaiApp(api_key='dbebac7e90f84eabbda37a5f604eaa39')

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    image = TextField('ImageURL:', validators=[validators.required()])

@app.route("/")
def index():
    return render_template('index.html')
 
@app.route("/image", methods=['GET', 'POST'])
def image():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        image_url=request.form['image']

        img_model = cli.models.get('Galaxy merger Propertiesxc')
        image = Image(file_obj=open(image_url, 'rb'))
        response = img_model.predict([image])
 
        if form.validate():
            concepts = response['outputs'][0]['data']['concepts']
            for concept in concepts:
                flash((concept['name'], concept['value']))
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('image.html', form=form)

@app.route("/video", methods=['GET', 'POST'])
def video():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        video_url=request.form['video']

        model = cli.models.get('general-v1.3')
        video = ClVideo(url=video_url)
        response = model.predict([video])
 
        if form.validate():
            flash(response)
        else:
            flash(response)
 
    return render_template('video.html', form=form)
 
if __name__ == "__main__":
    app.run()