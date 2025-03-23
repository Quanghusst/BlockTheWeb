# NOTE
This code runs search engine is duckduckgo!
---

# Before the run (only window)
```bash
pip install requests beautifulsoup4 lxml
```
# Run
```bash
.\run.bat
```
# Explain
If you put `127.0.0.1   example.com` in your hosts file, `example.com` will be blocked!!!

Locate hosts file: 
```
C:\Windows\System32\Drivers\etc\hosts
```
---
# J2team block extension

- Run `GenJson.py` to create a json block domain file (`block.json`)
- Install [J2team extension](https://chromewebstore.google.com/detail/j2team-security/hmlcjjclebjnfohgmgikjfnbmfkigocc) 
- Import `block.json` in Website Blocker of J2team extension.
