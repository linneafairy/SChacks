
friends = 10

print "Welcome. To begin this game, you are a middle school student. You have " + str(friends) + " friends. Try not to lose any as you navigate your life."
print "You will be presented with a series of choices. Answer yes or no to continue."

#start choices- page-flipping animation thing?

print"You are in a fight with one of your friends. You get home and get on your anonymous social media profile."
print"You notice the friend has posted a photo on social media. You type out a mean comment, but hesitate before pressing post."
print"You know it might hurt your friend, but your friend already hurt you today."
first = raw_input("Do you click send? ")

if first == 'yes' or 'Yes':
    print "You hit send."
    friends = friends - 1
    print "Sending that message really hurt your friend. You lose this friend. You now have " + str(friends) + " friends."
elif first == 'no' or 'No':
    print "You realize your message could really hurt your friend, especially because they don't know it's you. You don't hit send."
    secondone = raw_input("You decide to talk to the friend. You notice they are online in chat. Do you chat them?")
    if secondone == 'yes' or 'Yes':
        #insert video of textx
        print "You apologize to your friend but the friend does not accept your apology. They are very upset with you."
        print "You are mad at them for not being accepting. You type out a scathing reply. But, rembering your earlier "
        secondtwo == raw_input("Do you send it?")
    print "Answer yes or no, or the computer will not understand you."



