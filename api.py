import requests

Courses = {
"0001":"CSM 388",
"0002":"CSM 354",
"0003":"CSM 352",
"0004":"CSM 374",
"0005":"CSM 358",
"0006":"CSM 394",
"0007":"CSM 376",
"0008":"CSM 286"
}

Lecturers = {
"0001":"Prof.Hayfron Acquah",
"0002":"N.Ussiph",
"0003":"D. Asamoah",
"0004":"J.K Panford",
"0005":"F.Twum",
"0006":"B.E. Owusu",
"0007":"Gadaffi Salam",
"0008":"B. Arthur"
}

results = ""

def send_msg(text):
    global results
    try:
        API_KEY = "6210250509:AAFMpFtUM4LkI1OT6V9oJCQyiBf7pgOx3_Y"
        chat_id = "651829015"
        url_req = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={text}"
        results = requests.get(url_req)
        if results.status_code ==200:
                results = "Response 200"
    except requests.exceptions.RequestException as e:
        results = "Response 404"
        print("An error occurred while making the request:", e)
    except requests.exceptions.HTTPError as e:
        results = "Response 404"
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        results = "Response 404"
        print("Connection Error: Check your internet connection or the specified URL.")
    except requests.exceptions.Timeout as e:
        results = "Response 404"
        print("Timeout Error:", e)
    except requests.exceptions.TooManyRedirects as e:
        results = "Response 404"
        print("Too Many Redirects Error:", e)
    except Exception as e:
        results = "Response 404"
        print("An unexpected error occurred:", e)

def confirmation_message():
    global results
    from home import leccc_code ,getDetails
    try:
        text = f"Please be informed. The {Courses[leccc_code]} lecture for {getDetails()}has been CONFIRMED. See you in class! "
        API_KEY = "6210250509:AAFMpFtUM4LkI1OT6V9oJCQyiBf7pgOx3_Y"
        chat_id = "651829015"
        url_req = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={text}"
        results = requests.get(url_req)
        if results.status_code ==200:
            results = "Response 200"
    except requests.exceptions.RequestException as e:
        results = "Response 404"
        print("An error occurred while making the request:", e)
    except requests.exceptions.HTTPError as e:
        results = "Response 404"
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        results = "Response 404"
        print("Connection Error: Check your internet connection or the specified URL.")
    except requests.exceptions.Timeout as e:
        results = "Response 404"
        print("Timeout Error:", e)
    except requests.exceptions.TooManyRedirects as e:
        results = "Response 404"
        print("Too Many Redirects Error:", e)
    except Exception as e:
        results = "Response 404"
        print("An unexpected error occurred:", e)


def postpone_message():
    global results
    from home import leccc_code ,getDetails, new_time
    try:
        text = f"Please be informed. The {Courses[leccc_code]} lecture for {getDetails()}has been POSTPONED. The new meeting time is: {new_time} "
        API_KEY = "6210250509:AAFMpFtUM4LkI1OT6V9oJCQyiBf7pgOx3_Y"
        chat_id = "651829015"
        url_req = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={text}"
        results = requests.get(url_req)
        if results.status_code ==200:
                    results = "Response 200"
    except requests.exceptions.RequestException as e:
        results = "Response 404"
        print("An error occurred while making the request:", e)
    except requests.exceptions.HTTPError as e:
        results = "Response 404"
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        results = "Response 404"
        print("Connection Error: Check your internet connection or the specified URL.")
    except requests.exceptions.Timeout as e:
        results = "Response 404"
        print("Timeout Error:", e)
    except requests.exceptions.TooManyRedirects as e:
        results = "Response 404"
        print("Too Many Redirects Error:", e)
    except Exception as e:
        results = "Response 404"
        print("An unexpected error occurred:", e)


def announcement_message():
    global results
    from home import leccc_code ,announce_msg
    try:
        text = f"{Lecturers[leccc_code]}: ANNOUNCEMENT!!!! {announce_msg} "
        API_KEY = "6210250509:AAFMpFtUM4LkI1OT6V9oJCQyiBf7pgOx3_Y"
        chat_id = "651829015"
        url_req = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={text}"
        results = requests.get(url_req)
        if results.status_code ==200:
                results = "Response 200"
    except requests.exceptions.RequestException as e:
        results = "Response 404"
        print("An error occurred while making the request:", e)
    except requests.exceptions.HTTPError as e:
        results = "Response 404"
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        results = "Response 404"
        print("Connection Error: Check your internet connection or the specified URL.")
    except requests.exceptions.Timeout as e:
        results = "Response 404"
        print("Timeout Error:", e)
    except requests.exceptions.TooManyRedirects as e:
        results = "Response 404"
        print("Too Many Redirects Error:", e)
    except Exception as e:
        results = "Response 404"
        print("An unexpected error occurred:", e)


def cancellation_message():
    global results
    from home import leccc_code ,getDetails
    try:
        text = f"Please be informed. The {Courses[leccc_code]} lecture for {getDetails()}has been CANCELED. Please stay tuned for any more announcements"
        API_KEY = "6210250509:AAFMpFtUM4LkI1OT6V9oJCQyiBf7pgOx3_Y"
        chat_id = "651829015"
        url_req = f"https://api.telegram.org/bot{API_KEY}/sendMessage?chat_id={chat_id}&text={text}"
        results = requests.get(url_req)
        if results.status_code ==200:
                results = "Response 200"
    except requests.exceptions.RequestException as e:
        results = "Response 404"
        print("An error occurred while making the request:", e)
    except requests.exceptions.HTTPError as e:
        results = "Response 404"
        print("HTTP Error:", e)
    except requests.exceptions.ConnectionError as e:
        results = "Response 404"
        print("Connection Error: Check your internet connection or the specified URL.")
    except requests.exceptions.Timeout as e:
        results = "Response 404"
        print("Timeout Error:", e)
    except requests.exceptions.TooManyRedirects as e:
        results = "Response 404"
        print("Too Many Redirects Error:", e)
    except Exception as e:
        results = "Response 404"
        print("An unexpected error occurred:", e)






 