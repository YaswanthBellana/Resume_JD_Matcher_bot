from parser import extract_text_from_pdf, read_text_file
from prompts import get_match_prompt
from evaluator import evaluate_with_gemini

def main():
    resume_path = "examples/Yaswanth_Bellana_Resume.pdf"
    jd_path = "examples/job_description.txt"

    resume_text = extract_text_from_pdf(resume_path)
    jd_text = read_text_file(jd_path)

    prompt = get_match_prompt(resume_text, jd_text)
    result = evaluate_with_gemini(prompt)

    print("\n----- MATCH REPORT (Gemini) -----\n")
    print(result)

if __name__ == "__main__":
    main()
