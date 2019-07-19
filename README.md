Install the requirements with

`pip install -R requirements.txt`

generate a slack token https://api.slack.com/custom-integrations/legacy-tokens

and run the script with, for example

```
$ python check_website.py \
    https://time.is/ \
    time \
    \#bla \
    --seconds 1
```
