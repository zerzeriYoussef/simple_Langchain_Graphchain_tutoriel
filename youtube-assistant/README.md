# YouTube Assistant

A Streamlit-based application that allows you to ask questions about YouTube videos by analyzing their transcripts using LangChain and Google's Gemini AI.

## Features

- Extract transcripts from YouTube videos
- Ask questions about video content
- Get AI-powered answers based on video transcripts
- Simple and intuitive web interface

## Prerequisites

- Python 3.8 or higher
- Google API Key (for Gemini AI)
- Hugging Face API Token (for embeddings)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd youtube-assistant
```

2. Install the required packages:
```bash
pip install streamlit
pip install langchain-community
pip install langchain-text-splitters
pip install langchain-google-genai
pip install langchain-core
pip install python-dotenv
pip install youtube-transcript-api
pip install faiss-cpu
```

Or create a `requirements.txt` file with:
```
streamlit
langchain-community
langchain-text-splitters
langchain-google-genai
langchain-core
python-dotenv
youtube-transcript-api
faiss-cpu
```

Then install with:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
HUGGINGFACE_API_TOKEN=your_huggingface_token_here
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run main.py
```

2. Open your browser and navigate to the URL shown in the terminal (usually `http://localhost:8501`)

3. In the sidebar:
   - Enter a YouTube video URL
   - Enter your question about the video
   - Click "Submit"

4. The application will:
   - Extract the video transcript
   - Create a vector database from the transcript
   - Search for relevant content
   - Generate an AI-powered answer

## How It Works

1. **Transcript Extraction**: Uses `YoutubeLoader` to fetch the transcript from the YouTube video
2. **Text Splitting**: Splits the transcript into smaller chunks for better processing
3. **Vector Embeddings**: Converts text chunks into embeddings using Hugging Face models
4. **Vector Store**: Stores embeddings in a FAISS vector database for efficient similarity search
5. **Query Processing**: When you ask a question, it searches for relevant transcript chunks
6. **AI Response**: Uses Google's Gemini AI to generate answers based on the relevant transcript content

## Project Structure

```
youtube-assistant/
├── main.py                 # Streamlit application entry point
├── langchain_helper.py     # Helper functions for LangChain operations
├── .env                    # Environment variables (not in git)
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Notes

- Make sure your `.env` file is not committed to version control (it's in `.gitignore`)
- The application requires internet connection to fetch YouTube transcripts
- Some videos may not have transcripts available
- Processing time depends on video length and transcript size

## License

[Add your license here]

