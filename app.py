import streamlit as st
import google.generativeai as genai

# إعداد صفحة الموقع
st.set_page_config(
    page_title="PharmaAI - المساعد السريع",
    page_icon="💊",
    layout="centered"
)

st.title("💊 PharmaAI - مساعد صيدلي فوري")
st.write("اكتب أي سؤال صيدلي أو كيميائي، وهطلع لك الإجابة فوراً!")

# إدخال مفتاح الـ API في الشريط الجانبي
with st.sidebar:
    st.header("إعدادات الاتصال")
    api_key = st.text_input("أدخل Google Gemini API Key:", type="password")
    st.markdown("---")
    st.info("💡 المفتاح مجاني من Google AI Studio.")

if not api_key:
    st.warning("⚠️ يرجى إدخال مفتاح الـ API في القائمة الجانبية أولاً.")
else:
    genai.configure(api_key=api_key)
    
    # استخدام النموذج السريع والمستقر
    model = genai.GenerativeModel('gemini-1.5-flash')

    # صندوق الإدخال المباشر للسرعة
    user_query = st.text_area("اكتب سؤالك هنا:", placeholder="مثلاً: ايه هو استركشر الهكسان؟ أو تفاعلات الأدوية...")

    if st.button("إرسال السؤال 🚀"):
        if not user_query.strip():
            st.warning("⚠️ من فضلك اكتب سؤالاً أولاً!")
        else:
            with st.spinner("جاري جلب الإجابة فوراً..."):
                try:
                    prompt = f"أنت صيدلي خبير وأستاذ كيمياء وعليوم صيدلية. أجب بدقة واختصار ووضوح باللغة العربية على السؤال التالي:\n\n{user_query}"
                    response = model.generate_content(prompt)
                    
                    st.success("✅ الإجابة:")
                    st.markdown(response.text)
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")