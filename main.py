
#import the necesary libraries
import praw
import beepy as beep
import time

nagreedacounts = 50 #number of accounts that are desired to check

naccounts = nagreedacounts #variable number of accouts for repeated acconts on the subreddit
fixedaccounts = nagreedacounts #fixed number of accounts


print("\nMain program started...")
subreddit = str(input("Type the subreddit you want to check (without the r/): ")) #input of the desired subreddit

start_time = time.time() #starts the timer that returns the amount of time it takes to run

reddit = praw.Reddit(
    client_id="X", #Client ID of the Reddit bot
    client_secret="X", #Secret Client ID
    user_agent="testscript by u/Raymon22", #brief description
    username = "X", #Username (to avoid some 403 errors)
    password= "X" #password (to avoid some 403 errors)
)

postcounter = 0 #counts the posts that the user has in r/depression
accountschecked = 0 #number of accounts checked
users = [] #list of users checked

file = open(f"{subreddit}log.txt", "w+") #Creates the file with the name of the subreddit that is desired + log.txt
file.write("\nLog: ")
file.write("\n")

#while the users checked is not the same as the fixed number of accounts
while len(users) != fixedaccounts:

    #for every hot submission in the desired subreddit (limited by naccounts)
    for submission in reddit.subreddit(subreddit).hot(limit=naccounts):

        redditorstartime = time.time() #starts timer to check how long does it take per user


        redditor = submission.author #gets the author of the post

        #filters the name of the author
        name = str(redditor)
        name = name.replace("Redditor(name='", "")
        name = name.replace("')", "")

        if name in users:
            naccounts += 1
            pass #if the name is in the list, it ignores the name
        else:
            users.append(name) #adds the new name to the array


            accountschecked += 1 #adds one in the number of checked accounts

            #gets the IDs of the posts of user. Limit is the number of posts. None for all posts
            submisions = list(redditor.submissions.new(limit=None))

            #print(submisions)
            idstring = str(submisions)  # transform to string

            #this fragment of code "cleans" the sting, leaving only the ids
            idstring = idstring.lower()  # lowes all the string
            idstring = idstring.replace("submission", "")
            idstring = idstring.replace("(", "")
            idstring = idstring.replace(")", "")
            idstring = idstring.replace("id=", "")
            idstring = idstring.replace('\'', "")
            idstring = idstring.replace('[', "")
            idstring = idstring.replace(']', "")
            idstring = idstring.replace(" ", "")
            #print(idstring)

            array_id = idstring.split(",")  #splits the string and stores that string into an array/list
            #print(array_id) #shows the array/list


            #if any of the ids are missing, give a specified id (not in r/depression)
            for id in array_id:

                if id == " " or id == "":
                    id = "dy6cvb"

                post = reddit.submission(id=id) #get the post information
                subredditname = post.subreddit_name_prefixed #get the subredditname

                #if the word "depression" is in the subbredit name
                if "depression" in subredditname:

                    postcounter += 1 #add one in the counter
                    #print(str(post.title) + " ---- " + str(subredditname)) #shows the title + the subreddit (always r/depression)
                else:
                    pass #add something here if wanted

            timeaccount = (time.time() - redditorstartime) #stop the user timer

            #this prints some info in the console and txt: number of accounts checked, time it took for every account, and how many posts does the user has
            print(f"Accounts Checked: {accountschecked}" + " in --- %s seconds ---" % timeaccount + f" ({len(array_id)} posts)")
            file.write(f"\n - Accounts Checked: {accountschecked}" + " in --- %s seconds ---" % timeaccount + f" ({len(array_id)} posts)")

            #emergency break
            if accountschecked == nagreedacounts:
                break

timeprogram = (time.time() - start_time) #stop the main timer
print("\n-------------------------------------------------------------------------------")
print(f"\n - Posts in r/depression by the redditors of the {subreddit} subreddit : {postcounter}")
print("\n --- %s seconds to execute the program---" % timeprogram)

#TXT write

file.write(f"\n-------------------------------------------------------------------------------")
file.write(f"\n - Posts in r/depression by the redditors of the {subreddit} subreddit : {postcounter}")
file.write(f"\n --- %s seconds to execute the program---" % timeprogram)
file.write(f"\nCoded by RamonG")
file.close()

beep.beep(4)
print("\nCoded by RaymonDev")
print("\n----DeveloperInfo----")
print("\n -Array users: " + str(users))
print("\n -Array size: " + str(len(users)))
enter = input("\nPress enter to finish...")
