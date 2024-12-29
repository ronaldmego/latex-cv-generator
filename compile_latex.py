# compile_latex.py
import os
import subprocess

def compile_latex():
    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the path to your LaTeX file relative to the script location
    latex_file_path = os.path.join(script_dir, 'cv.tex')
    
    # Check if the LaTeX file exists
    if not os.path.exists(latex_file_path):
        print(f"Error: LaTeX file not found at {latex_file_path}")
        return
    
    # Change the working directory to the script location
    os.chdir(script_dir)
    
    # Compile the LaTeX file to PDF
    try:
        subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", latex_file_path], 
            check=True,
            capture_output=True,
            text=True
        )
        print("PDF generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the PDF: {e}")
        print("\nError output:")
        print(e.output)
    except FileNotFoundError:
        print("Error: pdflatex command not found. Please ensure LaTeX is installed and in your system PATH.")

if __name__ == "__main__":
    compile_latex()