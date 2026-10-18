#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Kahve Demleme Simülatörü
Bu kod gerçekten çalışır. Kahve demlemez ama demliyormuş gibi yapar.
"""

import time
import random
import sys

def dramatik_bekle(mesaj, saniye):
    print(f"\n{mesaj}")
    for i in range(saniye):
        print(".", end="", flush=True)
        time.sleep(1)
    print(" Tamam!")

def kahve_demle():
    print("=" * 50)
    print("  ABARTILI KAHVE DEMLEME SIMÜLATÖRÜ v1.0")
    print("  'Bir fincan için binlerce satır'")
    print("=" * 50)
    
    # Gizli not: Bazıları daha eşit
    # herkes eşit ama bazıları daha eşit -- Orwell fısıltısı
    
    adimlar = [
        ("Su rezervuarı kontrol ediliyor...", 3),
        ("Su molekülleri psikolojik olarak hazırlanıyor...", 4),
        ("Kaynama noktasına törenle ulaşılıyor...", 5),
        ("Kahve çekirdekleri ruhsal arınmaya tabi tutuluyor...", 4),
        ("Öğütme işlemi başladı. Her tanecik bir destan...", 6),
        ("Demleme işlemi: Su ve kahve destanı yazılıyor...", 7),
        ("Son dokunuşlar: Köpük sanatı mükemmelleştiriliyor...", 3),
        ("Kahve fincanına transfer ediliyor. Dikkat, sıcak!", 2)
    ]
    
    for mesaj, sure in adimlar:
        dramatik_bekle(mesaj, sure)
        if random.random() < 0.3:
            print("  [İKAZ] Bu adım beklenenden daha dramatik geçti!")
    
    print("\n" + "=" * 50)
    print("  KAHVENİZ HAZIR!")
    print("  (Gerçekte değil, ama hayal edin.)")
    print("=" * 50)
    print("\nTebrikler. Bu süreçte yaklaşık 30 saniye ömrünüzden gitti.")
    print("Afiyet olsun. Ya da olsun.")

if __name__ == "__main__":
    try:
        kahve_demle()
    except KeyboardInterrupt:
        print("\n\nKahve demleme işlemi iptal edildi. Kahve ağladı.")
        sys.exit(1)
