class SocialNetwork:
    __instance = None
    # Users = None

    def __init__(self, name):
        if SocialNetwork.__instance != None:
            raise Exception("SocialNetwork is already instantiated")
        else:
            self.Name = name
            self.Users = []
            SocialNetwork.instance = self

    @staticmethod
    def get_instance():
        if not SocialNetwork.instance:
            SocialNetwork.instance = SocialNetwork("SocialNetwork")
        return SocialNetwork.instance

    def sign_up(self, username, password):
        user = User(username, password)
        self.Users.append(user)

    def log_in(self, username, password):
        for user in self.Users:
            if user.username == username and user.password == password:
                user.online = True
                return
        print("wrong username or password")

    def log_out(self, username):
        for user in self.Users:
            if user.username == username:
                user.online = False
                return
        print("user not found")


class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.following = []
        self.followers = []
        self.online = False


    def follow(self, user):
        self.following.append(user)
        user.followers.append(self)

    def unfollow(self, user):
        user.followers.remove(self)
        self.following.remove(user)

