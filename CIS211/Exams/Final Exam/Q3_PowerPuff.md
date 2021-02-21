# Powerpuff Girls Residuals Payments

When a television series is rerun, actors expect
to be paid "residuals".  This goes for cartoon characters too. 

Each character in the cast of the series should be
payed in proportion to the total time they have 
been "on-screen" in the series.   For example, if 
there is $5000.00 to be distributed to the characters,
the total payed out to all characters must be $5000.00
(or very close to it, in case of rounding errors
in floating point math), and a character X who is 
credited with twice as much screen time as character 
Y should get twice as much of the money. 

Your task is to complete the `payout` method of 
class `Cast`.  I suggest a two-pass algorithm: You
will need to determine the total screen time credited
to all characters in the cast first, so that you 
can determine what portion of the payment should 
go to each character. 

Note that many details of the code (e.g., episode titles)
are not really relevant to your task.  A good first step 
would be to determine what is relevant, so you can focus 
your design on that.  I suggest writing pseudocode before 
writing the final code. 
