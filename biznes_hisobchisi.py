print("=== Biznes Hisobchisi ===")
print()

mahsulot_nomi = input("Mahsulot nomini kiriting: ")
tannarx = float(input("Tannarxi (siz sotib olgan narx): "))
sotuv_narxi = float(input("Sotuv narxi (mijozga sotiladigan narx): "))
soni = int(input("Nechta dona bor: "))

bitta_foyda = sotuv_narxi - tannarx
umumiy_foyda = bitta_foyda * soni
umumiy_tannarx = tannarx * soni
umumiy_sotuv = sotuv_narxi * soni

print()
print("=== Natija ===")
print(f"Mahsulot: {mahsulot_nomi}")
print(f"Bitta donadan foyda: {bitta_foyda} so'm")
print(f"Jami sotilsa daromad: {umumiy_sotuv} so'm")
print(f"Jami sarflangan pul: {umumiy_tannarx} so'm")
print(f"Jami foyda: {umumiy_foyda} so'm")

if umumiy_foyda > 0:
    print("Bu mahsulot foyda keltiradi! ✅")
elif umumiy_foyda == 0:
    print("Bu mahsulotdan foyda yo'q (0 daromad)")
else:
    print("Diqqat! Bu mahsulot zarar keltiradi! ⚠️")