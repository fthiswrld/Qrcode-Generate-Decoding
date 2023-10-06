import qrcode 
import cv2

while True:
    a = input("What your want ?\n1)Read the QRCode.\n2)Create the QRCode.\nYour answer:")
    if a == '1':
        a = input("Enter path to your image(qrcode):")
        img = cv2.imread(a)
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(img)
        print(data)
        break
    elif a == '2':
        data = input("Enter data:")
        img = qrcode.make(data)
        name_file = input('Enter name of qrcode:')
        img.save(f"{name_file}.png")
        break
    else:
        print("Enter correct answer!")
