class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.follow = []

    def following(self, other_user):
        self.follow.append(other_user)


class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.like = 0

    def like_post(self):
        self.like += 1


class SocialMedia:
    def __init__(self):
        self.users = {}
        self.posts = []

    def registration(self, username, password):
        if username in self.users:
            print("User already exists!")
        else:
            self.users[username] = User(username, password)
            print(f"Registration for {username} Successful!")

    def create_post(self, username, content):
        post = Post(username, content)
        self.posts.append(post)
        print(f"{username} posted {content}.")

    def interact_post(self, username, index):
        if index < 0 or index >= len(self.posts):
            print("Invalid")
        post = self.posts[index]
        post.like_post()
        print(f"{username} liked a {post.content}.")

    def follow_user(self, follower_1, follower_2):
        person1 = self.users[follower_1]
        person2 = self.users[follower_2]
        if follower_1 and follower_2 in self.users:
            person1.following(person2)
            print(f"{person1.username} followed {person2.username}")


if __name__ == "__main__":
    social_media = SocialMedia()

    social_media.registration("User1", "password1")
    social_media.registration("User2", "password2")
    social_media.registration("User3", "password3")
    social_media.registration("User1", "password1")

    social_media.create_post("User1", "Good day!")
    social_media.create_post("User2", "unga bunga today")
    social_media.create_post("User2", "No Caption")

    social_media.interact_post("User2", 1)
    social_media.interact_post("User1", 1)
    social_media.interact_post("User3", 1)

    social_media.follow_user("User1", "User2")
    social_media.follow_user("User3", "User2")
