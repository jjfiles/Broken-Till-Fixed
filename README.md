# Installation Instrucitons

### Start Your Virtual Environment
```virtualenv venv```

### Install the required packages
```pip install -r requirements.txt```

### Create a .env file
It should have the following variables:
```SECRET = "YOUR_DISCORD_TOKEN"```

# Run the bot
```python ./main.py```

# Git Structure
Currently the main branch is ***master***, when deployed the branch being pulled from will be dev

- If you want to start on a new feature create a new branch with the name being a short camel cased description of the feature and your initials: 
  - ```git branch diceGame-JF```
- Switch to that branch:
  - ```git checkout diceGame-JF```
- Add files you've changed with: 
  - ```git add .```
- Commit changes with a description of what you changed: 
  - ```git commit -m "added a dice game, with options x, y, z. Fixed bug A"```
- Push to your branch:
  - ```git push origin diceGame-JF```
- Make a pull request through the button on github
- How to pull from branch
  - ```git pull<space><tab><space><tab>```