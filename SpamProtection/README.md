# AutoEmoteAndFollowerExt
Extension to auto kick in emote mode and follower only mode using lioran board.

## NOTE
This has the potential to hit legit raids from friends. It just depends on how strict you decide to make the variance and how many messages you watch for.

## How to use
1. Download the extension and install it in Lioranboard.
2. Take the SpamProtectionButton.json content and copy it.
3. Right click on an empty slot in Lioranboard.
4. Right Click > Edit Commands
5. Fill in the content that has <> in it.
    - username = Your twitch login all lowercase. 
    - watch_number = The number of messages to watch. The more messages you watch the more resource it will use. I recommend 20 but you are welcome to tweek this.
    - trigger_number = The number of similar messages to trigger on. I recommend 10 off the bat. 
    - similarity = The percentage match between messages. I recommend 90.
    - count_exact_match = true or false. If you want to count exact matches (100% match) set to true otherwise make it false.
6. Restart Lioranboard.

That's it! You're good to go. Now every time you load Lioranboard if spam hits your chat that meets your criteria it will put chat into emote only and 10 minute follower only mode.
