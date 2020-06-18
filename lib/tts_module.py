from google.cloud import texttospeech as tts
from playsound import playsound as ps
import os

def text_to_speech(input_text):
    # Instantiates a client
    client = tts.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = tts.SynthesisInput(text=input_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = tts.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=tts.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # The response's audio_content is binary.
    path = input_text.replace('?','') + '.wav'
    with open(path, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file ' + path)

    # play the file
    ps(path)
    os.remove(path)

def text_to_speech(input_text, aw):
    # Instantiates a client
    client = tts.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = tts.SynthesisInput(text=input_text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = tts.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=tts.SsmlVoiceGender.FEMALE)

    # Select the type of audio file you want returned
    audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.LINEAR16)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    # The response's audio_content is binary.
    path = input_text.replace('?','') + '.wav'
    with open(path, 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        print('Audio content written to file ' + path)

    # play the file
    aw.play(path)
    os.remove(path)
