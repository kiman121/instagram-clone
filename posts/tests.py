from django.test import TestCase
from .models import Post, Tag, Comment, Like, Follow
from users.models import Profile
from django.contrib.auth.models import User
# Create your tests here.
class PostTestCase(TestCase):
    '''
    Test class for the Post module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Post class before every test
        '''
        # Save Profile
        self.new_profile = Profile(name='James')
        self.new_profile.save()

        # Save Tag
        self.new_tag = Tag(name="Travel")   
        self.new_tag.save()
        # Save Post
        self.new_post = Post(user=self.new_profile.user,title='Crying stone', description='Tourist attraction for ages!', post_image='posts/crying_stone.jpeg', tag=self.new_tag)

    def tearDown(self):
        Tag.objects.all().delete()
        Post.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_post, Post))

    def test_save_method(self):
        '''
        Test case that confirms that the Post object is being saved
        '''
        self.new_post.save_post()
        my_posts = Post.objects.all()
        self.assertTrue(len(my_posts) > 0)
    
    def test_update_method(self):
        '''
        Test case that confirms if the update_post method updates a post record (title attribute)
        '''
        self.new_post.save_post()
        record_id = Post.objects.last().id
        Post.update_post(record_id, "Kakamega's jewel")
       
        my_post = Post.objects.get(id=record_id)

        self.assertEqual(my_post.title, "Kakamega's jewel")
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_post method deletes a post
        '''
        self.new_post.save_post()
        record_id = Post.objects.last().id
        Post.delete_post(record_id)

        my_posts = Post.objects.all()
        self.assertTrue(len(my_posts) == 0)

class TagTestCase(TestCase):
    '''
    Test class for the Tag module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Tag class before every test
        '''
        # Save Tag
        self.new_tag = Tag(name="Travel")   
        self.new_tag.save()

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_tag, Tag))

    def test_save_method(self):
        '''
        Test case that confirms that the Tag object is being saved
        '''
        self.new_tag.save_tag()
        my_tags = Tag.objects.all()
        self.assertTrue(len(my_tags) > 0)
    
    def test_update_method(self):
        '''
        Test case that confirms if the update_image method updates a tag record (title attribute)
        '''
        self.new_tag.save_tag()
        record_id = Tag.objects.last().id
        Tag.update_tag(record_id, "Entertainment")
       
        my_tags = Tag.objects.get(id=record_id)

        self.assertEqual(my_tags.name, "Entertainment")
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_tag method deletes a tag
        '''
        self.new_tag.save_tag()
        record_id = Tag.objects.last().id
        Tag.delete_tag(record_id)

        my_tags = Tag.objects.all()
        self.assertTrue(len(my_tags) == 0)

class CommentTestCase(TestCase):
    '''
    Test class for the Comment module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Comment class before every test
        '''
        # Save Tag
        self.new_comment = Comment(comment="What a lovely place!")   
        self.new_comment.save()

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_save_method(self):
        '''
        Test case that confirms that the Comment object is being saved
        '''
        self.new_comment.save_comment()
        my_comments = Comment.objects.all()
        self.assertTrue(len(my_comments) > 0)
    
    def test_update_method(self):
        '''
        Test case that confirms if the update_comment method updates an comment record (comment attribute)
        '''
        self.new_comment.save_comment()
        record_id = Comment.objects.last().id
        Comment.update_comment(record_id, "Plan for take 2")
       
        my_comments = Comment.objects.get(id=record_id)

        self.assertEqual(my_comments.comment, "Plan for take 2")
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_comment method deletes a comment
        '''
        self.new_comment.save_comment()
        record_id = Comment.objects.last().id
        Comment.delete_comment(record_id)

        my_comments = Comment.objects.all()
        self.assertTrue(len(my_comments) == 0)

class LikeTestCase(TestCase):
    '''
    Test class for the Like module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Like class before every test
        '''
       # Save Profile
        self.new_profile = Profile(name='James')
        self.new_profile.save()

        # Save Tag
        self.new_tag = Tag(name="Travel")   
        self.new_tag.save()

        # Save Post
        self.new_post = Post(user=self.new_profile.user,title='Crying stone', description='Tourist attraction for ages!', post_image='posts/crying_stone.jpeg', tag=self.new_tag)
        self.new_post.save()

        # new like
        self.new_like = Like(user=self.new_profile.user, post=self.new_post)

    def tearDown(self):
        Tag.objects.all().delete()
        Post.objects.all().delete()
        Like.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_like, Like))

    def test_save_method(self):
        '''
        Test case that confirms that the Like object is being saved
        '''
        self.new_like.save_like()
        my_likes = Like.objects.all()
        self.assertTrue(len(my_likes) > 0)
    
    def test_update_method(self):
        '''
        Test case that confirms if the update_like method updates a like record (post attribute)
        '''
        self.new_like.save_like()
        record_id = Like.objects.last().id
        another_post = Post(user=self.new_profile.user,title='Lamu', description='A hotspot for tourist', post_image='posts/vascodagama.jpeg', tag=self.new_tag)
        another_post.save(self)

        Like.update_like(record_id, another_post)
       
        my_likes = Like.objects.get(id=record_id)

        self.assertEqual(my_likes.post, another_post)
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_like method deletes a like
        '''
        self.new_like.save_like()
        record_id = Like.objects.last().id
        Like.delete_like(record_id)

        my_likes = Like.objects.all()
        self.assertTrue(len(my_likes) == 0)


class FollowTestCase(TestCase):
    '''
    Test class for the Follow module
    '''
    def setUp(self):
        '''
        Method that creates the instance of the Follow class before every test
        '''
        # Save follower profile
        self.follower_profile = Profile(name='James')
        self.follower_profile.save()

        # Save followee profile
        self.followee_profile = Profile(name='Hellen')
        self.followee_profile.save()

        # save another followee profile
        self.another_followee = Profile(name='Enock')
        self.another_followee.save(self)

        # new like
        self.new_follow = Follow(follower=self.follower_profile.user, followee=self.followee_profile.user,)

    def tearDown(self):
        Follow.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        '''
        Test case that checks if the object is being instanciated correctly
        '''
        self.assertTrue(isinstance(self.new_follow, Follow))

    def test_save_method(self):
        '''
        Test case that confirms that the Follow object is being saved
        '''
        self.new_follow.save_follow()
        my_follows = Follow.objects.all()
        self.assertTrue(len(my_follows) > 0)
    
    def test_delete_method(self):
        '''
        Test case that confirms if the delete_follow method deletes a follow
        '''
        self.new_follow.save_follow()
        record_id = Follow.objects.last().id
        Follow.delete_follow(record_id)

        my_follows = Follow.objects.all()
        self.assertTrue(len(my_follows) == 0)