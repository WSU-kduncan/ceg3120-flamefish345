# Project 2 Documentation

# How to get your API Key

- This is here for those that have been making the error of having their own API key for their bot program get shown on GitHub.

- You might have received a message from Discord which is like this:

- 'Hey User####,

    Safety Jim here! It appears that the token for your bot, MstieQuoteBot has been posted to the internet. Luckily, our token-scanning gremlins noticed, and have reset your bot's token - hopefully before anyone could have maliciously used it!

    Your token was found here: 

    Be more careful in the future, and make sure to not accidentally upload your token publicly!

    Obtain a New Bot Token: '


- First go to the Discord Developer Portal and click on your application.

![Discord Developer Portal Home Screen](discorddevportal#1.PNG)

- This will take you to 'General Information'

![Application General Information](discorddevportal#2.PNG)

- Next click on 'OAuth2', this will take you to your bot's API key page

![OAuth2 page](discorddevportal#3.PNG)

- At this point, Discord should have changed your API key when it became exposed on GitHub but if you need to, click on the 'Regenerate' button to create a new key and then click 'Copy' to copy the key to paste into your .env file in Visual Studio Code or WSL.

![.env file in Visual Studio Code](envfile.PNG)