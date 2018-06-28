from clarifai.rest import ClarifaiApp
from clarifai.rest import Image 
from clarifai.rest import Video as ClVideo

cli = ClarifaiApp(api_key='dbebac7e90f84eabbda37a5f604eaa39')


# vid_model = cli.models.get('Galaxy merger Propertiesxc')
# vid = Video(file_obj=open('/home/captain/Downloads/videoplayback(10).mp4', 'rb'))
# response = vid_model.predict([vid])

model = cli.models.get('general-v1.3')
video = ClVideo(url='https://samples.clarifai.com/beer.mp4')
response = model.predict([video])

print response
 