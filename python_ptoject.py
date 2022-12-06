import random
print("Hello Reader,We are goin to tell a story for you")
name=["Jony","Pavel","SHushan","Reddy","Aswin","Tanvir"]
role=["writer","cricketer","singer","scientist","nobelist"]
organization=["SSC","BSC","GSC","GDS"," S&S"]
date=["2010","2015","2021","2000","2003"]
profession=["doctor","professor","politician","businessman","Artist"]

randoname=random.choice(name)
randorole=random.choice(role)
randoorg=random.choice(organization)
randodate=random.choice(date)
randoprof=random.choice(profession)


story="once there was a boy called "+randoname+" who was a good "+randorole+". He used to donate money to a organization named "+randoorg+". He passed away in "+randodate+".Now his daughter started donate who is a "+randoprof+"."
print(story)