# hotdog cookout lab
def getTotalHotDogs():
  attendees = int(input("Enter the maximum number of attendees: "))
  hotDogs = int(input("Enter the number of hot dogs per attendee: "))
  total = attendees * hotDogs
  return total

def showResults(total):
  DOGS = 10
  BUNS = 8
  dogsLeft = (DOGS - total % DOGS) % DOGS
  minDogs = (total // DOGS) + (0 ** (0 ** dogsLeft))
  bunsLeft = (BUNS - total % BUNS) % BUNS
  minBuns = (total // BUNS) + (0 ** (0 ** bunsLeft))
  print(f"Minimum packages of hot dogs needed: {minDogs}")
  print(f"Minimum packages of hot dog buns needed: {minBuns}")
  print(f"Hot dogs remaining: {dogsLeft}")
  print(f"Hot dog buns remaining: {bunsLeft}")

totalHotDogs = getTotalHotDogs()
showResults(totalHotDogs)
