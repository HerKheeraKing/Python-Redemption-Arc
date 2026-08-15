

# HEADER: Learning dictionaries
# when?: storing username/passwords or a user to their list of comments, could be a nested structure.

current_movies = {'The Grinch': '11:00am', 
                  'Rudolph': '1:00pm', 
                  'Frosty the Snowman': '3:00pm', 
                  'Christmas Vacation': '5:00pm'}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime == None: 
    print("Requested movie isn't playing")
else:
    print(movie, "is playing at", showtime)

