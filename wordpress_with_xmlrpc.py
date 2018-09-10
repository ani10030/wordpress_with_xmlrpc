#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import xmlrpclib

wp_url = "https://www.exmaple.com/wp/xmlrpc.php" # Location of your xmlrpc.php file
wp_username = "username" # Wordpress Username
wp_password = "password" # Wordpress Password
wp_blogid = ""

def post_to_wordpress(post_title,post_content):
	try:
		print '-- Attempting to post on blog --'

		status_draft = 0
		status_published = 1
		mt_allow_comments = 'open'

		title = post_title
		content = post_content

		server = xmlrpclib.ServerProxy(wp_url)
		data = {'title': title, 'description': content, 'mt_allow_comments': mt_allow_comments}
		try:
			# Post to Wordpress and get Post ID
			post_id = server.metaWeblog.newPost(wp_blogid, wp_username, wp_password, data, status_published)
			print '-- Successfully posted to Wordpress. Post ID : '+str(post_id)+' --'
			return post_id
		except Exception,e:
			print '[X]- Failed to post message to blog -[X]'
			print 'Error : '+str(e)
	except Exception,e:
		print '[X]- Failed to post message to blog -[X]'
		print 'Error : '+str(e)

def get_post(post_id):
	try:
		server = xmlrpclib.ServerProxy(wp_url)
		post_data = server.metaWeblog.getPost(post_id,wp_username,wp_password)
		for key,value in post_data.iteritems():
			print key,' : ',value
	except Exception,e:
		print '[X]- Failed to get Post data from blog -[X]'
		print 'Error : '+str(e)

def edit_post(post_id,title,description):
	status_published = 1

	edited_title = title
	edited_desc = description
	mt_allow_comments = 'open'

	server = xmlrpclib.ServerProxy(wp_url)
	data = {'title': edited_title, 'description': edited_desc, 'mt_allow_comments': mt_allow_comments}

	try:
		# Post to Wordpress and get Post ID
		edit_status = server.metaWeblog.editPost(post_id, wp_username, wp_password, data, status_published)
		if edit_status == True:
			print '-- Edited message successfully posted to Wordpress. Post ID : '+str(post_id)+' --'
		else:
			print '[X]- Failed to post edited message to blog -[X]'
	except Exception,e:
		print '[X]- Failed to post edited message to blog -[X]'
		print 'Error : '+str(e)

def delete_post(post_id):
	try:
		server = xmlrpclib.ServerProxy(wp_url)
		delete_status = server.metaWeblog.deletePost('',post_id,wp_username,wp_password)
		if delete_status == True:
			print '-- Post Successfully deleted --'
		else:
			print '[X]- Failed to delete post -[X]'
	except Exception,e:
		print '[X]- Failed to delete post -[X]'
		print 'Error : '+str(e)

# Create a new Post
post_id = post_to_wordpress("Post Remotely with Python","This is a sample post.")

# Edit the above created Post
edit_post = edit_post(post_id,"This title is edited","This description is edited")

# Get the contents of the above edited post
get_post(post_id)

# Delete the above post
delete_post(post_id)