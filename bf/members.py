new_member = input("Enter the name of the new member")

file = open('members.txt', 'r')
members = file.readlines()
file.close()

members.append(new_member)

file = open('members.txt', 'w')
members = file.writelines(members)
file.close()
