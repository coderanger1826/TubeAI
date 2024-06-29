import os
import openai
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.text_splitter import RecursiveCharacterTextSplitter
from dotenv import load_dotenv, find_dotenv

env_path = '/home/USER/.env/openai_api' 
load_dotenv(env_path)
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_transcript(youtube_url):
    video_id = youtube_url.split("v=")[-1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    try:
        transcript = transcript_list.find_manually_created_transcript()
        language_code = transcript.language_code  
    except:
        try:
            generated_transcripts = [trans for trans in transcript_list if trans.is_generated]
            transcript = generated_transcripts[0]
            language_code = transcript.language_code  
        except:
            raise Exception("Unable to locate an appropriate transcript.")

    full_transcript = " ".join([part['text'] for part in transcript.fetch()])
    return full_transcript, language_code 


def summarize_with_langchain_and_openai(transcript, language_code, model_name='gpt-3.5-turbo'):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    texts = text_splitter.split_text(transcript)
    text_to_summarize = " ".join(texts[:4]) 

    system_prompt = 'I want you to act as a Life Coach that can create good summaries!'
    prompt = f'''Summarize the following text in {language_code}.
    Text: {text_to_summarize}

    Add a title to the summary in {language_code}. 
    Include an INTRODUCTION, BULLET POINTS if possible, and a CONCLUSION in {language_code}.'''

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': prompt}
        ],
        temperature=1
    )
    
    return response['choices'][0]['message']['content']

def main():
    st.title('TubeAI video summarizer')
    link = st.text_input('Please input the link to the YouTube video you wish to summarize:')

    if st.button('Start'):
        if link:
            try:
                progress = st.progress(0)
                status_text = st.empty()

                status_text.text('Fetching the transcript...')
                progress.progress(25)

                transcript, language_code = get_transcript(link)

                status_text.text(f'Generating summary...')
                progress.progress(75)

                model_name = 'gpt-3.5-turbo'
                summary = summarize_with_langchain_and_openai(transcript, language_code, model_name)

                status_text.text('Summary:')
                st.markdown(summary)
                progress.progress(100)
            except Exception as e:
                st.write(str(e))
        else:
            st.write('Please provide a valid YouTube link.')

if __name__ == "__main__":
    main()