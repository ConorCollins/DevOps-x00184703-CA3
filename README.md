# DevOps-x00184703-CA3 - Conor Collins

# Calculator CI/CD Pipeline Project
This project demonstrates the implementation of a CI/CD pipeline for a Python-based calculator application. The pipeline automates testing, static code analysis, code coverage reporting, and deployment across multiple environments using Azure DevOps. The pipeline ensures that the application meets quality standards through automated testing, security checks, and deployment procedures.

# Features
- A Python calculator application with basic mathematical operations.
- Unit testing using unittest for functionality verification.
- Code coverage reporting with coverage.
- Static code analysis with bandit.
- A multi-stage CI/CD pipeline configured on Azure DevOps.
- Deployment to Test and Production environments with approval gates for Production.

# Technology Used
- Python 3.12 for the calculator application.
- unittest.
- coverage
- bandit
- Azure DevOps
- Github

# Local Development Setup
1 - Clone the repository:

    git clone https://github.com/ConorCollins/DevOps-x00184703-CA3.git
2 - Set up a virtual environment

A virtual environment ensures that all dependencies are installed in an isolated environment, preventing conflicts with global Python libraries.

    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
3 - Install Dependencies

    pip install -r requirements.txt
4 - Run the application Locally

Run the Calculator

    python src/calculator.py
Run the Unit Tests

    python -m unittest discover -s tests
# Application Features

The calculator application supports the following operations:
- Addition
- Subtraction
- Mulitplication
- Division

Each operation is tested with unit tests located in the tests/ directory.

# CI/CD Pipeline Implementation

The pipeline is configured on Azure DevOps and includes the following stages:

1 - Build Stage
  - Sets up Python 3.12.
  - Creates and activates a virtual environment.
  - Installs dependencies from requirements.txt.

2 - Test Stage
  - Runs unit tests with coverage to ensure functionality and generates a coverage report.
  - Performs static code analysis using bandit for security testing.
  - Publishes test results and coverage reports as artifacts.

3 - Deploy Stage
  - Deploys to the Test environment.
  - Requires manual approval before deploying to the Production environment.

![image](https://github.com/user-attachments/assets/acb82601-e1dd-4943-a212-6ab7009f4442)

The pipeline is defined in the file: 

      azure-pipelines.yml

# Branch Policies and Protection

Branch policies are enforced to maintain code quality and prevent accidental changes to critical branches:

1 - Restrict deletions: Prevents the deletion of important branches such as main.

2 - Require status checks to pass: Enforces that all pipeline checks (build, test, static analysis) pass before merging.

3 - Block force pushes: Disables force pushes to protected branches to preserve commit history integrity.

# Testing Strategy

The testing strategy focuses on ensuring code quality and functionality:

1 - The pipeline uses coverage to ensure at least 80% of the code is covered by unit tests.

2 - bandit is used for security analysis of the source code.

3 - Located in the tests/ directory, unit tests cover all calculator operations.

# Troubleshooting Guide

1 - Error: No tests ran
  - Cause: Test discovery failed due to incorrect test structure or file naming.
  - Solution: Ensure test files are named test_*.py and are located in the tests/ directory.

2 - Error: ModuleNotFoundError
  - Cause: Missing dependencies.
  - Solution: Run pip install -r requirements.txt to install the required dependencies.

3 - Error: Bandit not recognized
  - Cause: Bandit is not installed or not in the correct environment.
  - Solution: Ensure Bandit is listed in requirements.txt and the virtual environment is activated before running it.

# Environment Setup and Configuration
To ensure a consistent development and CI/CD environment, the following setup and configuration steps are implemented:

1 - Development Environment:
  - The application is developed using Python 3.12.
  - A virtual environment is created using venv for dependency isolation.
  - Dependencies are installed using pip from the requirements.txt file.

2 - Pipeline Environment:
  - Self-Hosted Agent: The CI/CD pipeline uses the ConorSelfHostedPool for executing jobs.
  - Azure Variable Groups: Sensitive data such as tokens or credentials are stored in Azure DevOps variable groups for secure access.

3 - Environment-Specific Configurations:
  - Test Environment: Used for running automated tests and validation.
  - Production Environment: Deploys the final, validated version of the application.
  - Approval gates are implemented to promote deployments from Test to Production.

# Deployment Process

The deployment process is implemented as part of the Deploy Stage in the Azure DevOps pipeline.

1 - Deployment to Test:
  - After successful execution of the Build and Test stages, the pipeline automatically deploys to the Test environment.
  - The deployment is handled by a runOnce strategy in the DeployTest job.
  - The runOnce strategy is a simple deployment strategy that executes the deployment steps exactly once for the specified environment.

2 - Deployment to Production:
  - Deployments to Production are triggered only after manual approval, ensuring validated releases.
  - The DeployProd job depends on the success of the DeployTest job.

3 - Steps for Deployment:
  - The deployment scripts echo the deployment steps as placeholders for actual deployment logic.

# Security Testing

Tool
  - Bandit 
  - Integrated into the Test Stage of the pipeline

Purpose
  -  Identifies potential security vulnerabilities in the Python codebase through static code analysis.

Running the Command

    python -m bandit -r src/

Outcome
  - Any vulnerabilities are logged in the pipeline for review
  - The pipeline can fail if critical issues are detected.

# Performance Testing

1 - Benchmark Testing

    tests/performance_tests/benchmark_test.py
Purpose 
  - The benchmark test evaluates the performance of the add operation under high load by measuring how long it takes to execute a specific operation repeatedly.

Use Case 
  - This test provides insights into the efficiency of the addition function under a high computational load.
  - It's useful for detecting performance bottlenecks.

2 - Stress Test 

    tests/performance_tests/stress_test.py
Purpose 
  - The stress test evaluates the calculator's behavior under extreme conditions, including large inputs and edge cases like division by zero.

Use Case
  - Ensures the calculator can handle edge cases and extreme inputs.

# Pipeline Approval Gates

Purpose - Approval gates are implemented to ensure that only validated deployments are promoted to Production.

How to Setup in Azure DevOps:

1 - Navigate to Environments:
  - Go to Pipelines > Environments in Azure DevOps.
  - Select the Prod environment.

2 - Add Approval Gate:
  - Click + Approvals and Checks.
  - Select Approvals and configure:
    - Approvers: Specify the individuals or groups responsible for approving deployments.
    - Timeout: Set a timeout for the approval (e.g., 24 hours).

![image](https://github.com/user-attachments/assets/4e848198-da33-4e49-92ae-b251ca7a5c69)

3 - Pipeline behaviour
  - The deployment to Production will pause at the approval gate until manual approval is provided.









































