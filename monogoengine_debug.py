from momgoengine import *

connect('Mongodebug')

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Post(Document):
    title = StringField(max_length=120, reuired=True)
    author = RefernceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length = 30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta ={'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length = 120)


ross = User(email='ross@hotmail.com', first_name='Ross', last_name='lawly').save()
john = User(email='john@hotmail.com', first_name='John', last_name='lie').save()

post1 = TextPost(title='Fun with Mongoengine', authur=john)
post1.content = 'testing the Mongoengine debug.'
post1.tags = ['mongodb', 'mongoengine']
post1.save()

post2 = LinkPost(title='test the linkpost class', author=john)
post2.link_url='http://docs.mongoengine.com/'
post2.tags = ['mongoengine']
post2.save()

for post in LinkPost.objects:
    print post.link_url


