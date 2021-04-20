# QAInterview

This is the challenge for the Fetch Rewards QA Engineer role.

The challenge is to, in the most efficient manner possible, solve the scales puzzle using selenium.

I chose to use python to solve this challenge. In order to begin you will need to download python onto your machine. For this test I used the python version: 3.9.0. You will also need to download the chrome webdrivers. This is the version used and the version present in this repo: https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/
You will need to download the driver that works with your operating system and have that present in the same directory as the python file that solves this challenge provided in this repo.

The comments in the test file named: scales_selenium_test.py do a good job of explaining each individual step in detail. But here is the overall goal for how I chose to solve this challenge:

Like many programming problems there are many ways to solve this challenge. Given the sudo-code and the in-depth instructions I would like to at least give another means of solving this problem a look-over for the sake of being thorough. A simple means to solve this problem would be to assign an array for each side of the scale. A and B. We will add indexes to each side until we have an uneven scale. Once we have a side greater than the other we know which index is the fake bar.

THIS HOWEVER IS WORK THAT IS NOT NEEDED!

Given selenium we can reverse engineer the React app. If one inspects the HTML source you can see immediately which index and its' button represents the fake bar.

For a more in-depth step by step instructions be sure to look at the comments in the code.
