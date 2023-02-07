import speedtest
import msvcrt


test = speedtest.Speedtest()

print("Sunucu listesi alınıyor...")
test.get_servers()
print("En iyi sunucu seçiliyor...")
best = test.get_best_server()

print(f"{best['country']}'de bulunan en iyi konum bulundu: {best['host']} ")

print("Download testi gerçekleştiriliyor...")
download_result = test.download()
print("Upload testi gerçekleştiriliyor...")
upload_result = test.upload()
ping_result = test.results.ping

print(f"Download hızınız: {download_result / 1024 / 1024:.2f}Mbit/s")
print(f"Upload hızınız: {upload_result / 1024 / 1024:.2f}Mbit/s")
print(f"Ping Süresi: {ping_result}ms")

print(f"Bir tuşa basınız")
msvcrt.getch()