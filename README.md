
# WHAT IS THIS APP?
See running app right here:

This is for anyone wanting to transcribe audio from an .mp3 or .mp4 file no longer than 10mins. 

It is completely free to use thanks to openAPI Whisper model. 

Note: Larger files do take a while to process. So I recommend keeping the file as small as possible, ideally less than 10MB.



# WHAT I LEARNED
- Streamlit
- OpenAI Whisper

# INSTALLATION LOCALLY (MacOS)

Step 1: 
`pip install streamlit`
Step 2:
`pip install git+https://github.com/openai/whisper.git`
Step 3: 
`streamlit run main.py`


## TROUBLE SHOOTING
If you get this error on MacOS:
`ERROR: Could not build wheels for backports.zoneinfo which use PEP 517 and cannot be installed directly`

You must follow these two steps:

1. `export C_INCLUDE_PATH=/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/Headers`
2. `pip install backports.zoneinfo`



