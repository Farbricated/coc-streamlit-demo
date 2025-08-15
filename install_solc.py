from solcx import install_solc, get_installed_solc_versions

try:
    install_solc('0.8.0')
    print("✅ Solidity compiler 0.8.0 installed successfully!")
    versions = get_installed_solc_versions()
    print(f"Installed versions: {versions}")
except Exception as e:
    print(f"❌ Error: {e}")
