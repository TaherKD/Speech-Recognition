from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from pydub import AudioSegment

app = Flask(__name__)

with open('<google-cloud-creds-json-path>') as file:
    gcp_creds = file.read()
    
def transcribe(request):
    transcript = ""
    formatError = ""
    dst = 'audio.wav'
    file = None
    if 'audio_data' in request.files:
        f = open('audio.wav', 'wb')
        f.write(request.files["audio_data"].read())
        f.close()
        file = open(dst, 'rb')
    elif "file" in request.files:
        file = request.files["file"]
        
        if file.filename == "":
            return redirect(request.url)    
    
        frmt = file.filename.split('.')[-1].lower()
        if frmt not in ['mp3','wav']:
            formatError = "Unsupported file format. Please provide wav or mp3 file."
            return render_template('index.html', formatError=formatError)
			
        if frmt == "mp3":
            sound = AudioSegment.from_mp3(file)
            sound.export(dst, format="wav")
            file = open(dst, 'rb')
    else:
        return redirect(request.url)

    if file:
        recognizer = sr.Recognizer()
        audioFile = sr.AudioFile(file)
        with audioFile as source:
            data = recognizer.record(source)
        try:
            transcript = recognizer.recognize_google(data, key=None)
            # transcript = recognizer.recognize_google_cloud(data, credentials_json=gcp_creds)
        except:
            formatError = "Sorry could not understand audio. Please try again."
            return render_template('index.html', formatError=formatError, transcript="")
        
    # print("Transcript: "+transcript)
    return render_template('index.html', formatError="", transcript=transcript)

# def record(request):
#     transcript = ""
#     formatError = ""
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening!")
#         recognizer.adjust_for_ambient_noise(source, duration=1)
#         audio = recognizer.listen(source)
#     try:
#         # transcript = recognizer.recognize_google(audio, key=None)
#         transcript = recognizer.recognize_google_cloud(audio, credentials_json=gcp_creds)
#     except:
#         formatError = "Sorry could not understand audio. Please try again."
#         return render_template('index.html', formatError=formatError, transcript="")
    
#     return render_template('index.html', transcript=transcript)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # print("FORM DATA RECEIVED")
        
        # if request.form.get("Transcribe"):
        return transcribe(request)
        
        # if 'audio_data' in request.files:
            # return transcribe(request)
    else:
        return render_template('index.html', formatError="", transcript="")
        


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
