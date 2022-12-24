import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser
import os


def greet():
  # Get the current hour
  now = datetime.datetime.now()
  current_hour = now.hour

  # Use different greetings depending on the time of day
  if current_hour < 12:
    return "Good morning, How may I help you today?"
  elif 12 <= current_hour < 18:
    return "Good afternoon! How may I help you today?"
  else:
    return "Good evening! How may I help you today?"

def handle_command(command):
  # Default response
  response = "I'm sorry, I didn't understand. Could you please rephrase that for me?"

  # Assistant Name Command
  if "what is your name" in command:
    response = "My name is Sirus, I'm an AI Model Prototype classified as CIS-16. I was built by Chenuka Thishen, AKA Artemis ."

  # What is the Time Command
  elif "what time is it" in command:
    # Get the current time and format it
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    response = f"The current time is {current_time}."
  elif "what's the time" in command:
    # Get the current time and format it
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    response = f"The current time is {current_time}."

  # Set a Reminder Command
  elif "set a reminder" in command:
    response = "I'm sorry, I am unable to set reminders at this time."

  # Help Command
  elif "help" in command:
    response = "Here are the Commands that you could ask me to do, Number 1, What's the time, Number 2, Open Gmail, Number 3, What is your name?" \
               "or if not you could say,'Goodbye to me & I'll shutdown'"

  # Discord Command
  elif "open discord" in command:
    os.startfile(r"C:\Users\my\AppData\Local\Discord\app-1.0.9008\Discord.exe")
    response = "Opening Discord..."


  # Open Gmail Command
  elif "open mail" in command:
    webbrowser.open("https://gmail.com")
    response = "Opening Gmail..."

  # Kill Command
  elif "goodbye" in command or "bye" in command:
    response = f"Goodbye! Have a great day."
    exit()

  return response

def listen_for_command():
  # Set up the speech recognition object
  r = sr.Recognizer()

  # Continuously listen for user input
  while True:
    with sr.Microphone() as source:
      # Wait for a short period of silence before starting to listen
      r.pause_threshold = 0.6
      r.adjust_for_ambient_noise(source, duration=0.6)
      print("Listening...")
      audio = r.listen(source)

    # Try to recognize the spoken command
    try:
      command = r.recognize_google(audio).lower()
      print(f"You said: {command}")
      return command
    except sr.UnknownValueError:
      print("I'm sorry, I didn't understand that.")

def speak(text):
  # Set up the text-to-speech engine
  engine = pyttsx3.init()

  voices = engine.getProperty('voices')
  engine.setProperty('voice', voices[1].id)

  # Set the voice and rate
  engine.setProperty('rate', 210)

  # Say the text
  engine.say(text)
  engine.runAndWait()

def main():
  # Introduce the virtual assistant
  greet_text = greet()
  print(greet_text)
  speak(greet_text)


  # Continuously prompt the user for commands
  while True:
    command = listen_for_command()
    response = handle_command(command)
    print(response)
    speak(response)

if __name__ == "__main__":
  main()
