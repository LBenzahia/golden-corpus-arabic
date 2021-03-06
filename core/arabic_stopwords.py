arabic_stopwords = ['\u0625\u0630', # إذ
               '\u0625\u0630\u0627', # إذا
               '\u0625\u0630\u0645\u0627', # إذما
               '\u0625\u0630\u0646', # إذن
               '\u0623\u0641', # أف
               '\u0623\u0642\u0644', # أقل
               '\u0623\u0643\u062B\u0631', # أكثر
               '\u0623\u0644\u0627', # ألا
               '\u0625\u0644\u0627', # إلا
               '\u0627\u0644\u062A\u064A', # التي
               '\u0627\u0644\u0630\u064A', # الذي
               '\u0627\u0644\u0630\u064A\u0646', # الذين
               '\u0627\u0644\u0644\u0627\u062A\u064A', # اللاتي
               '\u0627\u0644\u0644\u0627\u0626\u064A', # اللائي
               '\u0627\u0644\u0644\u062A\u0627\u0646', # اللتان
               '\u0627\u0644\u0644\u062A\u064A\u0627', # اللتيا
               '\u0627\u0644\u0644\u062A\u064A\u0646', # اللتين
               '\u0627\u0644\u0644\u0630\u0627\u0646', # اللذان
               '\u0627\u0644\u0644\u0630\u064A\u0646', # اللذين
               '\u0627\u0644\u0644\u0648\u0627\u062A\u064A', # اللواتي
               '\u0625\u0644\u0649', # إلى
               '\u0625\u0644\u064A\u0643', # إليك
               '\u0625\u0644\u064A\u0643\u0645', # إليكم
               '\u0625\u0644\u064A\u0643\u0645\u0627', # إليكما
               '\u0625\u0644\u064A\u0643\u0646', # إليكن
               '\u0623\u0645', # أم
               '\u0623\u0645\u0627', # أما
               '\u0625\u0645\u0627', # إما
               '\u0623\u0646', # أن
               '\u0625\u0646', # إن
               '\u0625\u0646\u0627', # إنا
               '\u0623\u0646\u0627', #  أنا
               '\u0623\u0646\u062A', # أنت
               '\u0623\u0646\u062A\u0645', # أنتم
               '\u0623\u0646\u062A\u0645\u0627', # أنتما
               '\u0623\u0646\u062A\u0646', # أنتن
               '\u0625\u0646\u0645\u0627', # إنما
               '\u0625\u0646\u0647', # إنه
               '\u0623\u0646\u0649', # أنى
               '\u0622\u0647', # آه
               '\u0622\u0647\u0627', # آها
               '\u0623\u0648', # أو
               '\u0623\u0648\u0644\u0627\u0621', # أولاء
               '\u0623\u0648\u0644\u0626\u0643', # أولئك
               '\u0623\u0648\u0647', # أوه
               '\u0622\u064A', # آي
               '\u0623\u064A', # أي
               '\u0623\u064A\u0647\u0627', # أيها
               '\u0625\u064A', # إي
               '\u0623\u064A\u0646', # أين
               '\u0623\u064A\u0646\u0645\u0627', # أينما
               '\u0625\u064A\u0647', # إيه
               '\u0628\u062E', # بخ
               '\u0628\u0633', # بس
               '\u0628\u0639\u062F', # بعد
               '\u0628\u0639\u0636', # بعض
               '\u0628\u0643', # بك
               '\u0628\u0643\u0645', # بكم
               '\u0628\u0643\u0645\u0627', # بكما
               '\u0628\u0643\u0646', # بكن
               '\u0628\u0644', # بل
               '\u0628\u0644\u0649', # بلى
               '\u0628\u0645\u0627', # بما
               '\u0628\u0645\u0627\u0630\u0627', # بماذا
               '\u0628\u0645\u0646', # بمن
               '\u0628\u0646\u0627', # بنا
               '\u0628\u0647', # به
               '\u0628\u0647\u0627', # بها
               '\u0628\u0647\u0645', # بهم
               '\u0628\u0647\u0645\u0627', # بهما
               '\u0628\u0647\u0646', # بهن
               '\u0628\u064A', # بي
               '\u0628\u064A\u0646', # بين
               '\u0628\u064A\u062F', # though بيد
               '\u062A\u0644\u0643', # تلك
               '\u062A\u0644\u0643\u0645', # تلكم
               '\u062A\u0644\u0643\u0645\u0627', # تلكما
               '\u062A\u0647', # ته
               '\u062A\u064A', # تي
               '\u062A\u064A\u0646', # تين
               '\u062A\u064A\u0646\u0643', # تينك
               '\u062B\u0645', # ثم
               '\u062B\u0645\u0629', # ثمة
               '\u062D\u0627\u0634\u0627', # حاشا
               '\u062D\u0628\u0630\u0627', # حبذا
               '\u062D\u062A\u0649', # حتى
               '\u062D\u064A\u062B', # حيث
               '\u062D\u064A\u062B\u0645\u0627', # حيثما
               '\u062D\u064A\u0646', # حين
               '\u062E\u0644\u0627', # خلا
               '\u062F\u0648\u0646', # دون
               '\u0630\u0627', # ذا
               '\u0630\u0627\u062A', # ذات
               '\u0630\u0627\u0643', # ذاك
               '\u0630\u0627\u0646', # ذان
               '\u0630\u0627\u0646\u0643', # ذانك
               '\u0630\u0644\u0643', # ذلك
               '\u0630\u0644\u0643\u0645', # ذلكم
               '\u0630\u0644\u0643\u0645\u0627', # ذلكما
               '\u0630\u0644\u0643\u0646', # ذلكن
               '\u0630\u0647', # ذه
               '\u0630\u0648', # ذو
               '\u0630\u0648\u0627', # ذوا
               '\u0630\u0648\u0627\u062A\u0627', # ذواتا
               '\u0630\u0648\u0627\u062A\u064A', # ذواتي
               '\u0630\u064A', # ذي
               '\u0630\u064A\u0646', # ذين
               '\u0630\u064A\u0646\u0643', # ذينك
               '\u0631\u064A\u062B', # ريث
               '\u0633\u0648\u0641', # سوف
               '\u0633\u0648\u0649', # except سوى
               '\u0634\u062A\u0627\u0646', # شتان
               '\u0639\u062F\u0627', # عدا
               '\u0639\u0633\u0649', # عسى
               '\u0639\u0644', # عل
               '\u0639\u0644\u0649', # على
               '\u0639\u0644\u064A\u0643', # عليك
               '\u0639\u0644\u064A\u0647', # عليه
               '\u0639\u0645\u0627', # عما
               '\u0639\u0646', # عن
               '\u0639\u0646\u062F', # عند
               '\u063A\u064A\u0631',  # except غير
               '\u0641\u0625\u0630\u0627', # فإذا
               '\u0641\u0625\u0646', # فإن
               '\u0641\u0644\u0627', # فلا
               '\u0641\u0645\u0646', # فمن
               '\u0641\u064A', # في
               '\u0641\u064A\u0645', # فيم
               '\u0641\u064A\u0645\u0627', # فيما
               '\u0641\u064A\u0647', # فيه
               '\u0641\u064A\u0647\u0627', # فيها
               '\u0642\u0628\u0644', # قبل
               '\u0642\u062F', # قد
               '\u0643\u0623\u0646', # كأن
               '\u0643\u0623\u0646\u0645\u0627', # كأنما
               '\u0643\u0623\u064A', # كأي
               '\u0643\u0623\u064A\u0646', # كأين
               '\u0643\u0630\u0627', # كذا
               '\u0643\u0630\u0644\u0643', # كذلك
               '\u0643\u0644', # كل
               '\u0643\u0644\u0627', # كلا
               '\u0643\u0644\u0627\u0647\u0645\u0627', # كلاهما
               '\u0643\u0644\u062A\u0627', # كلتا
               '\u0643\u0644\u0645\u0627', # كلما
               '\u0643\u0644\u064A\u0643\u0645\u0627', # كليكما
               '\u0643\u0644\u064A\u0647\u0645\u0627', # كليهما
               '\u0643\u0645', # كم
               '\u0643\u0645\u0627', # كما
               '\u0643\u064A', # كي
               '\u0643\u064A\u062A', # كيت
               '\u0643\u064A\u0641', # كيف
               '\u0643\u064A\u0641\u0645\u0627', # كيفما
               '\u0644\u0627', # لا
               '\u0644\u0627\u0633\u064A\u0645\u0627', # لاسيما
               '\u0644\u062F\u0649', # لدى
               '\u0644\u0633\u062A', # لست
               '\u0644\u0633\u062A\u0645', # لستم
               '\u0644\u0633\u062A\u0645\u0627', # لستما
               '\u0644\u0633\u062A\u0646', # لستن
               '\u0644\u0633\u0646', # لسن
               '\u0644\u0633\u0646\u0627', # لسنا
               '\u0644\u0639\u0644', # لعل
               '\u0644\u0643', # لك
               '\u0644\u0643\u0645', # لكم
               '\u0644\u0643\u0645\u0627', # لكما
               '\u0644\u0643\u0646', # لكن
               '\u0644\u0643\u0646\u0645\u0627', # لكنما
               '\u0644\u0643\u064A', # لكي
               '\u0644\u0643\u064A\u0644\u0627', # لكيلا
               '\u0644\u0645', # لم
               '\u0644\u0645\u0627', # لما
               '\u0644\u0646', # لن
               '\u0644\u0646\u0627', # لنا
               '\u0644\u0647', # له
               '\u0644\u0647\u0627', # لها
               '\u0644\u0647\u0645', # لهم
               '\u0644\u0647\u0645\u0627', # لهما
               '\u0644\u0647\u0646', # لهن
               '\u0644\u0648', # لو
               '\u0644\u0648\u0644\u0627', # لولا
               '\u0644\u0648\u0645\u0627', # لوما
               '\u0644\u064A', # لي
               '\u0644\u0626\u0646', # لئن
               '\u0644\u064A\u062A', # ليت
               '\u0644\u064A\u0633', # ليس
               '\u0644\u064A\u0633\u0627', # ليسا
               '\u0644\u064A\u0633\u062A', # ليست
               '\u0644\u064A\u0633\u062A\u0627', # ليستا
               '\u0644\u064A\u0633\u0648\u0627', # ليسوا
               '\u0645\u0627', # ما
               '\u0645\u0627\u0630\u0627', # ماذا
               '\u0645\u062A\u0649',  # when متى
               '\u0645\u0630', # مذ
               '\u0645\u0639', # مع
               '\u0645\u0645\u0627', # مما
               '\u0645\u0645\u0646', # ممن
               '\u0645\u0646', # من
               '\u0645\u0646\u0647', # منه
               '\u0645\u0646\u0647\u0627', # منها
               '\u0645\u0646\u0630', # منذ
               '\u0645\u0647', # مه
               '\u0645\u0647\u0645\u0627', # مهما
               '\u0646\u062D\u0646', # نحن
               '\u0646\u062D\u0648', # نحو
               '\u0646\u0639\u0645', # نعم
               '\u0647\u0627', # ها
               '\u0647\u0627\u062A\u0627\u0646', # هاتان
               '\u0647\u0627\u062A\u0647', # هاته
               '\u0647\u0627\u062A\u064A', # هاتي
               '\u0647\u0627\u062A\u064A\u0646', # هاتين
               '\u0647\u0627\u0643', # هاك
               '\u0647\u0627\u0647\u0646\u0627', # هاهنا
               '\u0647\u0630\u0627', # هذا
               '\u0647\u0630\u0627\u0646', # هذان
               '\u0647\u0630\u0647', # هذه
               '\u0647\u0630\u064A', # هذي
               '\u0647\u0630\u064A\u0646', # هذين
               '\u0647\u0643\u0630\u0627', # هكذا
               '\u0647\u0644', # هل
               '\u0647\u0644\u0627', # هلا
               '\u0647\u0645', # هم
               '\u0647\u0645\u0627', # هما
               '\u0647\u0646', # هن
               '\u0647\u0646\u0627', # هنا
               '\u0647\u0646\u0627\u0643', # هناك
               '\u0647\u0646\u0627\u0644\u0643', # هنالك
               '\u0647\u0648', # هو
               '\u0647\u0624\u0644\u0627\u0621', # هؤلاء
               '\u0647\u064A', # هي
               '\u0647\u064A\u0627', # هيا
               '\u0647\u064A\u062A', # هيت
               '\u0647\u064A\u0647\u0627\u062A', # هيهات
               '\u0648\u0627\u0644\u0630\u064A', # والذي
               '\u0648\u0627\u0644\u0630\u064A\u0646', # والذين
               '\u0648\u0625\u0630', # وإذ
               '\u0648\u0625\u0630\u0627', # وإذا
               '\u0648\u0625\u0646', # وإن
               '\u0648\u0644\u0627', # ولا
               '\u0648\u0644\u0643\u0646', # ولكن
               '\u0648\u0644\u0648', # ولو
               '\u0648\u0645\u0627', # وما
               '\u0648\u0645\u0646', # ومن
               '\u0648\u0647\u0648', # وهو
               '\u064A\u0627' # يا
             ]
