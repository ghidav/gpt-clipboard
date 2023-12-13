# 🔮 GPT Clipboard
Automate your tasks with GPT Shortcuts, a powerful tool to interact with GPT directly from your clipboard!

**Requirements**
* Python installed on your pc
* An OpenAI API key

## Setup

Clone the repository and install the python requirements.

```
git clone https://github.com/ghidav/gpt-clipboard.git
cd gpt-clipboard
pip install -r requirements.txt
```

You also need to know the path to your pyhton compiler, to find it you can use `which python` or `which python3`.

Open the python script (`coding.py`) and paste your OpenAI API key in `os.environ["OPENAI_API_KEY"] = "..."`. The example contains the prompt for code completion, here's the prompt passed to the model before the selected text: 

```
"You are a coding assistant.
You read code and a comment; you take the comment as an instruction to complete the code.\nYou write only the code completion.
```

⚠️**You can freely customize the prompt to meet your personal needs!**

### Mac

To make GPT Clipboard to work on Mac you have to setup an action in Automator. Here's how to do it:

1) When Automator opens, choose New Document.
2) In the document type selection, choose Quick Action.
3) Configure the Quick Action:
    * In the left panel, search for *Run Bash Script* and double click it.
    * In the right panel, set everything as shown in the following image. 

<img width="577" alt="gpt-clipboard" src="https://github.com/ghidav/gpt-clipboard/assets/131039402/ed8c57fe-2d46-4b65-9ecb-35517ee6b4c3">

4) Save quick action (it will be saved in /Users/name/Library/Services by deafult)
5) Go to settings > keyboard and click on *Keyboard Shortcuts...*
6) Click on Services on the left panel and expand the *Text* section
7) Here you can find the quick action and set a keyboard shortcut for it (e.g. ⌘⇧9)

<img width="647" alt="Screenshot 2023-12-13 at 23 25 24" src="https://github.com/ghidav/gpt-clipboard/assets/131039402/3f6ba498-c7c4-43f8-b9ec-e8a74b079adb">

✅ You're all set! Now select a text and type the shortcut you choose to see the output of GPT magicically appear in your clipboard! 🪄
