from mycroft import MycroftSkill, intent_file_handler


class Japanrecall(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('japanrecall.intent')
    def handle_japanrecall(self, message):
        self.speak_dialog('japanrecall')


def create_skill():
    return Japanrecall()

