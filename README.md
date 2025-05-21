<h1>Braille Typing Companion</h1>

This project implements a beginner-friendly autocorrect and autosuggest tool for QWERTY-to-Braille typists in Python. It features:

<ul>
  <li>Autocorrect and suggestion system for Braille input</li>
  <li>Weighted Levenshtein algorithm tailored for Braille keystrokes</li>
  <li>Graphical interface using Tkinter</li>
</ul>

<h2>Features</h2>
<ul>
  <li>Core autocorrect using weighted Levenshtein algorithm</li>
  <li>Dot distance module for Braille-specific error weighting</li>
  <li>Beginner-friendly mode for common typing errors</li>
  <li>Multilingual support (English/Spanish dictionaries)</li>
  <li>Audio narration for corrected sentences</li>
  <li>Learning-based suggestions based on frequency and recency</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>Tkinter</li>
  <li>pyttsx3 (for offline text-to-speech)</li>
</ul>

<h2>How to Run</h2>
<ol>
  <li>Install Python 3.x and required libraries (<code>tkinter</code>, <code>pyttsx3</code>).</li>
  <li>Clone or download the project files.</li>
  <li>Run <code>python main.py</code> to launch the GUI.</li>
  <li>Select language (English/Spanish), beginner mode, and number of suggestions.</li>
  <li>Input Braille text (e.g., <code>d dqko wqko\ wqk d dko</code>) and submit for correction.</li>
</ol>

<h2>Files</h2>
<ul>
  <li><b>main.py</b>: Main GUI and processing logic</li>
  <li><b>qwerty_to_braille.py</b>: Braille key mappings and dot value encodings</li>
  <li><b>word_dictionary.py</b>: English and Spanish word dictionaries</li>
  <li><b>Braille_Typing_Companion_Writeup.pdf</b>: Project write-up and version history</li>
</ul>

<h2>Notes</h2>
<ul>
  <li>This project is a prototype for educational/demo purposes only.</li>
  <li>Future improvements include BK tree implementation for optimisation, adjacent key error detection, Grade 2 Braille support, and real-time input handling.</li>
</ul>

<h2>License</h2>
This project is a prototype and free to use for educational purposes.
