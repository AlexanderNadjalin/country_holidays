# country_holidays
## Country holidays per year in a simple format.
This file is intended to be used by anyone who needs to be able to list all holidays with corresponding dates for a specific country. An example could be to see if a future date is a banking day or not.

### Nice-to-knows
Currently, only Sweden (SE) is completely implemented.

country_holidays.py essentially produces a class object 'Calendar' given a few parameters. The holidays are a pandas DataFrame with dates as the index and the English name of the corresponding holiday.

country_holidays.py relies on date_utils.py to work.

### Prerequisites
pandas
datetime
date_utils.py (included in this repo)

### Usage
```python
`import country_holidays as ch`
`import datetime as dti

start_year = dt.datetime(2017, 1, 1)
end_year = dt.datetime(2018, 1, 1)
sweden = ch.Calendar('SE', start_year, end_year)
print(sweden.holidays)`
```

Results in a DataFrame:

*Index* | holiday_name
--- | ---
2017-01-01 | new years day
2017-01-06 | epiphany
2017-04-14 | good friday
2017-04-15 | easter saturday
2017-04-17 | easter monday
2017-05-01 | first may
2017-05-25 | ascension thursday
2017-06-04 | whitsun eve
2017-06-05 | pentecost
2017-06-06 | june six
2017-06-23 | midsummer eve
2017-12-24 | christmas eve
2017-12-25 | christmas day
2017-12-26 | christmas second
2017-12-31 | new years eve
2018-01-01 | new years day
2018-01-06 | epiphany
2018-03-30 | good friday
2018-03-31 | easter saturday
2018-04-02 | easter monday
2018-05-01 | first may
2018-05-10 | ascension thursday
2018-05-20 | whitsun eve
2018-05-21 | pentecost
2018-06-06 | june six
2018-06-22 | midsummer eve
2018-12-24 | christmas eve
2018-12-25 | christmas day
2018-12-26 | christmas second
2018-12-31 | new years eve


### Contributing
Contribution is most welcome and wanted. I want to collaborate and learn to code python properly.

Please contact [Alexander Nadjalin](https://github.com/AlexanderNadjalin) for the process of contributing. This is my first public repository and I'm unfamiliar with how contribution usually works.

### Authors
[Alexander Nadjalin](https://github.com/AlexanderNadjalin) - Initial work.

### License
This project is licensed under the MIT License - see the LICENSE file for details

### Acknowledgments
Hat tip to "http://pydoc.net/FinDates/0.2/findates.dateutils/" for some of the date_utils.py code.
