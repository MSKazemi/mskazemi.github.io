#!/usr/bin/env python3
"""Generate the Persian (/fa/) and Turkish (/tr/) landing pages.

Why these two languages: Mohsen is a native speaker of Persian, Azerbaijani and
Turkish, and the estate had zero non-English surface. Those markets carry a
fraction of English's competition for the same terms, so a single strong page
per language is the highest-value content move available — see BRAND.md §4 and
strategy/visibility/2026-08-10-seo-audit-mskazemi-com.md.

Structure mirrors the English pages deliberately: question-shaped headings with
the answer in the first sentence, plus FAQPage data mirroring the visible copy.
That is the pattern Search Console shows already ranking in English.

Claims discipline: no citation counts (a page cannot carry the read-date in the
places they would go), no benchmark numbers, no forbidden project claims. Every
statement here is biographical or a description of services.

Run from the site root:  python3 tools/build_lang_pages.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

NAV_ITEMS = [("../#systems", None), ("../projects/kubeintellect/", "KubeIntellect"),
             ("../projects/yazses/", "YazSes"), ("../datasets/", None), ("../hire/", None)]

# --------------------------------------------------------------------------- fa
FA = dict(
    lang="fa", direction="rtl", slug="fa",
    # NOTE: the Persian rendering of the name is the standard one, but it is the
    # single element here that only Mohsen can confirm. If it is wrong, it is a
    # one-line fix — and a wrong variant is exactly what splits an identity, so
    # it is flagged rather than assumed correct.
    name="محسن سیدکاظمی اردبیلی",
    title="محسن سیدکاظمی اردبیلی — زیرساخت هوش مصنوعی، MLOps و کوبرنتیز",
    description="محسن سیدکاظمی اردبیلی، مهندس زیرساخت هوش مصنوعی و پژوهشگر دانشگاه بولونیا. سامانه‌هایی می‌سازد که روی زیرساخت عمل می‌کنند. همکاری دورکاری در سراسر جهان.",
    role="مهندس زیرساخت هوش مصنوعی · پژوهشگر دانشگاه بولونیا",
    thesis_pre="من هوش مصنوعی خودگردانی می‌سازم که روی زیرساخت ",
    thesis_em="عمل می‌کند",
    thesis_post="، نه اینکه فقط دربارهٔ آن توضیح بدهد.",
    lede="نه یک چت‌بات که خوشهٔ شما را توضیح می‌دهد — سامانه‌هایی که آن را رصد می‌کنند، دربارهٔ خرابی‌ها استدلال می‌کنند و اصلاح را اجرا می‌کنند، در حالی که تصمیم نهایی با یک انسان است.",
    strip=[("جایگاه", "بولونیا، ایتالیا · دورکاری در سراسر جهان"),
           ("پیشینه", "هفت سال زیرساخت حیاتی ← دکترای رایانش کارایی بالا"),
           ("زمینه", "AI SRE · AIOps · MLOps · کوبرنتیز · HPC")],
    sections=[
        ("چه کسی هستم؟",
         ["""پیش از دکترا، هفت سال مدیر فناوری اطلاعات و شبکهٔ یک نیروگاه سیکل ترکیبی با ظرفیت بیش از ۱۰۰۰ مگاوات بودم — محیطی بدون سامانهٔ آزمایشی، جایی که هزینهٔ یک تغییر اشتباه با مگاوات سنجیده می‌شود، نه با بودجهٔ خطا.""",
          """سپس دکترای «طراحی، تحلیل و مدیریت سامانه‌های رایانش کارایی بالا» را در دانشگاه بولونیا گذراندم و از آن پس روی پروژه‌های اروپایی EuroHPC کار پژوهشی و مهندسی سکو انجام می‌دهم.""",
          """همین پیشینه است که توضیح می‌دهد چرا سامانه‌های من پیش از عمل اجازه می‌گیرند: نخست عملیات، سپس پژوهش."""]),
        ("چه کاری انجام می‌دهم؟",
         ["""کار من در سه حوزه است و هر کدام می‌تواند با یک بازبینی کوتاه و با قیمت مشخص آغاز شود، تا پیش از تعهد بلندمدت نتیجهٔ کار را ببینید:""",
          """<strong>قابلیت اطمینان کوبرنتیز و AIOps</strong> — بررسی سلامت خوشه، مشاهده‌پذیری، مقاوم‌سازی و ریشه‌یابی حوادث.""",
          """<strong>MLOps و یادگیری ماشین در محیط عملیاتی</strong> — رجیستری مدل، سرویس‌دهی، تشخیص دریفت، بازآموزی تحت نظارت و پایش.""",
          """<strong>عامل‌های زبانی در محیط عملیاتی</strong> — مرزبندی ابزارها، دسترسی حداقلی، دروازهٔ تأیید انسانی، ردگیری و گزارش حسابرسی."""]),
        ("AI SRE چیست و با یک چت‌بات چه فرقی دارد؟",
         ["""یک AI SRE روی خوشهٔ زنده <strong>عمل می‌کند</strong>، در حالی که یک چت‌بات تنها توضیح می‌دهد. شواهد را خودش از ابزارهای واقعی گرد می‌آورد — kubectl، پرومتئوس، لوکی — دربارهٔ علت واقعی خرابی استدلال می‌کند و سپس اصلاح را اجرا می‌کند.""",
          """تفاوتی که در محیط عملیاتی اهمیت دارد، همان دروازهٔ تأیید است: تغییر را یک انسان تأیید می‌کند و کل زنجیره به‌صورت یک ردّ حسابرسی باقی می‌ماند."""]),
        ("آیا برای همکاری دورکاری در دسترس هستم؟",
         ["""بله — دورکاری با کارفرمایان سراسر جهان. پایگاه کاری من بولونیا در ایتالیا و بر اساس وقت مرکز اروپا (CET) است و برای هم‌پوشانی با دیگر مناطق زمانی هماهنگ می‌شوم.""",
          """برای جزئیات، صفحهٔ <a href="../hire/">همکاری</a> را ببینید یا مستقیم ایمیل بزنید."""]),
        ("چه چیزهایی ساخته‌ام؟",
         ["""<strong><a href="../projects/kubeintellect/">KubeIntellect</a></strong> — یک AI SRE برای کوبرنتیز که با ابزارهای واقعی خوشه را بررسی می‌کند، علت ریشه‌ای را به زبان ساده توضیح می‌دهد و تنها پس از تأیید شما آن را برطرف می‌کند. داوری‌شده در نشریهٔ Journal of Grid Computing.""",
          """<strong><a href="../projects/novafabric/">NovaFabric</a></strong> — ضبط، بازپخش، مقایسه و حسابرسی هر اجرای عامل هوش مصنوعی، بدون تغییر در کد.""",
          """<strong><a href="../projects/yazses/">YazSes</a></strong> — نرم‌افزار آزاد و متن‌باز دیکتهٔ صوتی برای لینوکس، مک و ویندوز؛ تبدیل گفتار به متن به‌صورت پیش‌فرض کاملاً روی دستگاه خودتان.""",
          """<strong><a href="../projects/aobench/">AOBench</a></strong> — سنجه‌ای برای ارزیابی عامل‌های زبانی در کارهای واقعی عملیات ابررایانه، با اعمال سیاست دسترسی."""]),
    ],
    cta="همکاری با من",
    contact_h="بیایید دربارهٔ کار شما صحبت کنیم.",
    contact_p="برای همکاری پژوهشی، کار متن‌باز یا پروژه‌های صنعتی در حوزهٔ زیرساخت هوش مصنوعی، HPC و عملیات خودکار در دسترس هستم.",
    other=[("English", "../"), ("Türkçe", "../tr/")],
    faq_note="پرسش‌های پرتکرار",
)

# --------------------------------------------------------------------------- tr
TR = dict(
    lang="tr", direction="ltr", slug="tr",
    name="Mohsen Seyedkazemi Ardebili",   # Latin script — identical to canonical
    title="Mohsen Seyedkazemi Ardebili — Yapay zekâ altyapısı, MLOps ve Kubernetes",
    description="Mohsen Seyedkazemi Ardebili, yapay zekâ altyapısı mühendisi ve Bologna Üniversitesi'nde araştırmacı. Altyapı üzerinde hareket eden sistemler geliştirir. Dünya genelinde uzaktan çalışır.",
    role="Yapay zekâ altyapısı mühendisi · Bologna Üniversitesi'nde Araştırmacı",
    thesis_pre="Altyapı üzerinde ",
    thesis_em="hareket eden",
    thesis_post=" otonom yapay zekâ sistemleri geliştiriyorum — yalnızca açıklayan değil.",
    lede="Kümenizi anlatan bir sohbet botu değil: onu gözleyen, arızalar üzerine akıl yürüten ve düzeltmeyi uygulayan sistemler — son kararı bir insan verir.",
    strip=[("KONUM", "Bologna, İtalya · dünya genelinde uzaktan"),
           ("GEÇMİŞ", "Yedi yıl kritik altyapı → HPC doktorası"),
           ("ALAN", "AI SRE · AIOps · MLOps · Kubernetes · HPC")],
    sections=[
        ("Kimim?",
         ["""Doktoradan önce yedi yıl boyunca 1.000 MW'ın üzerindeki bir kombine çevrim santralinin BT ve ağ yöneticisiydim — hazırlık ortamının bulunmadığı, hatalı bir değişikliğin bedelinin hata bütçesiyle değil megavatla ölçüldüğü bir ortam.""",
          """Ardından Bologna Üniversitesi'nde "Yüksek Başarımlı Hesaplama Sistemlerinin Tasarımı, Analizi ve Yönetimi" alanında doktora yaptım; o günden beri EuroHPC projelerinde araştırma ve platform mühendisliği yürütüyorum.""",
          """Sistemlerimin harekete geçmeden önce izin istemesinin nedeni tam olarak bu geçmiş: önce operasyon, sonra araştırma."""]),
        ("Ne yapıyorum?",
         ["""Çalışmam üç alanda yoğunlaşıyor. Her biri sabit fiyatlı kısa bir denetimle başlayabilir; böylece uzun bir taahhüde girmeden işin niteliğini görürsünüz:""",
          """<strong>Kubernetes güvenilirliği ve AIOps</strong> — sağlık denetimi, gözlemlenebilirlik, sıkılaştırma ve olayların kök neden analizi.""",
          """<strong>MLOps ve üretimde makine öğrenmesi</strong> — model kaydı, servis etme, kayma tespiti, denetimli yeniden eğitim ve izleme.""",
          """<strong>Üretim ortamında LLM ajanları</strong> — araç sınırları, dar kapsamlı yetkilendirme, insan onayı kapısı, izleme ve denetim kaydı."""]),
        ("AI SRE nedir, bir sohbet botundan farkı ne?",
         ["""Bir AI SRE canlı küme üzerinde <strong>hareket eder</strong>; sohbet botu ise yalnızca açıklar. Kanıtı kendisi gerçek araçlardan toplar — kubectl, Prometheus, Loki — gerçekte neyin bozulduğu üzerine akıl yürütür ve ardından düzeltmeyi uygular.""",
          """Üretimde asıl fark yaratan şey onay kapısıdır: değişikliği bir insan yetkilendirir ve tüm zincir bir denetim kaydı olarak geride kalır."""]),
        ("Uzaktan çalışmaya açık mıyım?",
         ["""Evet — dünya genelindeki müşterilerle uzaktan çalışıyorum. Çalışma günümün temeli Bologna, İtalya ve CET saat dilimi; diğer saat dilimleriyle örtüşmeyi ayrıca ayarlıyorum.""",
          """Ayrıntılar için <a href="../hire/">çalışma sayfasına</a> bakabilir ya da doğrudan e-posta gönderebilirsiniz."""]),
        ("Neler geliştirdim?",
         ["""<strong><a href="../projects/kubeintellect/">KubeIntellect</a></strong> — Kubernetes için bir AI SRE: kümeye bağlanır, gerçek araçlarla inceler, kök nedeni sade bir dille anlatır ve düzeltmeyi ancak siz onayladıktan sonra uygular. Journal of Grid Computing'de hakem değerlendirmesinden geçti.""",
          """<strong><a href="../projects/novafabric/">NovaFabric</a></strong> — herhangi bir yapay zekâ ajanı çalışmasını kod değişikliği olmadan kaydeder, yeniden oynatır, karşılaştırır ve denetler.""",
          """<strong><a href="../projects/yazses/">YazSes</a></strong> — Linux, macOS ve Windows için özgür ve açık kaynaklı sesli yazma yazılımı; konuşmadan metne dönüştürme varsayılan olarak tümüyle kendi cihazınızda çalışır.""",
          """<strong><a href="../projects/aobench/">AOBench</a></strong> — LLM ajanlarını gerçek süperbilgisayar operasyon görevlerinde, erişim politikasını da uygulayarak değerlendiren bir kıyaslama."""]),
    ],
    cta="Birlikte çalışalım",
    contact_h="İşinizi konuşalım.",
    contact_p="Yapay zekâ altyapısı, HPC ve otonom operasyonlar alanında araştırma iş birliklerine, açık kaynak çalışmalarına ve endüstriyel projelere açığım.",
    other=[("English", "../"), ("فارسی", "../fa/")],
    faq_note="Sık sorulan sorular",
)

EMAIL = "mohsen.seyedkazemi@gmail.com"


def page(c):
    lang, d = c["lang"], c["direction"]
    url = f"https://mskazemi.com/{c['slug']}/"
    rtl_css = """
  <style>
    /* Persian is right-to-left; style.css is authored LTR, so only the flow
       needs flipping. Everything else (colours, spacing, type scale) is shared. */
    body { direction: rtl; }
    .nav-inner, .footer-inner { direction: ltr; }
    .prose, .proj-hero, .section-title, .contact { text-align: right; }
    /* style.css sets the strip in IBM Plex Mono, which has no Arabic-script
       coverage — Persian falls back to a disconnected face and the letterforms
       stop joining. Use the body font here instead. */
    .status-strip { padding-right: 0; font-family: inherit; font-size: .92rem; }
    .status-strip li { line-height: 1.95; }
    .status-strip .k { font-family: inherit; letter-spacing: normal;
                       margin-right: 0; margin-left: 8px; opacity: .85; }
    .prose a { text-underline-offset: 3px; }
  </style>""" if d == "rtl" else ""

    # Person + FAQPage, in this language, referencing the one canonical entity.
    faq = [{"@type": "Question", "name": h,
            "acceptedAnswer": {"@type": "Answer",
                               "text": " ".join(p.replace("<strong>", "").replace("</strong>", "")
                                                 .replace('<a href="../hire/">', "").replace("</a>", "")
                                                 .replace('<a href="../projects/kubeintellect/">', "")
                                                 .replace('<a href="../projects/novafabric/">', "")
                                                 .replace('<a href="../projects/yazses/">', "")
                                                 .replace('<a href="../projects/aobench/">', "")
                                                 for p in ps)}}
           for h, ps in c["sections"]]
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": c["title"],
         "inLanguage": lang, "dateModified": "2026-08-11T03:30:00+02:00",
         "isPartOf": {"@id": "https://mskazemi.com/#website"},
         "about": {"@id": "https://mskazemi.com/#person"}},
        {"@type": "Person", "@id": "https://mskazemi.com/#person", "name": c["name"],
         "alternateName": "Mohsen Seyedkazemi Ardebili",
         "jobTitle": c["role"], "url": "https://mskazemi.com/",
         "description": c["description"],
         "sameAs": ["https://mskazemi.com/", "https://github.com/MSKazemi",
                    "https://www.linkedin.com/in/mskazemi/",
                    "https://orcid.org/0000-0002-1166-6559",
                    "https://www.wikidata.org/wiki/Q140935575"]},
        {"@type": "FAQPage", "@id": url + "#faq", "inLanguage": lang,
         "isPartOf": {"@id": url + "#webpage"}, "mainEntity": faq}]}

    alts = "\n".join(
        f'  <link rel="alternate" hreflang="{h}" href="{u}" />'
        for h, u in [("en", "https://mskazemi.com/"), ("fa", "https://mskazemi.com/fa/"),
                     ("tr", "https://mskazemi.com/tr/"), ("x-default", "https://mskazemi.com/")])

    secs = "\n".join(
        f"""  <section class="proj-section panel-section{' alt' if i % 2 == 0 else ''}">
    <div class="container">
      <h2 class="section-title">{h}</h2>
      <div class="prose">
{chr(10).join(f'        <p>{p}</p>' for p in ps)}
      </div>
    </div>
  </section>""" for i, (h, ps) in enumerate(c["sections"]))

    strip = "\n".join(f'          <li><span class="k">{k}</span> {v}</li>' for k, v in c["strip"])
    other = " &nbsp;·&nbsp; ".join(f'<a href="{u}">{n}</a>' for n, u in c["other"])

    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{d}">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <script>try{{if(localStorage.getItem('theme')==='dark')document.documentElement.setAttribute('data-theme','dark');}}catch(e){{}}</script>
  <title>{c['title']}</title>
  <meta name="description" content="{c['description']}" />
  <meta name="author" content="Mohsen Seyedkazemi Ardebili" />
  <link rel="canonical" href="{url}" />
{alts}
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1" />
  <meta property="og:title" content="{c['title']}" />
  <meta property="og:description" content="{c['description']}" />
  <meta property="og:type" content="profile" />
  <meta property="og:url" content="{url}" />
  <meta property="og:locale" content="{lang}" />
  <meta property="og:image" content="https://mskazemi.com/assets/mohsen-portrait.jpg" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230A0E14'/%3E%3Cpath d='M9 16a7 7 0 1 1 2.05 4.95' fill='none' stroke='%23F2A93B' stroke-width='2.4' stroke-linecap='round'/%3E%3Ccircle cx='9' cy='16' r='2.4' fill='%233FD79A'/%3E%3C/svg%3E" />
  <link rel="preload" href="/assets/fonts/space-grotesk-600-latin.woff2" as="font" type="font/woff2" crossorigin />
  <link rel="stylesheet" href="/assets/fonts/fonts.css" />
  <link rel="stylesheet" href="../style.css" />
  <link rel="stylesheet" href="../project.css" />{rtl_css}
  <script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=2)}
  </script>
</head>
<body>
  <header class="nav" id="nav">
    <div class="container nav-inner">
      <a class="brand" href="../">Mohsen Seyedkazemi</a>
      <button class="nav-toggle" id="navToggle" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span></button>
      <nav class="nav-links" id="navLinks" aria-label="Primary">
        <a href="../projects/kubeintellect/">KubeIntellect</a>
        <a href="../projects/yazses/">YazSes</a>
        <a href="../datasets/">Datasets</a>
        <a href="../hire/">Hire</a>
        <a href="../#contact" class="nav-cta">Get in touch</a>
        <button class="theme-toggle" id="themeToggle" type="button" aria-label="Toggle theme" title="Toggle theme" aria-pressed="false">
          <svg class="ic-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
          <svg class="ic-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
        </button>
      </nav>
    </div>
  </header>

  <section class="proj-hero">
    <div class="container">
      <h1>{c['name']}</h1>
      <p class="proj-tagline">{c['role']}</p>
      <p class="hero-thesis">{c['thesis_pre']}<span class="amber">{c['thesis_em']}</span>{c['thesis_post']}</p>
      <p class="lede">{c['lede']}</p>
      <div class="proj-links">
        <a class="btn-primary" href="../hire/">{c['cta']}</a>
        <a class="btn-ghost" href="https://github.com/MSKazemi" target="_blank" rel="noopener">GitHub ↗</a>
        <a class="btn-ghost" href="https://scholar.google.com/citations?user=xP64pZsAAAAJ" target="_blank" rel="noopener">Google Scholar ↗</a>
      </div>
      <ul class="status-strip">
{strip}
      </ul>
      <p class="lede" style="margin-top:1.2rem">{other}</p>
    </div>
  </section>

{secs}

  <section class="contact">
    <div class="container">
      <h2 class="contact-h">{c['contact_h']}</h2>
      <p class="contact-lead">{c['contact_p']}</p>
      <div class="proj-links">
        <a class="btn-primary" href="mailto:{EMAIL}">{EMAIL}</a>
        <a class="btn-ghost" href="https://www.linkedin.com/in/mskazemi/" target="_blank" rel="noopener">LinkedIn ↗</a>
      </div>
    </div>
  </section>

  <footer>
    <div class="container footer-inner">
      <span>© <span id="year"></span> Mohsen Seyedkazemi Ardebili</span>
      <nav class="footer-nav" aria-label="Site pages">
        <a href="../">English</a>
        <a href="../fa/">فارسی</a>
        <a href="../tr/">Türkçe</a>
        <a href="../about/">About</a>
        <a href="../hire/">Hire</a>
      </nav>
      <span class="foot-meta">Bologna, Italy · mskazemi.com</span>
    </div>
  </footer>
  <script src="../script.js"></script>
</body>
</html>
"""


def main():
    for c in (FA, TR):
        d = ROOT / c["slug"]
        d.mkdir(exist_ok=True)
        (d / "index.html").write_text(page(c), encoding="utf-8")
        print(f"wrote {c['slug']}/index.html  ({c['lang']}, dir={c['direction']})")


if __name__ == "__main__":
    main()
