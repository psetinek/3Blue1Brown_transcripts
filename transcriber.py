import whisper
import pandas as pd
import os
from tqdm import tqdm

whisper_model = whisper.load_model("base")
audio_dir = 'data_audio'

files = os.listdir(audio_dir)
files.remove('.DS_Store')
files.remove('.gitignore')

df = pd.DataFrame(columns=['video_title', 'transcription'])

for file in tqdm(files):
    path = os.path.join(audio_dir, file)
    result = whisper_model.transcribe(path)
    df_temp = pd.DataFrame({'video_title': file.strip('.mp3'),
                            'transcription': result['text']}, index=[0])
    df = pd.concat([df, df_temp]).reset_index(drop=True)

df.to_parquet('3Blue1Brown_transcriptions.parquet', engine='pyarrow')
