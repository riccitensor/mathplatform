from openai import OpenAI

import subprocess
import tempfile
import os
import argparse

client = OpenAI()
# Configure OpenAI API key

OpenAI.api_key = os.getenv('OPENAI_API_KEY')


def generate_proof(prompt, prover='lean', llm = "openai"):
    """
    Generate mathematical insights.
    """
    if prover not in ['lean', 'prover9', 'mace4']:
        raise ValueError("Unsupported prover. Choose from 'lean', 'prover9', 'mace4'.")
    
    full_prompt = f"Translate the following mathematical statement into {prover.upper()} syntax and provide a proof.\n\n{prompt}"
    
    if llm not in ['openai']:
      raise ValueError("Unsupported prover. Choose from 'openai'.")

    response = client.completions.create(
      model="gpt-3.5-turbo-instruct",
      prompt=prompt,
      max_tokens=7,
      temperature=0
    )
        
    return response.choices[0].text

def verify_with_lean(lean_code):
    """
    Verify Lean code using the Lean prover.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.lean', delete=False) as tmp_file:
        tmp_file.write(lean_code)
        tmp_filename = tmp_file.name
    
    try:
        result = subprocess.run(['lean', tmp_filename], capture_output=True, text=True, check=True)
        os.unlink(tmp_filename)  # Clean up the temporary file
        return "Lean verification successful."
    except subprocess.CalledProcessError as e:
        os.unlink(tmp_filename)
        return f"Lean verification failed:\n{e.stderr}"

def verify_with_prover9(prover9_code):
    """
    Verify Prover9 code using the Prover9 theorem prover.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.p', delete=False) as tmp_file:
        tmp_file.write(prover9_code)
        tmp_filename = tmp_file.name
    
    try:
        result = subprocess.run(['prover9', '-f', tmp_filename], capture_output=True, text=True, check=True)
        os.unlink(tmp_filename)
        return "Prover9 verification successful. Proof found."
    except subprocess.CalledProcessError as e:
        os.unlink(tmp_filename)
        return f"Prover9 verification failed:\n{e.stderr}"

def verify_with_mace4(mace4_code):
    """
    Verify or find models using Mace4.
    """
    with tempfile.NamedTemporaryFile(mode='w', suffix='.p', delete=False) as tmp_file:
        tmp_file.write(mace4_code)
        tmp_filename = tmp_file.name
    
    try:
        result = subprocess.run(['mace4', tmp_filename], capture_output=True, text=True, check=True)
        os.unlink(tmp_filename)
        if "Found 1 models." in result.stdout:
            return f"Mace4 found a model:\n{result.stdout}"
        else:
            return "Mace4 did not find any models."
    except subprocess.CalledProcessError as e:
        os.unlink(tmp_filename)
        return f"Mace4 verification failed:\n{e.stderr}"

def main():
    # Get the task as a command line argument
    parser = argparse.ArgumentParser(description='Process the theorem task.')
    parser.add_argument('task', type=str, nargs='+', help='The theorem task to be processed.')
    args = parser.parse_args()
    task = ' '.join(args.task)

    print ("Task: " + task)

    # Generate Lean proof
    lean_code = generate_proof(task, prover='lean')
    
    lean_result = verify_with_lean(task)
    print("\nLean Verification Result:\n", lean_result)

    # Generate Prover9 proof
    # prover9_code = generate_proof(theorem_description, prover='prover9')
    # print("\nGenerated Prover9 Code:\n", prover9_code)
    # prover9_result = verify_with_prover9(prover9_code)
    # print("\nProver9 Verification Result:\n", prover9_result)

    # Generate Mace4 model
    # mace4_code = generate_proof(theorem_description, prover='mace4')
    # print("\nGenerated Mace4 Code:\n", mace4_code)
    # mace4_result = verify_with_mace4(mace4_code)
    # print("\nMace4 Verification Result:\n", mace4_result)

if __name__ == "__main__":
        main()
