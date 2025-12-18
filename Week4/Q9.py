import json
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self):
        """Abstract method to send notification"""
        pass


class EmailNotification(Notification):
    def send(self):
        return "Sending Email Notification"
    
    def __str__(self):
        return "EmailNotification"


class SMSNotification(Notification):
    def send(self):
        return "Sending SMS Notification"
    
    def __str__(self):
        return "SMSNotification"


def create_notification(notification_data):
    """Creates notification objects based on type from JSON"""
    notification_type = notification_data.get("type", "").lower()
    
    if notification_type == "email":
        return EmailNotification()
    elif notification_type == "sms":
        return SMSNotification()
    else:
        raise ValueError(f"Unknown notification type: {notification_type}")


def main():
   
    json_data = '''
    [
        {"type": "email"},
        {"type": "sms"}
    ]
    '''
    
    
    notifications_data = json.loads(json_data)
    
   
    notifications = [] # Create notification objects
    for data in notifications_data:
        try:
            notification = create_notification(data)
            notifications.append(notification)
            print(f"Created: {notification}")
        except ValueError as e:
            print(f"Error: {e}")
    
    print("\n--- Sending Notifications (Polymorphism) ---")
    for notification in notifications:
        result = notification.send()
        print(f"{notification}: {result}")


if __name__ == "__main__":
    main()