import pandas as pd
import numpy as np
import random as random

iterations = int(input("How many times would you like to iterate? (i.e., 8 types of entries x # of iterations = your # of entries"))
max_val = int(input("What would your largest sale look like?")) #example: $500,000
min_val = int(input("What would your smallest sale look like?")) #example: $1,000
step_val = int(input("How much would you like to step up/down randomly by")) #Example: $25,000

i = random.randrange(min_val,max_val,step_val) #this calculated i value will be utilized thorughout loop (considered it the base)

#Original transaction - to create the table that will be appended in loop
journal_all = pd.DataFrame(np.array([['4000','JNO 00',i, 0], ['4000','JNO 00',0, i/2], ['4000','JNO 00',0, i/2]]),
	                columns=['Account','Journal','Debit', 'Credit'])

#Loop for creating journals over # of iterations
for x in range(1, iterations+1):
	i = random.randrange(1000,500000,25000) #recalculate the i value for each loop
	jno = "JNO {}0".format(x) #define the journal # based on 

	#Define variables for Chart of Accounts
	rev_acc = random.randrange(4000,4900,300)
	rev_acc2 = random.randrange(4000,4900,300)
	ref_acc = random.randrange(4910,4990,10)
	cash_acc = random.randrange(1000,1200,200)
	inventory_acc = random.randrange(1600,1900,100)
	tax_acc = random.randrange(2000,2900,100)
	cogs = 5000
	ar_acc = 1500

	#Invoice Transactions
	e1 = pd.DataFrame(np.array([[ar_acc, jno, i, 0], [rev_acc, jno, 0, i/2], [rev_acc2, jno, 0, i/2], [inventory_acc, jno, 0, i*0.45], [cogs, jno, i*0.45, 0] ]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e1,ignore_index=True) 

	jno = "JNO {}1".format(x)
	rev_acc = random.randrange(4000,4900,300)
	rev_acc2 = random.randrange(4000,4900,300)
	inventory_acc = random.randrange(1600,1900,100)

	e2 = pd.DataFrame(np.array([[ar_acc, jno, i, 0], [rev_acc, jno, 0, i/4], [rev_acc2, jno, 0, i*3/4], [inventory_acc, jno, 0, i*0.2], [cogs, jno, i*0.2, 0] ]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e2,ignore_index=True)

	#Invoice Transactions - WITH TAX
	jno = "JNO {}2".format(x)
	rev_acc = random.randrange(4000,4900,300)
	rev_acc2 = random.randrange(4000,4900,300)
	inventory_acc = random.randrange(1600,1900,100)
	tax_acc = random.randrange(2000,2900,100)

	e3 = pd.DataFrame(np.array([[ar_acc, jno, i, 0], [rev_acc, jno, 0, i*1.5/4], [rev_acc2, jno, 0, i*1.5/4], [tax_acc, jno, 0, i/4], [inventory_acc, jno, 0, i*0.12], [cogs, jno, i*0.12, 0] ]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e3,ignore_index=True) 

	jno = "JNO {}3".format(x)
	rev_acc = random.randrange(4000,4900,300)
	rev_acc2 = random.randrange(4000,4900,300)
	inventory_acc = random.randrange(1600,1900,100)
	tax_acc = random.randrange(2000,2900,100)

	e4 = pd.DataFrame(np.array([[ar_acc, jno, i, 0], [rev_acc, jno, 0, i*2/5], [rev_acc2, jno, 0, i*2/5], [tax_acc, jno, 0, i/5], [inventory_acc, jno, 0, i*0.15], [cogs, jno, i*0.15, 0] ]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e4,ignore_index=True) 

	#Payment Received Transaction
	jno = "JNO {}4".format(x)
	cash_acc = random.randrange(1000,1200,200)

	e5 = pd.DataFrame(np.array([[cash_acc, jno, i*0.8, 0], [ar_acc, jno, 0, i*0.8]]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e5,ignore_index=True) 


	jno = "JNO {}5".format(x)
	cash_acc = random.randrange(1000,1200,200)

	e6 = pd.DataFrame(np.array([[cash_acc, jno, i*0.4, 0], [ar_acc, jno, 0, i*0.4]]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e6,ignore_index=True) 

	#Refunds - cash or a/r
	jno = "JNO {}6".format(x)
	ref_acc = random.randrange(4910,4990,10)
	cash_acc = random.randrange(1000,1200,200)
	inventory_acc = random.randrange(1600,1900,100)
	tax_acc = random.randrange(2000,2900,100)
	cogs = 5000

	e7 = pd.DataFrame(np.array([[ar_acc, jno, 0, 0.7*i], [ref_acc, jno, 0.5*i, 0], [tax_acc, jno, i*0.2, 0], [inventory_acc, jno, i*0.2, 0], [cogs, jno, 0, i*0.2] ]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e7,ignore_index=True) 

	jno = "JNO {}7".format(x)
	ref_acc = random.randrange(4910,4990,10)
	cash_acc = random.randrange(1000,1200,200)
	inventory_acc = random.randrange(1600,1900,100)
	tax_acc = random.randrange(2000,2900,100)
	cogs = 5000

	e8 = pd.DataFrame(np.array([[cash_acc, jno, 0, 0.5*i], [ref_acc, jno, 0.4*i, 0], [tax_acc, jno, i*0.1, 0], [inventory_acc, jno, i*0.1, 0], [cogs, jno, 0, i*0.1] ]),
	                   columns=['Account','Journal','Debit', 'Credit'])

	journal_all = journal_all.append(e8,ignore_index=True) 

#Export results to CSV
journal_all.to_csv('GENERATED_GL.csv', index=False)

