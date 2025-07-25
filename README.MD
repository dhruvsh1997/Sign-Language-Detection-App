\# Sign Language Detection App



A Python-based application that converts audio speech to sign language representations through word recognition and transliteration.



\## 📋 Overview



This application processes audio input (either recorded live or from pre-existing files) to detect spoken words and convert them into sign language visual representations. The system uses audio processing, word recognition, and transliteration to provide both text output and corresponding sign language GIF animations.



\## ✨ Features



\- \*\*Live Audio Recording\*\*: Record audio in real-time for immediate processing

\- \*\*Pre-recorded Audio Support\*\*: Process existing audio files from the samples directory

\- \*\*Word Recognition\*\*: Advanced audio processing to identify spoken words

\- \*\*Multi-language Support\*\*: Includes Hindi transliteration capabilities

\- \*\*Visual Sign Language\*\*: Displays corresponding GIF animations for recognized words

\- \*\*Dictionary Caching\*\*: Serialized dictionary for improved performance

\- \*\*Audio Segmentation\*\*: Automatic word chopping from continuous speech



\## 🛠️ Technical Components



\### Core Modules



1\. \*\*Main Processing (`main.py`)\*\*

&nbsp;  - Dictionary loading and caching

&nbsp;  - Audio file processing coordination

&nbsp;  - Word recognition and transliteration

&nbsp;  - GIF path resolution



2\. \*\*Audio Recording (`record.py`)\*\*

&nbsp;  - Real-time audio capture using PyAudio

&nbsp;  - Configurable recording duration

&nbsp;  - WAV file output generation



3\. \*\*Supporting Modules\*\*

&nbsp;  - `chop\_words.py`: Audio segmentation into individual words

&nbsp;  - `dictionary.py`: Word matching and recognition

&nbsp;  - `transliteration.py`: Multi-language text conversion

&nbsp;  - `AnimatedGif.py`: GIF animation handling



\## 📦 Dependencies



```bash

pip install pyaudio

pip install wave

pip install pickle

```



\*\*System Requirements:\*\*

\- Python 2.7 (Note: Code uses Python 2 syntax)

\- Audio input device (microphone)

\- Required audio codec support



\## 🚀 Installation



1\. Clone the repository:

```bash

git clone https://github.com/yourusername/sign-language-detection-app.git

cd sign-language-detection-app

```



2\. Install required dependencies:

```bash

pip install -r requirements.txt

```



3\. Ensure you have the following directory structure:

```

├── main.py

├── record.py

├── chop\_words.py

├── dictionary.py

├── transliteration.py

├── AnimatedGif.py

├── dictionary1/

│   ├── serialized.txt

│   └── dictionary.pkl

├── samples/

│   └── \[audio files].wav

├── img/

│   └── \[sign language gifs].gif

└── chopped-words/

```



\## 💻 Usage



\### Method 1: Live Audio Recording

```python

from main import callByAudio

result, gif\_path = callByAudio()

print(result)  # Recognized word with transliteration

```



\### Method 2: Process Pre-recorded Audio

```python

from main import callByName

result, gif\_path = callByName("word\_name")

print(result)  # Recognized word with transliteration

```



\### Method 3: Direct Audio File Processing

```python

from main import start

result, gif\_path = start("path/to/audio/file.wav")

```



\### Command Line Recording

```bash

python record.py \[DURATION\_IN\_SECONDS]

```



\## 📁 Project Structure



```

sign-language-detection-app/

├── main.py                 # Main application logic

├── record.py              # Audio recording functionality

├── chop\_words.py          # Audio word segmentation

├── dictionary.py          # Word recognition dictionary

├── transliteration.py     # Language transliteration

├── AnimatedGif.py         # GIF animation handling

├── dictionary1/           # Dictionary data and cache

├── samples/               # Pre-recorded audio samples

├── img/                   # Sign language GIF animations

├── chopped-words/         # Temporary segmented audio files

└── README.md

```



\## ⚙️ Configuration



\### Audio Settings

\- \*\*Sample Rate\*\*: 44,100 Hz

\- \*\*Channels\*\*: Mono (1 channel)

\- \*\*Format\*\*: 16-bit PCM

\- \*\*Default Recording Duration\*\*: 3 seconds



\### Dictionary Settings

\- Supports serialized dictionary caching for performance

\- Located in `dictionary1/` directory

\- Automatic serialization on first run



\## 🎯 How It Works



1\. \*\*Audio Input\*\*: System captures audio either through live recording or file input

2\. \*\*Word Segmentation\*\*: Audio is processed and segmented into individual words

3\. \*\*Recognition\*\*: Each word segment is matched against the trained dictionary

4\. \*\*Transliteration\*\*: Recognized words are transliterated (e.g., Hindi to English)

5\. \*\*Visual Output\*\*: Corresponding sign language GIF is located and returned

6\. \*\*Result\*\*: Both text and visual representation are provided



\## ⚠️ Limitations



\- Currently optimized for single word recognition

\- Requires pre-existing dictionary training data

\- GIF animations must be pre-created and stored

\- Python 2.7 syntax (consider upgrading to Python 3)

\- Audio quality dependent recognition accuracy



\## 🔧 Troubleshooting



\*\*"Problem in Recognition" Error:\*\*

\- Occurs when word count ≠ 1

\- Check audio quality and clarity

\- Ensure single word pronunciation

\- Verify microphone functionality



\*\*"Word Not Found" Error:\*\*

\- Audio file doesn't exist in samples directory

\- Check file naming convention

\- Verify file path and extension



\## 🤝 Contributing



1\. Fork the repository

2\. Create a feature branch (`git checkout -b feature/amazing-feature`)

3\. Commit your changes (`git commit -m 'Add amazing feature'`)

4\. Push to the branch (`git push origin feature/amazing-feature`)

5\. Open a Pull Request



\## 📈 Future Enhancements



\- \[ ] Python 3 compatibility

\- \[ ] Multi-word phrase recognition

\- \[ ] Real-time sign language video generation

\- \[ ] Web interface integration

\- \[ ] Mobile app development

\- \[ ] Extended language support

\- \[ ] Machine learning model integration



\## 📄 License



This project is licensed under the MIT License - see the \[LICENSE](LICENSE) file for details.



\## 👥 Authors



\- Your Name - \*Initial work\* - \[YourGitHub](https://github.com/yourusername)



\## 🙏 Acknowledgments



\- Sign language community for inspiration

\- Contributors to audio processing libraries

\- Open source community for tools and resources



---



\*\*Note\*\*: This application is designed to assist in sign language learning and communication. Please ensure proper testing and validation before production use.

