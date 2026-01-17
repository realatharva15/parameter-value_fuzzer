# Parameter fuzzer: parafuzzer
# Author: Atharva Bordavekar
# Only for CTF purposes! 

`Description: parafuzzer.py can help you find out hidden paramters and value pairs from a wordlist which covers almost all widely used parameters and their respective values which are use in CTF environment.`

# How to use (Linux):
clone the repository on your machine.

```bash
git clone https://github.com/realatharva15/parameter-value_fuzzer
```
now navigate to the parameter-value_fuzzer directory and directly start with the fuzzing process.
you don't have to provide any options or flags to this tool. just execute it like how you would execute a normal python script.
```bash
python3 parafuzzer.py
```
once you are prompted the url, enter the url with the exact path to the page which might have parameters.

enter the default page size, i.e the size of the page when you visit the page where you suspect a vulnerability. you can find this out using the command:

```bash
curl -s "http://<target>" | wc -c
```
![image1](https://github.com/realatharva15/parameter-value_fuzzer/blob/main/images/parafuzzer.png)

this will print out the size of the webpage in bytes. use this to answer the second prompt. after this you have to relax and wait for the output. depending on the parameter it could take anywhere between 1 minute to 5 minutes.

# Logic of the script:

