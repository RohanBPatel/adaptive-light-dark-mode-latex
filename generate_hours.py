import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

template_script = Path("template.tex")
out_path = Path("hourly_pdfs")
out_path.mkdir(exist_ok=True)

def compile_pdf(hour):
    job_name = f"Hour_{hour:02d}"

    # injects hour via command line to override \currenthour
    cmd = [
        "pdflatex",
        f"-jobname={job_name}",
        f"\\def\\currenthour{{{hour}}}\\input{{{template_script}}}"
    ]
    
    print(f"Compiling: {job_name}")
    subprocess.run(cmd, stdout=subprocess.DEVNULL)

    # move PDF
    pdf_file = Path(f"{job_name}.pdf")
    if pdf_file.exists():
        pdf_file.replace(out_path / pdf_file.name)
    
    # clean up
    for ext in [".aux", ".log", ".out"]:
        Path(f"{job_name}{ext}").unlink(missing_ok=True)

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        executor.map(compile_pdf, range(24))