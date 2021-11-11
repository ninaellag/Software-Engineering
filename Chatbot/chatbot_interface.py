from tkinter import *

# def bot_reply(text): -- Takes as input the message from the user and returns chatbot's reply
#     pass

# bname = "GG" -- Will be showed in front of the chatbot's reply, followed by a colon 


# Defining fonts and the colors used for the application
gray, background, t_color = "#ABB2B9", "#17202A", "#EAECEE"
text_font, b_font = "Arial 11", "Arial 9 bold"



class ChatBot:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
    
    # Function to display everything 
    def run(self):
        self.window.mainloop()
    
    
    def _setup_main_window(self):
        
        # Setting up the main window
        self.window.title("Groupy Grouperson Chatbot")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=410, height=520, bg=background)
        
        # Placing the header 
        header = Label(self.window, bg=background, fg=t_color, text="Welcome to the Chat", font=b_font, pady=9)
        header.place(relwidth=1)
        
        # Adding a divider
        div = Label(self.window, width=300, bg=gray)
        div.place(relwidth=1, rely=0.07, relheight=0.02)
        
        # Adding the chat box
        self.chatbox = Text(self.window, width=15, height=5, bg=background, fg=t_color, font=text_font, padx=4, pady=4)
        self.chatbox.place(relheight=0.75, relwidth=1, rely=0.08)
        self.chatbox.configure(cursor="arrow", state=DISABLED)
        
        # Adding the Scroll Bar
        scroll = Scrollbar(self.chatbox)
        scroll.place(relheight=1, relx=0.972)
        scroll.configure(command=self.chatbox.yview)
        
        # Adding bottom section
        bottom = Label(self.window, bg=gray, height=80)
        bottom.place(relwidth=1, rely=0.825)
        
        # Adding the text box
        self.text_box = Entry(bottom, bg="#2C3E50", fg=t_color, font=text_font)
        self.text_box.place(relwidth=0.75, relheight=0.06, rely=0.008, relx=0.011)
        self.text_box.focus()
        self.text_box.bind("<Return>", self.enter_pressed)
        
        # Adding the 'Send' button
        send_button = Button(bottom, text="Send", font=b_font, width=20, bg=gray, command=lambda: self.enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.22)
     
    # This part allows to send messages by pressing 'Enter', alongside the 'Send' button
    def enter_pressed(self, event):
        message = self.text_box.get()
        self.add_message(message, "Me")
        
    # Outputting messages
    def add_message(self, message, user):
        if not message:
            return

        # Message from user        
        self.text_box.delete(0, END)
        user_message = f"{user}: {message}\n"
        self.chatbox.configure(state=NORMAL)
        self.chatbox.insert(END, user_message)
        self.chatbox.configure(state=DISABLED)
        
        ## Reply from chatbot 
        # chatbot_response = f"\n{bname}: {bot_reply(message)}\n\n"
        # self.chatbox.configure(state=NORMAL)
        # self.chatbox.insert(END, chatbot_response)
        # self.chatbox.configure(state=DISABLED)
        
        # Always looking at the last message
        self.chatbox.see(END)
             
        
if __name__ == "__main__":
    application = ChatBot()
    application.run()