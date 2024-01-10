import random
import pandas as pd

districts_cairo = [
    "التبين", "حلوان", "المعصرة", "خمسة عشر مايو", "طره", "المعادى", "البساتين", "دار السلام",
    "مصر القديمة", "السيدة زينب", "الخليفة", "المقطم", "منشأة ناصر", "الدرب الاحمر", "الموسكى",
    "عابدين", "قصر النيل", "الزمالك", "بولاق", "الازبكية", "باب الشعرية", "الجمالية", "الظاهر",
    "الوايلى", "حدائق القبة", "الشرابية", "شبرا", "روض الفرج", "الساحل", "الزاوية الحمراء", "الاميرية",
    "الزيتون", "المطرية", "عين شمس", "المرج", "أول السلام", "ثان السلام", "النزهة", "مصر الجديدة",
    "أول مدينة نصر", "ثان مدينة نصر", "التجمع الخامس", "أول القاهره الجديده", "التجمع الاول",
    "ثان القاهره الجديده", "القطامية", "ثالث القاهره الجديده", "الشروق", "مدينه بدر"
]

districts_alexandria = [
    "الإسكندرية", "المنتزه", "الجمرك", "الرملة", "العطارين", "اللبان", "برج العرب", "العامرية", "السيوف",
    "سموحة", "العصافرة", "كرموز", "السيدة زينب", "فلمنج", "منشية البكري", "العجمي", "أبو قير", "الورديان",
    "المعمورة", "العامرية البحرية", "الدخيلة", "الساحل الشمالي"
]

districts_giza = [
    "الجيزة", "العمرانية", "الحوامدية", "البدرشين", "الصف", "أوسيم", "كرداسة", "الأميرية", "العياط",
    "الباويطى", "إمبابة", "طه حسين", "العشار", "أطفيح", "منشية القناطر", "الإسماعيلية", "الوراق",
    "الصف الأعلى", "الزمالك", "الشيخ زايد", "الحصري", "أكتوبر"
]


def generate_random_addresses(districts_list, num_examples,):
    addresses_examples = []

    for _ in range(num_examples):
        district = random.choice(districts_list)
        street_name = f"شارع {random.choice(['العربي', 'الفتح', 'الشهداء', 'السلام','البحر',''])}"
        random_number = random.randint(1, 100)
        address = f"{street_name}، {district}،  رقم {random_number}"
        addresses_examples.append(address)

    return addresses_examples

cairo_addresses_examples= generate_random_addresses(districts_cairo,500,)
alexandria_addresses_examples= generate_random_addresses(districts_alexandria,500,)
giza_addresses_examples= generate_random_addresses(districts_giza,500,)


addresses = cairo_addresses_examples + alexandria_addresses_examples + giza_addresses_examples
labels = [1] * len(cairo_addresses_examples) + [0] * len(alexandria_addresses_examples) + [0] * len(giza_addresses_examples)

data = pd.DataFrame({"address": addresses, "label": labels})


data.to_csv('labeled_addresses.csv',index=False)

