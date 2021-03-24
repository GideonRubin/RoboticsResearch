# Client Server face detection game

Gideon Rubin - 24/03/2021
<br/>
<br/>

Based on the concept of empathetic mimicry explored by Hoffman. This uses a 'master / slave' setup where the robot (slave) waits to listen from the game (master) for emotion recognition results to respond accordingly.

## Overview


1. This application runs a Connect4 game by Keith Galli https://github.com/KeithGalli/Connect4-Python
2. In between turns, it runs an open-cv based emotion-detection algorithm using DeepFace https://github.com/serengil/deepface using the default model.
3. It saves an image and calls the classification algorithm on it.   
4. As part of the main application, a client instance is created and sends the most pronounced facial expression to the server over UDP.
5. The server receives the most significant emotion and sends a relevant response through the robot interface (in this case the NAO API).

## Running the application

Run `` pip install -r dependancies.txt`` to access required libraries.

### Client (game and face detection)
This runs in python 3+
1. cd into 1. FacialEmotionRecogntion/RobotClient directory.
2. run ``python connectFourWithAi.py``

### Server
This runs in Python 2.7 (due to the Nao python API.)
1. cd into 1. FacialEmotionRecogntion/RobotServer directory.
2. run ``python server.py``


## To do:
* Convert to a flask application with big 5 personality test such as https://fetzer.org/sites/default/files/images/stories/pdf/selfmeasures/Personality-BigFiveInventory.pdf
* Incorporate a hybrid approach to empathy based on two different models suggested by Hoffman (2001).  
* Create a memory over time for multiple and more informed interactions.
* Test conversational / static interaction with a robot

## Two models of empathy
<details>
  <summary>Paiva, Ana & Leite (et al.)</summary>
      <p>"The first is to consider the human interaction partner as the observer (empathiser) and the agent as the target that triggers empathy in the human partner. In this case, the agent does not necessarily need to be endowed with empathic behaviour, but is designed to evoke empathy in the human observer. Such agents have been employed, for example, in scenarios where it is important to persuade the human partner to select the “right” action (Paiva et al. 2004).</p>
     <p>...The second way to look at empathy in social agents is to consider agents as observers that empathize with other agents, particularly with human partners as targets of empathy… Accordingly, we follow Paiva’s definition of empathic agents, which encompasses these two perspectives (Paiva 2011): Empathic agents are (1) agents that respond emotionally to situations that are more congruent with the user’s or another agent’s emotional situation or (2) are agents that, by their design and behaviours, lead users to respond in a way that is more congruent with the agent’s emotional situation."</p>
</details>


## References
* Martin L. Hoffman. 2001. Empathy and Moral Development: Implications for Caring and Justice. Cambridge University Press.
* Paiva, Ana & Leite, Iolanda & Boukricha, Hana & Wachsmuth, Ipke. (2017). Empathy in Virtual Agents and Robots: A Survey. ACM Transactions on Interactive Intelligent Systems. 7. 1-40. 10.1145/2912150.
* S. I. Serengil and A. Ozpinar, "LightFace: A Hybrid Deep Face Recognition Framework," 2020 Innovations in Intelligent Systems and Applications Conference (ASYU), Istanbul, Turkey, 2020, pp. 1-5, doi: 10.1109/ASYU50717.2020.9259802.

