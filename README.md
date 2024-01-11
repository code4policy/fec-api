# Sample APIs

## Setup
1. Make sure to install the python `requests` library, by entering `pip3 install requests` into the terminal
2. To make JSON output more readable in Sublime Text, follow the instructions [here](https://blog.adriaan.io/sublime-pretty-json.html)

## FEC API
## Part 1: Set up.
1. Take a look around at the [FEC API documentation](https://api.open.fec.gov/developers/)
2. Before running the FEC API script, you will need your own API key, which you can find [here](https://api.data.gov/signup/)
3. Since you don't want to make your key public, add your key to your environment variables by typing `export FECKEY='<your_key_here>'` into the terminal

## Part 2: Endpoints
4. Run the following command in your terminal to see candidates who ran for office in Massachusetts in 2022:
```
python3 fecAPI.py
```
5. The script will also save the raw json results in a file called `fec_api_results.json`. To make these results more readable, follow the instructions in the **Setup** section above
6. Create a new `.py` file with the same structure as step 4, but that reaches `receipt` in Massachusetts for 2022 as the endpoint named `fecapi_receipts.py`. Add a `_receipts` to the output `.json` file. 
7. Create a new `.py` file with the same structure as step 4, but that reaches `loans` in Massachusetts for 2022 as the endpoint named `fecapi_loans.py`. Add a `_loans` to the output `.json` file.
