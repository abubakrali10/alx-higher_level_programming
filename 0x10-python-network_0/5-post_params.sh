#!/bin/bash
# sends a POST request to the passed URL, and displays the body of the response
email="test@gmail.com"
subject="I will always be here for PLD"
curl -s -X POST "$1" -d "email=$email&subject=$subject"
