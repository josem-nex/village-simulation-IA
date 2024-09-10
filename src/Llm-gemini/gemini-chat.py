import google.generativeai as genai

# Configure API key
genai.configure(api_key='YOUR-API-KEY')

class ChatBot:
    def __init__(self, model_name='gemini-1.5-flash'):
        self.model = genai.GenerativeModel(model_name)
        self.chatSession =  self.model.start_chat(history=[])
        

    def chat(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text

    def handle_user_input(self, prompt=""):
        user_input = input("Tú: ")
        if user_input.lower() in {'salir','adios','bye','exit'} :
            return False
        user_input= prompt + " " + user_input
        return user_input 

    def chat_with_historial(self, input_usr):
        response = self.chatSession.send_message(input_usr)
        return response.text
    
    def run(self):
        while True:
            # user_input = self.handle_user_input(prompt="Hazme una anécdota verdadera sobre:")
            user_input = self.handle_user_input()
            if not user_input:
                break
            response = self.chat_with_historial(user_input)
            print(f"Asistente: {response}")
    
    

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.run()