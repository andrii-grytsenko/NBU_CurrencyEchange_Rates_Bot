class Actor:
    def __init__(self, message):
        self.__id = message.from_user.id
        self.__locale = "EN"
        self.__state = "START"

    def get_id(self):
        return self.__id

    def set_locale(self, locale):
        self.__locale = locale

    def get_locale(self):
        return self.__locale

    def set_state(self, state):
        self.__state = state

    def get_state(self):
        return self.__state


class ActorList:
    def __init__(self):
        self.__actors = []

    def get_actor(self, message):
        for actor in self.__actors:
            if actor.get_id() == message.from_user.id:
                actor.set_state("IN_PROCESS")
                return actor
        actor = Actor(message)
        self.__actors.append(actor)
        return actor

    def set_actor_state(self, message, state):
        self.get_actor(message).set_state(state)
