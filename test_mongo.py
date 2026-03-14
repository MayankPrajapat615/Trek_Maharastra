import ssl
import socket
import certifi

host = "ac-lms2pyp-shard-00-00.wtxrcs7.mongodb.net"
port = 27017

# Test 1: TLS 1.3
print("--- Test 1: TLS 1.3 ---")
try:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_3
    ctx.load_verify_locations(certifi.where())
    with ctx.wrap_socket(socket.create_connection((host, port), timeout=5), server_hostname=host) as s:
        print(f"✅ TLS 1.3 succeeded: {s.version()}")
except Exception as e:
    print(f"❌ TLS 1.3 failed: {e}")

# Test 2: TLS 1.2 with cert verification OFF (isolates cert vs cipher issue)
print("\n--- Test 2: TLS 1.2, no cert check ---")
try:
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.minimum_version = ssl.TLSVersion.TLSv1_2
    ctx.maximum_version = ssl.TLSVersion.TLSv1_2
    ctx.check_hostname = False          # ← disable hostname check
    ctx.verify_mode = ssl.CERT_NONE     # ← disable cert verification
    with ctx.wrap_socket(socket.create_connection((host, port), timeout=5), server_hostname=host) as s:
        print(f"✅ TLS 1.2 (no verify) succeeded: {s.version()}")
        print(f"Cipher: {s.cipher()}")
except Exception as e:
    print(f"❌ TLS 1.2 (no verify) failed: {e}")

# Test 3: Check available TLS versions
print("\n--- Test 3: System TLS info ---")
print(f"Has TLS 1.2: {hasattr(ssl.TLSVersion, 'TLSv1_2')}")
print(f"Has TLS 1.3: {hasattr(ssl.TLSVersion, 'TLSv1_3')}")
print(f"Default ciphers snippet: {ssl.create_default_context().get_ciphers()[0]}")