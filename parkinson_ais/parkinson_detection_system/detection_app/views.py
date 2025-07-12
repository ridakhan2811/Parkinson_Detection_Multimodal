# detection_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate # Import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms # Import forms to define custom widgets
from django.contrib import messages # Import the messages framework

# Define custom forms for styling
class CustomAuthenticationForm(AuthenticationForm):
    """
    Custom form for user login to apply specific styling.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your username or email', # Updated placeholder
            'class': 'input-field' # Use 'input-field' as per your HTML
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter your password',
            'class': 'input-field' # Use 'input-field' as per your HTML
        })
    )

class CustomUserCreationForm(UserCreationForm):
    """
    Custom form for user registration to apply specific styling.
    """
    class Meta(UserCreationForm.Meta):
        model = UserCreationForm.Meta.model
        fields = ('username',) + UserCreationForm.Meta.fields[1:]
        # Define widgets directly in Meta to ensure they are initialized correctly
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'input-field'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Enter your password',
                'class': 'input-field'
            }),
            'password2': forms.PasswordInput(attrs={
                'placeholder': 'Confirm your password',
                'class': 'input-field'
            }),
        }


def home(request):
    """
    Renders the landing page (index.html) of the Parkinson's Detection System.
    The request.user object is automatically available in templates if
    'django.contrib.auth.context_processors.auth' is in TEMPLATES['OPTIONS']['context_processors']
    in settings.py, which it is by default.
    """
    return render(request, 'index.html')

def quiz(request):
    """
    Renders the placeholder page for the Parkinson's Detection Quiz.
    This is where the actual quiz logic would be implemented.
    """
    return render(request, 'quiz.html')

def results(request):
    """
    Renders the results page, displaying symptoms based on quiz answers and analysis findings.
    """
    # Get all data from query parameters (quiz answers + analysis results)
    all_data = request.GET.dict()

    # --- Process Quiz-based Symptoms ---
    symptom_map = {
        'tremor': "Tremors (shaking, especially at rest)",
        'bradykinesia': "Slowness of movement (bradykinesia)",
        'rigidity': "Stiffness or rigidity in limbs/trunk",
        'postural_instability': "Problems with balance or increased tendency to fall",
        'gait_changes': "Changes in walking (shuffling, reduced arm swing)",
        'stooped_posture': "Stooped or leaning forward posture",
        'facial_masking': "Less animated or 'mask-like' facial expression",
        'arm_swing_reduction': "Reduced arm swing when walking",
        'handwriting_changes_general': "General changes in handwriting (less clear/difficult to read)",
        'micrographia_detailed': "Handwriting becoming progressively smaller (micrographia)",
        'finger_tapping': "Difficulty with rapid, repetitive movements with fingers",
        'buttoning_difficulty': "Difficulty with fine motor tasks (buttoning, tying laces)",
        'speech_changes': "Softer, hoarser, or more monotone voice (dysphonia)",
        'smell_loss': "Loss or reduction in sense of smell (anosmia)",
        'sleep_disorder': "Vivid dreams that cause you to act out physically during sleep (e.g., kicking, punching, shouting)",
        'daytime_sleepiness': "Excessive daytime sleepiness",
        'vision_changes': "Changes in vision (double vision, difficulty reading)",
        'constipation': "Frequent constipation",
        'mood_changes': "Persistent feelings of depression, anxiety, or apathy",
        'memory_issues': "Problems with memory, attention, or decision-making",
        'dizziness': "Dizziness or lightheadedness, especially when standing up",
        'other_symptoms': "Other reported symptoms" # Added for the 'other_symptoms' textarea
    }

    quiz_identified_symptoms = []
    for key, description in symptom_map.items():
        if all_data.get(key) == 'yes':
            quiz_identified_symptoms.append(description)
            # Add details if available
            detail_key = f"{key}_details"
            if all_data.get(detail_key) and all_data.get(detail_key).strip():
                quiz_identified_symptoms.append(f"  - Details: {all_data.get(detail_key)}")
        elif key == 'other_symptoms' and all_data.get(key) and all_data.get(key).strip():
            quiz_identified_symptoms.append(f"Other reported symptoms: {all_data.get(key)}")


    # --- Process Analysis Findings (Simulated) ---
    analysis_findings = []
    # Check for specific analysis findings and add them
    if all_data.get('analysis_speech_tremor') == 'detected':
        analysis_findings.append("Speech Tremor Detected (from voice analysis)")
    if all_data.get('analysis_spiral_irregularity') == 'moderate':
        analysis_findings.append("Moderate Irregularity in Spiral Drawing (from spiral analysis)")
    if all_data.get('analysis_spiral_irregularity') == 'severe':
        analysis_findings.append("Severe Irregularity in Spiral Drawing (from spiral analysis)")
    if all_data.get('analysis_gait_instability') == 'mild':
        analysis_findings.append("Mild Gait Instability Detected (from posture video)")
    if all_data.get('analysis_gait_instability') == 'moderate':
        analysis_findings.append("Moderate Gait Instability Detected (from posture video)")
    if all_data.get('analysis_facial_masking') == 'subtle':
        analysis_findings.append("Subtle Facial Masking Indicated (from posture video)")
    if all_data.get('analysis_facial_masking') == 'pronounced':
        analysis_findings.append("Pronounced Facial Masking Indicated (from posture video)")
    if all_data.get('analysis_handwriting_micrographia') == 'present':
        analysis_findings.append("Micrographia Present (from handwriting analysis)")

    overall_score = int(all_data.get('analysis_overall_score', 0)) # Get analysis score

    # Combine all symptoms for overall assessment (using a set to ensure uniqueness)
    all_symptoms = list(set(quiz_identified_symptoms + analysis_findings))
    all_symptoms.sort() # Sort for consistent display

    # --- Determine Potential Indication Level and Consultation Advice ---
    num_total_indications = len(all_symptoms)
    
    consultation_advice = {
        'level': "No significant indications",
        'stage_description': "Based on the assessment, there are no significant indications of Parkinson's-like symptoms. However, if you have persistent health concerns, it's always best to consult a healthcare professional.",
        'doctor_type': "Primary Care Physician",
        'next_steps': [
            "Maintain a healthy lifestyle.",
            "Monitor any new or worsening symptoms.",
            "Discuss any general health concerns with your primary care physician during your next routine check-up."
        ]
    }

    if overall_score >= 80 or num_total_indications >= 8:
        consultation_advice['level'] = "High Indication - Urgent Consultation Recommended"
        consultation_advice['stage_description'] = "The assessment indicates a high number of symptoms and markers consistent with Parkinson's disease. **Immediate consultation with a Neurologist specializing in Movement Disorders is strongly recommended.**"
        consultation_advice['doctor_type'] = "Neurologist (Movement Disorders Specialist)"
        consultation_advice['next_steps'] = [
            "Schedule an urgent appointment with a Movement Disorders Specialist.",
            "Prepare a detailed history of all symptoms, their onset, and progression. Include any family history.",
            "Be ready to discuss medications you are currently taking.",
            "Consider bringing a family member or close friend to the appointment for additional observations and support."
        ]
    elif overall_score >= 60 or num_total_indications >= 5:
        consultation_advice['level'] = "Moderate Indication - Specialist Consultation Advised"
        consultation_advice['stage_description'] = "The assessment shows a moderate number of symptoms and markers that warrant further investigation. **Consultation with a Neurologist is highly advised for a comprehensive evaluation.**"
        consultation_advice['doctor_type'] = "Neurologist"
        consultation_advice['next_steps'] = [
            "Make an appointment with a Neurologist.",
            "Document all your symptoms, including when they started and how they affect your daily life.",
            "Discuss the results of this assessment with your doctor.",
            "Follow any recommendations for further tests or evaluations."
        ]
    elif overall_score >= 40 or num_total_indications >= 2:
        consultation_advice['level'] = "Mild Indication - Discuss with Primary Care"
        consultation_advice['stage_description'] = "A few symptoms or markers were noted. While not strongly indicative of Parkinson's, it's advisable to discuss these findings with your primary care physician for initial guidance and monitoring."
        consultation_advice['doctor_type'] = "Primary Care Physician"
        consultation_advice['next_steps'] = [
            "Schedule an appointment with your primary care physician.",
            "Share the results of this assessment and your concerns.",
            "Your doctor may recommend monitoring, lifestyle changes, or a referral to a specialist if symptoms persist or worsen."
        ]

    # Placeholder for "kind of Parkinson's" - emphasize it's not a diagnosis
    kind_of_parkinsons = "Determining the specific type of Parkinson's disease or related conditions requires extensive medical evaluation, including neurological examinations and potentially imaging. This assessment provides a *preliminary indication only* and is not a diagnosis."
    if overall_score >= 70 and 'tremor' in all_data and all_data.get('tremor') == 'yes':
        kind_of_parkinsons += "\n\nBased on prominent tremor, the doctor might consider Tremor-Dominant Parkinson's Disease, but this needs professional confirmation."
    elif overall_score >= 70 and 'bradykinesia' in all_data and all_data.get('bradykinesia') == 'yes' and 'rigidity' in all_data and all_data.get('rigidity') == 'yes':
        kind_of_parkinsons += "\n\nBased on significant slowness and stiffness, the doctor might consider Postural Instability and Gait Difficulty (PIGD) dominant Parkinson's Disease, but this needs professional confirmation."


    context = {
        'quiz_identified_symptoms': quiz_identified_symptoms,
        'analysis_findings': analysis_findings,
        'all_symptoms': all_symptoms, # Combined list for display
        'potential_stage': consultation_advice['level'], # Renamed for clarity in template
        'stage_description': consultation_advice['stage_description'],
        'doctor_type': consultation_advice['doctor_type'],
        'next_steps_advice': consultation_advice['next_steps'],
        'kind_of_parkinsons': kind_of_parkinsons,
        'overall_score': overall_score,
        'quiz_data': all_data # For debugging or displaying raw data if needed
    }
    return render(request, 'results.html', context)

def upload_assessment(request):
    """
    Renders the page for uploading handwriting, speech, and posture files.
    """
    quiz_data = request.GET.dict()
    context = {
        'quiz_data': quiz_data
    }
    return render(request, 'upload_assessment.html', context)

def thank_you(request):
    """
    Renders the thank you page after quiz completion.
    """
    return render(request, 'thank_you.html')

def register_view(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log the user in immediately after registration
            messages.success(request, 'Account created successfully! Welcome to ParkPredict.')
            return redirect('home') # Redirect to home page after successful registration
        else:
            # Display form errors to the user
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) # This sets the user in the session
                messages.success(request, f'Login successful! Welcome back, {user.username}.')
                return redirect('home') # Redirects to the URL named 'home' (which is '/')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request) # This clears the user from the session
    messages.info(request, 'You have been logged out.')
    return redirect('home') # Redirects to the URL named 'home' (which is '/')

def logout_view(request):
    """
    Handles user logout.
    """
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home') # Redirect to home page after logout

def demo_video_view(request):
    """
    Renders the page to display the YouTube demo video.
    """
    return render(request, 'demo_video.html')
