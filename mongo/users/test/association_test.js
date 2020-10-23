const assert = require('assert');
const User = require('../src/models/user.model');
const BlogPost = require('../src/models/blogPost.model');
const Comment = require('../src/models/comment.model');

describe('Associations', () => {
  let joe;
  let blogPost;
  let comment;

  beforeEach((done) => {
    joe = new User({ name: 'Joe' });
    blogPost = new BlogPost({ title: 'JS is Great', content: 'Yep it really is' });
    comment = new Comment({ content: 'Hello world!' });

    joe.blogPosts.push(blogPost);
    blogPost.comments.push(comment);
    comment.user = joe;

    Promise.all([joe, blogPost, comment].map((i) => i.save())).then(() => {
      done();
    });
  });

  it('saves a relation between a user and a blog post', (done) => {
    User.findOne({ name: 'Joe' })
      .populate('blogPosts')
      .then((user) => {
        assert(user.blogPosts[0].title === 'JS is Great');
        done();
      });
  });

  it('saves a full relation graph', (done) => {
    User.findOne({ name: 'Joe' })
      .populate({
        path: 'blogPosts',
        populate: {
          path: 'comments',
          model: 'comment',
          populate: {
            path: 'user',
            model: 'user',
          },
        },
      })
      .then((user) => {
        assert(user.name === 'Joe');
        assert(user.blogPosts[0].title === 'JS is Great');
        assert(user.blogPosts[0].comments[0].content === 'Hello world!');
        assert(user.blogPosts[0].comments[0].user.name === 'Joe');
        done();
      });
  });
});
