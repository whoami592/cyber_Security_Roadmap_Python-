import tkinter as tk
from tkinter import ttk, scrolledtext

def create_roadmap_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Cybersecurity Complete Roadmap")
    root.geometry("800x600")
    root.configure(bg='black')

    # Banner frame
    banner_frame = tk.Frame(root, bg='red', height=80)
    banner_frame.pack(fill=tk.X, padx=10, pady=10)
    banner_frame.pack_propagate(False)

    # Banner text
    banner_label = tk.Label(
        banner_frame,
        text="PAKISTANI WHITE HAT HACKER\nMR SABAZ ALI KHAN",
        font=("Arial", 16, "bold"),
        fg='white',
        bg='red',
        justify=tk.CENTER
    )
    banner_label.pack(expand=True)

    # Roadmap frame
    roadmap_frame = tk.Frame(root, bg='black')
    roadmap_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Title for roadmap
    title_label = tk.Label(
        roadmap_frame,
        text="Complete Cybersecurity Roadmap",
        font=("Arial", 14, "bold"),
        fg='white',
        bg='black'
    )
    title_label.pack(anchor=tk.W, pady=(0, 10))

    # Scrolled text widget for the roadmap content
    roadmap_text = scrolledtext.ScrolledText(
        roadmap_frame,
        wrap=tk.WORD,
        width=90,
        height=30,
        font=("Consolas", 10),
        bg='black',
        fg='lime',
        insertbackground='white'
    )
    roadmap_text.pack(fill=tk.BOTH, expand=True)

    # Roadmap content
    roadmap_content = """
Cybersecurity Complete Roadmap
===============================

Phase 1: Fundamentals (1-2 Months)
----------------------------------
- Learn Operating Systems: Linux (Ubuntu/Kali), Windows, macOS
  - Commands: Bash/PowerShell basics
- Networking Basics: OSI Model, TCP/IP, Subnetting, DNS, HTTP/HTTPS
  - Tools: Wireshark for packet analysis
- Programming for Security: Python (scripting, automation), Bash scripting
  - Libraries: Scapy, Requests

Phase 2: Web Application Security (2-3 Months)
----------------------------------------------
- Web Technologies: HTML, CSS, JavaScript, SQL
- Common Vulnerabilities: OWASP Top 10 (XSS, CSRF, SQL Injection, etc.)
- Tools: Burp Suite, OWASP ZAP
- Practice: DVWA, WebGoat labs

Phase 3: Cryptography (1 Month)
-------------------------------
- Symmetric/Asymmetric Encryption: AES, RSA
- Hashing: SHA, MD5
- PKI, SSL/TLS
- Tools: OpenSSL

Phase 4: Penetration Testing (3-4 Months)
-----------------------------------------
- Reconnaissance: Nmap, Maltego
- Scanning & Enumeration: Nessus, OpenVAS
- Exploitation: Metasploit, SQLMap
- Post-Exploitation: Meterpreter
- Practice: HackTheBox, TryHackMe, CTF challenges

Phase 5: Defensive Security (2 Months)
--------------------------------------
- Firewalls, IDS/IPS: Snort, Suricata
- SIEM: ELK Stack, Splunk
- Incident Response: NIST Framework
- Secure Coding Practices

Phase 6: Advanced Topics (Ongoing)
----------------------------------
- Reverse Engineering: IDA Pro, Ghidra
- Malware Analysis: Cuckoo Sandbox
- Cloud Security: AWS/Azure security
- Forensics: Autopsy, Volatility
- Compliance: GDPR, PCI-DSS

Phase 7: Certifications & Projects
----------------------------------
- Certs: CompTIA Security+, CEH, OSCP, CISSP
- Projects: Build a secure home lab, contribute to open-source security tools
- Community: Join DEF CON, Black Hat, local meetups

Tips:
- Practice ethically on legal platforms only.
- Stay updated via blogs (Krebs on Security), podcasts (Darknet Diaries).
- Time commitment: 10-15 hours/week.

Created by: Pakistani White Hat Hacker Mr Sabaz Ali Khan
    """

    roadmap_text.insert(tk.END, roadmap_content)
    roadmap_text.config(state=tk.DISABLED)  # Make read-only

    # Run the GUI
    root.mainloop()

if __name__ == "__main__":
    create_roadmap_gui()