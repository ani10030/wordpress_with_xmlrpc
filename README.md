# wordpress_with_xmlrpc
Remotely connect to your Wordpress blog with XML-RPC

<p>
	XML-RPC is one of the good features provided by Wordpress to take control of your blog remotely.Usually, XML-RPC is enabled by default in Wordpress. Wordpress XML-RPC is considered a good option when you need to remotely control your blog, but it has some security concerns.<br>
	For Example, XML-RPC can be used to brute-force login to your Wordpress blog.<br>
	The security concerns can be handled by using <b>Manage XML-RPC</b> Plugin. Check the below link to see how to setup XML-RPC on your Wordpress installation before posting remotely.<br>
	<a href="">Remotely Post to Wordpress with XML-RPC</a>
</p>
<p>
	Once XML-RPC is setup on your Wordpress installation, you can remotely perform the below operations:<br>
	1. Create Posts<br>
	2. Edit Posts<br>
	3. Delete Posts
</p>
<p>
	<b>wordpress_with_xmlrpc.py</b> is built with Python 2.7 and uses Python's <b>xmlrpclib</b> library.<br>
	<em>Note : xmlrpclib library has been renamed to xmlrpc.client in Python 3+</em><br>
	<em>If you are unable to import xmlrpclib, you can download it from below link and import it.</em>
	<a href="https://github.com/python/cpython/blob/2.7/Lib/xmlrpclib.py">Python xmlrpclib</a>
</p>