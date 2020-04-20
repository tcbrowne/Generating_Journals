# Generating Journals

Objective: randomly generate a sample of journals for testing of accounting / audit related scripts

The current focus of the script is around four different types of A/R related entries:
- Invoicing
- Invoicing /w Tax
- Payment from customer
- Refunds

For each of these, I have two variants where I hardcode the proportion of "i" which is defined at the beginning as some random value between "x" and "y" (which you can define). The randomness between "x" and "y" will "step" by an amount defined by the user.

Currently there are four fields defined: Account, Journal, Debit and Credit. Planning to implement more as neccesary (i.e., user vields, journal descriptions, etc.) to be more useful for performing other data anlytic tests.

Chart of accounts is defined before each entry type (where relevant) within the loop. These accounts are also randomly generated. For instance, you can have revenue accounts between 4000 and 4900 by iterations of 300. This is realistic as typically there are multiple revenue streams. Same is true for cash, inventory, etc. See below for how chart of accounts is defined:


The script will loop through these 8 entries with a differnet "i" value each time until its completed the amount of iterations defined by the user. At this point it will export the file to CSV format.

# Plans for Future Implementation
- Include a way to choose the frequency of certain transactions / i.e., randomize transaction types rather than always having 8
- Include a random variable within eeach transaction type 0 to 2 to change magnitude, multiply by that amount (have defined distribution)
