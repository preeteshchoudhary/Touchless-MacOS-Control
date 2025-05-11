# create_default_profile.py
import os
import pickle
import numpy as np  # Required for feature handling
from cryptography.fernet import Fernet

# Configuration
profiles_dir = "core/voice/profiles"
user_id = "default_user"

# Generate valid features (10 float64 numbers = 80 bytes)
dummy_features = np.random.rand(10).astype(np.float64)  # ← Critical fix

# Ensure directory exists
os.makedirs(profiles_dir, exist_ok=True)

# Generate/load encryption key
key_path = "security.key"
if not os.path.exists(key_path):
    key = Fernet.generate_key()
    with open(key_path, "wb") as f:
        f.write(key)
else:
    with open(key_path, "rb") as f:
        key = f.read()

# Encrypt and save
fernet = Fernet(key)
encrypted_data = fernet.encrypt(pickle.dumps(dummy_features))
profile_path = os.path.join(profiles_dir, f"{user_id}.profile")

with open(profile_path, "wb") as f:
    f.write(encrypted_data)

print(f"Created default profile: {profile_path}")
