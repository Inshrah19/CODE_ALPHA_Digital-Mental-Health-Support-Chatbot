import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk
from tkinter import scrolledtext

# Download NLTK tokenizer model once
nltk.download('punkt')

# Define the FAQs dictionary with proper string values
faqs = {
    "What services do you offer?": "We offer virtual therapy sessions, self-help resources, and mental health assessments.",
    "How do I schedule a session?": "You can schedule a session through our app or website by selecting your preferred therapist and time.",
    "Is my information confidential?": "Yes, we prioritize your privacy and confidentiality. All information is securely stored and encrypted.",
    "What should I expect during my first session?": "During your first session, your therapist will discuss your goals and concerns to create a personalized plan.",
    "Do you accept insurance?": "We accept various insurance plans. Please check our website for a list of accepted providers.",
    "How can I contact customer support?": "You can reach our customer support team via email or through the chat feature on our website.",
    "What are the qualifications of your therapists?": "Our therapists are licensed professionals with experience in various mental health fields.",
    "Can I change my therapist?": "Yes, you can request a different therapist at any time through your account settings.",
    "What if I need to cancel or reschedule my appointment?": "You can cancel or reschedule your appointment through the app or website up to 24 hours in advance.",
    "Are your services available in multiple languages?": "Yes, we offer services in several languages. Please check our website for details.",
    "How do I pay for my sessions?": "Payments can be made through credit card, PayPal, or insurance, depending on your plan.",
    "What if I am in crisis?": "If you are in crisis, please contact emergency services or a crisis hotline immediately.",
    "Do you offer group therapy sessions?": "Yes, we offer group therapy sessions on various topics. Check our website for schedules.",
    "How do I access self-help resources?": "Self-help resources are available in the app under the 'Resources' section.",
    "Can I have therapy sessions with my partner or family?": "Yes, we offer couples and family therapy sessions. Please specify when scheduling.",
    "What is the duration of each therapy session?": "Each session typically lasts 50 minutes.",
    "How often should I attend therapy?": "The frequency of sessions depends on your individual needs and goals, which can be discussed with your therapist.",
    "Is there a minimum age requirement for therapy?": "Yes, we provide services for individuals aged 13 and above. Parental consent is required for minors.",
    "What types of therapy do you offer?": "We offer cognitive-behavioral therapy (CBT), mindfulness-based therapy, and more.",
    "Can I access my session recordings?": "Session recordings are not available for privacy reasons, but you can take notes during your sessions.",
    "What if I forget my appointment?": "You will receive reminders via email and/or SMS before your appointment.",
    "How do I provide feedback about my therapist?": "You can provide feedback through the app after each session.",
    "Are there any hidden fees?": "No, all fees are clearly outlined during the scheduling process.",
    "What if I have a technical issue during my session?": "If you experience technical issues, please contact customer support for assistance.",
    "Can I use the service on my mobile device?": "Yes, our platform is accessible via both desktop and mobile devices.",
    "What if I don’t feel comfortable with my therapist?": "You can request a different therapist at any time if you feel uncomfortable.",
    "Do you offer therapy for specific conditions?": "Yes, we provide therapy for anxiety, depression, PTSD, and more.",
    "How do I know if therapy is right for me?": "If you are experiencing emotional distress or mental health challenges, therapy can be beneficial. Consult with a professional for guidance.",
    "What is your cancellation policy?": "You can cancel or reschedule appointments up to 24 hours in advance without a fee.",
    "Do you offer any free resources?": "Yes, we provide free articles, videos, and self-help tools on our website.",
    "How do I update my personal information?": "You can update your personal information in your account settings on the app or website.",
    "What if I need support outside of business hours?": "Our customer support team is available during business hours. For urgent matters, please contact a crisis hotline.",
    "Can I access therapy from anywhere?": "Yes, as long as you have a stable internet connection, you can access therapy from anywhere.",
    "What if I have a disability?": "We strive to accommodate individuals with disabilities. Please contact us for specific needs.",
    "How do I know if my therapist is a good fit?": "You can assess the fit during your initial sessions and provide feedback to your therapist.",
    "What if I want to take a break from therapy?": "You can pause your sessions at any time and resume when you feel ready.",
    "Do you offer any workshops or webinars?": "Yes, we regularly host workshops and webinars on various mental health topics. Check our website for upcoming events.",
    "How do I access my therapy notes?": "Therapy notes are not shared for privacy reasons, but you can discuss key points with your therapist.",
    "What if I have a question that isn’t answered here?": "Feel free to contact our customer support team for any additional questions.",
    "Can I refer a friend to your services?": "Yes, we encourage referrals! You can share our website link with your friends.",
    "What is the process for becoming a therapist with your platform?": "Interested therapists can apply through our website, and they must meet our qualification criteria.",
    "Do you offer therapy for children?": "We provide services for adolescents aged 13 and above. For younger children, please contact us for recommendations.",
    "How do I know if my therapist is licensed?": "All our therapists are licensed professionals. You can view their credentials on their profiles.",
    "What if I have a language barrier?": "We offer services in multiple languages. Please check our website for available languages.",
    "Can I use my health savings account (HSA) for therapy?": "Yes, many clients use their HSA for therapy sessions. Please check with your HSA provider for details.",
    "How do I handle a medical emergency?": "In case of a medical emergency, please call emergency services immediately.",
    "How do I reset my password?": "You can reset your password by clicking the 'Forgot Password' link on the login page.",
    "What if I want to provide a testimonial?": "We appreciate testimonials! You can submit yours through our website or contact customer support.",
    "Do you offer therapy for couples?": "Yes, we provide couples therapy sessions. Please specify when scheduling.",
    "How do I know if my therapist is experienced in my specific issue?": "You can view your therapist's profile, which includes their areas of expertise and experience.",
    "What if I want to change my appointment time?": "You can change your appointment time through the app or website, subject to availability.",
    "Do you offer any discounts for students?": "Yes, we offer discounts for students. Please check our website for details.",
    "What if I have a question about billing?": "For billing inquiries, please contact our customer support team for assistance.",
    "Can I have therapy sessions with multiple therapists?": "Yes, you can schedule sessions with different therapists if you prefer.",
    "What if I want to discontinue therapy?": "You can discontinue therapy at any time. We recommend discussing your decision with your therapist.",
    "How do I stay motivated during therapy?": "Staying motivated can be challenging. Your therapist can provide strategies and support to help you stay on track.",
    "What types of mental health issues do you specialize in?": "We specialize in a range of mental health issues, including anxiety, depression, stress management, and relationship challenges.",
    "How do I know if I need therapy?": "If you are experiencing persistent feelings of sadness, anxiety, or stress or if you are struggling with daily life, therapy may be beneficial.",
    "Can I have a trial session before committing?": "Yes, we offer a trial session for new clients to help you determine if our services are a good fit.",
    "What if I miss my appointment?": "If you miss your appointment, please contact customer support to reschedule. Our cancellation policy applies.",
    "Are your therapists available for emergency consultations?": "Our therapists are not available for emergency consultations. Please contact emergency services or a crisis hotline for immediate help.",
    "How do I prepare for my first therapy session?": "It can be helpful to think about your goals for therapy and any specific issues you want to discuss.",
    "What if I feel uncomfortable discussing certain topics?": "You can take your time to discuss topics at your own pace. Your therapist will create a safe space for you.",
    "Do you offer therapy for LGBTQ+ individuals?": "Yes, we are inclusive and provide therapy services tailored to the needs of LGBTQ+ individuals.",
    "How do I know if my therapist is a good match for my needs?": "You can assess the fit during your initial sessions and provide feedback to your therapist.",
    "What if I want to switch therapists after a few sessions?": "You can request to switch therapists at any time if you feel it’s necessary.",
    "Do you provide therapy for addiction issues?": "Yes, we offer therapy for individuals struggling with addiction and substance abuse.",
    "How do I handle feelings of stigma around seeking therapy?": "It’s important to remember that seeking help is a sign of strength. Many people benefit from therapy.",
    "What if I have a specific cultural background?": "Our therapists are trained to be culturally sensitive and can accommodate various cultural backgrounds.",
    "Can I have therapy sessions while traveling?": "Yes, as long as you have a stable internet connection, you can attend sessions while traveling.",
    "What if I don’t see progress in therapy?": "It’s important to communicate with your therapist about your concerns. They can adjust your treatment plan as needed.",
    "Do you offer any resources for parents?": "Yes, we provide resources and support for parents dealing with children’s mental health issues.",
    "How do I know if therapy is working for me?": "You can assess your progress by discussing your feelings and experiences with your therapist regularly.",
    "What if I have a medical condition that affects my therapy?": "Please inform your therapist about any medical conditions so they can tailor your treatment accordingly.",
    "Do you offer therapy for trauma survivors?": "Yes, we specialize in trauma-informed care and provide therapy for trauma survivors.",
    "How do I find the right therapist for my needs?": "You can browse therapist profiles on our platform to find someone who specializes in your area of concern.",
    "What if I have a busy schedule?": "We offer flexible scheduling options to accommodate your busy lifestyle.",
    "Can I attend therapy sessions with a friend?": "Yes, you can attend sessions with a friend or family member if you both agree to it.",
    "What if I want to discuss sensitive topics?": "Your therapist will create a safe and confidential environment for you to discuss sensitive topics.",
    "Do you offer any online support groups?": "Yes, we offer online support groups for various mental health issues. Check our website for schedules.",
    "How do I know if I need medication?": "Your therapist can help assess whether medication may be beneficial for your situation.",
}

def find_best_match(user_question):
    all_questions = list(faqs.keys()) + [user_question]
    vectorizer = TfidfVectorizer().fit_transform(all_questions)
    vectors = vectorizer.toarray()
    cosine_sim = cosine_similarity(vectors)
    best_match_index = cosine_sim[-1][:-1].argmax()
    return list(faqs.keys())[best_match_index]

class ChatbotUI:
    def __init__(self, root):
        self.root = root
        root.title("Digital Mental Health Chatbot")

        # Chat display window (scrollable)
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', width=80, height=20, font=("Arial", 12))
        self.chat_area.pack(padx=10, pady=10)

        # Entry box for user input
        self.entry_box = tk.Entry(root, width=80, font=("Arial", 12))
        self.entry_box.pack(padx=10, pady=(0,10))
        self.entry_box.bind("<Return>", self.send_message)  # Bind Enter key to send message

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

        self.display_message("Chatbot: Welcome to the Digital Mental Health Support Chatbot! Type your question below or type 'exit' to quit.")

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + "\n\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(tk.END)

    def send_message(self, event=None):
        user_message = self.entry_box.get().strip()
        if not user_message:
            return

        self.display_message("You: " + user_message)
        self.entry_box.delete(0, tk.END)

        if user_message.lower() == 'exit':
            self.display_message("Chatbot: Goodbye!")
            self.root.after(1000, self.root.destroy)  # Close window after 1 second
            return

        best_match = find_best_match(user_message)
        answer = faqs[best_match]
        self.display_message("Chatbot: " + answer)

if __name__ == "__main__":
    root = tk.Tk()
    chatbot_ui = ChatbotUI(root)
    root.mainloop()