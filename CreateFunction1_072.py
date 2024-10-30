while True:
    temperature = float(input("Suhunya berapa : "))
    satuan = input("Celcius atau Farenheit : ")

    farenheit = (9/5) * temperature + 32
    celcius = (temperature - 32) * 5/9

    if satuan in ['celcius','Celcius','C','c']:
        print(f"Suhu farenheitnya adalah {farenheit}°F")
        break  
    elif satuan in ['farenheit','F','f','Farenheit']:
        print(f"Suhu celciusnya adalah {celcius}°C")
        break  
    else:
        print("Anda salah memasukkan satuan. Silakan coba lagi.")