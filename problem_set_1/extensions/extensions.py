file = input("Insert your file")
if file.lower().endswith((".gif", ".jpeg", ".png")):
    print("image/" + file.split(".",1)[1])
elif file.lower().endswith(".jpg"):
    print("image/" + "jpeg")
elif ".txt" in file.lower().strip() and ".pdf" in file.lower().strip():
    print("application/pdf")
elif file.lower().strip().endswith((".pdf", ".zip")):
    print("application/" + file.lower().strip().split(".",1)[1])
elif file.lower().endswith(".txt"):
    print("text/" + "plain")
else:
    print("application/octet-stream")