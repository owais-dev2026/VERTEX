from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

path="/mnt/data/خطة_جلب_اول_عميل_أويس.pdf"
pdfmetrics.registerFont(UnicodeCIDFont("HYSMyeongJo-Medium"))

doc=SimpleDocTemplate(path,pagesize=A4,rightMargin=36,leftMargin=36,topMargin=36,bottomMargin=36)
styles=getSampleStyleSheet()
title=ParagraphStyle("t",parent=styles["Title"],fontName="HYSMyeongJo-Medium",fontSize=19,leading=27,alignment=TA_CENTER,spaceAfter=14)
head=ParagraphStyle("h",parent=styles["Heading2"],fontName="HYSMyeongJo-Medium",fontSize=13,leading=20,alignment=TA_RIGHT,spaceBefore=8,spaceAfter=6)
body=ParagraphStyle("b",parent=styles["BodyText"],fontName="HYSMyeongJo-Medium",fontSize=10.5,leading=18,alignment=TA_RIGHT,spaceAfter=5)

story=[Paragraph("خطة الحصول على أول عميل",title),
       Paragraph("خطة مختصرة لمدة 7 أيام — نفّذها بدون تشتّت",body)]

days=[
("اليوم 1 — البحث","ابحث عن 20 مطعمًا أو كافيهًا أو مشروعًا تجاريًا يحتاج موقعًا. سجّل الاسم ووسيلة التواصل."),
("اليوم 2 — التواصل","أرسل الرسالة الجاهزة أدناه إلى 20 مشروعًا مستهدفًا، مع رابط موقعك."),
("اليوم 3 — دفعة جديدة","ابحث عن 20 مشروعًا جديدًا وأرسل لهم نفس الرسالة."),
("اليوم 4 — المتابعة","تابع الأشخاص الذين لم يردوا برسالة قصيرة، بدون ضغط."),
("اليوم 5 — دفعة جديدة","20 مشروعًا جديدًا + نفس الرسالة. ركّز على المشاريع التي تشبه نماذجك."),
("اليوم 6 — إغلاق المهتمين","تحدث مع المهتمين، أرسل الرابط، وافهم احتياجاتهم ثم أعطهم السعر حسب طلبهم."),
("اليوم 7 — المراجعة","احسب الرسائل والردود والمهتمين والعملاء. كرر ما أعطى أفضل نتيجة للأسبوع التالي.")
]
for d,x in days:
    story += [Paragraph(d,head),Paragraph(x,body)]

story.append(PageBreak())
story.append(Paragraph("الرسالة الجاهزة",title))
story.append(Paragraph("انسخها كما هي، وضع رابط موقعك مكان السطر الأخير:",body))
msg="""مرحبًا، يعطيكم العافية 🌷<br/><br/>
أقدّم تصميم مواقع ويب احترافية ومتوافقة مع الموبايل للمطاعم والمشاريع التجارية، مع إمكانية إضافة WhatsApp والحجز والطلبات والأتمتة حسب الحاجة.<br/><br/>
جهزت صفحة فيها نماذج أعمالي وتفاصيل الخدمة، ويمكنكم مشاهدة النماذج مباشرة من هنا:<br/><br/>
<b>🔗 ضع رابط موقعك هنا</b><br/><br/>
إذا أعجبكم أحد النماذج، يمكنني تنفيذ موقع خاص بمشروعكم حسب احتياجكم وبسعر يُحسب حسب التفاصيل المطلوبة."""
story.append(Paragraph(msg,body))

story += [
Paragraph("إذا سأل: «كم السعر؟»",head),
Paragraph("السعر يختلف حسب حجم الموقع والصفحات والميزات المطلوبة. ادخل على الرابط وشاهد النماذج واختر التفاصيل، وسيظهر السعر حسب طلبك.",body),
Paragraph("قواعد مهمة",head),
Paragraph("🎯 هدفنا الأول: أول عميل مدفوع.<br/>📩 20 تواصلًا مستهدفًا يوميًا.<br/>🚫 لا تعمل موقعًا كاملًا مجانًا.<br/>🔗 أرسل الرابط مبكرًا ليشاهد العميل شغلك.<br/>📊 سجّل عدد الرسائل والردود والمهتمين يوميًا.",body)
]
doc.build(story)
print(path)
