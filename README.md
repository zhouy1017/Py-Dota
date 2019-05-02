# What is Py-Dota?
This project aims to calculate Fantasy Scores for all completed DPC tournaments (during 2018-19 season) to provide insights for choosing rosters for upcoming matches.  With the help of historical data, we can easily get to know how effeicently a player is earning Fantasy Scores(to solve the problem that many famous competitive players like Miracle or Maybe do not always win a lot of FS due to the method used to calculate FS).

The calculation formula is based on DPC app by Valve.
As shown in the app:
<p align="center">
  <img src="https://github.com/zhouy1017/Py-Dota/blob/master/DPC_Screenshot.png"  width="250" height="550">
</p>

## Notes:
1.Since the term "Teamfight Participation" is not explicitly defined by Valve, the formula I used here is:

Teamfight Participation = (The kills of the player + The assists of the player)/The total kills of the team.

2.Since the roles of a player is not accessible directly from DPC app, the role of players is classified by following rules:
 
 Mid: The player goes to mid lane most during a tournament and gets an average last hit at 10 mins higher than 20.
 
 Core: The player goes to lanes other than mid and gets an average last hit at 10 mins higher than 20.
 
 Support: The player gets an average last hit at 10 mins lower than 20.

#  Reuslts
[Main Evnet Mid](https://github.com/zhouy1017/Py-Dota/blob/master/mid_main.html)

[Main Evnet Sup](https://github.com/zhouy1017/Py-Dota/blob/master/sup_main.html)

[Main Evnet Core](https://github.com/zhouy1017/Py-Dota/blob/master/core_main.html)

[Qualifier Mid](https://github.com/zhouy1017/Py-Dota/blob/master/mid_qu.html)

[Qualifier Sup](https://github.com/zhouy1017/Py-Dota/blob/master/sup_qu.html)

[Qualifier Core](https://github.com/zhouy1017/Py-Dota/blob/master/core_qu.html)


# Sources
This project pulls information from website of DotaBuff(https://www.dotabuff.com/) 
and uses API from OpenDota(https://www.opendota.com/) as source of data.  
And manually take tournaments information from Liquipedia(https://liquipedia.net/dota2/Main_Page).

# TODO
