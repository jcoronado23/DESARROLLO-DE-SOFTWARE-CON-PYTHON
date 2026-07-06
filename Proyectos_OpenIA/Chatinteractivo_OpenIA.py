from openai import OpenAI
import os

class LLMChat:
    def __init__(self):
        self.client = OpenAI()
        self.history = []
        self.model = os.getenv("OPENAI_MODEL", "gpt-5.5")
        
    def ask_llm(self, user_input):
        self.history.append({"role": "user", "content": user_input})

        response = self.client.responses.create(
            model=self.model,
            input=self.history,
            max_output_tokens=10000
        )

        answer = response.output_text.strip()

        self.history.append({"role": "assistant", "content": answer})
        return answer


def main():

    chat = LLMChat()

    print("Chat iniciado. Escribe 'FINISH' para salir.\n")

    while True:
        user_input = input("Tú: ")

        if user_input.strip().upper() == "FINISH":
            print("Chat terminado.")
            break

        response = chat.ask_llm(user_input)
        print("IA:", response)
        print()


if __name__ == "__main__":
    main()