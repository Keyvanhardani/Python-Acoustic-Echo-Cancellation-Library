# Python Acoustic Echo Cancellation Library

## Description
This project implements adaptive filter algorithms for **Acoustic Echo Cancellation (AEC)** and general audio processing. The library includes adaptive filtering algorithms such as:
- **LMS (Least Mean Squares)**
- **NLMS (Normalized LMS)**
- **RLS (Recursive Least Squares)**

These filters are crucial for applications in speech processing, **echo suppression**, and **noise reduction**. The adaptive nature of these algorithms allows them to adjust dynamically to incoming signals and reduce unwanted echoes in real-time.

### **What is Acoustic Echo Cancellation?**
Acoustic Echo Cancellation (AEC) is the process of removing the echo that occurs when a microphone picks up audio output from nearby speakers. AEC is commonly used in telecommunication systems, video conferencing, and other audio processing systems to improve clarity and prevent feedback loops.

## Features
- **LMS (Least Mean Squares):** A simple adaptive filter that adjusts coefficients based on the error between the desired and estimated signal.
- **NLMS (Normalized LMS):** An extension of LMS with normalized step size for greater stability and performance across varying signal strengths.
- **RLS (Recursive Least Squares):** A more sophisticated filter using an inverse correlation matrix for fast and precise adaptation.

## Installation
To use the library, clone the repository and install the necessary dependencies:

```bash
pip install numpy scipy matplotlib
