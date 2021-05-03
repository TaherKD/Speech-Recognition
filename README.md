# Speech-Recognition
Speech recognition using Flask and Google Cloud Speech-to-Text.

## Steps to run the application
1. Clone the Speech-Recognition repo into your local machine.
2. Create and activate a virtual environment (optional but recommended).
3. Change the current working directory to the cloned repo.
4. Install required modules using `pip install -r requirements.txt`.
5. Use command `flask run` to run the application.
6. Application will be running on `http://127.0.0.1:5000/` by default.

## Steps to use the application
1. To transcribe an audio file, upload the file and click `Transcribe` button (only .mp3 and .wav format supported). Wait for the transcription to load up.
2. To transcribe a recorded audio, record an audio using `Record and Stop` buttons. Confirm the recorded audio and click `Upload` next to the confirmed audio. Wait for the transcription to load up.

***Note:*** By default the application uses Google Web API to transcribe audio. To use Google Cloud Speech-to-Text API, add path of Google Cloud service account credential json in line 7 in app.py. Also comment line 44 and uncomment line 45.
