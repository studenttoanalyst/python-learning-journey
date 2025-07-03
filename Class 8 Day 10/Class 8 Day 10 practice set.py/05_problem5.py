# write a class train which has methods to book a ticket,get status (no of seats) and get fare informaton
# of train running under indian railways
from random import randint
class train:
    def book(self,trainno,fro,to):
        print(f"ticket fare in train no : {trainno} from {fro} to {to}")
    def getstatus(self,trainno):
        print(f"Train no {trainno} this is running successfully")
    def getfare(self,trainno,fro,to):
        print(f"ticket fare in train no : {trainno} from {fro} to {to} is {randint(333,5555)} ")

t = train()
t.book(1122,"karachi","islamabad")
t.getstatus(1122)
t.getfare(1122,"karachi","islamabd")
