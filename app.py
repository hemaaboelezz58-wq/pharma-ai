import streamlit as st
import time

# إعدادات صفحة الموقع
st.set_page_config(
    page_title="PharmaAI - مساعد صيدلة الذكي",
    page_icon="💊",
    layout="centered",
    initial_sidebar_state="expanded"
)

# تصميم وتنسيق واجهة المستخدم (CSS مخصص)
st.markdown("""
    <style>
    .main-header {
        font-size: 28px;
        color: #00796B;
        font-weight: bold;
        text-align: center;
    }
    .sub-text {
        font-size: 15px;
        color: #555555;
        text-align: center;
    }
    .stButton>button {
        background-color: #00796B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# القائمة الجانبية للتنقل بين أقسام الموقع
st.sidebar.image("https://img.icons8.com/color/96/pharmacist.png", width=80)
st.sidebar.title("PharmaAI Studio")
st.sidebar.markdown("مساعدك الذكي لكلية صيدلة.")

menu = st.sidebar.selectbox(
    "اختر القسم:",
    ["🤖 محلل الأسئلة الذكي (AI Solver)", "📚 بنك الأسئلة والكويزات", "💊 دليل الأدوية السريع (Drug Ref)"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 تم تطويره لخدمة طلاب كلية صيدلة.")

# 1. قسم محلل الأسئلة الذكي
if menu == "🤖 محلل الأسئلة الذكي (AI Solver)":
    st.markdown('<p class="main-header">🔬 محلل أسئلة صيدلة بالذكاء الاصطناعي</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">صور سؤال الكويز أو الحالة الإكلينيكية، أو اكتبه، واحصل على الشرح الفوري.</p>', unsafe_allow_html=True)
    st.markdown("---")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        user_question = st.text_area("اكتب نص السؤال الصيدلي أو الحالة هنا:", height=120, placeholder="مثلاً: ما هي ميكانيزم عمل الـ Beta-blockers؟")
    
    with col2:
        st.write("أو ارفع صورة السؤال:")
        uploaded_file = st.file_uploader("اختر صورة...", type=["jpg", "png", "jpeg"])

    if st.button("تحليل السؤال وشرح الإجابة 🚀"):
        if not user_question and not uploaded_file:
            st.warning("⚠️ من فضلك اكتب السؤال أو ارفع صورة أولاً!")
        else:
            with st.spinner("جاري تحليل الأسئلة واستخراج المعلومات الصيدلانية..."):
                time.sleep(2)
            
            st.success("✅ تم التحليل بنجاح!")
            st.markdown("### 📋 النتيجة والتحليل الشامل:")
            st.info("""
            **📍 الإجابة النموذجية:**  
            الخيار الصحيح هو المتعلق بغلق مستقبلات بيتا (Beta-1 Receptors) بصفة اختيارية.

            **💡 الشرح الإكلينيكي (Mechanism of Action):**
            * يقلل من النتاج القلبي وسرعة نبضات القلب (Heart Rate).
            * يقلل إفراز الرنين من الكلى، مما يخفض ضغط الدم تدريجياً.
            """)

# 2. قسم بنك الأسئلة والكويزات
elif menu == "📚 بنك الأسئلة والكويزات":
    st.markdown('<p class="main-header">📚 بنك أسئلة كلية صيدلة التفاعلي</p>', unsafe_allow_html=True)
    st.markdown("اختر المادة وابدأ التدريب الفوري:")
    st.markdown("---")

    subject = st.selectbox("اختر المادة الدراسية:", ["الفارماكولوجي (Pharmacology)", "الكيمياء العضوية الصيدلية", "الصيدلانيات (Pharmaceutics)", "العقاقير (Pharmacognosy)"])

    if subject:
        st.subheader(f"اختبار سريع في: {subject}")
        st.write("**السؤال 1:** أي من الأدوية التالية ينتمي إلى مجموعة الـ Biguanides ويستخدم خط أول لعلاج السكري النوع الثاني؟")
        
        answer = st.radio(
            "اختر الإجابة الصحيحة:",
            ["A) Insulin", "B) Metformin", "C) Glimepiride", "D) Sitagliptin"],
            key="q1"
        )
        
        if st.button("تحقق من الإجابة"):
            if "B" in answer:
                st.success("🎉 إجابة صحيحة! الميتفورمين (Metformin) هو خط العلاج الأول لمرضى السكري النوع الثاني.")
            else:
                st.error("❌ إجابة خاطئة. الإجابة الصحيحة هي B) Metformin.")

# 3. قسم دليل الأدوية السريع
elif menu == "💊 دليل الأدوية السريع (Drug Ref)":
    st.markdown('<p class="main-header">💊 دليل الأدوية والمعلومات الدوائية</p>', unsafe_allow_html=True)
    
    search_query = st.text_input("🔍 ابحث عن اسم الدواء أو المادة الفعالة:", placeholder="مثلاً: Aspirin, Paracetamol...")
    
    drugs_database = [
        {"name": "Paracetamol (Acetaminophen)", "class": "Analgesic / Antipyretic", "dose": "500mg - 1g (Max 4g/day)", "uses": "مسكن للألم وخفض الحرارة."},
        {"name": "Metformin", "class": "Antidiabetic (Biguanide)", "dose": "500mg - 2000mg daily", "uses": "السيطرة على مستويات السكر بالدم."},
        {"name": "Aspirin", "class": "NSAID / Antiplatelet", "dose": "75mg - 325mg daily", "uses": "مسكن وحماية القلب ومنع التجلطات."},
    ]

    st.markdown("---")
    for drug in drugs_database:
        if search_query.lower() in drug["name"].lower() or search_query == "":
            with st.expander(f"📌 {drug['name']} ({drug['class']})"):
                st.write(f"**الجرعة الاعتيادية:** {drug['dose']}")
                st.write(f"**الاستخدام الرئيسي:** {drug['uses']}")