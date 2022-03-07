Part 1 - Explain how you implemented the random selection

At first I used the choices function from the random module in Python. However after a reading more into it on Python documentation (https://docs.python.org/3/library/random.html#random.choices) and from the examples given here: https://stackoverflow.com/questions/59763933/what-is-the-difference-between-the-random-choices-and-random-sample-function, I changed to the sample functions (random.sample) to avoid repeating elements. Besides that I used it without weights so that it wouldn't be biased. "k" represents the size that is returned and in this case it is 100000 lines.

Part 6 - Comparison of these simple measures on the two models 

For linear model (shown as "SVC(kernel='linear')"):

Precision:  0.14285714285714285 Recall:  0.0024691358024691358 F1:  0.004854368932038835

For RBF model (shown as "SVC()"):

Precision:  0.0 Recall:  0.0 F1:  0.0

Could not be calculated by program since no matter how I did my code in this part I got an "UndefinedMetricWarning" for this model. I tried finding solutions on how to solve it or if there was something wrong somewhere else in my code but I did not manage to find any solution that would avoid this problem. At first I thought it could be because I was testing on such a small sample but even with bigger samples, and the one in the assignment, all scores were set to 0.
The warning says: "UndefinedMetricWarning: Precision is ill-defined and being set to 0.0 due to no predicted samples. Use `zero_division` parameter to control this behavior.", so I tried doing as suggested by setting zero_division to 1 or 0 but that still only generated scores of 0.0. There is probably some problem with what's in my data (y_pred and test_y) that are used to calculate these scores but no matter how I tried solving them or looking it up manually I could not see where the error lies. As suggested by Asad I could calculate this by hand but I'm not really sure of how to do it with this big dataset and to do it so that it would be comparable with the linear model above. 

Nevertheless, looking at the scores from the linear model, it is not so good at predicting the labels.
