{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "20281196",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Speak something...\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 12\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m sr\u001b[38;5;241m.\u001b[39mMicrophone() \u001b[38;5;28;01mas\u001b[39;00m source:\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mSpeak something...\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m---> 12\u001b[0m     audio \u001b[38;5;241m=\u001b[39m recognizer\u001b[38;5;241m.\u001b[39mlisten(source)\n\u001b[0;32m     14\u001b[0m \u001b[38;5;66;03m# Recognize the speech\u001b[39;00m\n\u001b[0;32m     15\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\speech_recognition\\__init__.py:523\u001b[0m, in \u001b[0;36mRecognizer.listen\u001b[1;34m(self, source, timeout, phrase_time_limit, snowboy_configuration)\u001b[0m\n\u001b[0;32m    520\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m phrase_time_limit \u001b[38;5;129;01mand\u001b[39;00m elapsed_time \u001b[38;5;241m-\u001b[39m phrase_start_time \u001b[38;5;241m>\u001b[39m phrase_time_limit:\n\u001b[0;32m    521\u001b[0m     \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[1;32m--> 523\u001b[0m buffer \u001b[38;5;241m=\u001b[39m source\u001b[38;5;241m.\u001b[39mstream\u001b[38;5;241m.\u001b[39mread(source\u001b[38;5;241m.\u001b[39mCHUNK)\n\u001b[0;32m    524\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(buffer) \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m: \u001b[38;5;28;01mbreak\u001b[39;00m  \u001b[38;5;66;03m# reached end of the stream\u001b[39;00m\n\u001b[0;32m    525\u001b[0m frames\u001b[38;5;241m.\u001b[39mappend(buffer)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\speech_recognition\\__init__.py:199\u001b[0m, in \u001b[0;36mMicrophone.MicrophoneStream.read\u001b[1;34m(self, size)\u001b[0m\n\u001b[0;32m    198\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mread\u001b[39m(\u001b[38;5;28mself\u001b[39m, size):\n\u001b[1;32m--> 199\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpyaudio_stream\u001b[38;5;241m.\u001b[39mread(size, exception_on_overflow\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pyaudio\\__init__.py:570\u001b[0m, in \u001b[0;36mPyAudio.Stream.read\u001b[1;34m(self, num_frames, exception_on_overflow)\u001b[0m\n\u001b[0;32m    567\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_is_input:\n\u001b[0;32m    568\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mIOError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNot input stream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    569\u001b[0m                   paCanNotReadFromAnOutputOnlyStream)\n\u001b[1;32m--> 570\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m pa\u001b[38;5;241m.\u001b[39mread_stream(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_stream, num_frames,\n\u001b[0;32m    571\u001b[0m                       exception_on_overflow)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "from googletrans import Translator\n",
    "from gtts import gTTS\n",
    "from IPython.display import Audio\n",
    "\n",
    "# Initialize the recognizer\n",
    "recognizer = sr.Recognizer()\n",
    "\n",
    "# Capture audio from the microphone\n",
    "with sr.Microphone() as source:\n",
    "    print(\"Speak something...\")\n",
    "    audio = recognizer.listen(source)\n",
    "\n",
    "# Recognize the speech\n",
    "try:\n",
    "    recognized_text = recognizer.recognize_google(audio)\n",
    "    print(\"You said:\", recognized_text)\n",
    "\n",
    "    # Translate the recognized text\n",
    "    translator = Translator()\n",
    "    translation = translator.translate(recognized_text, src='auto', dest='fr')  # Translate to French\n",
    "    print(\"Translation:\", translation.text)\n",
    "\n",
    "    # Convert the translated text to speech\n",
    "    tts = gTTS(text=translation.text, lang='fr')\n",
    "    tts.save(\"translated_audio.mp3\")\n",
    "\n",
    "    # Play the translated audio within Jupyter Notebook\n",
    "    audio = Audio(\"translated_audio.mp3\")\n",
    "    display(audio)\n",
    "\n",
    "except sr.UnknownValueError:\n",
    "    print(\"Speech recognition could not understand the audio.\")\n",
    "except sr.RequestError as e:\n",
    "    print(\"Could not request results from Google Speech Recognition service; {0}\".format(e))\n",
    "except Exception as e:\n",
    "    print(\"An error occurred: {0}\".format(e))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f43520a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tkinter as tk\n",
    "from tkinter import ttk\n",
    "from gtts import gTTS\n",
    "from googletrans import Translator\n",
    "from IPython.display import Audio\n",
    "import speech_recognition as sr\n",
    "\n",
    "def translate_and_play():\n",
    "    recognized_text = \"\"\n",
    "\n",
    "    def capture_audio():\n",
    "        nonlocal recognized_text\n",
    "        recognizer = sr.Recognizer()\n",
    "        with sr.Microphone() as source:\n",
    "            recognized_text_label.config(text=\"Listening...\")\n",
    "            audio = recognizer.listen(source)\n",
    "            recognized_text_label.config(text=\"Processing...\")\n",
    "            try:\n",
    "                recognized_text = recognizer.recognize_google(audio)\n",
    "                recognized_text_label.config(text=recognized_text)\n",
    "            except sr.UnknownValueError:\n",
    "                recognized_text_label.config(text=\"Couldn't understand audio.\")\n",
    "            except sr.RequestError as e:\n",
    "                recognized_text_label.config(text=\"Could not request results; {0}\".format(e))\n",
    "\n",
    "        translator = Translator()\n",
    "        translation = translator.translate(recognized_text, src='auto', dest='fr')\n",
    "        translated_text_label.config(text=translation.text)\n",
    "        tts = gTTS(text=translation.text, lang='fr')\n",
    "        tts.save(\"translated_audio.mp3\")\n",
    "        audio = Audio(\"translated_audio.mp3\")\n",
    "        display(audio)\n",
    "\n",
    "    window = tk.Tk()\n",
    "    window.title(\"Voice Translator\")\n",
    "\n",
    "    capture_button = ttk.Button(window, text=\"Capture and Translate\", command=capture_audio)\n",
    "    capture_button.pack(pady=10)\n",
    "\n",
    "    recognized_text_label = ttk.Label(window, text=\"\", wraplength=400)\n",
    "    recognized_text_label.pack(pady=10)\n",
    "\n",
    "    translated_text_label = ttk.Label(window, text=\"\", wraplength=400)\n",
    "    translated_text_label.pack(pady=10)\n",
    "\n",
    "    window.mainloop()\n",
    "\n",
    "# Call the function to create and display the GUI\n",
    "translate_and_play()\n",
    "def capture_audio():\n",
    "    nonlocal recognized_text\n",
    "    recognized_text_label.config(text=\"Listening...\")\n",
    "    print(\"Capture button clicked\")  # Add this line\n",
    "    # ... (rest of the code)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5d11ba80",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Listening...\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 7\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m sr\u001b[38;5;241m.\u001b[39mMicrophone() \u001b[38;5;28;01mas\u001b[39;00m source:\n\u001b[0;32m      6\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mListening...\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 7\u001b[0m     audio \u001b[38;5;241m=\u001b[39m recognizer\u001b[38;5;241m.\u001b[39mlisten(source)\n\u001b[0;32m      9\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m     10\u001b[0m     recognized_text \u001b[38;5;241m=\u001b[39m recognizer\u001b[38;5;241m.\u001b[39mrecognize_google(audio)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\speech_recognition\\__init__.py:523\u001b[0m, in \u001b[0;36mRecognizer.listen\u001b[1;34m(self, source, timeout, phrase_time_limit, snowboy_configuration)\u001b[0m\n\u001b[0;32m    520\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m phrase_time_limit \u001b[38;5;129;01mand\u001b[39;00m elapsed_time \u001b[38;5;241m-\u001b[39m phrase_start_time \u001b[38;5;241m>\u001b[39m phrase_time_limit:\n\u001b[0;32m    521\u001b[0m     \u001b[38;5;28;01mbreak\u001b[39;00m\n\u001b[1;32m--> 523\u001b[0m buffer \u001b[38;5;241m=\u001b[39m source\u001b[38;5;241m.\u001b[39mstream\u001b[38;5;241m.\u001b[39mread(source\u001b[38;5;241m.\u001b[39mCHUNK)\n\u001b[0;32m    524\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(buffer) \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m: \u001b[38;5;28;01mbreak\u001b[39;00m  \u001b[38;5;66;03m# reached end of the stream\u001b[39;00m\n\u001b[0;32m    525\u001b[0m frames\u001b[38;5;241m.\u001b[39mappend(buffer)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\speech_recognition\\__init__.py:199\u001b[0m, in \u001b[0;36mMicrophone.MicrophoneStream.read\u001b[1;34m(self, size)\u001b[0m\n\u001b[0;32m    198\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mread\u001b[39m(\u001b[38;5;28mself\u001b[39m, size):\n\u001b[1;32m--> 199\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mpyaudio_stream\u001b[38;5;241m.\u001b[39mread(size, exception_on_overflow\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\pyaudio\\__init__.py:570\u001b[0m, in \u001b[0;36mPyAudio.Stream.read\u001b[1;34m(self, num_frames, exception_on_overflow)\u001b[0m\n\u001b[0;32m    567\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_is_input:\n\u001b[0;32m    568\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mIOError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mNot input stream\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m    569\u001b[0m                   paCanNotReadFromAnOutputOnlyStream)\n\u001b[1;32m--> 570\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m pa\u001b[38;5;241m.\u001b[39mread_stream(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_stream, num_frames,\n\u001b[0;32m    571\u001b[0m                       exception_on_overflow)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "\n",
    "recognizer = sr.Recognizer()\n",
    "\n",
    "with sr.Microphone() as source:\n",
    "    print(\"Listening...\")\n",
    "    audio = recognizer.listen(source)\n",
    "\n",
    "try:\n",
    "    recognized_text = recognizer.recognize_google(audio)\n",
    "    print(\"Recognized:\", recognized_text)\n",
    "except sr.UnknownValueError:\n",
    "    print(\"Couldn't understand audio.\")\n",
    "except sr.RequestError as e:\n",
    "    print(\"Could not request results; {0}\".format(e))\n",
    "Ch"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5de7c999",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e7e47e8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87af0c2b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
