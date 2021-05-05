# FastAPI demo :rocket:

Step-by-step demo of some of the amazing functionalities of **FastAPI**. Check out the [video!](https://www.youtube.com/watch?v=nHGAGtxSeNk)

## Requirements
Python 3.6+

## Running the demo

### Preparation

Create a virtual env:
```
python3 -m venv fastapi-env
source fastapi-env/bin/activate
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Create the `git previous` and `git next` aliases:
```
git config --global alias.previous '!git checkout $(git rev-list demo-start~1..HEAD | head -2 | tail -1)'
git config --global alias.next '!git checkout $(git rev-list HEAD..demo-end | tail -1 )'
```

Checkout the demo-start tag:
```
git checkout demo-start
```

### Let the demo start :sparkles:
Run the app:
```
uvicorn main:app --reload
```

When you are ready, move to the next step with `git next`.
To move backwards use  `git previous`.

The demo ends at commit 41be930448ddb24e88e4602eb615389951c50f1b: `Add 404 response to docs`. 
After this, use `git checkout master` to see how the app can be evolved
by using some other features of FastAPI. From this point run the app as:
```
uvicorn app.main:app --reload
```



