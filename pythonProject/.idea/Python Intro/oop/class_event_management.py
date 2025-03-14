class Event:
    # def __init__(self, event_id, event_name, description, date):
    #     self.event_id = event_id
    #     self.event_name = event_name
    #     self.description = description
    #     self.date = date
    #     self.attendees = []
    #
    # def add_attendees(self, attendee):
    #     self.attendees.append(attendee)
    #
    # def listing_attendees(self):
    #     if self.attendees:
    #         print(f"Attendees in {self.event_name}:")
    #         for y in self.attendees:
    #             print(f" - {y.username}")
    def __init__(self, event_id, event_name, description, date):
        self.event_id = event_id
        self.event_name = event_name
        self.description = description
        self.date = date
        self.attendees = []

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def listing_attendees(self):
        if self.attendees:
            print(f"Attendees in {self.event_name}:")
            for y in self.attendees:
                print(f" - {y.username}")


class Attendee:
    # def __init__(self, username, password):
    #     # self.name = name
    #     self.username = username
    #     self.password = password
    #     self.events = []
    #
    # def add_event(self, event):
    #     self.events.append(event)
    #
    # def listing_events(self):
    #     if self.events:
    #         print(f"This event has {self.username}:")
    #         for event in self.events:
    #             print(f"- {event.event_name}")
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def listing_events(self):
        if self.events:
            print(f"This attendee has events:")
            for event in self.events:
                print(f"- {event.event_name}")


class EventManager:
    # def __init__(self):
    #     self.user = {}
    #
    # def registration(self, username, password):
    #     if username in self.user:
    #         print("User already exists")
    #
    #     else:
    #         self.user[username] = Attendee(username, password)
    #
    # def create_event(self, event_id, event_name, description, date):
    #     return Event(event_id, event_name, description, date)
    #
    # def register_attendee(self, username, password):
    #     return Attendee(username, password)
    #
    # # @staticmethod
    # def login(self, username, password):
    #     if username in self.user and self.user[username].password == password:
    #         return self.user[username]
    #     else:
    #         print(f"Invalid username/password")
    #
    # @staticmethod
    # def display_list_of_attendees_for_each_event(events):
    #     if not events:
    #         print("No Events")
    #         return
    #     print("Information:")
    #     print("-" * 30)
    #     print("{:<15} {:<15}".format("Event Name", "Attendees"))
    #     for attendee in events:
    #         name = event.event_name
    #         print([attendee.username for a in attendee.add_event])
    #         add_event = ", ".join([attendee.username for a in attendee.add_event])
    #
    #         print("=" * 40)
    #         print("{:<20} {:<20}".format(name, add_event))
    def __init__(self):
        self.users = {}

    def registration(self, username, password):
        if username in self.users:
            print("User already exists")
        else:
            self.users[username] = Attendee(username, password)

    def create_event(self, event_id, event_name, description, date):
        return Event(event_id, event_name, description, date)

    def register_attendee(self, username, password):
        return Attendee(username, password)

    def login(self, username, password):
        if username in self.users and self.users[username].password == password:
            return self.users[username]
        else:
            print("Invalid username/password")

    @staticmethod
    def display_list_of_attendees_for_each_event(events):
        if not events:
            print("No Events")
            return
        print("Information:")
        print("-" * 30)
        print("{:<15} {:<15}".format("Event Name", "Attendees"))
        for event in events:
            name = event.event_name
            # print([attendee.username for attendee in event.attendees])
            attendees = ", ".join([attendee.username for attendee in event.attendees])
            print("{:<15} {:<15}".format(name, attendees))


# if __name__ == "__main__":
#     event_manager = EventManager()
#     event_manager.create_event("E0001", "Event-1", "Birthday event", "01-01-25")
#     event_manager.create_event("E0002", "Event-2", "Anniversary event", "21-08-24")
#     event_manager.create_event("E0003", "Event-3", "Birthday event", "15-06-24")
#     event_manager.create_event("E0004", "Event-4", "Birthday event", "02-06-24")
#
#     event_manager.register_attendee("attendee1", "password01")
#     event_manager.register_attendee("attendee2", "password02")
#
#     attendee1 = event_manager.login("attendee1", "password01")
#     if attendee1:
#         event_1 = Event("E0001", "Event-1", "Birthday event", "01-01-25")
#         event_3 = Event("E0003", "Event-3", "Birthday event", "15-06-24")
#         event_4 = Event("E0004", "Event-4", "Birthday event", "02-06-24")
#
#         attendee1.add_event(event_1)
#         attendee1.add_event(event_3)
#         attendee1.add_event(event_4)
#
#         print("List of Events:")
#         for event in attendee1.listing_events():
#             print(event)
#
#         events = [event_1, event_3, event_4]
#
#         attendee1.display_list_of_attendees_for_each_event(events)
#
#     else:
#         print("Invalid user")
if __name__ == "__main__":
    event_manager = EventManager()
    event1 = event_manager.create_event("E0001", "Event-1", "Birthday event", "01-01-25")
    event2 = event_manager.create_event("E0002", "Event-2", "Anniversary event", "21-08-24")
    event3 = event_manager.create_event("E0003", "Event-3", "Birthday event", "15-06-24")
    event4 = event_manager.create_event("E0004", "Event-4", "Birthday event", "02-06-24")

    event_manager.registration("attendee1", "password01")
    event_manager.registration("attendee2", "password02")

    attendee1 = event_manager.login("attendee1", "password01")
    if attendee1:
        attendee1.add_event(event1)
        attendee1.add_event(event3)
        attendee1.add_event(event4)

        event1.add_attendee(attendee1)
        event3.add_attendee(attendee1)
        event4.add_attendee(attendee1)

        print("List of Events:")
        attendee1.listing_events()

        events = [event1, event3, event4]

        event_manager.display_list_of_attendees_for_each_event(events)

    else:
        print("Invalid user")

