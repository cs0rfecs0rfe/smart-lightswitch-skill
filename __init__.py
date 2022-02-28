from mycroft import MycroftSkill, intent_file_handler


class SmartLightswitch(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('lightswitch.smart.intent')
    def handle_lightswitch_smart(self, message):
        self.speak_dialog('lightswitch.smart')


def create_skill():
    return SmartLightswitch()

