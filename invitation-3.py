people_invited = ['Jesus', 'Mom', 'Tito']

# first invitation

messageA = f"Hey {people_invited[0].title()}, you are invited to my dinner!"
print(messageA)

# second invitation
messageB = f"Hey {people_invited[1].title()}, you are invited to my dinner!"
print(messageB)
# third message
messageC = f"Hey {people_invited[2].title()}, you are invited to my dinner!"
print(messageC)

cant_come = people_invited.pop(0)
print(cant_come)

people_invited.append('Kijohn')

print(people_invited)

message_A = f"Hey {people_invited[0].title()}!, you are still invited to my dinner, I had made small changes"
print(message_A)

message_B = f"Hey {people_invited[1].title()}!, you are still invited to my dinner, I had made small changes"
print(message_B)

message_C = f"Hey {people_invited[2].title()}!, you are invited to my dinner"
print(message_C)

people_invited.insert(0, 'Adryan')
people_invited.insert(3, 'Malakiyah')
people_invited.append('Ayden')

message_AA = f"Hey {people_invited[0].title()}!, you are invited to my dinner"
print(message_AA)

message_MM = f"Hey {people_invited[1].title()}!, you are still invited to my dinner"
print(message_MM)

message_TT =  f"Hey {people_invited[2].title()}!, you are still invited to my dinner"
print(message_TT)

message_M =  f"Hey {people_invited[3].title()}!, you are invited to my dinner"
print(message_M)

message_KK =  f"Hey {people_invited[4].title()}!, you are still invited to my dinner"
print(message_KK)

message_AY =  f"Hey {people_invited[5].title()}!, you are invited to my dinner"
