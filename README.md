
# int.pl Generator

A bulk-account generator for a Polish email provider int.pl


## Requirements

- Google Chrome version 101+
- Selenium
## Installation

If you haven't already, install Selenium:

```bash
pip install selenium
```
Open the config.json file and set your login (before the @), password and a recovery email.
The program will append random numbers to the login for each account.

```
    "login": "isu",
    "password": "samplepassword",
    "recovery": "recovery@example.com"
```
Make sure the password meets the requirements:
- 8 - 32 Characters
- min. 1 number/special character

## Usage/Examples
1. Run main.py.
2. Enter the amount of accounts to be generated.
3. The accounts in an email:password format are saved to log.txt
```
isu33982@int.pl:samplepassword
isu11349@int.pl:samplepassword
isu45538@int.pl:samplepassword
```
## FAQ
#### What's the point of this tool? Why use it over a catch-all on a custom domain?
Some websites don't like when users register accounts with emails from custom domains. This tool allows users who are looking to automate certain activities create bulk email accounts from a well-established email provider.

#### I'm getting an Error while creating the accounts
It's mostly the fault of a rate limit. Try using a different IP.

#### The program doesn't start
Make sure your Chrome is updated to v.101




## TODO
- Add threading
- Discord integration