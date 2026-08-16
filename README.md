# FastAPI Text Analysis API

A FastAPI-based REST API for text tokenization, word-frequency analysis, reading-time estimation, and case-insensitive word searching across multiple text records.

## Features

- Tokenize text into individual words
- Convert words to lowercase
- Remove common stop words
- Count total words
- Calculate word frequencies
- Estimate reading time
- Search for exact word matches across multiple records
- Sort search results by number of matches
- Interactive API documentation with Swagger UI

## Installation & Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set up a virtual environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API server

```bash
uvicorn app.main:app --reload
```

The application will be available at:

```text
http://127.0.0.1:8000
```

## API Endpoints

### 1. Root / Info

**Method:** `GET`

**Path:** `/`

Returns basic information about the API.

#### Example Response

```json
{
  "message": "Welcome",
  "for documentation": "go to /docs"
}
```

---

### 2. Tokenize Text

**Method:** `POST`

**Path:**

```text
/tokenize?text=<your_text>
```

The `/tokenize` endpoint extracts words from the provided text, converts them to lowercase, and removes predefined stop words.

The current stop-word list is:

```text
the
is
and
or
a
an
in
on
to
for
with
of
it
this
that
```

#### Example Input

```text
FastAPI is fast and clean
```

#### Example Response

```json
[
  "fastapi",
  "fast",
  "clean"
]
```

Notice that:

- `FastAPI` becomes `fastapi`
- `is` is removed
- `and` is removed
- `fast` remains
- `clean` remains

---

### 3. Analyze Text

**Method:** `POST`

**Path:**

```text
/analyze?text=<your_text>
```

The `/analyze` endpoint analyzes the provided text and returns:

- Total number of words
- Estimated reading time in seconds
- Frequency of every word

Words are converted to lowercase before being counted.

The reading time is calculated using a rate of **200 words per minute**:

```text
reading_time_seconds = (total_words × 60) / 200
```

#### Example Input

```text
FastAPI is fast. Really fast.
```

#### Example Response

```json
{
  "total_words": 5,
  "estimated_reading_time_seconds": 1.5,
  "words": {
    "fastapi": 1,
    "is": 1,
    "fast": 2,
    "really": 1
  }
}
```

> Note: `is` is included in the `/analyze` result because the analyzer does **not** remove stop words. Stop-word filtering is performed only by the tokenizer.

---

### 4. Relevance Search

**Method:** `POST`

**Path:**

```text
/search
```

The `/search` endpoint searches for an exact word across a list of text records.

Searches are **case-insensitive**.

For example:

```text
fast
Fast
FAST
```

are treated as the same search word.

The search matches complete words rather than partial words.

For example, searching for:

```text
fast
```

does **not** match:

```text
FastAPI
```

because `fastapi` is a different complete word.

#### Request Body

```json
{
  "word": "fast",
  "records": [
    "FastAPI is fast. Really fast.",
    "Python is a great programming language.",
    "Fast servers process data quickly."
  ]
}
```

#### Response

```json
[
  {
    "record": "FastAPI is fast. Really fast.",
    "matches": 2
  },
  {
    "record": "Fast servers process data quickly.",
    "matches": 1
  }
]
```

### How the Search Works

For the request above:

#### Record 1

```text
FastAPI is fast. Really fast.
```

The word `fast` appears twice as a complete word:

```text
FastAPI is [fast]. Really [fast].
```

Therefore:

```json
{
  "record": "FastAPI is fast. Really fast.",
  "matches": 2
}
```

#### Record 2

```text
Python is a great programming language.
```

The word `fast` does not appear.

Therefore, this record is not included in the response.

#### Record 3

```text
Fast servers process data quickly.
```

`Fast` is a complete word and is treated as `fast` because the search is case-insensitive.

Therefore:

```json
{
  "record": "Fast servers process data quickly.",
  "matches": 1
}
```

### Search Result Ordering

Search results are sorted by the number of matches in **descending order**.

For example:

```text
matches: 5
matches: 3
matches: 1
```

will be returned in that order.

Records with zero matches are excluded from the response.

## Word Processing Rules

The analyzer, tokenizer, and search functionality use the same basic character-processing approach.

### Letters

Uppercase letters are converted to lowercase.

For example:

```text
FastAPI
```

becomes:

```text
fastapi
```

### Apostrophes, Hyphens, and Underscores

The following characters are preserved inside words:

```text
'
-
_
```

For example:

```text
don't
well-known
user_name
```

are treated as individual words containing those characters.

### Other Characters

Characters such as spaces and punctuation terminate the current word.

For example:

```text
Hello, world!
```

is processed as:

```text
hello
world
```

## Tokenizer vs. Analyzer

The tokenizer and analyzer have different purposes.

### `tokenizer()`

The tokenizer:

1. Extracts words
2. Converts words to lowercase
3. Removes predefined stop words
4. Returns a list of words

Example:

```text
FastAPI is fast and clean
```

becomes:

```json
[
  "fastapi",
  "fast",
  "clean"
]
```

### `analyzer()`

The analyzer:

1. Extracts words
2. Converts words to lowercase
3. Counts the total number of words
4. Calculates word frequencies
5. Estimates reading time

It does **not** remove stop words.

Example:

```text
FastAPI is fast. Really fast.
```

produces:

```json
{
  "total_words": 5,
  "estimated_reading_time_seconds": 1.5,
  "words": {
    "fastapi": 1,
    "is": 1,
    "fast": 2,
    "really": 1
  }
}
```

## Interactive API Documentation

Once the server is running, FastAPI provides interactive API documentation through Swagger UI.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

You can use Swagger UI to:

- View all available endpoints
- Inspect request parameters
- Send test requests
- View API responses
- Experiment with the API without using an external API client

### OpenAPI Specification

The generated OpenAPI specification is available at:

```text
http://127.0.0.1:8000/openapi.json
```

## Project Structure

A typical project structure is:

```text
project/
│
├── app/
│   ├── main.py
│   └── ...
│
├── requirements.txt
├── README.md
└── venv/
```

## Requirements

- Python 3.x
- FastAPI
- Uvicorn
- Dependencies listed in `requirements.txt`

## Running the Project

After activating the virtual environment and installing the dependencies, start the development server:

```bash
uvicorn app.main:app --reload
```

Then open:

```text
http://127.0.0.1:8000/docs
```

to access the interactive API documentation.

## License

Add your project's license information here.