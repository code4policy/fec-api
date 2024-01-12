# Sample APIs

## Setup
1. Make sure to install the python `requests` library, by entering `pip3 install requests` into the terminal
2. To make JSON output more readable in Sublime Text, follow the instructions [here](https://blog.adriaan.io/sublime-pretty-json.html)

## FEC API
## Part 1: Set up.
1. Take a look around at the [FEC API documentation](https://api.open.fec.gov/developers/)
2. Before running the FEC API script, you will need your own API key, which you can find [here](https://api.data.gov/signup/)
3. Since you don't want to make your key public, add your key to your environment variables by typing `export FECKEY='<your_key_here>'` into the terminal
4. Run the following command in your terminal to see candidates who ran for office in Massachusetts in 2022:
```
python3 fecAPI.py
```
5. The comments in `fecAPI.py` have been left intentionally blank. Fill them out to explain how the program works. You can get ChatGPT's help, but please write the comments in your own words.

## Part 2: Pagination

You'll notice that the script only returnedd 20 candidates. But there may be a whole lot more. That's becuase the API only returns one page of results at a time. In order to get all of the results, you will need to loop through all the pages of results. Read the documentation and try to see what you'll need to modify in the code to get ALL the pages of results instead of just one. Make that edit and commit the change to GitHub

## Part 3: Other Endpoints

1. Think about a question you'd want to answer with the FEC API (answering a non-trivial question will probably involve hitting multiple endpoints). Create a new file called `question.py` and write the question in the comments of that file.

	```python
	# Question:
	# I'm wondering what senate candidates have fundraised the most so far in 2017.
	```
2. Think about the endpoints you'd need to hit in order to do this.
3. Plan out in the comments each individual step of how you will get the data.  Your finished product will look something like what you see below. Which endpoints would you have to hit? How would you have to combine the data? The more detailed (step-by-step, closer to code, using terms like endpoint and parameter) your answer, the better.
		
	```python
	## NOTE: What you see below isn't functioning code, its psudo-code. A set of notes that are a mix of code and comments. It is an outline.

	# I want to get a list of candidates and how much each spent on 
	import requests
		
	# Get a list of candidates from georgia by hitting the candidates/ endpoint
	candidates = []
		
	# Loop through all the pages to get a list of candidates
	page = 1
	on_last_page = false
	while !on_last_page:
		url = "https://api.open.fec.gov/v1/candidates/?api_key=DEMO_KEY&per_page=20&state=GA&sort=name&candidate_status=C&page=" + page
		response = requests.get(url)
		for candidate in response.json():
			candidates.append(candidate)
		
		page = page+1
	```

	
4. Commit and push this file to github
