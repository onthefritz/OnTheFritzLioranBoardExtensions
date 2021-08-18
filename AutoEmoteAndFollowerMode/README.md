# AutoEmoteAndFollowerExt
Extension to auto kick in emote mode and follower only mode using lioran board.

## How to use
1. Download the extension and install it in Lioranboard.
2. Take the SpamProtectionButton.json content and copy it.
3. Right click on an empty slot in Lioranboard.
4. Right Click > Edit Commands
5. Fill in the content that has <> in it.
    - Leave the oauth_token alone.
    - twitch_login = Your twitch login all lowercase. 
    - watch_number = The number of messages to watch. The more messages you watch the more resource it will use. I recommend 1000 but you are welcome to tweek this.
    - trigger_number = The number of similar messages to trigger on. I recommend 500 off the bat. 
    - variance = The difference in messages. For example, 20 would mean there is a 20% difference between two messages. The lower the number the more similar the messages have to be. 
        - As an example. "Hey" and "Hay" have a similarity of 66% so to catch this you would need a variance of at least 35.
6. Restart Lioranboard.

That's it! You're good to go. Now every time you load Lioranboard if spam hits your chat that meets your criteria it will put chat into emote only and 10 minute follower only mode.
