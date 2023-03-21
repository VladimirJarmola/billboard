<h1>Billboard fan server MMORPG </h1>

<h2>About</h2>

<p>

Internet resource for a fan server of a well-known MMORPG - something like a bulletin board</p>
</strong>
<h2>Status</h2>
 <strong>
<p>On development stage.</p>

<h2>Requirements</h2>
 
<p>Please refer to <a href="https://github.com/VladimirJarmola/billboard/blob/master/requirements.txt">requirements.txt</a> for an updated list of required packages.</p>

<h2>Running Locally</h2>

<p>First, clone the repository to your local machine:</p>

<pre><blockquote>git clone https://github.com/VladimirJarmola/billboard.git</blockquote></pre>

<p>Install the requirements:
</p>

<pre><blockquote>pip install -r requirements.txt</blockquote></pre>

<p>Apply the migrations:</p>
 
<pre><blockquote>python manage.py migrate</blockquote></pre>

<p>Finally, run the development server:</p>
 
<pre><blockquote>python manage.py runserver</blockquote></pre>

<p>The site will be available at</p>
 
<pre><blockquote>127.0.0.1:8000</blockquote></pre>
