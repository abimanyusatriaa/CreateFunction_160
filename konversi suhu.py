def konversisuhu (temperature, value): #membuat fungsi konversi suhu
    if value == 'C':
        temperaturesuhu = ( temperature - 32) * 5/9 #rumus menghitung celcius
        return temperaturesuhu, 'C'
    else:
        temperaturesuhu = ( temperature * 9/5 ) + 32 #rumus menghitung fahrenheit
        return temperaturesuhu, 'F'
    
celcius_temperature = 30 #menggunakan contoh 30 C
temperaturesuhu, target_value = konversisuhu (celcius_temperature, 'F') 
print (f"{celcius_temperature}°C dikonversi ke Fahrenheit adalah {temperaturesuhu}°{target_value}") #menampilkan hasil konversi celcius ke fahrenheit

fahrenheit_temperature = 86 #menggunakan contoh 86 F
temperaturesuhu, target_value = konversisuhu(fahrenheit_temperature, 'C')
print(f"{fahrenheit_temperature}°F dikonversi ke Celcius adalah {temperaturesuhu}°{target_value}") #menampilkan hasil konversi fahrenheit ke celcius
