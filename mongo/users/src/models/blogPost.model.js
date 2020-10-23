const mongoose = require('mongoose');
const BlogPostSchema = require('../schemas/blogPost.schema');

const BlogPost = mongoose.model('blogPost', BlogPostSchema);

module.exports = BlogPost;
