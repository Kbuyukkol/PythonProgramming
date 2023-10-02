browser_name = "opera"

if browser_name != "chrome" and browser_name !="firefox" and browser_name !="opera" and browser_name !="safari" and browser_name !="egde":
    print("invalid browser name")
else:
    if browser_name == "chrome":
        browser_name = "Chrome"
    if browser_name == "firefox":
        browser_name = "Firefox"
    if browser_name == "opera":
        browser_name = "Opera"
    if browser_name == "safari":
        browser_name = "Safari"
    if browser_name == "edge":
        browser_name = "Edge"
    print(f"{browser_name} Browser is selected")
