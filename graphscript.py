import matplotlib.pyplot as plt

#creating the dataset with the needed values
data = {"r/self": 72,"r/introvert": 70,"r/happy": 66,"r/lonely": 65,"r/Anxiety": 14,"r/offmychest": 5, "r/lgbt":4 ,"r/amiugly": 4,"r/memes": 4,"r/Asexual": 3,"r/funny": 2}
time = {"r/self": 137,"r/introvert": 85,"r/happy": 114,"r/lonely": 34,"r/Anxiety": 47,"r/offmychest": 33,"r/lgbt":102 , "r/amiugly":22,"r/memes": 173, "r/Asexual": 50,"r/funny": 167}
subbredits = list(data.keys()) #get the keys of de dictionary
posts = list(data.values()) #get the values of the dictionary
timeprocess = list(time.values()) #get the values of the time dictionary

font = "monospace" #specify font
plt.rcParams["font.size"] = "8"

fig, ax1 = plt.subplots(figsize=(10, 5))

#creating the bar plot
plt.bar(subbredits, posts, color='maroon', width=0.4)

plt.xlabel("Subreddit", fontsize=13, fontfamily = font)
plt.ylabel("Posts", fontsize=13, fontfamily = font)
plt.title("Posts in r/depression by the top 50 redditors of the subreddits",fontdict = {'fontfamily' : font, "fontsize": 15}, loc="left")
plt.suptitle("By: RaymonDev",y=0.91, x=0.92)

#second Y axis

ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Time (minutes)', color=color, fontfamily = font)
ax2.plot(subbredits, timeprocess, marker=".", color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()

#show the numbers in every pont of the second Y axis
for a,b in zip(subbredits, timeprocess):
    ax2.text(a, b, " " + str(b), fontsize=8, fontfamily = font )

#show the graph
plt.show()