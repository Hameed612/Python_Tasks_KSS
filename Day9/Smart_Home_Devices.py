# 12. Smart Home Devices (Multiple Inheritance)
# A smart home device may have both WiFi connectivity and Voice control features.
# Create classes WiFiDevice and VoiceAssistant, and a class SmartSpeaker that
# inherits from both using multiple inheritance.

# Explanation: SmartSpeaker inherits methods from two parent classes. This is multiple inheritance.

# First parent class
class WiFiDevice:

    def wifi(self):
        print("WiFi Connected")


# Second parent class
class VoiceAssistant:

    def voice(self):
        print("Voice Control Activated")


# Child class inheriting from two classes
class SmartSpeaker(WiFiDevice, VoiceAssistant):

    def display(self):
        print("Smart Speaker is Ready")


# Create object
s1 = SmartSpeaker()

# Call methods
s1.display()
s1.wifi()
s1.voice()