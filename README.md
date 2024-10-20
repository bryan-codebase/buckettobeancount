# bucket to beancount
Convert a "budget with buckets" file (partly) to a beancount file

This script is meant to help with converting a "budget with buckets" file to a beancount file on an ongoing basis.

First, change the FILE_PATH, OUTPUT_FILEPATH_START, and CURRENCY_SYMBOL constants to match your beancount file, your desired output location, and your currency.

It only converts "half" of each transaction.

So, for example, it will write a transaction like this:
```
2024-10-16 * "Checking-account" "Water supply"
    Assets:Checking-account                -104.20 USD
```
I will then add (using autocomplete from my favorite text editor) a line to complete the transaction:
```
2024-10-16 * "Checking-account" "Water supply"
    Assets:Checking-account                -104.20 USD
    Expenses:Monthly-Bills:Utilities
```
I then copy these over to my main .beancount file.

It would be possible to create code to automatically fill the second line.  
