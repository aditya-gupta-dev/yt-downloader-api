from flask import Flask, Response, request
from pytube import YouTube

app = Flask(__name__)


@app.route('/download')
def download():
  link = request.headers.get('link', default=None)
  if link is None:
    return Response(
        status=401,
        response='{"error": "No link provided"}',
    )

  youtube = YouTube(url=link)

  output = []

  for file in youtube.streams:
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


@app.route('/metadata')
def metadata():
  link = request.headers.get('link', default=None)

  if link is None:
    return Response(
        status=401,
        response='{"error": "No link provided"}',
    )

  youtube = YouTube(url=link)

  output = {
      'title': youtube.title,
      'views': youtube.views,
      'thumbnail': youtube.thumbnail_url
  }

  return output


@app.route('/')
def index():
  return f'Video ID : youtube.video_id'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
