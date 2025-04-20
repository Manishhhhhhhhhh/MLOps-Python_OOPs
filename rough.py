from oops_project import chatBook

user1 = chatBook()
print(user1.id)


## using static method directly from class rather than obj
chatBook.setter_id(10)
user2 = chatBook()
print(user2.id)

# user2 = chatBook()
# print(user2.id)

# user3 = chatBook()
# print(user3.id)


## Getter and Setter
# print(user1.getter_name())
# user1.setter_name("Agent X")
# print(user1.getter_name())