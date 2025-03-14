# mlb-spring-training

# Instructions

The easiest way to run this app is to use the docker compose file, and the easiest way to use the docker compose file is to use Docker Desktop. If you're using Docker for personal use, you can download Docker Desktop and use it for free. Take a look at these instructions to download Docker Desktop: https://docs.docker.com/compose/install/#scenario-one-install-docker-desktop. 

Once you have Docker Desktop, make sure that it is running. Then, open a terminal, change directory into the root repository for this GitHub Repo and run the following commands.

1. Open the `docker-compose.yml` file and replace `~/Documents/GitHub/mlb-spring-training` with the path to this Github repository on your own computer or VM. Make sure to save the `docker-compose.yml`. 
2. Run `docker compose up`. This runs the Dockerfile and mounts your virtual `app` folder to the directory path you set in step 1. Verify that there are no issues in the build. 
3. The server will start and generate a link to your local host (127.0.0.1:8888) AND a token for your jupyter lab instance. You'll want to copy and paste this link in your favorite browser - if you just go to 127.0.0.1:8888, you'll be prompted for a password or token. All development that you do here will be preserved since you've mounted your repository and the `app` folder. 
4. Once you're finished, shut down your kernel or close the terminal window. The container should stop automatically, but if something goes wrong, you can always run a `docker ps` to check for running containers and then run `docker stop mlb` to shut down this container. 


# 2/28 Meeting TODOs
Figure out a way to grab challenged pitches 

We can ID pitches that end at-bats

For pitches that don't end at-bats: 
1. Scraping box scores

Sub-optimal methods
1. Crowd sourcing from reporter tweets, journalism?

To start: 
- Grab challenged pitches that end at-bats
- Qualifications: Ball to strike challenge that results in a strikeout, strike to ball challenge that results in a walk.

TODOs
- Creating graphics on challenged pitches
- Analyzing batters vs. (catchers/pitchers), challenged pitchers and universe of challenge-able pitchers
- Analyzing umpires

# 3/14 Meeting 
Daniel put together some analysis in minor-league-analysis.ipynb.

Seth has been doing some manual things. 

Data TODOs 
- [Blocker] Figure out a method to capture all ABS pitches
- Write code that identifies pitches that should have been challenged (Seth)
  - Called Strikes/balls that are:
    - In the zone but were called a ball
    - Out of the zone but were called a strike
- Strike zone information
  - Minor league data. 

Analysis TODOs
- Umpire Analysis 
  - Questions
    - What does ABS mean for umpires?
- Team Strategic (Daniel)
  - Develop Recommendations for batters and defense
  - Questions
    - Are some teams better or worse at challenging?
    - What are the best pitches to challenge?
    - When is the best time to challenge? 

