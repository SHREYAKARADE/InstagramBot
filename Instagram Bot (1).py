#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install instabot


#                                                         Login

# In[ ]:


# Import instabot library
from instabot import Bot

# Initialize the bot
bot = Bot()

bot.login(username="your_userid", password="your_password")


#                                             1. Post a photo

# In[ ]:


from instabot import Bot
import time
bot = Bot()

bot.login(username="your_userid", password="your_password")
# A photo can be either in .jpg or .jpeg format.
img_path = "photo.jpg"
caption = "Your caption here"

# Upload the photo with the caption
bot.upload_photo(img_path, caption=caption)
time.sleep(30)


#                                         2. Follow one or more users

# In[ ]:


from instabot import Bot

bot = Bot()

bot.login(username="your_userid", password="your_password")

# To follow a single user.
bot.follow("username")


# In[ ]:


# To follow multiple users, use follow_users().
from instabot import Bot

bot = Bot()

bot.login(username="your_userid", password="your_password")

list_of_user = ["userId1", "userId2", "userId3", "...."] 
bot.follow_users(list_of_user)


#                                     3. Unfollow one or a list of users

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# To unfollow a single user.
bot.unfollow("username")


# In[ ]:


# To unfollow multiple users we use unfollow_users().
unfollow_list = ["userId1", "userId2", "userId3", "..."]
bot.unfollow_users(unfollow_list)


#                                             4. Unfollow everyone

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

bot.unfollow_everyone()


#                                     5. Count the number of followers of a user

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

#  Use get_user_followers function to retrieve followers 
followers = bot.get_user_followers("username")
print("Total number of followers:")

## Print the total number of followers
print(len(followers))


#                                     6. Like and comment on a post

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# enter post link
post_link = "https://www.instagram.com/abcdefghi/" 
post = bot.get_media_id_from_link(post_link)

# like
bot.like(post)

# comment
bot.comment(post, "Comments ..")


#                             7. Like post with specific Hashtag

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")



# Like posts with a specific hashtag
hashtag = "pythonprogramming"
bot.like_hashtag(hashtag)


#                             8. Follow users who posted with the hashtag 

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Follow users who posted with the hashtag
bot.follow_followers("username_of_user_with_hashtag")


#                                             9. Send messages to a user 

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# To send messages to a single user.
message = "Hello, How are you??"
bot.send_message(message, "username")


#                                                 10. Logout

# In[ ]:


from instabot import Bot

bot = Bot()
bot.login(username="your_username", password="your_password")

# Logout when you're done.
bot.logout()


# In[ ]:




