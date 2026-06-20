class ChatBot:
  def __init__(self, name="ChatBot"):
    self.name = name
  def reply(self, message:str) -> str:
    message = message.lower()
    if "hello" in message or "hi" in message:
      return "Hey there! How can I help you today?"
    if "help" in message:
      return "Sure - tell me what you need help with."
    else:
      return "I'm not sure I understand yet, but I'm learning!"
