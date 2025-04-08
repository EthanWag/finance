# finance
This is going to be a finance application I work on for a few years, by the end, I want an full-stack application that can do personal or corperate finances


### Notes as I build this thing ...

- So hands-down the easiest way to work with data inside of python is to use pandas. This library allows you to take json/excel/csv files and allows you put them inside a dataframe. Once inside a dataframe, you can almost tell the dataframe which information you want to keep or throw away, allowing for useful data manipulation. Once your done, you can take that dataframe and transfom that into whatever you want to again, similar to above. So it's super powerful and be sure to use in inside your project. To get it, you can run the command: pip install pandas to get the library
- ok some more important detials, on the first request, we are grabbing the meta data, which is like filing format for any given document. Then from there we can pick and choose which spesific data we want, given the metadata and then send a second request in order to grab the correct information



### Awesome libraries to consider for calculating finances
* pandas + numpy: Basic financial calculations and analysis.
* quantlib: Advanced quantitative finance (pricing models, interest rates).
* fina: Financial ratio calculations, stock performance, and valuation.
* pyfolio: Portfolio performance and risk analysis.
* yfinance: Pulling financial data for stocks (market data, financials, etc.).
* finquant: Portfolio optimization and analysis.
