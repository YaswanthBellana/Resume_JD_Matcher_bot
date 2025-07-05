def get_match_prompt(resume_text, jd_text):
    return f"""
You are a professional recruiter AI.

Given the following candidate resume and job description:

=== Resume ===
{resume_text}

=== Job Description ===
{jd_text}

Your task is to:
- Give a match score (0–10) based on how well the resume fits the job.
- Justify the score briefly.
- Suggest 3 improvements to make the resume a better fit.

Respond only in this format:

Match Score: <score>/10
Justification: <text>
Suggestions:
1. <tip>
2. <tip>
3. <tip>
"""
