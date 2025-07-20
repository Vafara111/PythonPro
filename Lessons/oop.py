class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance += amount


account = BankAccount("A", 1000)
print(account.balance)
account.balance = 550
print(account.balance)


class Animal:
    def __init__(self, name, type= "abc"):
        self.name = name

    def make_sount(self):
        return "AAAA"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, type= "nfa")
    def make_sount(self):
        return f"{self.name} A"


dog = Dog("S")
print(dog.make_sount())


from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#
# rect = Rectangle(2,3)
# print(rect.area())


class NotifiUser(ABC):
    @abstractmethod
    def send_notification(self):
        pass


class EmailNotification(NotifiUser):
    def __init__(self, smtp_str=None):
        self.smtp_str = smtp_str

    def smtp_connection(self):
        if self.smtp_str:
            return True
        return False

    def send_notification(self):
        configure_smtp = self.smtp_connection()
        if configure_smtp:
            return True
        return False


class SMSNotification(NotifiUser):
    def send_notification(self):
        return True


class InCallNotification(NotifiUser):
    def send_notification(self):
        return True


class Notification:
    def __init__(self, notif_list):
        self.notif_list = notif_list

    def notify(self):
        for notif in self.notif_list:
            print(notif.send_notification())


notification_clases = (EmailNotification("smtp"), SMSNotification(), InCallNotification())
notifi_handler = Notification(notification_clases)
notifi_handler.notify()

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        print("init")
        self.value = value

obj1 = Singleton(1)
obj2 = Singleton(2)
print(obj1 == obj2)
print(obj1.value)