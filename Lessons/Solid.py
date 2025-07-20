# Single Responsibility Principle   (SRP)

# wrong
class Report:
    def generate(self):
        print("Generating...")

    def save(self, filename):
        print(filename)

    def send_mail(self, email):
        print("sending email...")


# correct
class ReportGenerator:
    def generatereport(self):
        print("Generating...")


class FileSaver:
    def save(self, filename):
        print(filename)


class EmailSender:
    def send_mail(self, email):
        print("sending email...")


# Open/Closed Principle (OCP)

#wrong
class PaymentProcessor:
    def process_payment(self, payment_type, amout):
        if payment_type == "credit_card":
            pass
        elif payment_type == "paypal"
            pass


#correct
from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amout):
        pass


class CreditPayment(PaymentProcessor):
    def process_payment(self, amout):
        pass


class PaypalPayment(PaymentProcessor):
    def process_payment(self, amout):
        pass


def process_user_payment(processor: PaymentProcessor, amount):
    processor.process_payment(amount)


# Liskov Substitution Principle (LSP)

#wrong
class Bird:
    def fly(self):
        pass


class Sparrow(Bird):
    def fly(self):
        pass


class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError


def make_bird_fly(bird : Bird):
    bird.fly()

#correct
class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    def move(self):
        pass


class RunningBird(Bird):
    def move(self):
        pass


class Sparrow(FlyingBird):
    def fly(self):
        pass


class Ostrich(RunningBird):
    def fly(self):
        pass


# Interface Segregation Principle (ISP)

#wrong
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Worker):
    def work(self):
        pass

    def eat(self):
        pass


class RobotWorker(Worker):
    def work(self):
        pass

    def eat(self):
        raise NotImplementedError


#correct
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class HumanWorker(Workable, Eatable):
    def work(self):
        pass

    def eat(self):
        pass


class RobotWorker(Workable):
    def work(self):
        pass


# Depency Inversion Principle (DIP)

#wrong
class SQLDatabase:
    def save(self, data):
        pass


class UserService:
    def __init__(self):
        self.database = SQLDatabase()

    def save_user(self, user):
        self.database.save(user)


#correct
class Database(ABC):
    def save(self, data):
        pass


class SQLDatabase(Database):
    def save(self, data):
        pass


class NoSQLDatabase(Database):
    def save(self, data):
        pass


class UserService:
    def __init__(self, database: Database):
        self.database = database

    def save_user(self, user):
        self.database.save(user)