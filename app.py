import streamlit as st
import google.generativeai as genai

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

# إعداد مفتاح الذكاء الاصطناعي في القائمة الجانبية
st.sidebar.image("https://img.icons8.com/color/96/pharmacist.png", width=80)
st.sidebar.title("PharmaAI Studio")
api_key = st.sidebar.text_input("أدخل Google Gemini API Key:", type="password")

menu = st.sidebar.selectbox(
    "اختر القسم:",
    ["🤖 محلل الأسئلة الذكي (AI Solver)", "📚 بنك الأسئلة والكويزات", "💊 دليل الأدوية السريع (Drug Ref)"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 تم تطويره لخدمة طلاب كلية صيدلة بالذكاء الاصطناعي التوليدي.")

# 1. قسم محلل الأسئلة الذكي الحقيقي
if menu == "🤖 محلل الأسئلة الذكي (AI Solver)":
    st.markdown('<p class="main-header">🔬 محلل أسئلة صيدلة بالذكاء الاصطناعي</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">اكتب أي سؤال صيدلي أو حالة إكلينيكية لتحليلها عبر الذكاء الاصطناعي الفوري.</p>', unsafe_allow_html=True)
    st.markdown("---")

    user_question = st.text_area("اكتب نص السؤال أو الحالة هنا:", height=120, placeholder="مثلاً: ما هي آلية عمل الأدوية الخافضة لضغط الدم من نوع ARBs؟")

    if st.button("تحليل السؤال بالذكاء الاصطناعي 🚀"):
        if not api_key:
            st.error("⚠️ من فضلك أدخل مفتاح الـ API الخاص بـ Gemini في القائمة الجانبية أولاً!")
        elif not user_question.strip():
            st.warning("⚠️ من فضلك اكتب السؤال أولاً!")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(
                    model_name='gemini-1.5-flash',
                    system_instruction="أنت صيدلي إكلينيكي خبير وأستاذ صيدلة. قم بتحليل أسئلة وحالات طلاب صيدلة بدقة، واشرح الإجابة بالتفصيل مع ذكر Mechanism of Action والتفاعلات الدوائية باللغة العربية."
                )
                
                with st.spinner("جاري تحليل السؤال وصياغة الشرح الإكلينيكي..."):
                    response = model.generate_content(user_question)
                
                st.success("✅ تم التحليل بنجاح بواسطة الذكاء الاصطناعي!")
                st.markdown("### 📋 نتيجة التحليل والشرح:")
                st.markdown(response.text)
                
            except Exception as e:
                st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")

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