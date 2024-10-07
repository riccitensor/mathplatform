# Math Platform

**Math Platform** is a AI-powered tool designed to assist mathematicians by integrating multiple theorem provers and advanced language models. Leveraging tools like Lean, Prover9, Mace4, and more in the future, MathAssistant AI facilitates seamless interaction through natural language or Lean syntax, providing comprehensive support for formal proofs, theorem exploration, and mathematical research.

## Features

- **Multi-Theorem Prover Integration:** Utilize Lean, Prover9, Mace4, and expand to additional provers effortlessly.
- **Diverse Language Models:** Harness the capabilities of OpenAI's GPT-4, Anthropic's Claude and more to generate accurate and insightful mathematical assistance.
- **Flexible Communication:** Interact using natural language or Lean syntax to receive tailored help and solutions.
- **Automated Proof Generation & Verification:** Generate, verify, and refine mathematical proofs automatically across multiple platforms.
- **Future-Proof Architecture:** Designed to incorporate additional tools and models as they become available.

## Installation

### Prerequisites

- **Python 3.7+**
- **Lean Theorem Prover**
- **Prover9**
- **Mace4**
- **Farspeak**
- **API Keys** for OpenAI, Claude, and other LLMs.

### Steps

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/mathassistant-ai.git
    cd mathassistant-ai
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure API Keys:**
    - Create a `.env` file in the root directory.
    - Add your API keys:
      ```
      OPENAI_API_KEY=your_openai_api_key
      CLAUDE_API_KEY=your_claude_api_key
      ```
      (soon more)

4. **Install Theorem Provers:**
    - **Lean:** Follow the [Lean installation guide](https://leanprover.github.io/download/).
    - **Prover9:** Download from the [Prover9 website](https://www.prover9.info/).
    - **Mace4:** Download from the [Mace4 website](http://www.cs.unm.edu/~mccune/mace4/).
    - 
    (soon more)

## Usage

### Running the tool

Run the main application:


### Examples

```bash
Currently,

python3 mathplatform.py "#eval 1 + 2 * 5"

Lean Verification Result:
 Lean verification successful.

In principle,

1. Natural language
User: Prove that for all natural numbers n, n + 0 = n.
AI: [Generates and verifies proof using Lean, Prover9]

2. Lean
User: 
theorem add_zero (n : ℕ) : n + 0 = n :=
begin
  rw nat.zero_add,
end
AI: User inputs Lean code directly. [Verifies and provides feedback or suggestions]
```

### License

This project is licensed under the Apache License 2.0. You are free to use, modify, and distribute this software in accordance with the terms of the Apache License 2.0.


