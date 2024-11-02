# Textfile Translation

This 

```bash
# (Optional but highly recommended) First activate an environment using Conda or similar.
conda create -n translate
conda activate translate
conda install python=3.12

# Add OPENAI_API_KEY to a new `.env`
echo 'OPENAI_API_KEY=fill-me-with-your-key' > .env

# Install
pip install -r requirements.txt

# Add all the files you want to translate to /files
echo 'namaste, aap kaise hai?' > ./files/namaste.txt

# Run
python translate.py
```