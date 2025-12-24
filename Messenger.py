class Messenger:
    def send_message(self):
        print("I am sending a message")
    def receive_message(self):
        print("I am receiving a message")
class FacebookMessenger(Messenger):
    def send_message(self):
        print("I am sending message using Facebook")
    def receive_message(self):
        print("I am receiving message using Facebook")
class WhatsAppMessenger(Messenger):
    def send_message(self):
        print("I am sending message using WhatsApp")
    def receive_message(self):
        print("I am receiving message using WhatsApp")
    def live_location(self):
        print("I am sharing live location on WhatsApp")
def display(ref):
    ref.send_message()
    ref.receive_message()
    if isinstance(ref, WhatsAppMessenger):
        ref.live_location()
F = FacebookMessenger()
W = WhatsAppMessenger()
display(F)
display(W)
