from coment import comm
from latest_video import get_latest_video_details
import random
import os

# Get the current working directory
current_dir = os.getcwd()
print("Currrent Dir : "+current_dir)
# Combine the current directory with the filename (data.txt)
data = os.path.join(current_dir, "data.txt")
def time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    total_minutes = hours * 60 + minutes
    total_seconds = total_minutes * 60 + seconds
    remaining_seconds = total_seconds % 60
    return total_minutes, remaining_seconds

def generate_comment():
    comments = [
      "That moment when the showdown box betrays you 😂",
      "When you accidentally super into a wall 💀",
      "Trying to juke like a pro, ends up spinning in circles 😂",
      "When the team tries to coordinate but everyone goes in different directions 😂",
      "Getting hit by every single attack in a match 😂",
      "When you accidentally walk into a bush full of enemies 😂",
      "When the lag hits you at the worst moment 💀",
      "Trying to be sneaky but getting caught immediately 😂",
      "When your teammate steals your power cube 👌",
      "That one friend who always rushes into battle without thinking 😂",
      "When you try to dodge but end up walking right into the attack 😂",
      "Trying to hide in a bush but getting found immediately 😂",
      "Accidentally using your super in the wrong direction 😂",
      "When the enemy team wipes you out with a perfect combo 😂",
      "Trying to sneak up on someone but failing miserably 😂",
      "When the randoms on your team have no idea what they're doing 😂",
      "That feeling when you accidentally walk into a minefield 💀",
      "When you forget to check the bush and get ambushed 😂",
      "When your teammate throws the game with a bad move 😂",
      "Trying to predict enemy movements but failing miserably 😂",
      "That moment when you get taken out by a well-placed trap 😂",
      "When you panic and start spamming attacks in all directions 😂",
      "Accidentally activating your super at the wrong time 😂",
      "When your teammates refuse to stick together as a team 😂",
      "That awkward moment when you walk into an enemy's trap 😂",
      "When you accidentally walk into an enemy's line of fire 💀",
      "Trying to aim your shots but failing miserably 😂",
      "When your teammate steals your power-up right in front of you 👌",
      "That feeling when you're the only one left alive on your team 💀",
      "When you're about to win but then get taken out at the last second 😂",
      "When you think you're safe but then get hit by a surprise attack 😂",
      "Trying to run away but getting cornered by the entire enemy team 😂",
      "When you accidentally walk into an enemy's super 💀",
      "That moment when you respawn and immediately get taken out again 😂",
      "Trying to communicate with randoms but no one listens 😂",
      "When your teammate accidentally kills you with their super 😂",
      "That feeling when you're just one hit away from victory 💀",
      "When you accidentally activate your super in the wrong direction 😂",
      "Trying to dodge but failing miserably and getting hit anyway 😂",
      "When you're the last one standing and everyone's counting on you 💀",
      "That moment when you realize you're outnumbered and surrounded 😂",
      "When your team is winning but then throws the game at the last second 😂",
      "Trying to escape but getting chased down by the entire enemy team 😂",
      "That feeling when you respawn and immediately get taken out again 💀",
      "When you accidentally walk into a bush full of enemies 💀",
      "Trying to predict enemy movements but failing miserably 😂",
      "When you're about to win but then get taken out at the last second 💀",
      "When you accidentally walk into an enemy's super 😂",
      "That moment when you respawn and immediately get taken out again 😂",
      "Trying to communicate with randoms but no one listens 😂",
      "When your teammate accidentally kills you with their super 😂"
  ]
    channel_id = "UCfjQOWJqoQ69BUaUZtFtGZg"
    latest_video_details = get_latest_video_details(1, channel_id)
    minu, sec = time(latest_video_details["video_duration"])
    with open(data, "r") as f:
        last_vid = f.readline()

    if last_vid != latest_video_details["video_watch_url"]:
        comments_list = []
        with open(data, "w") as f:
            f.write(latest_video_details["video_watch_url"])
        for i in range(10):
            minute = random.randint(1, minu)
            second = random.randint(1, 59)
            timestamp = str(minute) + ":" + str(second)
            comment = timestamp + " " + random.choice(comments)
            comments_list.append(comment)
            comm(comment, i + 1, latest_video_details["video_id"])

        print({
            "Video ID": latest_video_details["video_id"],
            "Title": latest_video_details["video_title"],
            "Description": latest_video_details["video_description"],
            "Thumbnail URL": latest_video_details["video_thumbnail_url"],
            "Duration": latest_video_details["video_duration"],
            "Watch URL": latest_video_details["video_watch_url"],
            "Comments": comments_list
        })
    else:
        print("No new Video")




if __name__ == '__main__':
    generate_comment()
