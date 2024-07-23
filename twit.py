import asyncio
from colorama import init, Fore
from twikit import Client

###########################################
init(autoreset=True)

# Enter your account information
USERNAME = "yourusername"
EMAIL = "youremail"
PASSWORD = "yourpassword!"
HASHTAG = "#Hashtag"  # Replace with the hashtag you want to search for

client = Client('en-US')

async def main():
    # Login to the client
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

    ###########################################

    while True:
        print(Fore.CYAN + "Searching for tweets...")
        try:
            # Search for tweets with the specified hashtag
            tweets = await client.search_tweet(HASHTAG, 'Latest')
            
            if tweets:
                for tweet in tweets:
                    try:
                        # Retweet the tweet
                        print(Fore.GREEN + f"Retweeting: {tweet.text}")
                        await tweet.retweet()
                    except Exception as e:
                        print(Fore.RED + f"Error retweeting: {e}")
            else:
                print(Fore.YELLOW + "No new tweets found. Waiting for 60 seconds...")

        except Exception as e:
            print(Fore.RED + f"Error fetching tweets: {e}")
        
        # Wait for 300 seconds before checking again
        await asyncio.sleep(60)

# Run the bot
asyncio.run(main())
