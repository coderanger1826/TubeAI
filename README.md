# TubeAI Video Summarizer

This Python application enables users to summarize YouTube video content by utilizing OpenAI's GPT-3.5 language model and Langchain. It retrieves video transcriptions from YouTube, segments them using Langchain, and produces a summary in the video's language.

## Features
- Extracts the transcription from YouTube
- Segments the transcriptions using Langchain
- Generates summaries using OpenAI's GPT-3.5 model
- Developed with Streamlit for a user-friendly web interface

## Prerequisites

Before starting, make sure you have installed the following:

- Python 3.6 or newer
- [Streamlit](https://streamlit.io/)
- [PyTube](https://pytube.io/en/latest/)
- [OpenAI](https://beta.openai.com/docs/developer-quickstart/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [youtube-transcript-api](https://pypi.org/project/youtube-transcript-api/)
- [Langchain](https://pypi.org/project/langchain/)

## Installation 

To get started, follow these steps:

1. Clone this repository:
```bash
git clone https://github.com/coderanger1826/TubeAI.git
```
2. Change into the cloned repository:
```bash
cd TubeAI
```
3. Install all necessary packages:
```bash
pip install -r requirements.txt
```
4. Create a `.env` directory in your home directory (or any directory of your choice), and create in the directory `.env` a file called `openai_api` and add your OpenAI API Key:
```bash
OPENAI_API_KEY=your_openai_api_key
```
5. Change the `env_path` variable in the Python script to match the path of your `.env` file.

## Usage

To run the application and summarize a YouTube video:

1. Run the script:
```bash
streamlit run app.py
```
2. Once the web application starts, open it in your web browser.

3. Provide the link of the YouTube video you wish to summarize in the provided text input.

4. Click the "Start" button to begin the summarization process.

   - The application will extract the transcription from YouTube.
   - It will then use GPT-3.5 and Langchain to generate a summary.
   - The generated summary will be displayed on the web page in the language of the YouTube video.

5. The summary will provide an informative and factual overview of the video's content. It may include bullet points and an introduction and conclusion phrase to enhance clarity and comprehensiveness.