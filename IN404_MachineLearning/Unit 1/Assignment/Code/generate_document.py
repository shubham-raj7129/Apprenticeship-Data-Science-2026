"""
Generate the Word document for IN404 Unit 1 Assignment: Cyber Warfare
"""
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
import os

doc = Document()

# ── Styles ───────────────────────────────────────────────────────────
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(12)
paragraph_format = style.paragraph_format
paragraph_format.space_after = Pt(6)
paragraph_format.line_spacing = 1.15

# ── Title Page ───────────────────────────────────────────────────────
for _ in range(6):
    doc.add_paragraph()

title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run("Unit 1 Assignment: Cyber Warfare")
run.bold = True
run.font.size = Pt(24)
run.font.name = 'Times New Roman'

doc.add_paragraph()

for line in [
    "Shubham Raj",
    "Purdue University Global",
    "IN404: Machine Learning",
    "September 2026",
]:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(line)
    r.font.size = Pt(14)
    r.font.name = 'Times New Roman'

doc.add_page_break()

# ═══════════════════════ ITEM 3 ═══════════════════════════════════════
h = doc.add_heading('3. Mechanize Websites and MAC Address Lookup', level=1)

doc.add_paragraph(
    "The Python script below uses the mechanize module to browse websites and extract cookies, "
    "and the subprocess module with the arp command to retrieve the MAC address associated with "
    "a given IP address. The program presents an interactive menu with three options: "
    "(1) mechanize a website to read its content and cookies, (2) get the MAC address from an IP "
    "address using the system ARP table, or (3) quit the program."
)

doc.add_paragraph()
# Insert Step 3 screenshot
SCREENSHOTS = "/Users/L037129/Desktop/Apprenticeship/Data Science 2026/IN404_MachineLearning/Unit1/Assignment/Screenshots"
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run()
r.add_picture(os.path.join(SCREENSHOTS, "Step 3", "Screenshot 1.png"), width=Inches(5.5))

doc.add_paragraph(
    "Figure 1. Execution of step3_mechanize_mac.py showing website mechanization and MAC address lookup."
).italic = True

doc.add_paragraph(
    "The code file step3_mechanize_mac.py is submitted alongside this document."
)

doc.add_page_break()

# ═══════════════════════ ITEM 4 ═══════════════════════════════════════
h = doc.add_heading('4. Purpose of the Python Mechanize Module', level=1)

doc.add_paragraph(
    "The Python mechanize module is a programmable web browsing library that allows developers "
    "to automate interaction with websites through Python scripts. Originally inspired by Perl's "
    "WWW::Mechanize, the module provides a stateful browser object that can navigate web pages, "
    "follow links, fill out and submit forms, and handle HTTP redirects—all without requiring a "
    "graphical web browser (Richardson & Ruby, 2023)."
)

doc.add_paragraph(
    "One of mechanize's most powerful features is its built-in cookie handling. Cookies are small "
    "pieces of data that websites store on a user's browser to maintain session state, remember "
    "login credentials, and track user behavior. The mechanize module uses a CookieJar object "
    "(from Python's http.cookiejar standard library) to automatically store, send, and manage "
    "cookies across HTTP requests. When a website sets a cookie through a Set-Cookie header, "
    "mechanize captures it and includes it in subsequent requests, effectively simulating a real "
    "browser session. Developers can also create cookies programmatically and inject them into "
    "the CookieJar, enabling the simulation of authenticated sessions without manual login "
    "(Engebretson, 2013)."
)

doc.add_paragraph(
    "This capability is critically important for automated bots. A bot that can read, store, and "
    "create cookies can maintain persistent sessions on target websites, bypass simple "
    "authentication mechanisms, scrape content behind login walls, and impersonate legitimate "
    "users. In the context of cyber warfare, adversarial bots can use mechanize to conduct "
    "credential stuffing attacks, harvest sensitive information from web applications, or "
    "maintain command-and-control (C2) channels through legitimate-looking HTTP traffic. Because "
    "the module mimics a real browser's cookie behavior, requests made through mechanize are "
    "harder for web application firewalls to distinguish from genuine human traffic "
    "(Singer & Friedman, 2014)."
)

doc.add_page_break()

# ═══════════════════════ ITEM 5 ═══════════════════════════════════════
h = doc.add_heading('5. MAC Addresses and MAC Spoofing', level=1)

doc.add_paragraph(
    "A Media Access Control (MAC) address is a unique 48-bit hardware identifier assigned to "
    "every network interface card (NIC) by its manufacturer. Represented as six pairs of "
    "hexadecimal digits separated by colons (e.g., aa:bb:cc:dd:ee:ff), the MAC address operates "
    "at Layer 2 (Data Link Layer) of the OSI model and is used by network switches and routers "
    "to direct frames to the correct physical device on a local area network (LAN). Unlike IP "
    "addresses, which can change based on network configuration, MAC addresses are intended to "
    "be permanent and globally unique (Kurose & Ross, 2021)."
)

doc.add_paragraph(
    "MAC spoofing is the practice of changing the MAC address presented by a network interface "
    "to impersonate another device. There are several reasons why one might want to spoof a MAC "
    "address:"
)

# Bullet list for MAC spoofing reasons
reasons = [
    ("Bypassing Access Controls: ", "Many networks use MAC address filtering as a security "
     "mechanism, allowing only known MAC addresses to connect. An attacker who discovers an "
     "authorized MAC address (e.g., through network sniffing) can spoof that address to gain "
     "unauthorized access to the network."),
    ("Evading Tracking and Surveillance: ", "Since MAC addresses are unique identifiers, they "
     "can be used to track a device's movement across networks. Spoofing allows a user to "
     "preserve privacy by rotating MAC addresses, preventing persistent tracking."),
    ("Impersonation Attacks: ", "An attacker can spoof a trusted device's MAC address to "
     "conduct man-in-the-middle (MITM) attacks, intercept traffic, or hijack network sessions "
     "by exploiting the trust that switches and routers place in MAC addresses."),
    ("Circumventing License Restrictions: ", "Some software and services are licensed per "
     "MAC address. Spoofing allows users to bypass these restrictions by presenting a different "
     "hardware identifier (Stallings, 2017)."),
]

for bold_text, normal_text in reasons:
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

doc.add_paragraph(
    "In the context of cyber warfare, MAC spoofing is a foundational technique used during "
    "the reconnaissance and sustainment phases of an attack. By spoofing MAC addresses, "
    "adversaries can remain undetected on compromised networks, bypass network access controls, "
    "and masquerade as legitimate devices to avoid triggering security alerts (Engebretson, 2013)."
)

doc.add_page_break()

# ═══════════════════════ ITEM 6 ═══════════════════════════════════════
h = doc.add_heading('6. Scapy Network Traffic Analysis', level=1)

doc.add_paragraph(
    "The Python script below uses the scapy library to analyze a packet capture file "
    "(IN404.pcapng) and the pandas/matplotlib libraries to visualize protocol traffic from "
    "IN404.csv. The program provides seven analysis options for detecting suspicious network "
    "activity including spoofed MAC addresses, DNS queries, port scanning, denial-of-service "
    "indicators, TCP reset flags, and protocol distribution visualization."
)

doc.add_paragraph()
# Insert Step 6 screenshots
step6_shots = [
    ("Screenshot 1.png", "Figure 2. Menu and spoofed MAC address count (Choice 1)."),
    ("Screenshot 2.png", "Figure 3. DNS round robin queries (Choice 2)."),
    ("Screenshot 3.png", "Figure 4. Port 135 access count (Choice 3)."),
    ("Screenshot 4.png", "Figure 5. Denial of service check (Choice 4) and reset flag check (Choice 5)."),
    ("Screenshot 5.png", "Figure 6. Additional terminal output."),
    ("Screenshot 6.png", "Figure 7. Protocol traffic count bar chart (Choice 6)."),
]

for filename, caption in step6_shots:
    img_path = os.path.join(SCREENSHOTS, "Step 6", filename)
    if os.path.exists(img_path):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run()
        r.add_picture(img_path, width=Inches(5.5))
        cap = doc.add_paragraph(caption)
        cap.italic = True
        doc.add_paragraph()

doc.add_paragraph(
    "The code file step6_scapy_analysis.py is submitted alongside this document."
)

doc.add_page_break()

# ═══════════════════════ ITEM 7 ═══════════════════════════════════════
h = doc.add_heading('7. Explanation of the Scapy Analysis Code (Choices 1–7)', level=1)

doc.add_paragraph(
    "The Step 6 program is a menu-driven network traffic analyzer that uses scapy to parse "
    "a pcapng capture file and pandas to visualize protocol data from a CSV export. Each menu "
    "choice performs a specific security analysis function:"
)

choices = [
    ("Choice 1 – Check Ether Count for aa:bb:cc:dd:ee:ff (Spoofed MAC Detection): ",
     "This option iterates through every packet in the capture file and checks whether the "
     "source Ethernet (MAC) address matches the known spoofed address \"aa:bb:cc:dd:ee:ff.\" "
     "The address aa:bb:cc:dd:ee:ff is a placeholder address commonly used in spoofing "
     "attacks; no legitimate manufacturer assigns this address. The code counts how many "
     "packets originate from this spoofed address and prints the total. This is a basic "
     "intrusion detection technique: a high count indicates that an attacker on the network "
     "is using a forged MAC address to disguise their identity (Sanders, 2017)."),

    ("Choice 2 – Check DNS Round Robin Queries: ",
     "This option examines each packet for a DNS Resource Record (DNSRR) layer. When found, "
     "it checks whether the answer section (packet.an) contains a DNSRR response and prints "
     "the queried domain name (rrname). DNS round robin is a load-balancing technique where "
     "a single domain resolves to multiple IP addresses. Monitoring DNS responses helps "
     "identify potential DNS tunneling, data exfiltration through DNS queries, or "
     "command-and-control communications that use rapidly changing DNS records "
     "(known as fast-flux DNS) to evade detection (Antonakakis et al., 2012)."),

    ("Choice 3 – Check Source Port 135 Access: ",
     "This option scans all packets that contain either a UDP or TCP layer and counts those "
     "with a destination port of 135. Port 135 is used by Microsoft's Remote Procedure Call "
     "(RPC) and Distributed Component Object Model (DCOM) services. It is a frequent target "
     "for attackers because vulnerabilities in RPC services have historically been exploited "
     "by worms such as Blaster and Conficker. A high count of packets targeting port 135 "
     "may indicate port scanning, exploitation attempts, or lateral movement within a "
     "compromised network (Northcutt et al., 2006)."),

    ("Choice 4 – Check for Denial of Service: ",
     "This option counts TCP packets with a window size of 65535. The TCP window size "
     "indicates how much data a receiver can accept; a window size of 65535 (the maximum "
     "for the 16-bit window field without scaling) can be associated with certain denial-of-"
     "service (DoS) attack tools that set the window to its maximum value. While a window "
     "size of 65535 is not inherently malicious, a large volume of such packets may indicate "
     "a SYN flood or similar volumetric attack designed to overwhelm the target's resources. "
     "The code labels this as \"Ping of death\" detection, referencing a classic DoS technique "
     "(Mirkovic & Reiher, 2004)."),

    ("Choice 5 – Check Reset Flag: ",
     "This option iterates through TCP packets and counts those with the RST (Reset) flag "
     "set (flags == 'R'). TCP reset packets forcefully terminate connections. An unusually "
     "high number of reset packets can indicate several issues: a port scan where closed "
     "ports respond with RST packets, a reset attack (also called TCP reset injection) where "
     "an attacker sends forged RST packets to disrupt legitimate connections, or network "
     "misconfigurations. Monitoring RST counts is a standard practice in network forensics "
     "and intrusion detection (Bejtlich, 2013)."),

    ("Choice 6 – Visualize Protocol Traffic Count: ",
     "This option reads the IN404.csv file (a Wireshark export of the packet capture) into "
     "a pandas DataFrame, counts the occurrences of each protocol type in the 'Protocol' "
     "column, and generates a bar chart using matplotlib. This visualization provides a "
     "quick overview of the network traffic composition—showing the relative volume of "
     "TCP, UDP, DNS, TLS, HTTP, ARP, and other protocols. Anomalies in protocol distribution "
     "(e.g., an unexpectedly high proportion of ICMP or DNS traffic) can indicate scanning "
     "activity, tunneling, or denial-of-service attacks (Sanders, 2017)."),

    ("Choice 7 – Quit Program: ",
     "This option calls sys.exit() to cleanly terminate the program, ending the analysis "
     "session."),
]

for bold_text, normal_text in choices:
    p = doc.add_paragraph()
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

doc.add_page_break()

# ═══════════════════════ ITEM 8 ═══════════════════════════════════════
h = doc.add_heading('8. Scapy: Offensive and Defensive Uses', level=1)

doc.add_paragraph(
    "Scapy is a powerful Python-based packet manipulation tool that allows users to forge, "
    "send, capture, and decode network packets of a wide variety of protocols. Its versatility "
    "makes it valuable for both offensive security testing and defensive network monitoring "
    "(Biondi, 2023)."
)

# Offensive
doc.add_heading('Offensive Uses of Scapy', level=2)

offensive = [
    ("1. Network Reconnaissance and Port Scanning: ",
     "Scapy can craft custom SYN, ACK, or FIN packets to perform stealthy port scans on target "
     "systems. Unlike tools like Nmap that produce recognizable scan signatures, scapy allows "
     "attackers to customize every field of the packet header, making the scan harder to detect "
     "by intrusion detection systems (IDS). For example, an attacker can send SYN packets to a "
     "range of ports and analyze the responses (SYN-ACK for open ports, RST for closed ports) to "
     "map a target's attack surface (Engebretson, 2013)."),

    ("2. ARP Spoofing / Man-in-the-Middle Attacks: ",
     "Scapy can construct and send forged ARP (Address Resolution Protocol) reply packets to "
     "poison the ARP cache of devices on a local network. By associating the attacker's MAC "
     "address with the IP address of the default gateway, all traffic from victims is redirected "
     "through the attacker's machine, enabling interception, modification, or dropping of "
     "packets. This is a classic man-in-the-middle (MITM) attack and one of the most common uses "
     "of scapy in penetration testing (Kennedy et al., 2011)."),

    ("3. Denial-of-Service (DoS) Attacks: ",
     "Scapy can generate and send massive volumes of crafted packets to overwhelm a target's "
     "network resources. Examples include SYN flood attacks (sending thousands of TCP SYN packets "
     "with random source IPs to exhaust a server's connection table), ping floods (sending "
     "oversized ICMP packets), and DNS amplification attacks (sending small DNS queries with a "
     "spoofed source IP to generate large responses directed at the victim). Scapy's ability to "
     "set arbitrary source addresses makes it effective for these volumetric attacks "
     "(Mirkovic & Reiher, 2004)."),
]

for bold_text, normal_text in offensive:
    p = doc.add_paragraph()
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

# Defensive
doc.add_heading('Defensive Uses of Scapy', level=2)

defensive = [
    ("1. Network Traffic Monitoring and Anomaly Detection: ",
     "Security analysts use scapy to capture live network traffic or analyze packet captures "
     "(pcap/pcapng files) to identify anomalous behavior. By scripting custom filters and "
     "analysis logic, defenders can detect spoofed MAC addresses, unusual protocol distributions, "
     "unexpected port activity, and suspicious DNS queries—as demonstrated in the Step 6 code of "
     "this assignment. This programmable approach offers more flexibility than static IDS rules "
     "(Sanders, 2017)."),

    ("2. Firewall and IDS Testing: ",
     "Defenders use scapy to generate test traffic that simulates various attack patterns to "
     "validate that firewalls, intrusion detection systems (IDS), and intrusion prevention "
     "systems (IPS) are functioning correctly. For example, a security team can craft packets "
     "with known malicious signatures, fragmented packets, or packets with unusual flag "
     "combinations to ensure that security controls detect and block them appropriately. This "
     "proactive testing is essential for maintaining an effective security posture "
     "(Bejtlich, 2013)."),

    ("3. Network Forensics and Incident Response: ",
     "During incident response, scapy is used to parse and analyze packet captures from "
     "compromised networks. Analysts can extract indicators of compromise (IOCs) such as "
     "command-and-control server IP addresses, data exfiltration patterns, malware "
     "communication protocols, and lateral movement signatures. Scapy's Python integration "
     "allows analysts to automate forensic workflows, correlate findings with threat "
     "intelligence feeds, and produce detailed reports of network-based attack activity "
     "(Davidoff & Ham, 2012)."),
]

for bold_text, normal_text in defensive:
    p = doc.add_paragraph()
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

doc.add_page_break()

# ═══════════════════════ ITEM 9 ═══════════════════════════════════════
h = doc.add_heading('9. Logical Weapons of Cyber Warfare', level=1)

doc.add_paragraph(
    "The following section discusses tools used in two categories of cyber warfare operations: "
    "Reconnaissance and Access and Escalation. Each category includes three tools used as "
    "logical weapons."
)

# 9.1 Reconnaissance
doc.add_heading('9.1 Reconnaissance', level=2)

doc.add_paragraph(
    "Reconnaissance is the initial phase of a cyber operation where the adversary gathers "
    "information about the target to identify vulnerabilities, map network architecture, and "
    "plan subsequent attack phases."
)

recon_tools = [
    ("1. Shodan: ",
     "Shodan is a search engine for internet-connected devices that indexes information about "
     "servers, routers, webcams, industrial control systems (ICS), and other networked equipment. "
     "Unlike traditional search engines that index web page content, Shodan scans the internet for "
     "open ports and services, collecting banners that reveal software versions, configurations, "
     "and potential vulnerabilities. In cyber warfare, adversaries use Shodan to discover exposed "
     "critical infrastructure—such as SCADA systems, unpatched servers, and IoT devices—without "
     "ever sending a single packet to the target, making the reconnaissance entirely passive and "
     "undetectable (Matherly, 2016)."),

    ("2. Maltego: ",
     "Maltego is an open-source intelligence (OSINT) and graphical link analysis tool used for "
     "gathering and connecting information from public sources. It automates the process of "
     "querying DNS records, WHOIS databases, social media, email addresses, and organizational "
     "relationships, presenting the results as a visual graph of entities and their connections. "
     "Cyber warfare operators use Maltego to map an organization's digital footprint, identify "
     "key personnel for spear-phishing campaigns, discover subsidiary networks, and uncover "
     "relationships between IP addresses, domain names, and physical locations "
     "(Paterva, 2023)."),

    ("3. theHarvester: ",
     "theHarvester is a command-line reconnaissance tool designed to collect email addresses, "
     "subdomains, IP addresses, and employee names associated with a target domain from public "
     "sources including search engines (Google, Bing), certificate transparency logs, DNS "
     "databases, and social media platforms (LinkedIn). In the context of cyber warfare, "
     "theHarvester enables adversaries to rapidly enumerate a target organization's exposed "
     "digital assets and personnel, providing the information necessary to craft targeted "
     "phishing emails, identify entry points for network intrusion, and build a comprehensive "
     "intelligence profile of the target (Engebretson, 2013)."),
]

for bold_text, normal_text in recon_tools:
    p = doc.add_paragraph()
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

# 9.3 Access and Escalation
doc.add_heading('9.3 Access and Escalation', level=2)

doc.add_paragraph(
    "Access and Escalation is the phase where an adversary gains initial entry into a target "
    "system and then elevates their privileges to gain deeper control over the compromised "
    "environment."
)

access_tools = [
    ("1. Metasploit Framework: ",
     "Metasploit is the world's most widely used penetration testing framework, providing a "
     "comprehensive suite of exploit modules, payloads, encoders, and post-exploitation tools. "
     "It allows operators to identify vulnerabilities in target systems, deliver exploits to gain "
     "initial access, and then escalate privileges through local exploit modules and credential "
     "harvesting. In cyber warfare, Metasploit's Meterpreter payload provides an encrypted, "
     "in-memory command shell that can navigate firewalls and maintain persistent access to "
     "compromised systems. The framework's auxiliary modules also support brute-force attacks, "
     "password spraying, and lateral movement across networks (Kennedy et al., 2011)."),

    ("2. Cobalt Strike: ",
     "Cobalt Strike is a commercial adversary simulation and red team operations platform that "
     "provides a sophisticated command-and-control (C2) framework. Its Beacon payload supports "
     "multiple communication channels (HTTP, HTTPS, DNS, SMB), credential harvesting using "
     "Mimikatz integration, privilege escalation through named pipe impersonation and token "
     "manipulation, and lateral movement via PsExec, WMI, and WinRM. Cobalt Strike has been "
     "used extensively in nation-state cyber operations, including the SolarWinds supply chain "
     "attack of 2020, where adversaries deployed modified Cobalt Strike Beacons for persistent "
     "access to compromised government and corporate networks (MITRE, 2023)."),

    ("3. Mimikatz: ",
     "Mimikatz is a post-exploitation tool developed by security researcher Benjamin Delpy that "
     "extracts plaintext passwords, Kerberos tickets, NTLM hashes, and other authentication "
     "credentials from Windows memory. It exploits the way Windows stores credentials in the "
     "Local Security Authority Subsystem Service (LSASS) process. In cyber warfare, Mimikatz is "
     "a critical escalation tool: once an attacker gains initial access with limited privileges, "
     "they can use Mimikatz to harvest administrator credentials, perform pass-the-hash or "
     "pass-the-ticket attacks, create golden tickets for domain-wide access, and move laterally "
     "through Active Directory environments. It was a key component of the NotPetya and WannaCry "
     "attacks that caused billions of dollars in damage worldwide (Delpy, 2023)."),
]

for bold_text, normal_text in access_tools:
    p = doc.add_paragraph()
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

doc.add_page_break()

# ═══════════════════════ ITEM 10 ══════════════════════════════════════
h = doc.add_heading('10. Automated Bots in Cyber Warfare', level=1)

doc.add_paragraph(
    "Automated bots are software programs that execute predefined tasks autonomously, often "
    "at speeds and scales impossible for human operators. In cyber warfare, bots serve as "
    "force multipliers that enable adversaries to conduct large-scale operations with minimal "
    "human oversight. Their effectiveness stems from their ability to operate continuously, "
    "adapt to changing conditions through programmed logic, coordinate with other bots in a "
    "network (botnet), and evade detection through automated obfuscation techniques "
    "(Singer & Friedman, 2014)."
)

doc.add_heading('How Automated Bots Are Used in Cyber Warfare', level=2)

bot_uses = [
    ("Distributed Denial-of-Service (DDoS) Attacks: ",
     "Botnets—networks of thousands or millions of compromised devices controlled by a "
     "central command-and-control server—can generate massive volumes of traffic to overwhelm "
     "target infrastructure, taking down government websites, financial systems, and critical "
     "services."),
    ("Credential Stuffing and Brute-Force Attacks: ",
     "Bots can automatically test millions of stolen username/password combinations against "
     "login portals, exploiting password reuse to gain unauthorized access to email, banking, "
     "and government systems."),
    ("Reconnaissance and Scanning: ",
     "Automated bots continuously scan the internet for vulnerable systems, open ports, "
     "and misconfigured services, feeding intelligence back to operators for exploitation."),
    ("Information Warfare: ",
     "Social media bots create and amplify disinformation, manipulate public opinion, sow "
     "discord, and interfere with democratic processes by flooding platforms with coordinated "
     "propaganda."),
    ("Command-and-Control (C2) Operations: ",
     "Bots maintain persistent footholds in compromised networks, execute commands from remote "
     "operators, exfiltrate data, and spread laterally—all without requiring constant human "
     "intervention."),
]

for bold_text, normal_text in bot_uses:
    p = doc.add_paragraph(style='List Bullet')
    r = p.add_run(bold_text)
    r.bold = True
    p.add_run(normal_text)

doc.add_paragraph(
    "Bots are most effective in scenarios requiring speed, scale, and persistence: large-scale "
    "DDoS attacks against critical infrastructure, automated exploitation of zero-day "
    "vulnerabilities before patches are deployed, persistent surveillance of target networks, "
    "and coordinated disinformation campaigns across social media platforms."
)

doc.add_heading('Use Case 1: Mirai Botnet (2016)', level=2)

doc.add_paragraph(
    "The Mirai botnet was one of the most devastating automated bot attacks in history. Created "
    "by scanning the internet for IoT devices (security cameras, routers, DVRs) still using "
    "default factory credentials, Mirai infected over 600,000 devices worldwide. On October 21, "
    "2016, Mirai launched a massive DDoS attack against Dyn, a major DNS service provider, "
    "generating traffic volumes exceeding 1.2 Tbps. The attack disrupted access to major "
    "websites including Twitter, Netflix, Reddit, CNN, and GitHub for millions of users across "
    "the United States and Europe. The Mirai botnet demonstrated how automated bots can weaponize "
    "ordinary consumer devices into a coordinated cyber weapon capable of disrupting critical "
    "internet infrastructure. The source code was later released publicly, spawning numerous "
    "variants that continue to threaten IoT devices today (Antonakakis et al., 2017)."
)

doc.add_heading('Use Case 2: Russian Bot Operations Against Estonia (2007)', level=2)

doc.add_paragraph(
    "In April 2007, Estonia experienced what is widely considered the first major cyber warfare "
    "campaign against a nation-state. Following a political dispute with Russia over the relocation "
    "of a Soviet-era war memorial, Estonian government websites, banks, media outlets, and "
    "telecommunications systems were subjected to coordinated DDoS attacks lasting three weeks. "
    "The attacks were carried out by botnets comprising an estimated one million compromised "
    "computers worldwide. The bots flooded Estonian servers with traffic volumes that overwhelmed "
    "the country's internet infrastructure, effectively cutting Estonia off from the digital "
    "world. Parliament's email system was shut down, banks suspended online services, and media "
    "websites were rendered inaccessible. The Estonian cyber attacks are a landmark case study in "
    "cyber warfare because they demonstrated that automated bots could be used as strategic "
    "weapons against an entire nation's digital infrastructure, prompting NATO to establish the "
    "Cooperative Cyber Defence Centre of Excellence (CCDCOE) in Tallinn, Estonia "
    "(Herzog, 2011)."
)

doc.add_paragraph()

doc.add_heading('Conclusion', level=2)

doc.add_paragraph(
    "Automated bots have become indispensable tools in modern cyber warfare. Their ability to "
    "operate at machine speed, coordinate across vast networks of compromised devices, and "
    "execute complex attack sequences autonomously makes them powerful force multipliers for "
    "both state and non-state adversaries. As demonstrated by the Mirai botnet and the Estonian "
    "cyber attacks, bots can cause catastrophic disruption to critical infrastructure and "
    "national security. Defending against bot-driven attacks requires a combination of network "
    "monitoring, anomaly detection (as demonstrated in this assignment's scapy analysis), strong "
    "authentication practices, and international cooperation in cybersecurity defense."
)

doc.add_page_break()

# ═══════════════════════ REFERENCES ═══════════════════════════════════
h = doc.add_heading('References', level=1)

references = [
    "Antonakakis, M., Perdisci, R., Dagon, D., Lee, W., & Feamster, N. (2012). Building a "
    "dynamic reputation system for DNS. Proceedings of the 19th USENIX Security Symposium, "
    "273–290.",

    "Antonakakis, M., April, T., Bailey, M., Bernhard, M., Bursztein, E., Cochran, J., ... & "
    "Zhou, Y. (2017). Understanding the Mirai botnet. Proceedings of the 26th USENIX Security "
    "Symposium, 1093–1110.",

    "Bejtlich, R. (2013). The practice of network security monitoring: Understanding incident "
    "detection and response. No Starch Press.",

    "Biondi, P. (2023). Scapy: Packet crafting for Python2 and Python3. "
    "https://scapy.net/",

    "Davidoff, S., & Ham, J. (2012). Network forensics: Tracking hackers through cyberspace. "
    "Prentice Hall.",

    "Delpy, B. (2023). Mimikatz: A little tool to play with Windows security. "
    "https://github.com/gentilkiwi/mimikatz",

    "Engebretson, P. (2013). The basics of hacking and penetration testing: Ethical hacking "
    "and penetration testing made easy (2nd ed.). Syngress.",

    "Herzog, S. (2011). Revisiting the Estonian cyber attacks: Digital threats and "
    "multinational responses. Journal of Strategic Security, 4(2), 49–60.",

    "Kennedy, D., O'Gorman, J., Kearns, D., & Aharoni, M. (2011). Metasploit: The "
    "penetration tester's guide. No Starch Press.",

    "Kurose, J. F., & Ross, K. W. (2021). Computer networking: A top-down approach (8th ed.). "
    "Pearson.",

    "Matherly, J. (2016). Complete guide to Shodan. Shodan LLC.",

    "Mirkovic, J., & Reiher, P. (2004). A taxonomy of DDoS attack and DDoS defense mechanisms. "
    "ACM SIGCOMM Computer Communication Review, 34(2), 39–53.",

    "MITRE. (2023). MITRE ATT&CK: Cobalt Strike. "
    "https://attack.mitre.org/software/S0154/",

    "Northcutt, S., Shenk, J., Shackleford, D., Rosenberg, T., Siles, R., & Mancini, S. "
    "(2006). Penetration testing: Assessing your overall security before attackers do. SANS "
    "Institute.",

    "Paterva. (2023). Maltego: The tool for open source intelligence and graphical link "
    "analysis. https://www.maltego.com/",

    "Richardson, L., & Ruby, S. (2023). RESTful web APIs: Services for a changing world. "
    "O'Reilly Media.",

    "Sanders, C. (2017). Practical packet analysis: Using Wireshark to solve real-world "
    "network problems (3rd ed.). No Starch Press.",

    "Singer, P. W., & Friedman, A. (2014). Cybersecurity and cyberwar: What everyone needs "
    "to know. Oxford University Press.",

    "Stallings, W. (2017). Network security essentials: Applications and standards (6th ed.). "
    "Pearson.",
]

for ref in references:
    p = doc.add_paragraph(ref)
    p.paragraph_format.left_indent = Inches(0.5)
    p.paragraph_format.first_line_indent = Inches(-0.5)

# ── Save ─────────────────────────────────────────────────────────────
output_path = "/Users/L037129/Desktop/Apprenticeship/Data Science 2026/IN404_MachineLearning/Unit1/Assignment/IN404_ShubhamRaj_Unit1.docx"
doc.save(output_path)
print(f"Document saved to: {output_path}")
