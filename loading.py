chars = "|/-\|"
for i in range(30):
    time.sleep(0.1)
    sys.stdout.write("\r""["+chars[i % len(chars)]+"]Connecting...")
    sys.stdout.flush()
