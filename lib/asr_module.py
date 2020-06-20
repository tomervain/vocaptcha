import io
from google.cloud import speech_v1 as speech
from google.cloud.speech_v1 import enums
from google.cloud.speech_v1 import types
import numpy as np

# Audio recording parameters
RATE = 24000
CHUNK = int(RATE / 10)  # 100ms


def transcribe_streaming(stream_file):
    """Streams transcription of the given audio file."""

    client = speech.SpeechClient()

    with io.open(stream_file, 'rb') as audio_file:
        content = audio_file.read()

    # In practice, stream should be a generator yielding chunks of audio data.
    stream = [content]
    requests = (types.StreamingRecognizeRequest(audio_content=chunk)
                for chunk in stream)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=RATE,
        language_code='en-US',
        model="command_and_search"
    )
    streaming_config = types.StreamingRecognitionConfig(config=config)

    # streaming_recognize returns a generator.
    responses = client.streaming_recognize(streaming_config, requests)

    return_text = []
    confidence = []

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.

        for result in response.results:
            # print('Finished: {}'.format(result.is_final))
            # print('Stability: {}'.format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                # print('Confidence: {}'.format(alternative.confidence))
                # print(u'Transcript: {}'.format(alternative.transcript))
                return_text.append(alternative.transcript)
                confidence.append(alternative.confidence)

        confidence = np.mean(confidence)
        return return_text, confidence
    return return_text, confidence
