from firebase_admin import db


class StoreData:

    def __init__(self, text, hashtag, fake, real, token_count):
        self.text = text
        self.hashtag = hashtag
        self.fake = fake
        self.real = real
        self.token_count = token_count
        self.ref = db.reference("Twitter NFN Detector")

    def store(self):
        id_ref = self.ref.push()
        id_ref.set({
                'text': self.text,
                'hashtag': self.hashtag,
                'fake': self.fake,
                'real': self.real,
                'token_count': self.token_count

        })