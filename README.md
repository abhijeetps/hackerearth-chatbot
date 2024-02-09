
# HackerEarth Digital Assistant

HackerEarth's Digital Assistant that helps your answer queries around the HackerEarth's product!

![HackerEarth's Digital Assistant at work!](https://imgur.com/0S0p0BW.png)


## Features

- HackerEarth's digital assistant and salesperson
- Supports knowledgebase from the web
- Supports knowledgebase provided via PDFs.
- Answer all your queries around HackerEarth
- Asks user for contact details so that human sale sperson can reach back to the user
- Saves the contact detail and intent in a database for reference purpose
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

`PINECONE_API_KEY`

`PINECONE_ENVIRONMENT`

`PINECONE_INDEX`

You can simply perform the following command to prepare the env template.

`cp .env.example .env`

Add the value to the environment variables on your end.
## Run Locally

Clone the project

```bash
  https://github.com/abhijeetps/hackerearth-digital-assistant
```

Go to the project directory

```bash
  cd hackerearth-digital-assistant
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Add environment variables to _.env_ file.

Populate Vector Database with HackerEarth's content.

```bash
  python vdb.py
```

Run HackerEarth's chatbot locally:

```bash
streamlit run app.py
```
## Authors

- [@abhijeetps](https://www.github.com/abhijeetps)

