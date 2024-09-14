import instaloader
import getpass

def download_collection(username, collection_name):
    # Create an instance of Instaloader
    L = instaloader.Instaloader()

    # Login to Instagram
    password = getpass.getpass("Enter your Instagram password: ")
    L.login(username, password)

    # Get the profile
    profile = instaloader.Profile.from_username(L.context, username)

    # Get all saved posts
    saved_posts = profile.get_saved_posts()

    # Download posts
    for post in saved_posts:
        try:
            # Download the post
            L.download_post(post, target=f"{username}_saved_posts")
            print(f"Downloaded post {post.shortcode}")
        except Exception as e:
            print(f"Error downloading post {post.shortcode}: {str(e)}")

    print("Download complete for saved posts")

if __name__ == "__main__":
    username = input("Enter your Instagram username: ")
    collection_name = input("Enter the name of the collection to download (not used, but kept for compatibility): ")
    download_collection(username, collection_name)
