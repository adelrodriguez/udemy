const mongoose = require('mongoose');
const assert = require('assert');
const User = require('../src/models/user.model');
const BlogPost = require('../src/models/blogPost.model');

describe('Associations', () => {
  let joe;
  let blogPost;

  beforeEach((done) => {
    joe = new User({ name: 'Joe' });
    blogPost = new BlogPost({ title: 'JS is Great', content: 'Yep it really is' });

    joe.blogPosts.push(blogPost);

    Promise.all([joe, blogPost].map((i) => i.save())).then(() => {
      done();
    });
  });

  it('remove blog posts when removing user', (done) => {
    joe
      .remove()
      .then(() => BlogPost.count())
      .then((count) => {
        assert(count === 0);
        done();
      });
  });
});
