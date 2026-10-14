import streamlit as st
import google.generativeai as genai

# إعداد صفحة الموقع
st.set_page_config(
    page_title="PharmaAI Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 PharmaAI - مساعد صيدلي ذكي")
st.write("اسألني عن أي مادة، أدوية، تفاعلات دوائية، أو حالات إكلينيكية، وهرد عليك فوراً!")

# إدخال مفتاح الـ API في الشريط الجانبي
with st.sidebar:
    st.header("إعدادات الاتصال")
    api_key = st.text_input("أدخل Google Gemini API Key:", type="password")
    st.markdown("---")
    st.info("💡 احصل على المفتاح مجاناً من Google AI Studio.")
    if st.button("مسح المحادثة"):
        st.session_state.messages = []
        st.rerun()

if not api_key:
    st.warning("⚠️ يرجى إدخال مفتاح الـ API في القائمة الجانبية لبدء المحادثة.")
else:
    genai.configure(api_key=api_key)
    
    # تهيئة نموذج الشات المستقر
    model = genai.GenerativeModel('gemini-pro')
    
    # تخزين رسائل المحادثة
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "model", "parts": ["أهلاً بك يا دكتور! أنا مساعدك الذكي المتخصص في علوم الصيدلة. كيف يمكنني مساعدتك اليوم؟"]}
        ]

    # عرض سجل المحادثة
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["parts"][0])

    # استقبال سؤال المستخدم
    if user_input := st.chat_input("اكتب سؤالك هنا..."):
        # إضافة سؤال المستخدم للسجل
        st.session_state.messages.append({"role": "user", "parts": [user_input]})
        with st.chat_message("user"):
            st.markdown(user_input)

        # توليد رد الذكاء الاصطناعي
        with st.chat_message("model"):
            with st.spinner("جاري التفكير والصياغة..."):
                try:
                    # تجهيز سياق صيدلي للمساعد
                    chat_history = [
                        {"role": m["role"], "parts": m["parts"]} 
                        for m in st.session_state.messages[:-1]
                    ]
                    chat = model.start_chat(history=chat_history)
                    
                    prompt = f"باعتبارك صيدلي إكلينيكي خبير، أجب بدقة واحترافية باللغة العربية على التالي: {user_input}"
                    response = chat.send_message(prompt)
                    
                    bot_reply = response.text
                    st.markdown(bot_reply)
                    
                    # حفظ رد المساعد في السجل
                    st.session_state.messages.append({"role": "model", "parts": [bot_reply]})
                except Exception as e:
                    st.error(f"حدث خطأ أثناء الاتصال: {e}")