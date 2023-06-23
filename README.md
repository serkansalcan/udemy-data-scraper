<h1>Udemy Data Scraper</h1>
<p>This Python script fetches Udemy courses data using a hidden Udemy API and saves it in a CSV file. It retrieves course information such as title, rating, number of reviews, number of subscribers, course length, instructor, and more.</p>

<h2>Prerequisites</h2>
<p>Before running the script, make sure you have the following:</p>
<ul>
<li>Python 3.x installed on your machine.</li>
<li>Required libraries: <code>requests</code>, <code>csv</code>. You can install them using <code>pip</code>:</li>
</ul>
<pre><code>pip install requests csv</code></pre>

<h2>CSV File Structure</h2>
<p>The CSV file will contain the following columns:</p>
<ul>
<li>title: The title of the course.</li>
<li>id: The unique identifier of the course.</li>
<li>avg_rating: The average rating of the course.</li>
<li>num_reviews: The number of reviews for the course.</li>
<li>num_subscribers: The number of subscribers enrolled in the course.</li>
<li>is_paid: Indicates whether the course is paid or free.</li>
<li>course_length: The duration or length of the course.</li>
<li>num_published_lectures: The number of lectures published in the course.</li>
<li>created: The date the course was created.</li>
<li>published_time: The published time of the course.</li>
<li>last_update: The date of the last update to the course.</li>
</ul>
