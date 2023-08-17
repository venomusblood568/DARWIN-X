import os
import datetime

# Other function definitions and imports here

def sleep():
    ai_response = "Goodbye, sir! Take care."
    print(ai_response)
    return ai_response

def save_conversation_log(conversation_log, file_path):
    with open(file_path, "a") as f:
        for entry in conversation_log:
            f.write(f"Date: {entry['date']}\n")
            f.write(f"Time: {entry['time']}\n")
            f.write(f"You: {entry['user_input']}\n")
            f.write(f"Jarvis: {entry['ai_response']}\n")
            f.write("=" * 40 + "\n")

def main():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    
    conversation_log = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "sleep":
            ai_response = sleep()
        else:
            ai_response = "I'm sorry, I don't understand that."
        
        conversation_log.append({
            "date": current_date,
            "time": current_time,
            "user_input": user_input,
            "ai_response": ai_response
        })
        
    file_name = f"Conversation History/conversation_{current_date}.txt"
    if not os.path.exists("Conversation History"):
        os.mkdir("Conversation History")
    save_conversation_log(conversation_log, file_name)
    print("Conversation saved!")

if __name__ == "__main__":
    main()
