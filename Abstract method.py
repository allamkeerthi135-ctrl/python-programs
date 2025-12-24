from abc import ABC, abstractmethod
class Messenger(ABC):
    def send_message(self):
        pass
    def receive_message(self):
        pass
class Fmessage(Messenger):
    def send_message(self):
        print("Sending message using Facebook")
    def receive_message(self):
        print("Receiving message using Facebook")
m = Fmessage()
m.send_message()
m.receive_message()

