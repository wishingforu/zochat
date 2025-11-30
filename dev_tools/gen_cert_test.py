#!/usr/bin/env python3
"""
zoMount - HTTPS WebDAV Server for Zo Computer
Mounts workspace as local drive with SSL support for Windows compatibility
"""

import os
import sys
import socket
from datetime import datetime, timedelta

def generate_self_signed_cert(cert_file, key_file):
    """Generate a self-signed SSL certificate for localhost"""
    try:
        from cryptography import x509
        from cryptography.x509.oid import NameOID
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import rsa
        from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
        
        # Generate private key
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        
        # Create certificate
        subject = issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "CA"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Local"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Zo Computer"),
            x509.NameAttribute(NameOID.COMMON_NAME, "localhost"),
        ])
        
        cert = x509.CertificateBuilder().subject_name(
            subject
        ).issuer_name(
            issuer
        ).public_key(
            private_key.public_key()
        ).serial_number(
            x509.random_serial_number()
        ).not_valid_before(
            datetime.utcnow()
        ).not_valid_after(
            datetime.utcnow() + timedelta(days=365)
        ).add_extension(
            x509.SubjectAlternativeName([
                x509.DNSName("localhost"),
                x509.IPAddress(__import__('ipaddress').IPv4Address("127.0.0.1")),
            ]),
            critical=False,
        ).sign(private_key, hashes.SHA256())
        
        # Write files
        with open(cert_file, "wb") as f:
            f.write(cert.public_bytes(Encoding.PEM))
        
        with open(key_file, "wb") as f:
            f.write(private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=NoEncryption()
            ))
        
        return True
        
    except ImportError:
        print("ERROR: cryptography library not installed")
        print("Install with: pip install cryptography")
        return False
    except Exception as e:
        print(f"Error generating certificate: {e}")
        return False


if __name__ == "__main__":
    cert_dir = os.path.expanduser("~/.config/zo-chat")
    cert_file = os.path.join(cert_dir, "zoMount.crt")
    key_file = os.path.join(cert_dir, "zoMount.key")
    
    # Generate cert if it doesn't exist
    if not (os.path.exists(cert_file) and os.path.exists(key_file)):
        print("Generating self-signed SSL certificate for HTTPS...")
        os.makedirs(cert_dir, exist_ok=True)
        if not generate_self_signed_cert(cert_file, key_file):
            sys.exit(1)
        print(f"✓ Certificate generated: {cert_file}")
        print()
    
    print(f"Certificate: {cert_file}")
    print(f"Key: {key_file}")
