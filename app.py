from flask import Flask, redirect, request, jsonify
from flask_cors import CORS
from spotipy import oauth2, client
import os

app = Flask(__name__)
CORS(app)

spotify_auth = oauth2.SpotifyOAuth(
  os.environ.get('SPOTIPY_CLIENT_ID'),
  os.environ.get('SPOTIPY_CLIENT_SECRET'),
  os.environ.get('SPOTIPY_REDIRECT_URI'),
  scope='user-library-read'
)

@app.route('/login')
def login():
  return redirect(spotify_auth.get_authorize_url())

@app.route('/authenticate', methods=["POST"])
def authenticate():
  response = spotify_auth.get_access_token(request.json['code'])
  username = client.Spotify(
    auth=response['access_token']
  ).me()['id']
  response['username'] = username
  return jsonify(response)

if __name__ == '__main__':
  app.run(debug=True)