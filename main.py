import  praw
try:
    reddit = praw.Reddit(
        client_id="cC7NFolEl83-VvQkr0Dr9w",
        client_secret="rTFFQwh3K0Iqr9wDUoq88WHktcjpDQ",
        user_agent="Airscholar by /u/mg9729",
        username = "mg9729",
    )

except Exception as e:
    print(e)

subreddit = reddit.subreddit("dataengineering")

top_posts = subreddit.top(limit=10)
new_posts = subreddit.new(limit=10)

for post in top_posts:
    print("Title: " + post.title)
    print("ID - ", post.id)
    print("Author: ", post.author)
    print("URL - ", post.url)
    print("Score: ", post.score)
    print("Comments: ", post.num_comments)
    print("\n")

