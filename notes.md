Part 1 - Explain how you implemented the random selection

At first I used the choices function from the random module in Python. However after a reading more into it on Python documentation (https://docs.python.org/3/library/random.html#random.choices) and from the examples given here: https://stackoverflow.com/questions/59763933/what-is-the-difference-between-the-random-choices-and-random-sample-function, I changed to the sample functions (random.sample) to avoid repeating elements. Besides that I used it without weights so that it wouldn't be biased. "k" represents the size that is returned and in this case it is 100000 lines.

Part 6 - Comparison of these simple measures on the two models 
