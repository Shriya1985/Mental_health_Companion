import tkinter as tk
from tkinter import messagebox, scrolledtext
from textblob import TextBlob
import random

# Mood history storage
mood_history = []

# List of motivational quotes
quotes = [
    "🌟 Believe in yourself and all that you are.",
    "💡 Every day is a new beginning. Take a deep breath and start again.",
    "🌈 You are stronger than you think!",
    "🌞 Happiness is not out there, it’s in you.",
    "💙 Be kind to yourself, always."
]

# Function to get a random motivational quote
def get_quote():
    return random.choice(quotes)

# Function to analyze mood
def analyze_mood():
    user_input = text_entry.get("1.0", tk.END).strip()

    if not user_input:
        messagebox.showwarning("⚠️ Warning", "Please enter your thoughts.")
        return

    # Sentiment analysis
    analysis = TextBlob(user_input)
    polarity = analysis.sentiment.polarity

    # Determine mood
    if polarity > 0.2:
        mood = "😊 Happy"
        message = "Keep up the positive vibes! You're doing great!"
        color = "#32CD32"  # Green
    elif polarity < -0.2:
        mood = "😢 Sad"
        message = "It's okay to feel this way. Take a deep breath and be kind to yourself."
        color = "#FF6347"  # Red
    else:
        mood = "😐 Neutral"
        message = "A balanced mood is a good mood. Stay mindful!"
        color = "#FFD700"  # Yellow

    # Save history
    mood_history.append((user_input, mood))

    # Update UI
    result_label.config(text=f"Your Mood: {mood}", fg=color)
    messagebox.showinfo("Mood Analysis", message)

# Function to show mood history
def show_history():
    if not mood_history:
        messagebox.showinfo("📜 Mood History", "No mood entries yet.")
        return

    history_text = "\n".join([f"{text} -> {mood}" for text, mood in mood_history])
    messagebox.showinfo("📜 Mood History", history_text)

# Function to exit the application
def exit_app():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

# GUI setup
root = tk.Tk()
root.title("Mental Health Companion 🌿")
root.geometry("500x550")
root.config(bg="#f0f8ff")  # Light blue background

# Header Label
header_label = tk.Label(root, text="🌈 Mental Health Companion", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#008080")
header_label.pack(pady=10)

# Motivational Quote
quote_text = get_quote()
quote_label = tk.Label(root, text=quote_text, wraplength=450, font=("Arial", 12, "italic"), bg="#f0f8ff", fg="#555")
quote_label.pack(pady=10)

# Instructions
label = tk.Label(root, text="How are you feeling today?", font=("Arial", 14), bg="#f0f8ff", fg="#333")
label.pack(pady=5)

# Text Entry Box
text_entry = scrolledtext.ScrolledText(root, height=5, width=50, font=("Arial", 12))
text_entry.pack(pady=10)

# Analyze Button
analyze_button = tk.Button(root, text="Analyze Mood 🎭", font=("Arial", 12, "bold"), bg="#32CD32", fg="white",
                           padx=10, pady=5, command=analyze_mood)
analyze_button.pack(pady=5)

# View History Button
history_button = tk.Button(root, text="View Mood History 📜", font=("Arial", 12, "bold"), bg="#008B8B", fg="white",
                           padx=10, pady=5, command=show_history)
history_button.pack(pady=5)

# Exit Button
exit_button = tk.Button(root, text="Exit 🚪", font=("Arial", 12, "bold"), bg="#FF4500", fg="white",
                        padx=10, pady=5, command=exit_app)
exit_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="💙 Remember: Your feelings are valid!", font=("Arial", 12, "italic"), bg="#f0f8ff", fg="#555")
footer_label.pack(pady=10)

# Run the app
root.mainloop()
