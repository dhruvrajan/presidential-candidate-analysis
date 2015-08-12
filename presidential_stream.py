__author__ = 'dhruv'

from tweepy.streaming import StreamListener

class PresidentialListener(StreamListener):

    def on_data(self, data):
        try:
            with open("presidents.json", "a") as f:
                f.write(data)
                return True
        except Exception as e:
            print("Error in writing data")
            print(str(e.__traceback__))

    def on_error(self, status_code):
        print(status_code)
        return True