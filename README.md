# pycord-roblox-verification-bot
roblox verification bot

**How To Set Up**

  1. Go to replit and create a python repl and add the two python files
  
  2. On replit, click secrets and add the following:
  
      `discordkey` = your discord bot token
      
      `roauth` = make a string of random numbers and letters (can be anything you want)
      
  3. Create a new game on roblox studio
  
  4. Create a new `RemoteEvent` and name it `Verify`

  5. Copy `Script.lua` and add it under `game.ServerScriptService`
  
  6. Copy `Verify.lua` and add it under `game.StarterPlayer.StarterPlayerScripts`
  
  7. Open `Script.lua` and change the following:
  
      
      Set `url` to the url provided after you ran then python script and replit opened webview. it should end in `.repl.co`
      
      Set
