from flask import Flask, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/pager')
def pager():
  link = request.args.get('link', default=None)
  if link is None:
    return 'Failed'

  youtube = YouTube(url=link)

  return f'Video ID : {youtube.video_id}'


@app.route('/')
def index():
  
  return f'Video ID : youtube.video_id'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
