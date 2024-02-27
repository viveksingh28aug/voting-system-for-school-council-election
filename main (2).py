print("This is a voting system for the school council elections : \n")
nominee_1 = input("enter the first nominee name: ")
nominee_2 = input("enter the second nominee name: ")
nominee_3 = input("enter the third nominee name: ")
nominee_4 = input("enter the fourth nominee name: ")
print(f"press 1 vote for {nominee_1}")
print(f"press 2 vote for {nominee_2}")
print(f"press 3 vote for {nominee_3}")
print(f"press 4 vote for {nominee_4}\n")
nom_1_votes = 0
nom_2_votes = 0
nom_3_votes = 0
nom_4_votes = 0
num_of_voter = int(input("enter the number of voter: "))
votes_id = []
for i in range(1, num_of_voter + 1):
  votes_id.append(i)
num_of_voter = len(votes_id)
while True:
  if votes_id == []:
    print("Voting session is over")
    if (nom_1_votes > nom_2_votes and nom_1_votes > nom_3_votes
        and nom_1_votes > nom_4_votes):
      percent = (nom_1_votes / num_of_voter) * 100
      print(nominee_1, "has won the election with", percent, "% votes")
      break
    elif (nom_2_votes > nom_1_votes and nom_2_votes > nom_3_votes
          and nom_2_votes > nom_4_votes):
      percent = (nom_2_votes / num_of_voter) * 100
      print(nominee_2, "has won the election with", percent, "% votes")
      break
    elif (nom_3_votes > nom_1_votes and nom_3_votes > nom_2_votes
          and nom_3_votes > nom_4_votes):
      percent = (nom_3_votes / num_of_voter) * 100
      print(nominee_3, "has won the election with", percent, "% votes")
      break
    elif (nom_4_votes > nom_1_votes and nom_4_votes > nom_4_votes > nom_2_votes
          and nom_4_votes > nom_3_votes):
      percent = (nom_4_votes / num_of_voter) * 100
      print(nominee_4, "has won the election with", percent, "% votes")
      break
    elif (nom_1_votes == nom_2_votes):
      print("there is a tie between", nominee_1, "and", nominee_2,
            "please vote again")
      break
    elif (nom_1_votes == nom_3_votes):
      print(nominee_1, "and", nominee_3,
            "have tied for first place, please vote again")
      break
    elif (nom_1_votes == nom_4_votes):
      print(nominee_1, "and", nominee_4,
            "have tied for first place, please vote again")
      break
    elif (nom_2_votes == nom_3_votes):
      print(nominee_2, "and", nominee_3,
            "have tied for first place, please vote again")
      break
    elif (nom_2_votes == nom_4_votes):
      print(nominee_2, "and ", nominee_4,
            "have tied for first place, please vote again")
      break
    elif (nom_3_votes == nom_4_votes):
      print(nominee_3, "and ", nominee_4,
            "have tied for first place, please vote again")
      break

  else:
    voter = int(input("enter your roll number: "))
    if voter in votes_id:
      print("you are a voter\n")
      vote = int(input("enter your vote: "))
      if vote == 1:
        nom_1_votes += 1
        votes_id.remove(voter)
        print("Thank you for casting your vote\n")
      elif vote == 2:
        nom_2_votes += 1
        votes_id.remove(voter)
        print("Thank you for casting your vote\n")
      elif vote == 3:
        nom_3_votes += 1
        votes_id.remove(voter)
        print("Thank you for casting your vote\n")
      elif vote == 4:
        nom_4_votes += 1
        votes_id.remove(voter)
        print("Thank you for casting your vote\n")
      else:
        print("wrong option\n")
        print(f"press 1 for vote {nominee_1}")
        print(f"press 2 for vote {nominee_2}")
        print(f"press 3 for vote {nominee_3}")
        print(f"press 4 for vote {nominee_4}\n")
    else:
      print("you are not a voter or you have already voted\n")
