from flask import Flask, request, Response
from pytube import YouTube

app = Flask(__name__)


@app.route('/download')
def pager():
  link = request.args.get('link', default=None)
  if link is None:
    return Response(
        status=401,
        response='{"error": "No link provided"}',
    )

  youtube = YouTube(url='https://youtu.be/seNW8WeHyLs?feature=shared')

  files = youtube.streams

  for file in files:
    if 'webm' not in file.mime_type:
      print(
          f'{file.includes_audio_track} : {file.includes_video_track}:{file.mime_type} : {file.resolution}'
      )

  return f'Video ID : {link}'


@app.route('/')
def index():

  return f'Video ID : youtube.video_id'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
