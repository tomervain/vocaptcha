from google.cloud import texttospeech as tts
from playsound import playsound as ps
import os

def text_to_speech(input_text):
    # Instantiates a client
    client = tts.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = tts.types.SynthesisInput(text=input_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = tts.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=tts.enums.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = tts.types.AudioConfig(audio_encoding=tts.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)

    # The response's audio_content is binary.
    path = input_text.replace('?','') + '.mp3'
    with open(path, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file ' + path)

    # play the file
    ps(path)
    os.remove(path)
