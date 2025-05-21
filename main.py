from word_dictionary import english_words
from word_dictionary import spanish_words
from qwerty_to_braille import braille_codes
from qwerty_to_braille import dot_values
import tkinter as tk
from tkinter import ttk
import time
import pyttsx3 


word_info = {}

#function hold info of the frquency of a word used before and when the word was last used (most frequent and MRU)
def update_word_info(word):
    if word not in word_info:
        word_info[word]={"frequency":1,"last_used":time.time()}
    else:
        word_info[word]["frequency"]+=1
        word_info[word]["last_used"]=time.time()


def dot_distance(char1,char2):
    if char1 not in dot_values or char2 not in dot_values:
        return 1
    else:
        return sum(a!=b for a,b in zip(dot_values[char1],dot_values[char2]))


def weighted_levenshtein(s1,s2,weighted=True):
    dp = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i==0:
                dp[i][j]=j
            elif j==0:
                dp[i][j]=i
            elif s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                if (weighted):
                    weight = dot_distance(s1[i-1], s2[j-1]) 
                else:
                    weight=1
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+weight

    return dp[len(s1)][len(s2)]



def best_match(typed_word, weighted=True, suggestion_num=1,word_dict=english_words):
    word_details=[]
    for word in word_dict:
        if abs(len(word)-len(typed_word)) <=4:
            word_dist=weighted_levenshtein(typed_word,word,weighted)
            if (word in word_info):
                frequency=word_info[word]['frequency']
                last_used=word_info[word]['last_used']
            else:
                frequency=0
                last_used=0
            word_details.append((word_dist, -frequency, last_used, word)) #putting frequency in negative to order in ascending

    word_details.sort()

    return list(word_details[i][3] for i in range (min(len(word_details),suggestion_num)))



def process_input(input_sentence, weighted=True, suggestion_num=1,lang="English"):
    braille_words=[] #words typed in
    suggested_words=[] #possible other word suggestions for each word
    final_words=[] #corrected words

    #finalising dictionary used
    if (lang=="Spanish"):
        word_dict=spanish_words
    elif (lang=="English"):
        word_dict=english_words
    
    for word in input_sentence.strip().lower().split("\\"):
        letters=word.strip().split(" ")
        braille_chars = [] #each converted alphabet
        for char in letters:
                    input_char = frozenset(char)
                    if input_char in braille_codes:
                        braille_chars.append(braille_codes[input_char])
                    else:
                        braille_chars.append('?')  #incase unrecognised texts are used

        braille_word = ''.join(braille_chars).lower()
        braille_words.append(braille_word)

        suggestions = best_match(braille_word,weighted,suggestion_num,word_dict) #all possible suggestions
        suggested_words.append(suggestions)
        final_words.append(suggestions[0]) #final currect = all best suggestions
        update_word_info(suggestions[0])

    return braille_words, final_words, suggested_words






#----------------------------------------- GUI confirguration----------------------------------------

def speak_text(text, rate=150, volume=1.0):
    engine = pyttsx3.init()
    #set speech rate (can categorise into: very slow<=50,slow=100,normal=150,fast=200,very fast>=200)
    engine.setProperty('rate', rate)  
    #set volume level (min 0.0 and max 1.0)
    engine.setProperty('volume', volume)  
    engine.say(text)
    engine.runAndWait()



#main gui function to transfer text on convert button click
def convert_text():

    #initialising all variables from gui form
    text=input_entry.get()
    use_weighted=weighted_var.get()
    suggestion_num=int(suggestion_count.get())
    lang=language_choice.get()

    typed, final_words, suggestions = process_input(text, use_weighted, suggestion_num,lang)

    output_box.config(state="normal")
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, f"You typed: {' '.join(typed)}\n\n\n")
    final_corrected=' '.join(final_words)
    output_box.insert(tk.END, f"Did you mean: {final_corrected} \n\n","highlight_correct")
    for i, suggest in enumerate(suggestions):
        output_box.insert(tk.END, f"Other suggestions for '{typed[i]}' : {', '.join(suggest)}\n","highlight_suggest")
    output_box.config(state="disabled")
    output_box.update_idletasks()

    speak_text(text=("Did you mean: ",final_corrected), rate=150, volume=1.0)




#all initial root config
root = tk.Tk()
root.title("Braille Typing Companion")
root.configure(bg="black")
root.state("zoomed")

intro_text="Welcome to the Braille Autocorrect and Autosuggest System, let me help you type smarter with accurate suggestions!"
root.after(200, lambda: speak_text(text=intro_text))

title_label= tk.Label(root, text="BRAILLE TYPING COMPANION",font=("Times", 60),fg="#D0CECC",bg="black")
title_label.grid(pady=40,padx=50)

main_frame = tk.Frame(root, relief="ridge", borderwidth=5, highlightbackground="gray", highlightthickness=3, bg="black")
main_frame.grid(pady=(20,0), padx=85, sticky="ew")


#qwerty text entry input 
frame1 = tk.Frame(main_frame, bg="black")
frame1.grid(pady=20, padx=0, sticky="ew")
label1 = tk.Label(frame1, text="Enter QWERTY Braille (space for char, \ for word):", font=("Times", 25), fg="#F1E7C1", bg="black")
label1.grid(column=0, row=0, padx=5, pady=5, sticky="w")

input_entry = tk.Entry(frame1, width=50, font=("Verdana", 16),relief="sunken",borderwidth=3,bg="#D0CECC")
#input_entry.insert(0,"eg. for 'ant sad': d dqko wqko/ wqk d dko") #setting a default to show an example
input_entry.grid(column=1, row=0, padx=5, pady=5, sticky="ew")
input_entry.focus_set()

label_eg = tk.Label(frame1, text="eg. 'ant sad': d dqko wqko\ wqk d dko:", font=("Times", 15), fg="#F1E7C1", bg="black")
label_eg.grid(column=1, row=1, padx=5, pady=0, sticky="w")

#possible mode options available like: beginner friendly mode, language and number of suggestions req. 
frame2 = tk.Frame(main_frame, bg="black")
frame2.grid(pady=30, padx=15, sticky="ew")

weighted_var = tk.BooleanVar(value=True)
checkbutton_label = tk.Label(frame2, text="Beginner-friendly mode:",font=("Times", 18),bg="black",fg="#F1E7C1")
checkbutton_label.grid(column=0, row=0, sticky="w",padx=(40, 0))
tk.Checkbutton(frame2, variable=weighted_var, bg="black", fg="#F1E7C1", selectcolor="black",activebackground="black",activeforeground="white").grid(column=1, row=0)

language_label = tk.Label(frame2, text="Language:",font=("Times", 18),bg="black",fg="#F1E7C1")
language_label.grid(column=2, row=0, sticky="w",padx=(250, 0))
language_choice = ttk.Combobox(frame2, values=["English", "Spanish"],background="#F1E7C1",foreground="black", width=8,font=("Verdana",10))
language_choice.current(0)
language_choice.grid(column=3, row=0, sticky="w")

suggestion_label = tk.Label(frame2, text="Suggestions per word:",font=("Times", 18),bg="black",fg="#F1E7C1")
suggestion_label.grid(column=4, row=0, sticky="e",padx=(250, 0))
suggestion_count = ttk.Combobox(frame2, values=["1", "2", "3"],background="#F1E7C1",foreground="black", width=5,font=("Verdana",10))
suggestion_count.current(0)
suggestion_count.grid(column=5, row=0, sticky="e")


#button to convert braille keyboard text to words (can be removed if program is modified to take real-time input)
convert_btn = tk.Button(main_frame, text="Convert", command=convert_text,font=("Verdana", 15),background="#F1E7C1",foreground="black",activebackground="black",activeforeground="#F1E7C1",relief="sunken",borderwidth=3)
convert_btn.grid(column=0, row=6, pady=10)

#(output box can be modified to incorporate real-time input)
output_box = tk.Text(main_frame, height=10, width=60, state="disabled", bg="#D0CECC", fg="#333333",font=("Verdana", 15), wrap="word",relief="sunken",borderwidth=3)

output_box.tag_config("highlight_correct",font=("Verdana", 20, "bold"))
output_box.tag_config("highlight_suggest",font=("Verdana", 15,  "bold"))
output_box.grid(column=0, row=7, pady=10)


root.mainloop()
