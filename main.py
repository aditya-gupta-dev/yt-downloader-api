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

  youtube = YouTube(
      url='https://youtube.com/shorts/5hECAEzmBxc?feature=shared')

  output = []
  files = youtube.streams

  for file in files:
    if 'webm' not in file.mime_type:
      output.append({
          'type': file.mime_type,
          'quality': file.resolution,
          'size': file.filesize,
          'sizeKB': file.filesize_kb,
          'sizeMB': file.filesize_mb,
          'hasAudio': file.includes_audio_track,
          'hasVideo': file.includes_video_track
      })

  return output


@app.route('/')
def index():

  return f'Video ID : youtube.video_id'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
