# 🛡️ Blockchain-Backed Chain of Custody for Digital Images

## 📌 Overview
This project implements a **secure, tamper-proof digital evidence management system** tailored for forensic image handling.  
It extracts **hidden and non-visible information** from images, stores it in a searchable MongoDB Atlas database, and records cryptographic proofs on a blockchain network to maintain a **verifiable chain of custody**.

The system ensures that:
- All image evidence is processed consistently.
- Extracted metadata and hidden data are preserved.
- Evidence integrity can be verified at any point in the future.
- Handling history is immutable and tamper-resistant.

---

## 🛠 Technology Stack

### **Frontend & User Interface**
- **Streamlit** – Python-based web app framework for rapid dashboard creation.
- **HTML5/CSS3** – Automatically generated via Streamlit’s rendering engine.
- **JavaScript** – For custom interactivity and dynamic UI components.

### **Core Programming**
- **Python** – Main development language.
- **Pandas** – For structured data manipulation and analysis.
- **NumPy** – Numerical processing and array computations.

### **Image Processing & Forensics**
- **OpenCV (cv2)** – Advanced image processing, watermark detection, and manipulation.
- **Pillow (PIL)** – For image handling and EXIF metadata extraction.
- **scikit-image** – Specialized image processing algorithms.
- **stegano** – Detection and decoding of LSB-based steganography.
- **pyzbar** – QR code scanning and decoding.

### **Blockchain Integration**
- **web3.py** – Interface to Ethereum blockchain for transaction handling.
- **eth-account** – Secure Ethereum account and private key management.
- **Ganache** – Local Ethereum blockchain simulator for development/testing.

### **Database & Storage**
- **MongoDB Atlas** – Cloud-hosted NoSQL database for storing extracted metadata.
- **pymongo** – Python driver for MongoDB.
- **hashlib** – SHA-256 cryptographic hashing for integrity.

### **Development & Configuration**
- **python-dotenv** – Environment variable management.
- **os & sys** – System operations and path handling.
- **json** – Metadata serialization.
- **datetime** – Timestamp creation.

### **Deployment & Hosting**
- **Docker** – Portable deployment.
- **GitHub** – Version control.
- **Qovery** – Cloud hosting for Streamlit.

### **Security & Authentication**
- Private key cryptography – Blockchain transaction signing.
- Environment variables – Secure credential storage.
- SSL/TLS – Encrypted communication.

### **Demo-Specific Features**
- File upload handling – Evidence submission.
- Progress bars – Real-time feedback.
- Interactive dashboard – Evidence analytics.
- Risk assessment – High/Medium/Low categorization.
- JSON report generation – Downloadable forensic reports.
- Live status indicators – MongoDB, blockchain, and forensic module health.

---

## ⚙️ How It Works
1. **Upload Evidence**
   - Select an image file through the dashboard.
   - File is processed in memory.

2. **Hidden Data Extraction**
   - EXIF metadata (camera type, GPS, timestamps).
   - Steganographic messages, watermarks, QR codes.
   - SHA-256 hash generated for integrity.

3. **Database Storage**
   - Store metadata and hashes in MongoDB Atlas.
   - Indexed for fast retrieval.

4. **Blockchain Recording**
   - Hash + timestamp recorded on blockchain.
   - Transaction ID linked to database entry.

5. **Verification**
   - Upload later to check authenticity and chain of custody.

---

## 🛠 Installation Guide

You can set up this project in **two ways**:  
- **Option 1:** Install with `requirements.txt` (Recommended)  
- **Option 2:** Install manually without `requirements.txt`

---

### **Option 1: With `requirements.txt` (Recommended)**
```bash
# Clone repository
git clone https://github.com/Farbricated/coc-streamlit-demo.git
cd coc-streamlit-demo

# Optional: create a virtual environment
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Run the application
streamlit run src/app.py
```

### Option 2: Without requirements.txt (Manual Installation)
```bash
# Clone repository
git clone https://github.com/Farbricated/coc-streamlit-demo.git
cd coc-streamlit-demo

# Optional: create a virtual environment
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies manually
pip install streamlit pillow exifread pandas python-dotenv pymongo dnspython web3 eth-account py-solc-x stegano pyzbar opencv-python-headless numpy scikit-image

# Run the application
streamlit run src/app.py
```

### Environment Variables Setup

Before running, create a .env file in the root directory with:
```ini
MONGO_URI=your_mongodb_connection_string
BLOCKCHAIN_PROVIDER_URL=your_blockchain_node_url
PRIVATE_KEY=your_ethereum_private_key
```



---

## ▶️ First Run Checklist

✅ MongoDB Atlas connection string is correct.
✅ Blockchain node (Ganache/Testnet/Mainnet) is running.
✅ .env file contains valid keys.
✅ Python environment activated.

---

## 📊 Example Workflow

Investigator uploads photo1.jpg.
System extracts:
GPS: 40.7128° N, 74.0060° W
Camera: Canon EOS 80D
Timestamp: 2025-08-12 14:22:05
Hash generated: 7f5a9d0a0b4d...
MongoDB entry created.
Blockchain record created: 0xabc123def456...
Verification proves image is unchanged.

---

## 📜 License
MIT License – Use, modify, and distribute freely with attribution.

```yaml

---

If you want, I can also create a **text-based architecture diagram** inside this README so readers instantly see the “Upload → Extraction → Database → Blockchain → Verification” flow without opening any separate files. That would make this README even more reviewer-friendly.
```
