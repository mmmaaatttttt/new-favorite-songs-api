# New Favorite Songs API

A simple Flask API used to authenticate users with Spotify and get data on a user's favorite songs.

### Set up

Assuming you're using `virtualenvwrapper`:

```sh
mikvirtualenv new-favorite-songs
pip install -r requirements.txt
```

### Environment Variables

In order to get the application working locally, you'll need to register it with Spotify. Log in to Spotify and then go [here](https://developer.spotify.com/my-applications/#!/applications) to register your application. Give your app a name and a description. 

Once registered, you will be given a Client ID, and a Client secret. Both will need to be stored in your `postactivate` file. You will also need to set a Redirect URI to `http://localhost:3000/callback`. (If you're curious about what's going on, take a look at Spotify's [authorization guide](https://developer.spotify.com/web-api/authorization-guide/).

Next, from within your virtual environment:

```sh
echo "export SPOTIPY_CLIENT_ID=YOUR_CLIENT_ID_HERE" >> $VIRTUAL_ENV/bin/postactivate
echo "export SPOTIPY_CLIENT_SECRET=YOUR_CLIENT_SECRET_HERE" >> $VIRTUAL_ENV/bin/postactivate
echo "export SPOTIPY_REDIRECT_URI=http://localhost:3000/callback" >> $VIRTUAL_ENV/bin/postactivate
deactivate
workon new-favorite-songs
python app.py
```

You should be good to go!

Note that this configuration assumes the [front-end React app](https://github.com/mmmaaatttttt/new-favorite-songs) is being served from `localhost:3000`. Be sure to change your app's redirect URI and environment variable if you're serving from another port.